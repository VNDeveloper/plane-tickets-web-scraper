from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = r"C:\Users\Quang.Nguyen\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.kayak.co.uk/flights")
print(driver.title)

try:
    search = driver.find_element_by_class_name("d_E3")
    # search.send_keys("test")
    # search.send_keys(Keys.Return)
    # time.sleep(5)

    print('success')
    print(search)
    driver.quit()

except NameError:
    driver.quit()
    print("fail")
    print(NameError)





