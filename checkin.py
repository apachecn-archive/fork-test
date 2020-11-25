import requests
import os

cookie = os.getenv('GLADOS_COOKIE')
server_sckey = os.getenv('SERVER_SCKEY')
headers = {
    "referrer": "https://glados.network/console/checkin",
    "authority": "glados.network",
    "user-agent":
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "cookie": cookie
}

r = requests.post('https://glados.network/api/user/checkin',
                  data={'token': "glados_network"},
                  headers=headers)

data = r.json()
text = '签到失败'
desp = 'https://glados.network/console/checkin'

if data['code'] != 0:
    print(text, data['message'])
    url = f'https://sc.ftqq.com/{server_sckey}.send?text={text}&desp={desp}'
    requests.get(url)
else:
    print(data['code'], data['message'])
