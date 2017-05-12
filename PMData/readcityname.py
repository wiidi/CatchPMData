# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:28:07 2017

@author: wudi1
"""


def getCityName(filename='city.txt'):
    cityList=[]
    i=0
    with open(filename,'r') as f:
        #读取每一行
        lines=f.readlines()
        for line in lines:
            #通过逗号分词
            list=str(line).split(',')            
            cityList.append(list[0])    
#    for city in cityList:
#        print type(city)
#    print cityList
    return cityList

