import requests
from lxml import etree
import time
# 用于爬取可用的代理ip

class daili:

    # 1.发送请求，获取响应
    def send_request(self, page):
        print("=============正在抓取第{}页===========".format(page))
        # 目标网页，添加headers参数
        base_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

        # 发送请求：模拟浏览器发送请求，获取响应数据
        response = requests.get(base_url, headers=headers)
        data = response.content.decode()
        time.sleep(1)

        return data

    # 2.解析数据
    def parse_data(self, data):

        # 数据转换
        html_data = etree.HTML(data)
        # 分组数据
        parse_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')

        return parse_list

    # 4.检测代理IP
    def check_ip(self, proxies_list):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

        can_use = []
        for proxies in proxies_list:
            try:
                response = requests.get('https://www.baidu.com/', headers=headers, proxies=proxies, timeout=0.1)
                if response.status_code == 200:
                    can_use.append(proxies)

            except Exception as e:
                print(e)

        return can_use

    # 5.保存到文件
    def save(self, can_use):

        file = open('IP.txt', 'w')
        for i in range(len(can_use)):
            s = str(can_use[i]) + '\n'
            file.write(s)
        file.close()

    # 实现主要逻辑
    def run(self):
        proxies_list = []
        # 实现翻页，我这里只爬取了四页（可以修改5所在的数字）
        for page in range(1, 50):
            data = self.send_request(page)
            parse_list = self.parse_data(data)
            # 3.获取数据
            for tr in parse_list:
                proxies_dict = {}
                http_type = tr.xpath('./td[4]/text()')
                ip_num = tr.xpath('./td[1]/text()')
                port_num = tr.xpath('./td[2]/text()')

                http_type = ' '.join(http_type)
                ip_num = ' '.join(ip_num)
                port_num = ' '.join(port_num)

                proxies_dict[http_type] = ip_num + ":" + port_num

                proxies_list.append(proxies_dict)

        print("获取到的代理IP数量：", len(proxies_list))

        can_use = self.check_ip(proxies_list)

        print("能用的代理IP数量：", len(can_use))
        print("能用的代理IP:", can_use)

        self.save(can_use)


if __name__ == "__main__":
    dl = daili()
    dl.run()

