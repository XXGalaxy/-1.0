# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:08:29 2018

@author: X
"""

import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=lincang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

def weather(a,b):
    print('7月',a,'日的天气情况是:')
    print('气温:',data['list'][b]['main']['temp'])
    print('天气:',data['list'][b]['weather'][0]['main'])
    print('气压:',data['list'][b]['main']['pressure'])
    print('最高温:',data['list'][b]['main']['temp_max'])
    print('最低温:',data['list'][b]['main']['temp_min'])
    print('~'*30)
weather(17,2)
weather(18,10)
weather(19,18)
weather(20,26)
weather(21,34)

print('7月17日——7月21日的天气的温度折线图为：')
def chart(a):
    return '-'*int(data['list'][a]['main']['temp'])
print('7月17日',chart(2))
print('7月17日',chart(10))
print('7月17日',chart(18))
print('7月17日',chart(26))
print('7月17日',chart(34))

def ls(a):
    return data['list'][a]['main']['temp']
a1=ls(2)
a2=ls(10)
a3=ls(18)
a4=ls(26)
a5=ls(34)
b=[a1,a2,a3,a4,a5]
b.append(23)
print('7月17日——7月21日的天气温度从底到高排序为：')
print(sorted(b))
