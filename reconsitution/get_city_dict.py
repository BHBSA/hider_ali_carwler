# import requests
# from lib.standardization import standard_city
#
# url = 'http://www.dianping.com/ajax/citylist/getAllDomesticCity'
# res = requests.get(url)
# city_dict = res.json()['cityMap']
# city_ = {}
# no_city_ = {}
# for i in city_dict:
#     list_ = city_dict[i]
#     for city in list_:
#         if '县' in city['cityName']:
#             continue
#         is_a, is_b = standard_city(city['cityName'])
#         if is_a:
#             if city['cityName'] != is_b:
#                 print(city['cityName'], '-------', is_b)
#                 no_city_[city['cityEnName']] = (city['cityName'], is_b)
#             else:
#                 city_[city['cityEnName']] = is_b
# print(no_city_)
# print(city_)

a = {'longnan': '陇南', 'danzhou': '儋州', 'wuzhong': '吴忠', 'ningde': '宁德', 'wenshan': '文山州', 'yancheng': '盐城',
     'meishan': '眉山', 'heihe': '黑河', 'alaer': '阿拉尔', 'qinzhou': '钦州', 'anyang': '安阳', 'shangluo': '商洛',
     'chongqing': '重庆', 'linchang': '临沧', 'puer': '普洱', 'yunfu': '云浮', 'zhongwei': '中卫', 'liaocheng': '聊城',
     'anshun': '安顺', 'zaozhuang': '枣庄', 'wulanchabu': '乌兰察布', 'ledong': '乐东', 'changzhi': '长治', 'xinxiang': '新乡',
     'dandong': '丹东', 'fangchenggang': '防城港', 'liupanshui': '六盘水', 'taian': '泰安', 'jixi': '鸡西', 'longyan': '龙岩',
     'rikazediqu': '日喀则', 'hanzhong': '汉中', 'zhangzhou': '漳州', 'daqing': '大庆', 'shangqiu': '商丘', 'xianyang': '咸阳',
     'kunming': '昆明', 'chaozhou': '潮州', 'wuhu': '芜湖', 'yili': '伊犁', 'sansha': '三沙', 'lijiang': '丽江', 'wenchang': '文昌',
     'shuangyashan': '双鸭山', 'baoshan': '保山', 'tianjin': '天津', 'jinchang': '金昌', 'baicheng': '白城', 'yichang': '宜昌',
     'baishan': '白山', 'deyang': '德阳', 'xiamen': '厦门', 'xuancheng': '宣城', 'mudanjiang': '牡丹江', 'huhehaote': '呼和浩特',
     'huanggang': '黄冈', 'enshizhou': '恩施', 'zhaoqing': '肇庆', 'anhuisuzhou': '宿州', 'liuzhou': '柳州', 'wuzhishan': '五指山',
     'jinzhou': '锦州', 'weifang': '潍坊', 'chengde': '承德', 'xuzhou': '徐州', 'guilin': '桂林', 'qujing': '曲靖', 'binzhou': '滨州',
     'guangxiyulin': '玉林', 'nanping': '南平', 'anqing': '安庆', 'jincheng': '晋城', 'ezhou': '鄂州', 'nantong': '南通',
     'liuan': '六安', 'xinzhou': '忻州', 'hebi': '鹤壁', 'panjin': '盘锦', 'jieyang': '揭阳', 'zhangjiakou': '张家口', 'yaan': '雅安',
     'tianshui': '天水', 'wuwei': '武威', 'zhejiangtaizhou': '台州', 'qiongzhong': '琼中', 'zhongshan': '中山', 'yanan': '延安',
     'lianyuangang': '连云港', 'beitun': '北屯', 'jining': '济宁', 'qionghai': '琼海', 'jingdezhen': '景德镇', 'lvliang': '吕梁',
     'pingdingshan': '平顶山', 'jiangxifuzhou': '抚州', 'meizhou': '梅州', 'bengbu': '蚌埠', 'jilin': '吉林', 'ganzhou': '赣州',
     'changchun': '长春', 'jiayuguan': '嘉峪关', 'zhangjiajie': '张家界', 'jinhua': '金华', 'yinchuan': '银川', 'shuozhou': '朔州',
     'chifeng': '赤峰', 'shenyang': '沈阳', 'baoding': '保定', 'yangjiang': '阳江', 'yangzhou': '扬州', 'jiamusi': '佳木斯',
     'ankang': '安康', 'jiyuan': '济源', 'yiyang': '益阳', 'boertala': '博尔塔拉', 'xiantao': '仙桃', 'ali': '阿里', 'yueyang': '岳阳',
     'baotou': '包头', 'shantou': '汕头', 'xinyang': '信阳', 'tonghua': '通化', 'changsha': '长沙', 'qitaihe': '七台河',
     'shannan': '山南', 'jiangmen': '江门', 'lanzhou': '兰州', 'leshan': '乐山', 'taiyuan': '太原', 'shenzhen': '深圳',
     'daxinganling': '大兴安岭', 'haidong': '海东', 'guangan': '广安', 'laibin': '来宾', 'shaoxing': '绍兴', 'nanyang': '南阳',
     'zhenjiang': '镇江', 'siping': '四平', 'suining': '遂宁', 'nanning': '南宁', 'zhuzhou': '株洲', 'zhaotong': '昭通',
     'zibo': '淄博', 'jiaozuo': '焦作', 'dezhou': '德州', 'loudi': '娄底', 'wuhan': '武汉', 'huangshi': '黄石', 'yingkou': '营口',
     'chongzuo': '崇左', 'datong': '大同', 'jiangxiyichun': '宜春', 'yulin': '榆林', 'chizhou': '池州', 'changjiang': '昌江',
     'guiyang': '贵阳', 'fushun': '抚顺', 'guangzhou': '广州', 'zhoukou': '周口', 'shizuishan': '石嘴山', 'yanbian': '延边',
     'jingzhou': '荆州', 'mianyang': '绵阳', 'fuxin': '阜新', 'luoyang': '洛阳', 'lishui': '丽水', 'zhuhai': '珠海', 'suzhou': '苏州',
     'qiannan': '黔南', 'chenzhou': '郴州', 'xinyu': '新余', 'zhanjiang': '湛江', 'ziyang': '资阳', 'nanchang': '南昌',
     'shihezi': '石河子', 'luzhou': '泸州', 'laiwu': '莱芜', 'yuxi': '玉溪', 'jiujiang': '九江', 'heyuan': '河源',
     'sanmenxia': '三门峡', 'huzhou': '湖州', 'tongchuan': '铜川', 'guyuan': '固原', 'huaian': '淮安', 'eerduosi': '鄂尔多斯',
     'baiyin': '白银', 'chaoyang': '朝阳', 'baise': '百色', 'wuxi': '无锡', 'huludao': '葫芦岛', 'wuzhou': '梧州', 'bazhong': '巴中',
     'lingshui': '陵水', 'hengshui': '衡水', 'changde': '常德', 'xiangyang': '襄阳', 'suqian': '宿迁', 'hechi': '河池',
     'huaibei': '淮北', 'tongrendiqu': '铜仁', 'zigong': '自贡', 'xiangxi': '湘西', 'baoting': '保亭', 'xining': '西宁',
     'baisha': '白沙', 'sanya': '三亚', 'xianning': '咸宁', 'chuzhou': '滁州', 'haikou': '海口', 'qianxinan': '黔西南',
     'linfen': '临汾', 'quanzhou': '泉州', 'honghe': '红河', 'maanshan': '马鞍山', 'beijing': '北京', 'baoji': '宝鸡',
     'xiaogan': '孝感', 'jinan': '济南', 'zhengzhou': '郑州', 'neijiang': '内江', 'guigang': '贵港', 'huainan': '淮南',
     'huizhou': '惠州', 'zhangye': '张掖', 'quzhou': '衢州', 'yingtan': '鹰潭', 'tongliao': '通辽', 'tumushuke': '图木舒克',
     'panzhihua': '攀枝花', 'puyang': '濮阳', 'yuncheng': '运城', 'yongzhou': '永州', 'dazhou': '达州', 'shaoyang': '邵阳',
     'jiaxing': '嘉兴', 'heze': '菏泽', 'fuyang': '阜阳', 'wenzhou': '温州', 'zunyi': '遵义', 'tongling': '铜陵', 'wujiaqu': '五家渠',
     'tangshan': '唐山', 'jiuquan': '酒泉', 'hainanzhou': '海南州', 'yantai': '烟台', 'hefei': '合肥', 'bayannaoer': '巴彦淖尔',
     'chengdu': '成都', 'guangyuan': '广元', 'taizhou': '泰州', 'handan': '邯郸', 'jinmen': '荆门', 'huaihua': '怀化',
     'luohe': '漯河', 'yichun': '伊春', 'pingxiang': '萍乡', 'nanjing': '南京', 'haerbin': '哈尔滨', 'putian': '莆田',
     'ningbo': '宁波', 'lasa': '拉萨', 'wulumuqi': '乌鲁木齐', 'shiyan': '十堰', 'zhoushan': '舟山', 'naqu': '那曲', 'tieling': '铁岭',
     'zhumadian': '驻马店', 'qinhuangdao': '秦皇岛', 'wuhai': '乌海', 'qiandongnan': '黔东南', 'kelamayi': '克拉玛依', 'sanming': '三明',
     'shanghai': '上海', 'gannanzhou': '甘南', 'dongguan': '东莞', 'suihua': '绥化', 'liaoyuan': '辽源', 'maoming': '茂名',
     'bozhou': '亳州', 'shangrao': '上饶', 'xian': '西安', 'dongfang': '东方', 'weihai': '威海', 'qingdao': '青岛',
     'yangquan': '阳泉', 'qianjiang': '潜江', 'dalian': '大连', 'hezhou': '贺州', 'ganzi': '甘孜州', 'hengyang': '衡阳',
     'yibin': '宜宾', 'shaoguan': '韶关', 'bayinguoleng': '巴音郭楞', 'xingtai': '邢台', 'nanchong': '南充', 'cangzhou': '沧州',
     'wanning': '万宁', 'qingyang': '庆阳', 'hulunbeier': '呼伦贝尔', 'weinan': '渭南', 'foshan': '佛山', 'langfang': '廊坊',
     'hangzhou': '杭州', 'shijiazhuang': '石家庄', 'tianmen': '天门', 'dongying': '东营', 'liaoyang': '辽阳', 'xuchang': '许昌',
     'dingxi': '定西', 'pingliang': '平凉', 'anshan': '鞍山', 'songyuan': '松原', 'huangshan': '黄山', 'hegang': '鹤岗',
     'kaifeng': '开封', 'rizhao': '日照', 'xiangtan': '湘潭', 'beihai': '北海', 'jinzhong': '晋中', 'qiqihaer': '齐齐哈尔',
     'linyi': '临沂', 'kezilesu': '克孜勒苏', 'suizhou': '随州', 'shanwei': '汕尾', 'fuzhou': '福州', 'benxi': '本溪',
     'qingyuan': '清远', 'changzhou': '常州', 'jian': '吉安'}
from lib.region_block import city_dict

for i in city_dict:
    if i not in a.values():
        print(i)
