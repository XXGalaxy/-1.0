# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:44:59 2018
练习题4：
1.打印每天18点的天气信息，温度，情况，气压，最高温度，最低温度
2.写出英文版的天气-天气情况，用户输入英文   application应用
3.打印温度折线图
    1----------
    2--------------------
    3-------
    4----------
4.获取所有的温度，并且排序（sorted([1,4,-1,8])##########使用此方法排序）
5.友情提示，根据温度提示穿衣，打伞，出门(可选)

全球5天天气
@author: Administrator
"""
import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=lincang,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)
#第一题
print('7月17日的天气状况：')
print('温度:'+str(data['list'][2]['main']['temp']))
print('情况:'+str(data['list'][2]['weather'][0]['description']))
print('气压:'+str(data['list'][2]['main']['pressure']))
print('最高温度:'+str(data['list'][2]['main']['temp_max']))
print('最低温度:'+str(data['list'][2]['main']['temp_min']))
print('  ')
print('7月18日的天气状况：')
print('温度:'+str(data['list'][10]['main']['temp']))
print('情况:'+str(data['list'][10]['weather'][0]['description']))
print('气压:'+str(data['list'][10]['main']['pressure']))
print('最高温度:'+str(data['list'][10]['main']['temp_max']))
print('最低温度:'+str(data['list'][10]['main']['temp_min']))
print('  ')
print('7月19日的天气状况：')
print('温度:'+str(data['list'][18]['main']['temp']))
print('情况:'+str(data['list'][18]['weather'][0]['description']))
print('气压:'+str(data['list'][18]['main']['pressure']))
print('最高温度:'+str(data['list'][18]['main']['temp_max']))
print('最低温度:'+str(data['list'][18]['main']['temp_min']))
print('  ')
print('7月20日的天气状况：')
print('温度:'+str(data['list'][26]['main']['temp']))
print('情况:'+str(data['list'][26]['weather'][0]['description']))
print('气压:'+str(data['list'][26]['main']['pressure']))
print('最高温度:'+str(data['list'][26]['main']['temp_max']))
print('最低温度:'+str(data['list'][26]['main']['temp_min']))
print('  ')
print('7月21日的天气状况：')
print('温度:'+str(data['list'][34]['main']['temp']))
print('情况:'+str(data['list'][34]['weather'][0]['description']))
print('气压:'+str(data['list'][34]['main']['pressure']))
print('最高温度:'+str(data['list'][34]['main']['temp_max']))
print('最低温度:'+str(data['list'][34]['main']['temp_min']))
print('  ')
print('  ')
#第二题

input=input('Please input city:')
print(str(input))
print('The weather of 7.17:')
print('temp:'+str(data['list'][2]['main']['temp']))
print('description:'+str(data['list'][2]['weather'][0]['main']))
print('pressure:'+str(data['list'][2]['main']['pressure']))
print('temp_max:'+str(data['list'][2]['main']['temp_max']))
print('temp_min:'+str(data['list'][2]['main']['temp_min']))
print('  ')
print('The weather of 7.18:')
print('temp:'+str(data['list'][10]['main']['temp']))
print('description:'+str(data['list'][10]['weather'][0]['main']))
print('pressure:'+str(data['list'][10]['main']['pressure']))
print('temp_max:'+str(data['list'][10]['main']['temp_max']))
print('temp_min:'+str(data['list'][10]['main']['temp_min']))
print('  ')
print('The weather of 7.19:')
print('temp:'+str(data['list'][18]['main']['temp']))
print('description:'+str(data['list'][18]['weather'][0]['main']))
print('pressure:'+str(data['list'][18]['main']['pressure']))
print('temp_max:'+str(data['list'][18]['main']['temp_max']))
print('temp_min:'+str(data['list'][18]['main']['temp_min']))
print('  ')
print('The weather of 7.20:')
print('temp:'+str(data['list'][26]['main']['temp']))
print('description:'+str(data['list'][26]['weather'][0]['main']))
print('pressure:'+str(data['list'][26]['main']['pressure']))
print('temp_max:'+str(data['list'][26]['main']['temp_max']))
print('temp_min:'+str(data['list'][26]['main']['temp_min']))
print('  ')
print('The weather of 7.21:')
print('temp:'+str(data['list'][34]['main']['temp']))
print('description:'+str(data['list'][34]['weather'][0]['main']))
print('pressure:'+str(data['list'][34]['main']['pressure']))
print('temp_max:'+str(data['list'][34]['main']['temp_max']))
print('temp_min:'+str(data['list'][34]['main']['temp_min']))
print('  ')
print('  ')
#第三题
a=data['list'][2]['main']['temp']
b=data['list'][10]['main']['temp']
c=data['list'][18]['main']['temp']
d=data['list'][26]['main']['temp']
e=data['list'][34]['main']['temp']
a1=str('-')*int(a)
b1=str('-')*int(b)
c1=str('-')*int(c)
d1=str('-')*int(d)
e1=str('-')*int(e)
print('7月17日——7月21日的天气的温度折线图为：')
print('7月17日'+a1)
print('7月18日'+b1)
print('7月19日'+c1)
print('7月20日'+d1)
print('7月21日'+e1)

#第四题
list=[a,b,c,d,e]
print('7月17日——7月21日的天气温度从底到高排序为：')
print(sorted(list[0:4]))













  
