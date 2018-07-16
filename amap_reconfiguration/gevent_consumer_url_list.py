import json
import pika
import gevent

import requests
from lib.rabbitmq import Rabbit
from lib.log import LogHandler

log = LogHandler('gevent_consumer_url_list')

connection_result = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5673))


def asyn_message(_url):
    try:
        result = requests.get(_url, timeout=5)
        print(result.text, _url)
    except Exception as e:
        log.info('request error,url={}'.format(_url))
        return

    status = result.json()['status']

    if status is '1':
        count = int(result.json()['count'])
        if count != 0:
            if count < 50:
                print('count < 50')
                channel_result = connection_result.channel()

                channel_result.queue_declare(queue='amap_result_json')
                channel_result.basic_publish(exchange='', routing_key='amap_result_json',
                                             body=json.dumps(result.json()))
                channel_result.close()
            else:
                print('count > 50')

                r = Rabbit('192.168.0.192', 5673)
                channel_page = r.get_channel()
                # connection_page = pika.BlockingConnection(
                #     pika.ConnectionParameters(host='192.168.0.192', port=5673))
                # channel_page = connection_page.channel()
                channel_page.queue_declare(queue='amap_page_url')
                for i in range(1, int(count / 50 + 0.5)):
                    channel_page.basic_publish(exchange='',
                                               routing_key='amap_page_url',
                                               body=result.url + '&page=' + str(
                                                   i + 1), )
                    print('分页 的url放入')
                channel_page.close()
    else:
        log.info('url={},result={}'.format(_url, result.text))


def callback(ch, method, properties, body):
    jobs = [gevent.spawn(asyn_message, _url) for _url in json.loads(body.decode())]
    gevent.wait(jobs)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consume_all_url():
    connect_result = pika.BlockingConnection(
        pika.ConnectionParameters(host='192.168.0.192', port=5673))
    channel = connect_result.channel()
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback,
                          queue='amap_all_url',
                          )
    channel.start_consuming()
