'''
Real world example : multi threading for I/O bound tasks 
Scenario: web scraping 
web scarping often involves making numerous network requests to fetch web pages.
These tasks are I/o bound tasks are I/o bound beacause they spend a lot of
time waiting for response from servers. Multithereading can signigificantly
improve the performance by allowing multiple web pages to be fetched concurrently


https://docs.langchain.com/oss/python/langchain/overview

https://docs.langchain.com/oss/python/langchain/quickstart

https://docs.langchain.com/oss/python/langchain/agents

'''

import threading 
import requests 

## used for web scraping any url
from bs4 import BeautifulSoup 

urls=[
    'https://docs.langchain.com/oss/python/langchain/overview',

    'https://docs.langchain.com/oss/python/langchain/quickstart',

    'https://docs.langchain.com/oss/python/langchain/agents'
]

def fetch_contents(url) :
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(len(soup.text))
     
threads=[] 
for url in urls :
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(threads)
    thread.start() 
    
for thread in threads :
    thread.join() 
print("All webpages fetched")