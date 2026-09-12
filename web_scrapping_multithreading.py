'''

Real-World Example: Multithreading for  I/O bound tasks
Scenerio: Web Scrapping

'''
import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://docs.langchain.com/oss/python/langchain/install',

    'https://docs.langchain.com/oss/python/langchain/quickstart',

    'https://docs.langchain.com/oss/python/releases/changelog'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} character type{url}')

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fecthed")



