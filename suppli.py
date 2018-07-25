from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
from urllib import parse
from selenium import webdriver

import pandas as pd


chrome_path = r"C:\Users\Vamsi krishna badri\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

def go_to_about(sup_url):
    about = driver.get()
    about_html = about.read()
    about.close()
    about_soup = Soup(about_html, "html.parser")
    nav = about_soup.nav

    for url in nav.findAll("a"):
        #count = count+1
        sub_url = url.get('href')
        tot_url  = parse.urljoin(sup_url,sub_url)
        print(tot_url)


my_url = 'https://dir.indiamart.com/impcat/peanutbutter-all.html'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = Soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "prr w100"})
for container in containers:
    main_link = container.a["href"]
    #mainn = Soup(main_link, "html.parser")
    go_to_about(main_link)
    #break
    #print(len(containers))
    #print(main_link)
