"""
A sample Hello World server.
"""
import os
import requests
from flask import Flask, render_template
from datetime import datetime
# pylint: disable=C0103
app = Flask(__name__)

url = "https://script.google.com/macros/s/AKfycbz7Y0FsXuR4k3cryp53P8RbAwxScaqkedlU9LEDi_Fg_4kOdmKg78_2peVAKhkgrQa2SA/exec"

# 发送 HTTP GET 请求


def filter_weekend(data):
    """过滤掉'星期'为'六'或'日'的记录"""
    return [entry for entry in data if entry["星期"] not in ["六", "日"]]




@app.route('/')
def hello():
    return 'ok'

@app.route('/notify')
def dutyStudentsNotify():
    job1()
    return 'ok'


def line_notify(msg):
    token = 'uRt31oA2Uw5HiRVEjwHuI1BhlkpzEvQG8zWL03kHXyw'  # 填入你的token
    url = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': 'Bearer ' + token
    }
    data = {
        'message': msg
    }
    requests.post(url, headers=headers, data=data)




# line_notify(text)

import time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def job1():
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
       # 获取 JSON 数据
       data = response.json()
       # 过滤后的数据
       filtered_data = filter_weekend(data)
       now = datetime.now()
       formatted_date = now.strftime("%Y-%m-%d")
       result = next((data for data in filtered_data if data['日期'] == formatted_date), None)
       text =f"{result['日期']}值日生為{result['值日生1']},{result['值日生2']}"
       # 打印 JSON 数据
       # print(text)
       line_notify(text)
    else:
      print(f"请求失败，状态码：{response.status_code}")
    


# scheduler = BlockingScheduler(timezone="Asia/Shanghai")
# scheduler.add_job(job1, 'cron', day_of_week='1-5', hour=8, minute=50)
# scheduler.start()

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')

