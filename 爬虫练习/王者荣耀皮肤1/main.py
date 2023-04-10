import requests
from lxml import etree

if __name__ == '__main__':
    url="hhttps://pvp.qq.com/web201605/herolist.shtml"
    data={

    }
    headers={
        "user - agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 108.0.0.0Safari / 537.36Edg / 108.0.1462.54"
    }
    response=requests.post(url=url,headers=headers).content
    print(response)
