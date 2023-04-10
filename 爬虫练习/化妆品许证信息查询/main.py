from webbrowser import Mozilla

import requests
import json

if __name__ == '__main__':
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    data = {
        'on': ' true',
        'page': ' 1',
        'pageSize': ' 15',
        'productName': '',
        'conditionType': ' 1',
        'applyname': '',
        'applysn': '',
    }
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    id_list=[]#存储id值
    all_detail_json=[]#存储企业详细信息
    json_ids=requests.post(url=post_url,data=data,headers=header).json()
    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        id_data={
            'id':id
        }
        print(id_data)
        detail_json=requests.post(url=url,data=data,headers=header).json()
        print(detail_json)
        all_detail_json.append(detail_json)
    fp=open('./化妆品许可证.json','w',encoding='utf-8')
    json.dump(all_detail_json,fp=fp,ensure_ascii=False)
    print('保存成功！')


