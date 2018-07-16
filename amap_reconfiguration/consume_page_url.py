# coding=utf-8
import pika
import requests
import json
import yaml
from lib.log import LogHandler

log = LogHandler('consumer_page_url')

setting = yaml.load(open('config.yaml'))
rabbit_host = setting['amap']['rabbitmq']['host']
rabbit_port = setting['amap']['rabbitmq']['port']

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, port=rabbit_port))
rabbit = connection.channel()


def callback(ch, method, properties, body):
    result = requests.get(body.decode('utf8'))
    print(result.json())
    if result.json()['status'] is '1':
        rabbit.basic_publish(exchange='', routing_key='amap_result_json', body=json.dumps(result.json()))
        print('放入amap_result_json队列')
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        print(body)
        log.info('url={},result={}'.format(body, result.json()))
        ch.basic_ack(delivery_tag=method.delivery_tag)


def consume_page_url():
    rabbit.basic_qos(prefetch_count=1)
    rabbit.basic_consume(callback,
                         queue='amap_page_url',
                         )
    rabbit.start_consuming()
