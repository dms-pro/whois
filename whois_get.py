import requests
import datetime
import os

APIKEY= os.environ.get('APIKEY')

url = f"https://whois-download.com/api/v1/{API_KEY}/whois/csv/2023-01-05/"
SIZE = 1000
today = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
def analyze_str(url):
    s = requests.Session()
    send_to_srv = []
    cnt = 0
    with s.get(url, headers=None, stream=True) as resp:
        for line in resp.iter_lines():
            if line:
                cnt += 1
                line = line.decode('utf-8')
                tmp = {"domain": line, "registration_date": today}
                send_to_nodzilla.append(tmp)
                if cnt == SIZE:
                    yield send_to_srv
                    send_to_srv
                    cnt = 0


for batch in analyze_str(url):
    res = requests.post('http://127.0.0.1', json=batch, auth=('username1', 'password1'))
    print(res.status_code)
