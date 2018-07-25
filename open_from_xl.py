import xlrd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException



chrome_path = r"C:\Users\Vamsi krishna badri\Downloads\chromedriver_win32\chromedriver.exe"



def aboutlink(url):
    try:
        driver = webdriver.Chrome(chrome_path)
        driver.get(url)
        #WebDriverWait(driver, 10)
        navi = driver.find_element_by_tag_name("div")
        links = navi.find_elements_by_tag_name("a")
        count = 0
        for j in links:
            nav_links = j.get_attribute("href")
            if count is 3:
                print(nav_links)
                break
            count = count+1
    except NoSuchElementException:
        print("null")
        pass

    finally:
        driver.close()




workbook = xlrd.open_workbook("supli_links.xlsx")
worksheet = workbook.sheet_by_index(0)

for r in range(1,225):

    aboutlink(worksheet.cell(r,1).value)
