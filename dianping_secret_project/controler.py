from dianping_secret_project.category_orm import Category, SecondCategory, ThirdCategory, City, Region, \
    get_sqlalchemy_session
from lib.mongo import Mongo
import requests
import json

m = Mongo(host='114.80.150.196', port=27777, user_name='fangjia', password='fangjia123456')
collection = m.connect['dianping']['dianping_zhangshang']

REQUEST_LIMIT = 5000
db_session = get_sqlalchemy_session()


class Controller:
    def __init__(self):
        self.url = 'https://mapi.dianping.com/searchshop.json?'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def crawler_by_city(self, city):
        """

        :param city: city ORM
        :return:
        """
        second_category_list = db_session.query(SecondCategory).filter_by(cityId=city.city_id).filter_by(parentId=10)
        for second_category in second_category_list:
            if int(second_category.count) <= REQUEST_LIMIT:
                # 小于5000的抓取
                self.crawler_all_shop(second_category)
            else:
                # 大于5000的抓取
                self.crawler_shop_by_region(second_category)

    def analyzer_insert(self, r, second_category):
        """
        去重入库
        :param r: response object
        :return:
        """
        # todo 按照一批插入，提高速度
        json_body = json.loads(r.text)
        print(r.url)

        for k in json_body['list']:
            try:
                if not collection.find_one({'id': k['id']}):
                    k['search_city_id'] = second_category.cityId
                    collection.insert_one(k)
                else:
                    print('数据已经存在', k['id'])
            except Exception as e:
                collection.insert_one(k)
        print(r.text)

    def crawler_all_shop(self, second_category):
        """
        小于5000的抓取
        :param second_category: second_category ORM
        :return:
        """
        for i in range(int(second_category.count / 50) + 1):
            payload = {'start': i * 50,
                       'categoryid': second_category.second_categoryId,
                       'limit': '50',
                       'cityid': second_category.cityId, }
            r = requests.get(self.url, params=payload, headers=self.headers)
            try:
                if r.json()['isEnd']:
                    # todo 这个逻辑和函数刚刚开始逻辑重复了，不需要计算页码
                    print('当前已经抓完')
                    break
                self.analyzer_insert(r, second_category)
            except Exception as e:
                print('')

    def crawler_shop_by_region(self, second_category):
        """
        大于5000，通过区域抓取
        :return:
        """
        for region in db_session.query(Region).filter_by(city_id=second_category.cityId):
            for i in range(int(second_category.count / 50) + 1):
                payload = {'start': i * 50,
                           'categoryid': second_category.second_categoryId,
                           'limit': '50',
                           'cityid': second_category.cityId,
                           'regionid': region.region_id}
                r = requests.get(self.url, params=payload, headers=self.headers)
                if r.json()['isEnd']:
                    # todo 这个逻辑和函数刚刚开始逻辑重复了，不需要计算页码
                    print('当前已经抓完')
                    break
                self.analyzer_insert(r, second_category)


if __name__ == '__main__':
    pass
