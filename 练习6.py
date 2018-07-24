# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:05:53 2018
获取所有的商品价格并且给商品排序，从高到低的排序
按照销量排序
商品过滤，只要15天退款或者包邮的商品信息，显示
@author: X
"""

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
        print('商品名：'+str(title))
        print('商品价格：'+str(price))
        print('卖家位置：'+str(loc))
        print('商品销量：'+str(sales))
        if((x+1)%4==0):
            print('~'*50)
mess()

#按价格排序：   
ls=[]
def price():
    for x in range(0,36):
        price=float(data['mods']['itemlist']['data']['auctions'][x]['view_price'])
        ls.append(price)
    return ls
price()
a=sorted(ls)
b=list(reversed(a))
print('商品价格从高到低排序为：')
print(b)

#按销量排序：
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
        
#商品过滤，过滤出包邮的商品
print('其中包邮商品的信息如下：')
def fee(y):
    title=data['mods']['itemlist']['data']['auctions'][x]['title']
    price=data['mods']['itemlist']['data']['auctions'][x]['view_price']
    loc=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
    sales=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
    print('第'+str(y+1)+'件商品：')
    print('商品名：'+str(title))
    print('商品价格：'+str(price))
    print('卖家位置：'+str(loc))
    print('商品销量：'+str(sales))
for x in range(0,36):
    if float(data['mods']['itemlist']['data']['auctions'][x]['view_fee'])==0.00:
        fee(x)


    