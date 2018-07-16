from dianping import get_city_url_1, get_region_url_2, get_street_url_3, get_cooking_url_4, put_all_url_5, \
    get_all_html_6, analyzer_first_html_7
from multiprocessing import Process

from dianping import put_mongodb_8
from dianping import new_mongo_8

if __name__ == '__main__':
    # Process(target=get_city_url_1.start_consume).start()
    get_city_url_1.start_consume()
    ip = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {"host": "http-pro.abuyun.com", "port": "9010",
                                                         "user": "HRH476Q4A852N90P", "pass": "05BED1D0AF7F0715"}
    # for i in range(5):
    #     Process(target=get_region_url_2.consume_start, args=(ip,)).start()
    # for i in range(5):
    #     Process(target=get_street_url_3.consume_start, args=(ip,)).start()
    # for i in range(5):
    #     Process(target=get_cooking_url_4.consume_start,args=(ip,)).start()
    # for i in range(5):
    #     Process(target=put_all_url_5.consume_start,args=(ip,)).start()
    # for i in range(5):
    #     Process(target=get_all_html_6.consume_start, args=(ip,)).start()
    # Process(target=analyzer_first_html_7.consume_start).start()
    # new_mongo_8.consume_start(ip)
    # for i in range(3):
    #     Process(target=new_mongo_8.consume_start, args=(ip,)).start()
