import xlrd
from selenium import webdriver
import csv


chrome_path = r"C:\Users\Vamsi krishna badri\Downloads\chromedriver_win32\chromedriver.exe"
csvfile = open("fakeaddress.csv", 'wt', newline='')
writer = csv.writer(csvfile)


def getaddress(url):

    driver = webdriver.Chrome(chrome_path)
    driver.get(url)
    address =  driver.find_elements_by_xpath('//div[@class="ncnct_p f13_p"]')
    addvalue = [i.text for i in address]
    print(addvalue)
    writer.writerow(addvalue)
    driver.close()

workbook = xlrd.open_workbook("getlost.xlsx")
worksheet = workbook.sheet_by_index(0)

for r in range(1,225):
    getaddress(worksheet.cell(r,2).value)
