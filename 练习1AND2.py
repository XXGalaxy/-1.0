# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
Weather=['35°','36°','37°','38°','32°','30°']
print('Wednesday'+str(Weather[2]))

Weather={'Mon':['35°','多云'],
         'Tue':['36°','晴'],
         'Wed':['37°','晴'],
         'Tur':['38°','晴'],
         'Fri':['35°','小雨'],
         'Sat':['32°','大雨'],
         'Sun':['30°','大雨']}
print('Wednesday’s weather is:'
      +Weather['Wed'][0]
      +Weather['Wed'][1])