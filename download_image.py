#coding=utf-8
import time
import urllib
import urllib2
import os
import re
from colorama import Fore, Back, Style

pic_url = list()
name_list = list()
name_file = open("categories.txt", "r+")
name = name_file.read()
name_list = name.split("\n")
def get_picurl(pic_url, item):
    directory = '/Users/chris/百度云同步盘/CS/BrainHoles'
    os.chdir(directory)
    url_file = open(str(item)+ ".txt", "r+")
    pic_url.append(url_file.readlines())
    print str(item)

def urlcallback(a,b,c):
    print "Progress: "
    prec=100.0*a*b/c
    if 100 < prec:
        prec=100
    print "%.2f%%"%prec

def download_pic(pic_url):
    path = '/Users/chris/百度云同步盘/kitchen_pic'
    print 'downloading'
    for name in name_list:
        i = 1
        get_picurl(pic_url, name)
        directory = path+'/'+name
        print 'directory fetching'
        if not os.path.exists(directory):
            os.makedirs(directory)
        os.chdir(directory)
        print directory
        for url in pic_url:
            for URL in url:
                try:
                    urllib.urlretrieve(URL, directory+"/"+str(i)+'.jpg',urlcallback)
                    i+=1
                except:
                    i+=1
download_pic(pic_url)
