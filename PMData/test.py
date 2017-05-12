# -*- coding: utf-8 -*-
"""
Created on Tue May 09 09:55:07 2017

@author: wudi1
"""
#import codecs
#import time
#
##print time.time()
##date =time.strftime('%Y%m%d_%H%M',time.localtime(time.time()))
##filename='./data/'+date+'.txt'
##print date
##with codecs.open(filename,'w','gbk') as f:
##    f.write(u"中国")

import json
import codecs
import collections

def sortedDictValues(adict):
    items = adict.items()
    items.sort()
    return [value for key ,value in items]
def sortedDictValues1(dic):    
    return sorted(dic.iteritems(), key = lambda asd:asd[0])
    
def sortedDictValues2(adict):
    valuelist=['监测点','AQI','空气质量指数类别','首要污染物','PM2.5细颗粒物',
'PM10可吸附物','CO一氧化碳','NO2二氧化氮','O3臭氧1小时平均','O3臭氧8小时平均','SO2二氧化硫']
    
    return [valuelist,[adict[value] for value in adict.keys]]    
    
ls1={}
ls=collections.OrderedDict()
l=[]
i=0
valuelist=['监测点','AQI','空气质量指数类别','首要污染物','PM2.5细颗粒物',
'PM10可吸附物','CO一氧化碳','NO2二氧化氮','O3臭氧1小时平均','O3臭氧8小时平均','SO2二氧化硫']
ltr =["万寿西宫",96,"良","颗粒物(PM10)", 43 ,142, 0.5, 13 ,143,116,3 ]
for td in ltr :
    ls[valuelist[i]]=td
    i+=1
l.append(ls)    
lk={}
lk['北京']=l
string=u"北京"
lsjson=json.dumps(sortedDictValues1(lk),indent =4,separators=(',', ': '))
with codecs.open('./data/test.json','wb','utf-8') as f:
    f.write('"'+string+'"')
    f.write(lsjson.decode('unicode-escape'))

    
for l in ltr:
    l=str(l).replace('u\'','\'')
    l.decode("unicode-escape")
    print l
#print sortedDictValues2(ls)




