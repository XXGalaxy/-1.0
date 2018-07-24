# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:12:02 2018

保存淘宝数据（小组项目）
1、每个组员爬去某个商品的100页数据，每个组员爬取的不同的城市
2、保存淘宝商品信息，并且保存为csv格式

@author: X
"""

import urllib.request as r
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E9%9D%92%E5%B2%9B&s={}&ajax=true'
f=open('淘宝数据.txt','w',encoding='utf-8')
for i in range(0,100):
    url1=url.format(44*i)
    data=r.urlopen(url1).read().decode('utf-8','ignore')  
    f.write(data+'\n')
f.close()
    


