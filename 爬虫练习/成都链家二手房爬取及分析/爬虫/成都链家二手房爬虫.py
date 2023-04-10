import requests
import csv
import xlwt
from lxml import html

etree = html.etree
house_list = []
pages = range(1, 100)
city_name = {'北京': 'bj', '上海': 'sh', '成都': 'cd', '西安': 'xa', '深圳': 'sz'}
city = city_name.get(input('请输入城市名：'))
jinjiang = ['川师', '东大路', '东光小区', '东湖', '东客站', '合江亭', '红星路', '静居寺', '九眼桥', '蓝谷池',
            '莲花', '琉璃场', '攀成钢', '三官堂', '三圣乡', '沙河堡', '水碾河', '盐市口', '卓锦城']
qingyang = ['八宝街', '贝森', '草市街', '草堂', '府南新区', '光华泡小', '浣花溪', '金沙', '宽窄巷子', '人民公园',
            '蜀汉路', '太升路', '外光华', '外金沙', '万家湾', '西南财大', '优品道']
wuhou = ['草金立交', '川大', '川音', '簇桥', '高升桥', '广福桥', '航空路', '红牌楼', '华西', '火车南站', '丽都', '龙湾',
         '双楠', '桐梓林', '外双楠', '五大花园', '武侯祠', '武侯立交', '新双楠', '玉林', '紫荆', '棕北']
gaoxin = ['城南宜家', '大源', '东宛', '芳草', '高朋', '广都', '华府', '华阳', '金融城', '神仙树', '市一医院',
          '天府广场', '新北', '新会展', '衣冠庙', '远大', '中德', '中和']
chenghua = ['八里小区', '成渝立交', '东郊记忆', '动物园', '建设路', '理工大', '李家沱', '龙潭寺', '猛追湾 ', '驷马桥',
            'SM广场', '万年场', '万象城 ', '新华公园']
jinniu = ['茶店子', '成外', '抚琴小区', '高家庄', '国宾', '花牌坊', '华侨城', '花照壁', '金府', '金牛万达', '九里堤',
          '马鞍路', '沙湾', '石人小区', '蜀汉路', '天回镇', '通惠门', '营门口', '一品天下']
tianfuxinqu = ['大源', '海洋公园', '华阳', '锦江生态带', '麓湖生态城', '南湖', '彭山', '仁寿', '四河', '新会展',
               '雅居乐']
gaoxinxi = ['高新西', '中海国际']
shuangliu = ['东升镇', '公兴', '航空港', '花源', '蛟龙港', '警院', '九龙湖', '牧马山', '双流城区', '文星镇']
wenjiang = ['光华大道沿线', '国色天乡', '花都大道', '蛟龙港', '温江大学城', '温江老城', '温江新城', '永宁', '珠江新城']
pidu = ['成外', '红光', '郫县城区', '郫县万达', '橡树湾', '犀浦']
longquanyi = ['大面', '东山', '航天', '洪河', '龙泉驿城区', '十陵', '西河', '阳光城']
xindu = ['保利公园', '大丰', '毗河', '新都城区']
tianfuxinqunanjiang = ['麓山']
qingbaijiang = ['青白江']
dujiangyan = ['都江堰', '青城山']
pengzhou = ['彭州']
jianyang = ['城北片区', '城东片区', '城南片区', '城西片区', '城中片区', '东溪片区', '高铁新区', '河东新区', '石桥片区']
xinjin = ['牧马山', '普兴', '五津', '新津']
suizhou = ['祟州']
dayi = ['大邑']
jintang = ['金堂']
pujiang = ['浦江']
qiongxia = ['邛峡']
for page in pages:
    url = f'https://{city}.lianjia.com/ershoufang/pg{page}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/110.0.0.0 Safari/537.36'}

    resp = requests.get(url, headers=headers)

    parser = etree.HTMLParser(encoding='utf-8')
    tree = etree.XML(resp.text, parser=parser)

    elements = tree.xpath('//*[@id="content"]/div[1]/ul/li')
    for element in elements:
        img_url_list = tree.xpath("//*[@id='content']/div[1]/ul/li/a/img[2]/@data-original")
        count = 0
        for img_url in img_url_list:
            resp = requests.get(img_url)
            count += 1
            resp_con = resp.content
            pic_f = open(f'house{count}.jpg', 'wb')
            pic_f.write(resp_con)
        info_list = element.xpath('./div[1]/div[3]/div/text()')
        if info_list:
            zone = element.xpath('./div[1]/div[2]/div/a[2]/text()')[0]
            name = element.xpath('./div[1]/div[2]/div/a[1]/text()')[0]
            price = element.xpath('./div[1]/div[6]/div[1]/span/text()')[0]
            price_u = element.xpath('./div[1]/div[6]/div[2]/span/text()')[0]
            L = info_list[0].split('|')
            if len(L) >= 7:
                model = L[0].strip()
                area = L[1].strip()
                direction = L[2].strip()
                perfect = L[3].strip()
                floor = L[4].strip()
                year = L[5].strip()
                h_type = L[6].strip()
                if zone in jinjiang:
                    suoshu = '锦江'
                elif zone in qingyang:
                    suoshu = '青羊'
                elif zone in wuhou:
                    suoshu = '武侯'
                elif zone in gaoxin:
                    suoshu = '高新'
                elif zone in chenghua:
                    suoshu = '成华'
                elif zone in jinniu:
                    suoshu = '金牛'
                elif zone in tianfuxinqu:
                    suoshu = '天府新区'
                elif zone in gaoxinxi:
                    suoshu = '高新西'
                elif zone in shuangliu:
                    suoshu = '双流'
                elif zone in wenjiang:
                    suoshu = '温江'
                elif zone in pidu:
                    suoshu = '郫都'
                elif zone in longquanyi:
                    suoshu = '龙泉驿'
                elif zone in xindu:
                    suoshu = '新都'
                elif zone in tianfuxinqunanjiang:
                    suoshu = '天府新区南江'
                elif zone in qingbaijiang:
                    suoshu = '青白江'
                elif zone in dujiangyan:
                    suoshu = '都江堰'
                elif zone in pengzhou:
                    suoshu = '彭州'
                elif zone in jianyang:
                    suoshu = '简阳'
                elif zone in xinjin:
                    suoshu = '新津'
                elif zone in suizhou:
                    suoshu = '祟州'
                elif zone in dayi:
                    suoshu = '大邑'
                elif zone in jintang:
                    suoshu = '金堂'
                elif zone in pujiang:
                    suoshu = '蒲江'
                elif zone in qiongxia:
                    suoshu = '邛峡'
                else:
                    suoshu = zone
                house_list.append(
                    [suoshu, zone, name, model, direction, floor, perfect, area, price, price_u, year, h_type])
# write = csv.writer(open('house.csv', 'w', encoding='utf-8'))
# write.writerow(
#     ['所属区', '市区', '小区', '户型', '朝向', '楼层', '装修情况', '面积', '价格(万元)', '单价', '年份', '房型'])
# write.writerows(house_list)


