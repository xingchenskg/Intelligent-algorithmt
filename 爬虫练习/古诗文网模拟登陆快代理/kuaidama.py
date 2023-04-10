import requests
import base64
import json
def base64_api(uname, pwd,img,typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd,"image": b64,"typeid": typeid}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""
# def reportError(id):
#     data = {"id": id}
#     result = json.loads(requests.post("http://api.kuaishibie.cn/reporterror.json", json=data).text)
#     # print(result)
#     if result['success']:
#         return "成功!!!"
#     else:
#         return result["message"]
#     return ""