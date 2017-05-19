import json
import codecs
import csv
import collections

dirStation=collections.OrderedDict()

f=open("station.csv",'r') 
fw=open('station.json','w')
csv_read = csv.reader(f)
valuelist=['监测点编码','监测点名称','城市','经度','纬度']
i=0
for list1 in csv_read:
    for vl in valuelist:     
        dirStation[vl]=list1[i]        
        i+=1
    lsjson=json.dumps(dirStation,indent=4,separators=(',',':'),ensure_ascii=False)
    fw.write(lsjson)
    i=0

 
fw.close()
f.close()


