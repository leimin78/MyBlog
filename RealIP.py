__author__ = 'leimin'

# -*- coding: utf8 -*-
import urllib,json

url = "http://ip.taobao.com/service/getIpInfo.php?ip="

def ip_location(IP):
    data = urllib.urlopen( url + IP ).read()
    datadict=json.loads(data)
    attribution = datadict["data"]["country"] + datadict["data"]["city"]
    return attribution
