from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re
####################################Scenario 1:
options= webdriver.ChromeOptions
driver = webdriver.Chrome(executable_path="D:\DevOps\vois_test\chromedriver_win32")
driver.set_window_size(1024, 768)
driver.maximize_window()

driver.get("https://www.amazon.com/")

sleep(5)
if driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[4]/div[1]/div/div/div[3]/span[1]/span/input"):
    locations_pops=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[4]/div[1]/div/div/div[3]/span[1]/span/input")
    action=webdriver.ActionChains(driver)
    action.move_to_element(locations_pops).click().perform()
else : 
    pass 
#####select first item
todays_deal=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[4]/div[2]/div[2]/div/a[1]")
action=webdriver.ActionChains(driver)
action.move_to_element(todays_deal).click().perform()

############## add to chart 
#Headphones
#
#browser.find_element_by_id("C179003030-ORNL_DAAC-box").click()
#grocery=driver.find_element(By.XPATH,"//span[.='Grocery']").click()#//span[text()='Grocery']
headphone=driver.find_element(By.XPATH,"//span[text()='Headphones']").click()
discount=driver.find_element(By.XPATH,"//span[text()='10% off or more']").click()
sleep(3)
#groc=driver.find_element(By.XPATH,"//span[text()='Grocery']").click()
sleep(5)
#grocery=driver.find_element(By.XPATH,"//html/body/div[1]/div[21]/div/div/div/div[2]/div[2]/span[3]/ul/li[18]/label/span[text()='Grocery']").click()

##########page 4   
page4=driver.find_element(By.XPATH,"/html/body/div[1]/div[21]/div/div/div/div[3]/div/ul/li[5]/a").click()
# 
# item to buy /html/body/div[1]/div[21]/div/div/div/div[2]/div[3]/div/div[1]/div/div/a/div/div/img 
sleep(4)
item=driver.find_element(By.XPATH,"/html/body/div[1]/div[21]/div/div/div/div[2]/div[3]/div/div[1]").click()
sleep(4)
if driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[10]/div[6]/div[1]/div[4]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div[13]/div[1]/span/span/span/input"):
    add_to_cart=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[10]/div[6]/div[1]/div[4]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div[13]/div[1]/span/span/span/input").click()
#action.move_to_element(todays_deal).click().perform()
#filter_select=driver.find_element(By.XPATH,"//label[contains(@for,'Headphones')]")
#action=webdriver.ActionChains(driver)
#action.move_to_element(filter_select).click().perform()
sleep(10)
driver.quit()
