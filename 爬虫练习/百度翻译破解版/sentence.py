import requests
import execjs

# 解密json中的sign值
def main(sentence):
    with open('E:/仓库管理/gitee/machine-learning/爬虫练习/百度翻译破解版/code.js','r') as fp:
        js_data=fp.read()
        sign=execjs.compile(js_data).call('e',sentence)
        # print(sign)
        return sign
# 检验是否全是中文字符
def is_all_chinese(strs):
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

# 保存
def input_fp_txt(i,data_org,data_meaning):
    fp=open('./sentence.txt','a',encoding='utf-8')
    a = '--------------------'
    i=str(i)
    fp.write(i+'. '+data_org+'\n'+'\t'+data_meaning+'\n'+a+'\n')
    fp.close()

# 分析
def sentence_analysis(i,data_org,data_meaning):
    fw = open('./analysis.txt', 'a', encoding='utf-8')
    a = '--------------------'
    i = str(i)
    fw.write(i + '. ' + data_org + '\n' + '\t' + data_meaning + '\n' + a + '\n')
    fw.close()


#保存分析
def input_analysis(i,data_org,data_meaning):
    sentence_analysis(i,data_org,data_meaning)
    input_fp_txt(i,data_org,data_meaning)

#单词保存
def input_word_txt(i, data_org, data_meaning):
    fp = open('./words1.txt', 'a', encoding='utf-8')
    a = '--------------------'
    i = str(i)
    fp.write(i + '. ' + data_org + '\n' + '\t' + data_meaning + '\n' + a + '\n')
    fp.close()

if __name__ == '__main__':

    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
        'cookie':'BIDUPSID=DA4BD9173CA3D87DA18A84A79CC2657E; PSTM=1644217601; __yjs_duid=1_d8ddb53be2bee97443e91c0b98bdf19f1644218165636; BAIDUID=B6DE0C65DD265AAADC6A59700E8F890E:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; HISTORY_SWITCH=1; BDSFRCVID_BFESS=Nk-OJeC62uXMdrnDaYijTxR28z_EsPjTH6aoEZt3zXg8iNSsHSjTEG0P5U8g0KuMJXKdogKKXgOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tRk8_KtKtCI3HnRY-P4_-tAt2qoXetJyaR3n3lQvWJ5TMCo60p30Mp0v-Jrt2l3OLJuO-PF5MfQkShPC-tn0jPKU5bnmh46ZyHQWoqTM3l02VhnEe-t2ynLV34uHe4RMW23v0h7mWP02sxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjC5j5obeHAJtTn2aIOt0Tr25RrjeJrmq4bohjPF2lo9BtQmJJrf2qjVLKOUHfTGbpOW06jbDq7GQx7nQg-q3R7c0Jvffn5kb4K2-ljQhM-j0x-jLIbPVn0MW-5Y8IJ3W4nJyUPRbPnnBn-j3H8HL4nv2JcJbM5m3x6qLTKkQN3T-PKO5bRh_CFbJK8MhK-ljTRM5tAthxJJK4J3Hjb8XDvk256cOR5Jj65hWMuOKxTR5lc02HnObD_yMf7pqUJF3MA--t4kWl8ehqvMfI5wb-OdLbcxsq0x05ole-bQypouBqvi5IOMahv95h7xOKQoQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3tjjISKx-_J6LDtRcP; BAIDUID_BFESS=B6DE0C65DD265AAADC6A59700E8F890E:FG=1; APPGUIDE_10_0_2=1; ZFY=e0nR7:Bm6prK:AdxANPhhD0AXMni:ATVVRCXu7qM7OBq3E:C; BA_HECTOR=052g2k2h818hal8k0l1h980av15; BDRCVFR[xPiTFvxiYMt]=mk3SLVN4HKm; H_PS_PSSID=; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1653866857,1653872474,1653876219,1653892061; ab_sr=1.0.1_ZTQ0OGE5MGQxNDRiYTM5NDEzODk4MDgxNzljMjlmY2ZhMGE0Y2M5MzUyYjNiZWNjZTQxNDNmN2FlYTc1ODA0NDE0ZTQwNzAwMTJkNDA4MGQwYTEzMGQxY2I1YjAxZmU2ZDdjOGY2Yjk2MjQxODhlMDVkMjAzOGNmOTJkZjg2Y2Y4ZmI4N2ZjYWIxNDdjMGNlNDExMjA5MWNkODMyZmE4Yw==; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1653892946'
    }
    change={
        'l':'en',
        't':'zh'
    }
    for i in range(1,100):
        print(i)
        sentence=input('enter a sentence or word: ')
        sign = main(sentence)
        c=is_all_chinese(sentence.split())
        if c==True:
            l=change['t']
            t = change['l']
        else:
            l = change['l']
            t = change['t']
        url = 'https://fanyi.baidu.com/v2transapi?from=' + l + '&to=' + t
        data={
                'from':l,
                'to':t,
                'query': sentence,
                'simple_means_flag': 3,
                'sign': sign,
                'token': 'ce9b4a91807d8f15a75bb9ea230cae67',
                'domain': 'common'
        }
        response=requests.post(url=url,data=data,headers=headers)
        # r=response.status_code
        # print(r)
        data=response.json()
        # print(data)
        data_1=data['trans_result']
        data_2=data_1['data']
        data_3=data_2[0]
        data_meaning=data_3['dst']
        data_org=data_3['src']
        print(data_meaning)
        # 永久化储存
        in_put_fp=input('---------背诵(回车）保存(1)分析(2)并保存(3)单词保存(4)-------- \n')
        if not in_put_fp:
            print("吾心寄语:凝聚悟学，宁而致寒，寒而生冰!!!")
        elif int(in_put_fp) == 1:
            input_fp_txt(i, data_org, data_meaning)
        elif int(in_put_fp)==2:
            sentence_analysis(i,data_org,data_meaning)
        elif int(in_put_fp)==3:
            input_analysis(i, data_org, data_meaning)
        elif int(in_put_fp)==4:
            input_word_txt(i, data_org, data_meaning)