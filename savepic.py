import time
import urllib
import urllib2
import os
import re
from bs4 import BeautifulSoup


picURL = list()
f = open("categories.txt","rb")
txt = open("list.txt", "wb")
def get_picURL(pic_url):
    text = f.read()
    txt = text.split(' ')
    # l1 = list()
    print len('src="https://static.wixstatic.com/media/529735_5fc1e5e4c5ab4b9790ecc7d4b005e15e~mv2.jpg')
    for s in txt:
        if 'https' in s:
            s = s.split('"')[1].split('/v1')[0]
            pic_url.append(s)

def urlcallback(a,b,c):
    print "callback: "
    prec=100.0*a*b/c
    if 100 < prec:
        prec=100
    print "%.2f%%"%prec

def download_pic(pic_url):
    path = '/Users/chris/Downloads/zws/'
    i = 0
    for url in pic_url:
        urllib.urlretrieve(url, path+str(i)+'.jpg',urlcallback)
        i+=1

os.chdir('/Users/chris/Downloads/zws/')
get_picURL(picURL)
download_pic(picURL)
