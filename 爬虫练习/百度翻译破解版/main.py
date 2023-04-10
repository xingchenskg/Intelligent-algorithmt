import requests

def input_words(input_key,all_word,i,a):
    if int(input_key)==1:
        fp = open('./hight.txt', 'a', encoding='utf-8')
    elif int(input_key)==2:
        fp = open('./medium.txt', 'a', encoding='utf-8')
    elif int(input_key)==3:
        fp = open('./low.txt', 'a', encoding='utf-8')
    elif int(input_key)==4:
        fp = open('./supplement.txt', 'a', encoding='utf-8')
    elif int(input_key)==5:
        fp = open('./postgraduate.txt', 'a', encoding='utf-8')
    for data in all_word:
        i = str(i)
        fp.write(i + '. ' + data['k'] + ': ' + data['v'] + '\n')
    fp.write(a + '\n')
    fp.close()

if __name__ == '__main__':
    # 1.step:获取url
    post_url = 'https://fanyi.baidu.com/sug'
    # 2.step:url伪装
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
    }
    for i in range(1, 1000):
        print(i)
        word =input("enter a word: ")

        data = {
            'kw': word
        }
        # 发送请求
        respsonse = requests.post(url=post_url, data=data, headers=headers)
        dic_obj = respsonse.json()
        all_word = dic_obj['data']
        a = '--------------------'
        for data in all_word:
            print(data['k'], data['v'])
            i = str(i)
        input_key=input("=============背诵(回车)保存(1.高频词,2.中频词,3.低频词,4.补充词,5.考研词汇):============ \n")
        if not input_key:
            print("一生二，二生三，三生万物，回归成网，万事可图也!!!")
        # elif int(input_key)==1:
        elif input_key:
            input_words(input_key,all_word,i,a)
            print("不积小流，无以成江海，不积跬步，无以至千里!!!")

