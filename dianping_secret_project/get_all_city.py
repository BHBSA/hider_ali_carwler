import requests
import re
import json
from dianping_secret_project.category_orm import City, get_sqlalchemy_session, Region, SecondCategory

db_session = get_sqlalchemy_session()


class GetAllCity:
    @classmethod
    def get_all_city(cls):
        """

        :return: [city_object, city_object]
        """
        res = requests.get('http://www.dianping.com/ajax/citylist/getAllDomesticCity')
        for values in res.json()['cityMap'].values():
            for city_dict in filter(lambda x: x['parentCityId'] == 0, [city_info for city_info in values]):
                city = City()
                city.name = city_dict['cityName']
                city.city_id = city_dict['cityId']
                city.pingyin_name = city_dict['cityPyName']
                db_session.add(city)
                db_session.commit()


class GetRegion:
    def __init__(self, city):
        """

        :param city: city_object
        """
        self.city = city
        self.url = 'https://m.dianping.com/{}/ch0/r0'.format(city.pingyin_name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def get_region(self):
        """

        :return: [region_object, region_object, region_object], [category_object,category_object,category_object]
        """
        res = requests.get(self.url, headers=self.headers)
        json_body = re.search('window.PAGE_INITIAL_STATE = (.*?)</script>', res.text, re.S | re.M).group(1)
        body = json.loads(json_body.strip()[:-1])

        for region_info_dict in filter(
                lambda region_dict: region_dict['parentId'] == 0 and '热门' not in region_dict['name'],
                [region_dict for region_dict in body['mapiSearch']['data']['regionNavs']]):
            # region_info_dict:{'name': '城关区', 'lng': 0, 'id': 427, 'lat': 0, 'regionType': 0, 'count': 63830, 'parentId': 0}
            region = Region()
            region.region_id = region_info_dict['id']
            region.name = region_info_dict['name']
            region.city_id = self.city.city_id

            db_session.add(region)
            db_session.commit()

        for k in filter(lambda region_dict: region_dict['parentId'] != 0 and '全部' not in region_dict['name'],
                        [region_dict for region_dict in body['mapiSearch']['data']['categoryNavs']]):
            second_category = SecondCategory()
            second_category.second_categoryId = k['id']
            second_category.count = k['count']
            second_category.name = k['name']
            second_category.cityId = self.city.city_id
            second_category.parentId = k['parentId']

            db_session.add(second_category)
            db_session.commit()


# if __name__ == '__main__':
#     for instance in db_session.query(City):
#         g = GetRegion(instance)
#         g.get_region()
