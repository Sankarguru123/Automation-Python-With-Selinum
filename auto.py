import os
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Login:
    username = str(input('Enter username:\n'))
    password = input(("Enter your password?\n"))
    product_name = str(input('Enter product name\n'))


class TestWebDriver:

        def __init__(self,driver):
                self.driver = driver
                self.url = 'https://www.amazon.in/'
                self.username= Login.username
                self.password = Login.password
                self.product = Login.product_name

        def amazon_page(self):
           print(self.driver)
           action = ActionChains(self.driver)
           self.driver.get(self.url)
           print('Page title: ' +self.driver.title)
           first_menu_level = self.driver.find_element(by=By.XPATH, value='// *[ @ id = "nav-link-accountList-nav-line-1"]')
           action.move_to_element(first_menu_level).perform()
           time.sleep(3)
           second_level_menu = self.driver.find_element(by=By.XPATH, value='// *[ @ id= "nav-flyout-ya-signin"]')
           second_level_menu.click()
           time.sleep(3)
           sign_in_element = self.driver.find_element(by=By.XPATH, value='//*[@id="ap_email"]')
           sign_in_element.send_keys(self.username)
           time.sleep(3)
           continue_element = self.driver.find_element(by=By.XPATH, value='//*[@id="continue"]')
           continue_element.click()
           time.sleep(3)
           password_element = self.driver.find_element(by=By.XPATH, value='//*[@id="ap_password"]')
           password_element.send_keys(self.password)
           login = self.driver.find_element(by=By.XPATH, value='//*[@id="signInSubmit"]')
           login.click()
           time.sleep(3)
           search_bar = self.driver.find_element(by=By.XPATH, value='//*[@id="twotabsearchtextbox"]')
           search_bar.send_keys(self.product)
           search_bar.send_keys(Keys.ENTER)
           time.sleep(3)
           main_page_selector = self.driver.find_element(by=By.CSS_SELECTOR, value='div.sg-col-6-of-20')
           listofproducts = main_page_selector.find_elements(by=By.CSS_SELECTOR, value='#CardInstance3nt5715YaETbx85wPQ8v0Q > div._bXVsd_content_2rsXy > div.a-section.a-spacing-none._bXVsd_block_1vI8-._bXVsd_row_3CEm0 > div:nth-child(1) > div > div.a-section.a-spacing-none > div > a > div')
           for item in  listofproducts:
               try:
                    item.find_element(by=By.CSS_SELECTOR, value='div.a-row')
                    ans=True
               except:
                    ans=False

               if (ans):
                   item.find_elements(by=By.XPATH, value='span.a-size-medium').click()
                   break
           window_after = self.driver.window_handles[0]
           self.driver.switch_to.window(window_after)  ##used to switche between tabs
           print(window_after,'window')
           addtocart = self.driver.find_elements(by=By.XPATH,value='//*[@id="add-to-cart-button"]')
           addtocart.click()
           time.sleep(3)

           proceed = self.driver.find_elements(by=By.XPATH, value ='//*[@id="hlb-ptc-btn-native"]')
           proceed.click()
           time.sleep(3)

if __name__ == "__main__":
    options= webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    value = webdriver.Chrome(executable_path='./chromedriver4.exe',chrome_options=options)
    vs = TestWebDriver(value)
    vs.amazon_page()








import os
# import logindata
# #configure chromedriver path
# driver = webdriver.Chrome(executable_path='./chromedriver4.exe')
# #implicit wait
# driver.implicitly_wait(0.5)
# #url launch
# driver.get("https://www.tutorialspoint.com/questions/index.php")
# print('Page title: ' + driver.title)
# #browser close
# driver.close()


#
# def testing_page(driver):
#
#         action = ActionChains(driver)
#         url = "https://www.amazon.in/"
#         driver.implicitly_wait(0.05)
#         driver.get(url)
#         print('Page title: ' + driver.title)
#         first_menu_level = driver.find_element(by=By.XPATH, value='// *[ @ id = "nav-link-accountList-nav-line-1"]')
#         action.move_to_element(first_menu_level).perform()
#         time.sleep(3)
#         second_level_menu = driver.find_element(by=By.XPATH, value='// *[@ id= "nav-flyout-ya-signin"]')
#         second_level_menu.click()
#         time.sleep(3)
#         sign_in_element = driver.find_element(by=By.XPATH, value='//*[@id="ap_email"]')
#         sign_in_element.send_keys(logindata.username)
#         time.sleep(3)
#         continue_element = driver.find_element(by=By.XPATH, value='//*[@id="continue"]')
#         continue_element.click()
#         time.sleep(3)
#         password_element = driver.find_element(by=By.XPATH, value='//*[@id="ap_password"]')
#         password_element.send_keys(logindata.password)
#         login = driver.find_element(by=By.XPATH, value='//*[@id="signInSubmit"]')
#         login.click()
#         time.sleep(3)
#
#
#         # driver.find_element("username").send_keys("sankarguru63@gmail.com")
#         # driver.find_element("password").send_keys("Sankar@123")
#         # browser close
#         # driver.close()
#
#
# if __name__ == "__main__":
#     options= webdriver.ChromeOptions()
#     options.add_argument('--start-maximized')
#     value = webdriver.Chrome(executable_path='./chromedriver4.exe',chrome_options=options)
#     testing_page(value)
from urllib3.util import url
import getpass
