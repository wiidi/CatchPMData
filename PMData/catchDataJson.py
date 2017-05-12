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
import json
import collections

#文件名为 年月日_时分
date =time.strftime('%Y%m%d_%H%M',time.localtime(time.time()))
filename='./data/'+date+'.json'
#网址
url='http://www.pm25.in/'

f=open('./data/data1.json','wb')
f.write('{')
#获取城市拼音
cityList=getCityName()

dictall={}
dictcity={}
#dictpoint={}

#有序字典
dictpoint=collections.OrderedDict()
listcity=[]
valuelist=['监测点','AQI','空气质量指数类别','首要污染物','PM2.5细颗粒物',
'PM10可吸附物','CO一氧化碳','NO2二氧化氮','O3臭氧1小时平均','O3臭氧8小时平均','SO2二氧化硫']

try:    
    for cityname in cityList:
        r=requests.get(url+cityname)
        #转为utf-8编码
        r.encoding='utf-8'
#       解析器
#        b = BeautifulSoup(r.text,'html.parser')
        b = BeautifulSoup(r.text,'lxml')
        
#       城市名
        cityName=str(b.select('.city_name h2')[0].get_text().encode('utf-8'))
        f.write('"'+cityName+'":[')        
           
        dataTime = str(b.select('.live_data_time p')[0].get_text()[7:])       
#        dictcity['时间']=dataTime
        level=str(b.select('.level h4')[0].get_text().encode('utf-8').strip())
#        dictcity['等级']=level        

        tables=b.select('tr')
    
#        print tables[1]
        ltr=[]
    
        for tr in tables:    
            data=tr.select('td')
            for td in data:
#               通过正则表达式，替换字符串中间的多个空格为一个空格
                ltr.append(re.sub(r"\s{2,}"," ",td.get_text().encode('utf-8').strip()))
            i=0
            
            if len(ltr)==0:
                continue
            
            for td in ltr:
                dictpoint[valuelist[i]]=td
                
                i+=1
            
            jd=json.dumps(dictpoint,ensure_ascii=False)                    
                      
            f.write(jd)
            f.write(',')
            ltr=[]
            i=0
            
#           清空
            dictpoint.clear()
            
        f.write("],")
finally:
    f.write('}')
    f.close()
    
def sortedDictValues(adict):
    items = adict.items()
    item.sort()
    return [value for key ,value in items]