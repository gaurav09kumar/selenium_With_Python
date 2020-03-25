# Visit www.seleniumhq.org to download the required drivers

# This program displays - How to Run Tests on Chrome, Firefox & IE Browsers
# import  web driver from selenium package into the program

from selenium import webdriver

# set the path for chrome
# (For IE & Firefox replace webdriver.Chrome with webdriver.IE & webdriver.Firefox, change executable path accordingly)
driver = webdriver.Chrome(executable_path="C:/Users/Gaurav Kumar Rai/Downloads/chromedriver_win32/chromedriver.exe")

# enter the URL to open the page in browser
driver.get("https://www.orangehrm.com")

# get title of page
print("Title of the page is : "+driver.title)

# to return the URL's of the web page
print(driver.current_url)

# to get the HTML Source Code of the web page
print(driver.page_source)

# close the browser
driver.close()


