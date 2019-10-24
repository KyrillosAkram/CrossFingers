from urllib.request import urlopen
from bs4 import BeautifulSoup, NavigableString,re
from ssl import SSLContext
import requests

USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
address=''

def extract_links_in_this_page(link,online):
    if(online):
        respose=requests.get(link,headers=USER_AGENT).text
        respose=BeautifulSoup(respose,'lxml')
    else:
        disk=open(address,'r')
        respose=BeautifulSoup(disk,'lxml')
        disk.close()
    links=[alink.href for alink in respose.findAll('a',{'class':'category-list-item'})]
    