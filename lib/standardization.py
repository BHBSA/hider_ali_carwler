"""
格式化城市区域
"""
from lib.region_block import city_dict, region_dict
from lib.log import LogHandler

log = LogHandler(__name__)


def standard_city(city_name):
    """

    :param city_name: 城市名称
    :return: 城市名称
    """
    city_name_in_fangjia_list = []

    for city_name_in_fangjia in city_dict.keys():
        for nick_name in city_dict[city_name_in_fangjia]:
            if nick_name in city_name:
                city_name_in_fangjia_list.append(city_name_in_fangjia)

    if len(city_name_in_fangjia_list):
        return True, max(city_name_in_fangjia_list, key=lambda x: len(x))
    else:
        log.error("城市无法标准化：{}".format(city_name))
        return False, city_name


def standard_block(city_name, region_name):
    """

    :param city_name: 城市名称
    :param region_name: 区域
    :return: 区域
    """
    result, city_name = standard_city(city_name)
    if result:
        for region_list in region_dict[city_name].values():
            for region in region_list:
                if region in region_name:
                    return True, region
    else:
        log.error("城市无法标准化：{},无法格式话区域".format(city_name))
        return False, city_name