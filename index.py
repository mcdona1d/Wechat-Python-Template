#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import web
import time
import hashlib
from lxml import etree
 
 
urls = (
'/weixin','WeixinInterface'
)
 

def _check_hash(data):
    #sha1加密算法
    signature=data.signature
    timestamp=data.timestamp
    nonce=data.nonce
    #自己的token
    token="your_token" #这里改写你在微信公众平台里输入的token
    #字典序排序
    list=[token,timestamp,nonce]
    list.sort()
    sha1=hashlib.sha1()
    map(sha1.update,list)
    hashcode=sha1.hexdigest()
    #如果是来自微信的请求，则回复True
    if hashcode == signature:
        return True
    return False


class WeixinInterface:
 
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
 
    def GET(self):
        #获取输入参数
	data = web.input()
        if _check_hash(data):
            return data.echostr

    def POST(self):        
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml)#进行XML解析
        content=xml.find("Content").text#获得用户所输入的内容
        msgType=xml.find("MsgType").text
        fromUser=xml.find("FromUserName").text
        toUser=xml.find("ToUserName").text
        return self.render.reply_text(fromUser,toUser,int(time.time()),u"接收到的文字："+content) 
        

application = web.application(urls, globals())
if __name__ == "__main__":
    application.run()
