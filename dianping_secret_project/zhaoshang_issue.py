from dianping_secret_project.category_orm import City, get_sqlalchemy_session, Region, SecondCategory
from dianping_secret_project.controler import Controller

db_session = get_sqlalchemy_session()

cityid_list = [3, 103, 102, 105, 109, 11, 106, 104, 108, 101, 107]


def get_count():
    for i in cityid_list:
        print('------------------{}'.format(i))
        for sc in db_session.query(SecondCategory).filter_by(cityId=i).filter_by(parentId=10):
            print(sc.count)


if __name__ == '__main__':
    c = Controller()
    for i in cityid_list:
        city_ = db_session.query(City).filter_by(city_id=str(i))
        c.crawler_by_city(city_[0])
        print('开始抓取城市={}'.format(i))
