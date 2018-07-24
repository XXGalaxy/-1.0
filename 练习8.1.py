# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 20:21:46 2018

@author: X
"""

import urllib.request as r#导入联网工具包，名为为r    
f=open('湖北淘宝数据.txt','a',encoding='utf-8') 
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E9%9D%92%E5%B2%9B&s={}&ajax=true'
for i in range(0,100):
    url1=url.format(i*44)
    try:
        data=r.urlopen(url1).read().decode('utf-8','ignore')
        f.write(data+'\n')
        print('第{}行'.format(i+1))
    except Exception as err:
        print('输出有误')
f.close()