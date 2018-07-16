from amap_reconfiguration.consumer_result import consume_result
from amap_reconfiguration.consume_page_url import consume_page_url
from amap_reconfiguration.gevent_consumer_url_list import consume_all_url
from gevent import monkey
monkey.patch_all()


if __name__ == '__main__':
    # consume_result()
    # consume_page_url()
    consume_all_url()