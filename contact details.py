import xlrd
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
def getaddress(url):
    html = uReq(url)
    bsob = Soup(html,"lxml")
    address = bsob.findAll("div",{"class":"ncnct_p f13_p clr6_P"})
    for i in address:
        print(i.text)
workbook = xlrd.open_workbook("getlost.xlsx")
worksheet = workbook.sheet_by_index(0)

for r in range(223,225):
    getaddress(worksheet.cell(r,2).value)