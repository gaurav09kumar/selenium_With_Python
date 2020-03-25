# import  web driver from selenium package into the program
from selenium import webdriver
# import time packet so that we can add delay in the program
import time

# set the path for chrome
# (For IE & Firefox replace webdriver.Chrome with webdriver.IE & webdriver.Firefox, change executable path accordingly)
driver = webdriver.Chrome(executable_path="C:/Users/Gaurav Kumar Rai/Downloads/chromedriver_win32/chromedriver.exe")

# enter the URL to open the page in browser
driver.get("http://newtours.demoaut.com/")

# get title of page
print("Title of the page is : "+driver.title)

#click on the contact button
driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[4]/a").click()

#add delay
time.sleep(3)

#go back to home page
driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/a/img").click()

#add delay
time.sleep(3)

#click on support button
driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/a").click()

#add delay
time.sleep(3)

#go back to home page
driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/a/img").click()

# close the browser
driver.close()