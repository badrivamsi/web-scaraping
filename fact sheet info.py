from selenium import webdriver
import csv
import xlrd
from selenium.webdriver.support.wait import WebDriverWait




csvfile = open("icantworkbro.csv", 'wt', newline='')
writer = csv.writer(csvfile)



chrome_path = r"C:\Users\Vamsi krishna badri\Downloads\chromedriver_win32\chromedriver.exe"

def csvoutput(url):
    driver = webdriver.Chrome(chrome_path)
    WebDriverWait(driver, 10)
    driver.get(url)
    headers = driver.find_elements_by_xpath('//td[@width="35%"]')
    head = [i.text for i in headers]
    writer.writerow(head)
    print(head)


    values =  driver.find_elements_by_xpath('//td[@width="100%"]')
    value = [j.text for j in values]
    writer.writerow(value)
    print(value)
    driver.close()

workbook = xlrd.open_workbook("getlost.xlsx")
worksheet = workbook.sheet_by_index(0)

for r in range(1,225):
    csvoutput(worksheet.cell(r,1).value)


