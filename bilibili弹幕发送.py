import requests
import time
import random

class Danmu():
    def __init__(self,roomid):
        #直播的房间号
        self.roomid = str(roomid)

        #该网址用于获取数据
        self.url_1 = 'https://api.live.bilibili.com/ajax/msg'
        #发送请求弹幕的网址
        self.url_2 = 'https://api.live.bilibili.com/msg/send'


        #账号信息
        self.cookie = {'Cookie': "CURRENT_FNVAL=16; buvid3=008D4231-7AFC-4D09-8323-CFAF12CEB4AE110261infoc; stardustvideo=1; rpdid=|(um|)m)kJ|Y0J'ulYJkRmJYl; sid=94ajspep; _uuid=EEF44977-93A2-C306-F0EC-4D1709A893DF17732infoc; LIVE_BUVID=AUTO5515679194274871; DedeUserID=29555259; DedeUserID__ckMd5=18d7f2b8c163b249; SESSDATA=e00b0307%2C1570511453%2C86a1b691; bili_jct=1a93b95633d6ce9eeb00e0496f6a024d; INTVER=1; bsource=seo_sougo; _dfcaptcha=67714864d6b0eef9f3e3604bd8e48a76; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1568000781,1568000821; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1568000849"}

        #模拟浏览器
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'}

        #直播间信息
        self.form_1 = {
            'csrf_token': '1a93b95633d6ce9eeb00e0496f6a024d',
            'roomid': self.roomid,
            'token':''
        }

        self.timestamp = str(int(time.time()))

    def Send(self):
        while True:
            #请求弹幕信息，服务器会返回弹幕
            html_1 = requests.post(self.url_1,data = self.form_1,headers = self.header)

            #提取弹幕信息，每个text_1里面有10条弹幕
            text_1 = list(map(lambda ii:html_1.json()['data']['room'][ii]['text'],range(2)))

            #复制别人的弹幕，一般肤质最后几个，目的是避免重复，采用随机方式
            message = text_1[random.randint(0,1)]
            print(message)

            #需要提交的数据，提交给服务器
            form_2 = {
                'color': '16777215',#颜色可以改变
                'fontsize': '25',
                'mode': '1',
                'msg': message,
                'rnd': self.timestamp,#每次刷新网页的时间/可以不变
                'roomid': self.roomid,
                'bubble': '0',
                'csrf_token': '1a93b95633d6ce9eeb00e0496f6a024d',
                'csrf': '1a93b95633d6ce9eeb00e0496f6a024d'
            }

            #发射弹幕post方法
            requests.post(self.url_2,data = form_2,headers = self.header,cookies = self.cookie)

            #弹幕每隔5秒才能继续，bilibili规定
            time.sleep(6)

sendmessage = Danmu(21403274)
sendmessage.Send()