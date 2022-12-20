from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import re
####################################Scenario 1:
options= webdriver.ChromeOptions
driver = webdriver.Chrome(executable_path="D:\DevOps\vois_test\chromedriver_win32")#,options=options)
driver.set_window_size(1024, 600)
driver.maximize_window()
driver.get("https://www.amazon.com/")
print(driver.title)
#####select first item
first_item=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div[2]/div/div[8]/div/div/div[2]/div/ul/li[1]/span/a/img")
action=webdriver.ActionChains(driver)
action.move_to_element(first_item).click().perform()
############## add to chart 
##by id
add_to_cart=driver.find_element(By.ID,"add-to-cart-button")
action=webdriver.ActionChains(driver)
action.move_to_element(add_to_cart).click().perform()
sleep(30)

#if driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div[1]/div/div[1]/a") or driver.find_element(By.XPATH," /html/body/div[8]/div[3]/div/div/div[1]/a") :
if driver.find_element(By.ID,"attach-close_sideSheet-link") :
    #exit slider and go to cart
    print("slider exited and close")
    cart_slider=driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div/div[1]/div[3]/div[1]/div[2]/div[3]/form/span/span/input")
    action=webdriver.ActionChains(driver)
    action.move_to_element(cart_slider).click().perform()
else:
##go to cart
    cart_main=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[3]/div/a[4]/div[1]/span[2]")
    action=webdriver.ActionChains(driver)
    action.move_to_element(cart_main).click().perform()



# # ################ chec how many items in cart 
add_to_cart=driver.find_element(By.ID,"sc-subtotal-label-buybox").text

sleep(3)
# # ##
no_items_in_cart=re.findall(r'\d+', add_to_cart) #get number from text
print(no_items_in_cart[0])
if int(no_items_in_cart[0]) > 0 :
     print("item is added successfully")
else:
      print("cart is empty")
