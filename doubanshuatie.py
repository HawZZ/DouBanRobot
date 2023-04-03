from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import requests
import datetime

def comment_on_post():
    # 在此处添加上面的评论功能代码

    # 评论帖子的URL，每个URL用,隔开，记得url是字符串格式需要'url'
    post_urls = ['要评论的帖子的url',
                 '要评论的帖子的url',
                 '要评论的帖子的url']
    for url in post_urls:
        # 输入评论内容并提交评论，建立一个评论内容的列表
        comments = ['顶一下','顶','顶起来','刷新挽尊','再顶一下','可劲儿顶','顶起']
        # 随机选择评论内容
        comment = random.choice(comments)
        url = url + 'add_comment'
        # 随便在任一一个帖子点击提交评论后，获取到payload内容格式，将comment参数作为rv_comment的值
        payload={'ck': '你的ck值',
                 'rv_comment': comment,
                 'start': '0',
                 'submit_btn': '发送'}
        files=[

            ]
        # 在浏览器的开发者模式中，复制自己登录后的cookie到这里替换
        headers = {
            'Cookie': '你的cookie',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'
            }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        try:
          print(response.status_code,"\r\n",response.reason,"\r\n",datetime.datetime.now())
        except error:
          print ('repsonse.status_code or response.reason 找不到')
        # 增加请求间隔，随机请求间隔100~150秒，避免封号或者触发验证码
        time.sleep(random.randint(100, 150))

# 运行代码先跑一次
comment_on_post()

# 创建一个调度程序
scheduler = BlockingScheduler()

# 每隔半小时到一小时评论一轮帖子
scheduler.add_job(comment_on_post, 'interval', seconds=random.randint(1800,3600))

# 开始调度任务
scheduler.start()

