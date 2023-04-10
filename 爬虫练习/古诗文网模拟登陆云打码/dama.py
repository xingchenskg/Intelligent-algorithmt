import json
import requests
import base64


class YdmVerify(object):
    _nom_url = "https://www.jfbym.com/api/YmServer/verifyapi"
    _fun_url = "https://www.jfbym.com/api/YmServer/funnelapi"

    _token = ""
    _headers = {
        'Content-Type': 'application/json'
    }

    def common_verify(self, image_content, verify_type="10101"):
        # 英文数字,中文汉字,纯英文,纯数字,任意特殊字符
        # 请保证购买相应服务后请求对应 verify_type
        # verify_type="10101" 单次积分
        print(base64.b64encode(image_content).decode())
        payload = {
            "image": base64.b64encode(image_content).decode(),
            "token": self._token,
            "type": verify_type
        }
        resp = requests.post(self._nom_url, headers=self._headers, data=json.dumps(payload))
        print(resp.text)
        return resp.json()['data']['data']

    def slide_verify(self, slide_image, background_image, verify_type="20101"):
        # 通用滑块
        # 请保证购买相应服务后请求对应 verify_type
        # verify_type="20101" 单次积分
        # slide_image 需要识别图片的小图片的base64字符串
        # background_image 需要识别图片的背景图片的base64字符串(背景图需还原)
        payload = {
            "slide_image": base64.b64encode(slide_image).decode(),
            "background_image": base64.b64encode(background_image).decode(),
            "token": self._token,
            "type": verify_type
        }
        resp = requests.post(self._nom_url, headers=self._headers, data=json.dumps(payload))
        print(resp.text)
        return resp.json()['data']['data']

    def click_verify(self, image, extra=None, verify_type=30001):
        # 点选,点选+额外参数
        # 请保证购买相应服务后请求对应 verify_type
        # verify_type="30001" 单次积分 点选
        # verify_type="30002" 单次积分 点选+需要按某种语义点选

        # 注意:
        # 例如 :extra="请_点击_与小体积黄色物品有相同形状的大号物体。"
        # 例如 :extra="请点击正向的大写V。"
        # 例如 请依次点击 "鹤" "独" "剩" 这种 转换成:extra="鹤,独,剩"
        # 例如 拖动交换2个图块复原图片 这种 转换成:extra="拖动交换2个图块复原图片"
        # 如有其他未知类型,请联系我们

        payload = {
            "image": base64.b64encode(image).decode(),
            "token": self._token,
            "type": verify_type
        }
        print(base64.b64encode(image).decode())
        if extra:
            payload['extra'] = extra
            payload['type'] = str(int(payload['type']) + 1)
        resp = requests.post(self._nom_url, headers=self._headers, data=json.dumps(payload))
        print(resp.text)
        return resp.json()['data']['data']

    def hcaptcha_verify(self, site_key, site_url, verify_type="50001"):
        # Hcaptcha
        # 请保证购买相应服务后请求对应 verify_type
        # verify_type="50001"
        payload = {
            "site_key": site_key,
            "site_url": site_url,
            "token": self._token,
            "type": verify_type
        }
        resp = requests.post(self._fun_url, headers=self._headers, data=json.dumps(payload))
        print(resp.text)
        return resp.json()['data']['data']