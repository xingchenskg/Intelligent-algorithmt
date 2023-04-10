
import requests
from lxml import etree

# # 确定url
# url = 'https://ke-image.ljcdn.com/110000-inspection/pc1_HvoCRfKpK.jpg!m_fill,w_250,h_182,l_fbk,o_auto'
# resp = requests.get(url)
#
# # 转换为二进制数据
# resp_con = resp.content
# # print(resp_con)
#
# pic_f = open('pic1.jpg', 'wb')
# pic_f.write(resp_con)

url = 'https://cd.zu.ke.com/zufang/'
img_list = []
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36','Cookie':'lianjia_uuid=3d928fb9-0c20-4176-87df-44ce04d95135; lianjia_ssid=e22d9901-767d-4573-ba21-d4a5878757b3; select_city=510100; GUARANTEE_BANNER_SHOW=true; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiN2FjZDNkYTQ0YTdhY2U3MGRjMGRkODk0OThjODNkZWFhN2RmNWMxMzUyYmNiMDIyYWQ0NjA4NjI3YmNkODE4OGJmZWM3MmIzOWE3OWZiNDc4M2Y2OTk4NWMwZGJkMDNhMDExMGI4OTA3ZDFhNTUwNjM1NGUyYWJlOWUzZjY3ZDMyOGY1YzI3ZGFiNjRlOWNlNzE3MmQyYzI2YmQxNjlhZGJmNWI3NjI3NmE3NWMyOWM2YzdhYjdjZjA3NzAxNTA3OGJkMzBjNWM4OGMzYTFiYmQ0NThjNzc5ZTUxNTZjYjY2OTM5NTQxMjg0MTExNDI4ZGRjMjU0OTdhOWM2N2NlMlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhMmI4ZmM3Y1wifSIsInIiOiJodHRwczovL2NkLnp1LmtlLmNvbS96dWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0='}
resp = requests.get(url, headers=headers)

# 确定编码
parser = etree.HTMLParser(encoding='utf-8')

# 建立tree对象
tree = etree.XML(resp.text, parser=parser)

img_url_list = tree.xpath('//*[@id="content"]/div[1]/div[1]/div/a/img/@data-src')
print(img_url_list)
cont = 0
for img_url in img_url_list:
    cont += 1
    resp = requests.get(img_url)
    resp_con = resp.content
    pic_f = open(f'img\\pic{cont}.jpg', 'wb')
    pic_f.write(resp_con)
