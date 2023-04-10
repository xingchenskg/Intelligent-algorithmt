import requests
import json
if __name__ == '__main__':
    #url获取
    post_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    #url参数处理
    kw=input('enter a word:')
    param={
            'op':'keyword',
            'cname':'',
            'pid':'',
            'keyword': kw,
            'pageIndex':'1',
            'pageSize': '10'
    }
    headers={
        'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    respsonse=requests.post(url=post_url,data=param,headers=headers)
    #获取响应数据
    kfc_data=respsonse.json()
    #永久保存数据
    fp=open('./'+kw+'kfc.json','w',encoding='utf-8')
    json.dump(kfc_data,fp=fp,ensure_ascii=False)
    print("保存成功！")
