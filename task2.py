from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.common.keys import Keys
####################################Scenario 1:
options= webdriver.ChromeOptions
driver = webdriver.Chrome(executable_path="D:\DevOps\vois_test\chromedriver_win32")
driver.set_window_size(1024, 768)
driver.maximize_window()

driver.get("https://ksrtc.in/oprs-web/guest/home.do?h=1")
sleep(3)
from_cell=driver.find_element(By.XPATH,"/html/body/main/form/div[1]/div/div[2]/div[1]/div/div[1]/div/input").send_keys("CHIKKAMAGALURU")#.send_keys(Keys.TAB)

#from_cell=driver.find_element(By.XPATH,"/html/body/main/form/div[1]/div/div[2]/div[1]/div/div[1]/div/input").send_keys(Keys.ENTER)

action=webdriver.ActionChains(driver)
action.send_keys(Keys.DOWN)
action.send_keys(Keys.ENTER)
action.send_keys(Keys.TAB)
##to
action.send_keys("BENGALURU")
for i in range(15):
    action.send_keys(Keys.DOWN)
action.send_keys(Keys.ENTER)
action.send_keys(Keys.TAB)
##at from date 
#action.send_keys(Keys.ENTER)
action.perform()

from_=driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[4]/td[3]/a").click()
action.send_keys(Keys.TAB)
to_d=driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[4]/td[5]/a").click()
action.send_keys(Keys.TAB)

action.send_keys(Keys.TAB)
action.send_keys(Keys.TAB)

to_d=driver.find_element(By.XPATH,"/html/body/div[1]/table/tbody/tr[5]/td[7]/a").click()
action.perform()
# action.perform()

##search for bus
bus=driver.find_element(By.XPATH,"/html/body/main/form/div[1]/div/div[2]/div[3]/button/i").click()

#action.send_keys(Keys.TAB)
#at from date

sleep(3)




action.click()
action.perform()
if driver.find_element(By.XPATH,"/html/body/main/form/section/div/div[6]/div[3]/div/div/div[2]/div[1]/div[1]/div[3]/div/input[4]"):
    print("there are some seats")
    seats=driver.find_element(By.XPATH,"/html/body/main/form/section/div/div[6]/div[3]/div/div/div[2]/div[1]/div[1]/div[3]/div/input[4]").click()
    boardpoint=driver.find_element(By.XPATH,"/html/body/main/form/section/div/div[6]/div[3]/div/div/div[2]/div[4]/div/table/tbody/tr/td/div/div[1]/div[2]/div[1]/div/div[1]/div/div/div/ul[3]/li[6]/span").click()
    droppoint=driver.find_element(By.XPATH,"/html/body/main/form/section/div/div[6]/div[3]/div/div/div[2]/div[4]/div/table/tbody/tr/td/div/div[1]/div[2]/div[2]/div/div[2]/ul/li[2]/a").click()
    custom=driver.find_element(By.XPATH,"/html/body/main/form/section/div/div[6]/div[3]/div/div/div[2]/div[4]/div/table/tbody/tr/td/div/div[1]/div[2]/div[2]/div/div[2]/ul/li[3]/a").click()
    tel=driver.find_element(By.XPATH,"/html/body/main/form/section/div/div[6]/div[3]/div/div/div[2]/div[4]/div/table/tbody/tr/td/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/div/div/div/div[1]/div/input").send_keys("6789125987")
    
    email=driver.find_element(By.XPATH,"/html/body/main/form/section/div/div[6]/div[3]/div/div/div[2]/div[4]/div/table/tbody/tr/td/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/div/div/div/div[2]/div/input").send_keys("menna@gmail.com")
    #sleep(100)
else: 
    print("no seats")
 

sleep(100)
driver.quit()

