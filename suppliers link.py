from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


chrome_path = r"C:\Users\Vamsi krishna badri\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)




try:

    driver.get("https://dir.indiamart.com/impcat/peanutbutter-all.html")


    while True:
        element2 = WebDriverWait(driver, 200)
        element = driver.find_element_by_class_name("m_bt2")
        driver.execute_script("arguments[0].click();", element)

        #click_more(driver)

except NoSuchElementException:
    pass
    type1 = driver.find_elements_by_class_name("gcnm")
    for i in type1:
        suppliers_links = i.get_attribute('href')
        print(suppliers_links)
finally:
    #print(len(type1))
    driver.quit()


