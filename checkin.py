import requests
import os

cookie = os.getenv('GLADOS_COOKIE')
headers = {
    "referrer": "https://glados.network/console/checkin",
    "authority": "glados.network",
    "user-agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "cookie": cookie
}

r = requests.post('https://glados.network/api/user/checkin',
                  data={'token': "glados.network"},
                  headers=headers)
data = r.json()

if data['code'] != 0:
    print('签到失败', data['message'])
else:
    print(data['code'], data['message'])
