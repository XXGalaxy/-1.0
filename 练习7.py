# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:46:59 2018
1、使用多选其一，完成天气提醒，淘宝客户端
2、一定要多次使用for循环，偶尔使用while循环，在淘宝客户端中
3、使用到break或者continue，在淘宝客户端中

@author: X
"""
#天气建议
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
    a=str(data['list'][b]['weather'][0]['main'])
    if a=='Clear':
        print('来自QQ的建议：大太阳！今天不约，会晒黑的！')
    elif a=='Clouds':
        print('来自QQ的建议：天阴啦！恭喜你可以放心出门了！')
    elif a=='Rain':
        print('来自QQ的建议：下雨啦！你妈喊你回家收衣服！')
    print('~'*30)
weather(17,2)
weather(18,10)
weather(19,18)
weather(20,26)
weather(21,34)

#for循环
import urllib.request as q#导入联网工具包，名为为r
data=q.urlopen('https://s.taobao.com/search?q=%E8%A1%A3%E6%9C%8D&imgfile=&js=1&style=grid&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180718&ie=utf8&ajax=true').read().decode('utf-8','ignore')

import json#将字符串转换为字典
data=json.loads(data)

#获取商品信息
def mess():
    for x in range(0,36):
        title=data['mods']['itemlist']['data']['auctions'][x]['title']
        price=data['mods']['itemlist']['data']['auctions'][x]['view_price']
        loc=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
        sales=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        print('第'+str(x+1)+'件商品：')
        print('商品标题：'+str(title))
        print('商品价格：'+str(price))
        print('卖家位置：'+str(loc))
        print('商品销量：'+str(sales))
        if((x+1)%4==0):
            print('~'*50)
mess()
#包邮的商品
print('包邮的商品有：')
for x in range(0,35):
    if float(data['mods']['itemlist']['data']['auctions'][x]['view_fee'])==0.00:
        print('第'+str(x+1)+'件：')
#商品价格从高到低排序
print('所有商品的价格如下：')
ls=[]
for x in range(0,35):
    pri=float(data['mods']['itemlist']['data']['auctions'][x]['view_price'])
    ls.append(pri)
print(ls)
print('价格由低到高排序如下：')
a=sorted(ls)
print(a)
print('价格由高到低排序如下：')
b=reversed(a)
print(list(b))

ls1=[]    
def sales():
    for x in range(0,36):
        sales=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        y=int(sales[0:-3])
        ls1.append(y)
    return ls1
sales()
a1=sorted(ls1)
print('按商品销量排序为：')
print(a1)

for i in range(35):
    if i==5:break
    if i==10:continue
    print('商品标题：'+data['mods']['itemlist']['data']['auctions'][i]['title'])
    print('商品价格：'+data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    print('商品销量：'+data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    a=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    if a>str(10000):
        print('TB建议：传说中TB爆款！')
    elif a<str(500):
        print('TB建议：这就不容易撞衫！')
    else:
        print('TB建议：大家眼光都不错哦！')
    
                
                