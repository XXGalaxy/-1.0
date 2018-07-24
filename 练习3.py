# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:47:54 2018

@author: user
"""

import urllib.request as q
data=q.urlopen('http://api.openweathermap.org/data/2.5/weather?q=lincang&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')

import json
data=json.loads(data)

print('temp:'+str(data['main']['temp']))
print('description:'+str(data['weather'][0]['description']))
print('speed:'+str(data['wind']['speed']))