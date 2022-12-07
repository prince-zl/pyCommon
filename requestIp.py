import requests
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import os
import traceback


class RequestApi:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        self.url = 'http://39.105.223.183:1508'

        self.init_ip()
        sched = BlockingScheduler()
        sched.add_job(self.init_ip, 'interval', minutes=30)
        sched.start()

    def init_ip(self):
        time_date = time.strftime(
            '%Y-%m-%d',   time.localtime(time.time()))
        time_date_min = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        if (not os.path.exists('请求日志')):
            os.mkdir('请求日志')
        try:
            ip = self.commonGet()
            str_con = time_date_min + '【请求成功】'+'当前IP：' + ip
            with open(r'请求日志/'+time_date+'.txt', 'a', encoding='utf-8') as file_obj:
                file_obj.write(str_con+'\n')
                print(str_con)
        except:
            with open(r'请求日志/'+time_date+'.txt', 'a', encoding='utf-8') as file_obj:
                traceback.print_exc(file=file_obj)
            print(time_date,'请求失败，请查看日志')

    def commonGet(self):
        res = requests.get(self.url, headers=self.headers)
        res.encoding = "utf8"
        return res.text


if __name__ == '__main__':
    RequestApi()
