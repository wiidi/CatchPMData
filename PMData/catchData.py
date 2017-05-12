# -*- coding: utf-8 -*-
"""
Created on Mon May 08 11:51:57 2017

@author: wudi1
"""
import codecs
import requests
from bs4 import BeautifulSoup
from readcityname import getCityName 
import re
import time 

#文件名为 年月日_时分
date =time.strftime('%Y%m%d_%H%M',time.localtime(time.time()))
filename='./data/'+date+'.txt'
#网址
url='http://www.pm25.in/'

f=open(filename,'wb')
#获取城市拼音
cityList=getCityName()

try:    
    for cityname in cityList:

        r=requests.get(url+cityname)
        #转为utf-8编码
        r.encoding='utf-8'
#       解析器
#        b = BeautifulSoup(r.text,'html.parser')
        b = BeautifulSoup(r.text,'lxml')
        
        ls=[]
#       城市名
        cityName=str(b.select('.city_name h2')[0].get_text().encode('utf-8'))
        ls.append(cityName)
    
        dataTime = str(b.select('.live_data_time p')[0].get_text()[7:])
        ls.append(dataTime)
        level=str(b.select('.level h4')[0].get_text().encode('utf-8').strip())
        ls.append(level)
#       写入数据        
        for l in ls:    
            f.write(l)
            f.write(' ')
            
        tables=b.select('tr')
    
#        print tables[1]
        ltr=[]
    
        for tr in tables:    
            data=tr.select('td')
            for td in data:
#               通过正则表达式，替换字符串中间的多个空格为一个空格
                ltr.append(re.sub(r"\s{2,}"," ",td.get_text().encode('utf-8').strip()))
            
            for td in ltr:
                f.write(td)
                f.write(' ')
            f.write('\r\n')
            ltr=[]
        f.write('\r\n')
finally:
    f.close()
