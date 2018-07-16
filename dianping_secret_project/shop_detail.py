import requests
from lib.mongo import Mongo
import re

m = Mongo(host='114.80.150.196', port=27777, user_name='fangjia', password='fangjia123456')
collection = m.connect['dianping']['dianping_zhangshang']
collection_lat = m.connect['dianping']['dianping_zhangshang_lat']


class ShopDetail:
    def __init__(self):
        self.url = 'https://m.dianping.com/shop/20721516/map'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def get_shop_lat(self):
        for i in collection.find():
            try:
                r = requests.get(url='https://m.dianping.com/shop/{}/map'.format(i['id']), headers=self.headers)
                info = re.search('PAGE_INITIAL_STATE(.*?)</script>', r.text, re.S | re.M).group(1)
                lat = re.search('"shopLat":(.*?),', info, re.S | re.M).group(1)
                lng = re.search('"shopLng":(.*?),', info, re.S | re.M).group(1)
                print(lat, lng)
                collection_lat.insert_one({
                    'info': info,
                    'id': i['id'],
                    'lng': lng,
                    'lat': lat,
                })
            except Exception as e:
                print(e)
                print('key has no id')


if __name__ == '__main__':
    s = ShopDetail()
    s.get_shop_lat()
