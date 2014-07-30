# -*- coding: utf-8 -*-
import urllib2
import hashlib

server_url = 'http://localhost:2985/api/wechat/index.aspx'
token = 'zhelishitoken'

timestamp = '1406619842'
nonce = '123456654321'
echostr = 'hello'

default_from_open_id = 'oLFPQjub4lnsv1uhsrZC3NUB5rnk'
default_to_open_id = 'gh_sdfasdfsadfsd'

default_text = '洋葱名片'
default_image_media_id = '123123123'
default_image_url = 'http://www.yangcong.im'
default_voice_media_id = '321312321'
default_voice_format = 'amr'
default_voice_recognition = '嗷嗷嗷嗷'
default_video_media_id = '998998998'
default_video_thumb_media_id = '992992992'
default_location_x = '23.134521'
default_location_y = '113.358803'
default_location_scale = '20'
default_location_label = '广州羊城创意园'
default_location_precision = '119.385040'
default_link_title = '洋葱名片'
default_link_description = '首款微信CRM'
default_link_url = 'http://www.yangcong.im'
default_scene_id = '1002'
default_ticket = 'ticket'


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

TEMPLATE_MSG_IMAGE = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1348831860</CreateTime>
<MsgType><![CDATA[image]]></MsgType>
<PicUrl><![CDATA[%s]]></PicUrl>
<MediaId><![CDATA[%s]]></MediaId>
<MsgId>1234567890123456</MsgId>
</xml>'''

TEMPLATE_MSG_VOICE = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1357290913</CreateTime>
<MsgType><![CDATA[voice]]></MsgType>
<MediaId><![CDATA[%s]]></MediaId>
<Format><![CDATA[%s]]></Format>
<MsgId>1234567890123456</MsgId>
</xml>'''

TEMPLATE_MSG_VOICE_RECOGNITION = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1357290913</CreateTime>
<MsgType><![CDATA[voice]]></MsgType>
<MediaId><![CDATA[%s]]></MediaId>
<Format><![CDATA[%s]]></Format>
<Recognition><![CDATA[%s]]></Recognition>
<MsgId>1234567890123456</MsgId>
</xml>'''

TEMPLATE_MSG_VIDEO = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1357290913</CreateTime>
<MsgType><![CDATA[video]]></MsgType>
<MediaId><![CDATA[%s]]></MediaId>
<ThumbMediaId><![CDATA[%s]]></ThumbMediaId>
<MsgId>1234567890123456</MsgId>
</xml>'''

TEMPLATE_MSG_LOCATION = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1351776360</CreateTime>
<MsgType><![CDATA[location]]></MsgType>
<Location_X>%s</Location_X>
<Location_Y>%s</Location_Y>
<Scale>%s</Scale>
<Label><![CDATA[%s]]></Label>
<MsgId>1234567890123456</MsgId>
</xml>'''

TEMPLATE_MSG_LOCATION_REPORT = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1234567890</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[LOCATION]]></Event>
<Latitude>%s</Latitude>
<Longitude>%s</Longitude>
<Precision>%s</Precision>
</xml>'''

TEMPLATE_MSG_LINK = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1351776360</CreateTime>
<MsgType><![CDATA[link]]></MsgType>
<Title><![CDATA[%s]]></Title>
<Description><![CDATA[%s]]></Description>
<Url><![CDATA[%s]]></Url>
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
</xml>'''

TEMPLATE_MSG_SCAN_SCENE = '''
<xml><ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1234567890</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[SCAN]]></Event>
<EventKey><![CDATA[%s]]></EventKey>
<Ticket><![CDATA[%s]]></Ticket>
</xml>'''

TEMPLATE_MSG_UNSUBSCRIBE = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1234567890</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[unsubscribe]]></Event>
</xml>'''

TEMPLATE_MSG_CLICK = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1234567890</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[CLICK]]></Event>
<EventKey><![CDATA[%s]]></EventKey>
</xml>'''

TEMPLATE_MSG_VIEW = '''
<xml>
<ToUserName><![CDATA[%s]]></ToUserName>
<FromUserName><![CDATA[%s]]></FromUserName>
<CreateTime>1234567890</CreateTime>
<MsgType><![CDATA[event]]></MsgType>
<Event><![CDATA[VIEW]]></Event>
<EventKey><![CDATA[%s]]></EventKey>
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
    print 'RESULT :'
    print xml


def send_msg_text(from_open_id, content):
    msg = TEMPLATE_MSG_TEXT % (default_to_open_id, from_open_id, content)
    send_msg(msg)


def send_msg_text_default():
    send_msg_text(default_from_open_id, default_text)


def send_msg_image(from_open_id, media_id, pic_url):
    msg = TEMPLATE_MSG_IMAGE % (default_to_open_id, from_open_id, media_id, pic_url)
    send_msg(msg)


def send_msg_image_default():
    send_msg_image(default_from_open_id, default_image_media_id, default_image_url)


def send_msg_voice(from_open_id, media_id, voice_format):
    msg = TEMPLATE_MSG_VOICE % (default_to_open_id, from_open_id, media_id, voice_format)
    send_msg(msg)


def send_msg_voice_default():
    send_msg_voice(default_from_open_id, default_voice_media_id, default_voice_format)


def send_msg_voice_recognition(from_open_id, media_id, voice_format, recognition):
    msg = TEMPLATE_MSG_VOICE_RECOGNITION % (default_to_open_id, from_open_id, media_id, voice_format, recognition)
    send_msg(msg)


def send_msg_voice_recognition_default():
    send_msg_voice(default_from_open_id, default_voice_media_id, default_voice_format, default_voice_recognition)


def send_msg_video(from_open_id, media_id, thumb_media_id):
    msg = TEMPLATE_MSG_VIDEO % (default_to_open_id, from_open_id, media_id, thumb_media_id)
    send_msg(msg)


def send_msg_video_default():
    send_msg_video(default_from_open_id, default_video_media_id, default_video_thumb_media_id)


def send_msg_location(from_open_id, x, y, scale, label):
    msg = TEMPLATE_MSG_LOCATION % (default_to_open_id, from_open_id, x, y, scale, label)
    send_msg(msg)


def send_msg_location_default():
    send_msg_location(default_from_open_id, default_location_x, default_location_y, default_location_scale,
                      default_location_label)


def send_msg_location_report(from_open_id, x, y, precision):
    msg = TEMPLATE_MSG_LOCATION_REPORT % (default_to_open_id, from_open_id, x, y, precision)
    send_msg(msg)


def send_msg_location_report_default():
    send_msg_location_report(default_from_open_id, default_location_x, default_location_y, default_location_precision)


def send_msg_link(from_open_id, title, description, url):
    msg = TEMPLATE_MSG_LINK % (default_to_open_id, from_open_id, title, description, url)
    send_msg(msg)


def send_msg_link_default():
    send_msg_link(default_from_open_id, default_link_title, default_link_description, default_link_url)


def send_msg_subscribe(from_open_id):
    msg = TEMPLATE_MSG_SUBSCRIBE % (default_to_open_id, from_open_id)
    send_msg(msg)


def send_msg_subscribe_default():
    send_msg_subscribe(default_from_open_id)


def send_msg_subscribe_scene(from_open_id, scene_id, ticket):
    msg = TEMPLATE_MSG_SUBSCRIBE_SCENE % (default_to_open_id, from_open_id, scene_id, ticket)
    send_msg(msg)


def send_msg_subscribe_scene_default():
    send_msg_subscribe_scene(default_from_open_id, default_scene_id, default_ticket)


def send_msg_scan(from_open_id):
    msg = TEMPLATE_MSG_SCAN % (default_to_open_id, from_open_id)
    send_msg(msg)


def send_msg_scan_default():
    send_msg_scan(default_from_open_id)


def send_msg_scan_scene(from_open_id, scene_id, ticket):
    msg = TEMPLATE_MSG_SCAN_SCENE % (default_to_open_id, from_open_id, scene_id, ticket)
    send_msg(msg)


def send_msg_scan_scene_default():
    send_msg_scan_scene(default_from_open_id, default_scene_id, default_ticket)


def send_msg_unsubscribe(from_open_id):
    msg = TEMPLATE_MSG_UNSUBSCRIBE % (default_to_open_id, from_open_id)
    send_msg(msg)


def send_msg_unsubscribe_default():
    send_msg_unsubscribe(default_from_open_id)


def send_msg_click(from_open_id, key):
    msg = TEMPLATE_MSG_CLICK % (default_to_open_id, from_open_id, key)
    send_msg(msg)


def send_msg_click_default(key):
    send_msg_click(default_from_open_id, key)

    
def send_msg_view(from_open_id, view):
    msg = TEMPLATE_MSG_VIEW % (default_to_open_id, from_open_id, view)
    send_msg(msg)


def send_msg_view_default(view):
    send_msg_view(default_from_open_id, view)
    

if __name__ == '__main__':
    valid_url_and_token()
    send_msg_subscribe_default()
    send_msg_text_default()
    send_msg_click_default('MY_CARD')
    send_msg_click_default('MY_CARD')
