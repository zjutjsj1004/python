#!/usr/bin/env python
# coding=utf-8
import urllib
import re
import requests
import sys
import csv
import codecs
import time
reload(sys)
sys.setdefaultencoding("utf-8")
def PageNum(html,payload):
    res=requests.get(url,params=payload)
    pa=r'<span class=\"total-page\">(.*?)</span>'
    time.sleep(4)
    page=re.findall(pa,res.text,re.S)
    if page:
        str=page[0]
        str=str[1]
    else :
        str=0
    print "共%s页"%(str,)
    return str
def DoPa(html,payload):
    res=requests.get(url,params=payload)
    str1=r'<li class=\"bo-list-item\"(.*?)\</li>'
    ll=re.findall(str1,res.text,re.S)
    x =len(ll)
    for i in range(0,x):
        comm=r'item-company">(.*?)</div>'
        company=re.findall(comm,ll[i],re.S)
        if "title" in company[0]:
            comm=r'title=\"(.*?)\"'
            company=re.findall(comm,company[0],re.I)
            company=company[0]
        elif 'location">' in company[0]: 
            comm=r'location\">(.*?)<'
            company=re.findall(comm,company[0],re.I)
            company=u'来自'+company[0]+'的采购商'
        com=r'quantity\">(.*?)</p>'#采购量
        comm=re.findall(com,ll[i],re.S)
        if "<em>" not in comm[0]:
            count=" "
        else:
            count=r'<em>(.*?)</em>(.*?)</span>'#采购量
            co=re.findall(count,comm[0],re.S)
            count=co[0][0]+co[0][1]
        baojia=r'item-state">.*<span>(.*)<em>(.*)</em>(.*?)</span>'
        baojia=re.findall(baojia,ll[i],re.S)
        #baojia=baojia[0][0]+baojia[0][1]+baojia[0][2]
        baojia=baojia[0][1]+baojia[0][2]
        ss=r'title=\"(.*?)\"'#标题
        kinds=r'Days\"><span>.*?buyType\"><span>.*?</span><span>(.*?)</span></a>'#信息类型
        time=r'Days\"><span>(.*?)</span></a>'#剩余时间
        date=r'<span>.*?<span>(.*?)</span>'#发布日期
        mm=re.findall(ss,ll[i],re.S)
        Date=re.findall(date,ll[i],re.M)
        Kind=re.findall(kinds,ll[i],re.S)
        Time=re.findall(time,ll[i],re.S)
        if "<em>" in Time[0]:
            Time=re.findall(r'<em>(.*)</em>(.*)',Time[0],re.S)
            time=Time[0][0]+Time[0][1]
        else:
            str=Time[0]
            time=str.partition("：")[2]
        if "<em>" in Date[0]:
            pass
        else:
            print count
            data={
                (mm[0],count,Date[0],time,Kind[0],baojia,company)
            }
            writer.writerows(data)
url = 'https://s.1688.com/newbuyoffer/buyoffer_search.html'
#请求地址url
name=raw_input('请输入关键字:')
Key=name.encode('gb2312')
payload={'keywords':Key,'n':'y','mastheadtype':'','from':'industrySearch','industryFlag':'go'}
payload=urllib.urlencode(payload)
csvfile=file(name.encode('gb2312')+'.csv','wb')
csvfile.write(codecs.BOM_UTF8)
writer=csv.writer(csvfile)
writer.writerow(['名称','采购量','发布时间','剩余时间','信息类型','已有报名/价','公司'])
pagecount=PageNum(url,payload)
DoPa(url,payload)
for i in (1,pagecount):
    payload={'keywords':Key,'n':'y','from':'industrySearch','industryFlag':'go','sug':'1_0','n':'y','beginPage':i}
    DoPa(url,payload)
csvfile.close()
print '采集完毕'
