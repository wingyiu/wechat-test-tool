# -*- coding: utf-8 -*-
import urllib2
import hashlib

server_url = 'http://localhost:2985/api/wechat/index.aspx'
token = 'zhelishitoken'
timestamp = '1406619842'
nonce = '123456654321'
echostr = 'hello'

default_from_open_id = 'gh_sfaqer134sdfa'
default_to_open_id = 'gh_sdfasdfsadfsd'

TEMPLATE_REQUEST_URL = '%s?signature=%s&timestamp=%s&nonce=%s&echostr=%s'

TEMPLATE_MSG_TEXT = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>123456789</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[%s]]></Content>
<MsgId>1234567890123456</MsgId>
</xml>'''

TEMPLATE_MSG_SUBSCRIBE = '''
<xml><ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1234567890</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[subscribe]]></Event>
</xml>'''

TEMPLATE_MSG_SUBSCRIBE_SCENE = '''
<xml><ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1234567890</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[subscribe]]></Event>
<EventKey><![CDATA[qrscene_%s]]></EventKey>
<Ticket><![CDATA[%s]]></Ticket>
</xml>'''


TEMPLATE_MSG_SCAN = '''
<xml><ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1234567890</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[SCAN]]></Event>
<EventKey><![CDATA[%s]]></EventKey>
<Ticket><![CDATA[%s]]></Ticket>
</xml>'''


def request_url():
    tmp_arr = sorted([token, timestamp, nonce])
    tmp_str = ''.join(tmp_arr)
    signature = hashlib.sha1(tmp_str).hexdigest()
    return TEMPLATE_REQUEST_URL % (server_url, signature, timestamp, nonce, echostr)


def valid_url_and_token():
    print 'GET %s' % request_url()
    response = urllib2.urlopen(request_url())
    xml = response.read()
    print 'RESULT:'
    print xml


def send_msg(msg):
    print 'POST %s' % request_url()
    print msg
    req = urllib2.Request(request_url(), msg)
    response = urllib2.urlopen(req)
    xml = response.read()
    print 'RESULT:'
    print xml


def send_msg_text(from_open_id, content):
    msg = TEMPLATE_MSG_TEXT % (default_to_open_id, from_open_id, content)
    send_msg(msg)


def send_msg_text_default(content):
    msg = TEMPLATE_MSG_TEXT % (default_to_open_id, default_from_open_id, content)
    send_msg(msg)


def send_msg_subscribe_default(scene_id='', ticket='ticket'):
    if scene_id:
        msg = TEMPLATE_MSG_SUBSCRIBE_SCENE % (default_to_open_id, default_from_open_id, scene_id, ticket)
    else:
        msg = TEMPLATE_MSG_SUBSCRIBE % (default_to_open_id, default_from_open_id)
    send_msg(msg)


if __name__ == '__main__':
    valid_url_and_token()
    send_msg_subscribe_default()
    send_msg_text_default('来自自动测试工具')
