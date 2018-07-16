# coding=utf-8
import pika
import json
import yaml
from lib.mongo import Mongo

setting = yaml.load(open('config.yaml'))
rabbit_host = setting['amap']['rabbitmq']['host']
rabbit_port = setting['amap']['rabbitmq']['port']

mongo_host = setting['amap']['mongo']['host']
mongo_port = setting['amap']['mongo']['port']
mongo_db = setting['amap']['mongo']['db']
mongo_collection = setting['amap']['mongo']['collection']

connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbit_host, port=rabbit_port))
rabbit = connection.channel()

client = Mongo(mongo_host,
               mongo_port,
               user_name=setting['amap']['mongo']['user_name'],
               password=setting['amap']['mongo']['password'])
db = client.connect[mongo_db]
coll = db.get_collection(mongo_collection)


def callback(ch, method, properties, body):
    print(body.decode())
    json_result = json.loads(body.decode())
    pois = json_result.get('pois')
    if pois:
        coll.insert_many(pois)
    print('存储入库完毕')
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consume_result():
    rabbit.basic_qos(prefetch_count=1)
    rabbit.basic_consume(callback,
                         queue='amap_result_json',
                         )
    rabbit.start_consuming()
