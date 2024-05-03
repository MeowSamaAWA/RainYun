import requests
import json

url = "https://api.v2.rainyun.com/user/reward/tasks"
task = json.dumps({
    "task_name": "每日签到"
})
headers = {
    'x-api-key': 'ApiKey',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Content-Type': 'application/json'
}

request = requests.request("post", url, headers=headers, data=task)
if request.status_code == '200':
    print("状态" + request.text)
else:
    print("状态" + request.text)