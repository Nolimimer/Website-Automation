# Selenium/subprocesses need to be in your python env
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import subprocess
import time

base_url="<base_url>"

# Kill all other chromes as it may spawn every time one new instance
subprocess.call(["echo <password> | sudo -S killall Google\ Chrome"], shell=True)

# Open Webdriver Chrome
# You need to downlod chromedriver to get it to work
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})
driver=webdriver.Chrome(chrome_options=option, executable_path="<Path to ChromeDriver>/chromedriver")

driver.maximize_window()
driver.implicitly_wait(20)
driver.get(base_url)

# CLICK LOGIN BUTTON
openLoginButtonElement = driver.find_element_by_id('marketing-header-login')
openLoginButtonElement.click()

# EMAIL
loginFieldEmailElement = driver.find_element_by_xpath('<path>')
loginFieldEmailElement.send_keys('<Your Email>')
time.sleep(1)

# PASSWORD
loginFieldPasswordElement = driver.find_element_by_xpath('<path>')
loginFieldPasswordElement.send_keys('<Your Password>')

# SUBMIT
loginButtonElement = driver.find_element_by_id('<ELEMENT ID>')
loginButtonElement.click()

try: 
    assert "Assert the title" in driver.title
except:
    driver.close

# allowCookies = driver.find_element_by_xpath('').click()
# accept= driver.find_element_by_xpath('').click()
try:
    # Accept cookies or other sites popups
    acceptRules = driver.find_element_by_xpath('').click()
    #allowPushNotifications = driver.find_element_by_xpath('').click()
except:
    print("No Notification or Rule alert!")

# MAIN WEBSITE

print("Opened XY")

for id in range(0,150):
    # driver.execute_script("window.scrollTo(0, 240)") 
    # Way to go through lists
    xpath = "XPATH".format(id+1)
    print(xpath)
    time.sleep(1)
    try: 
        findXY =  driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
        try:
            body = driver.find_element_by_xpath("").text
            time.sleep(2)
            if body == '':
             textInput = driver.find_element_by_xpath('')
             textInput.send_keys("")
            time.sleep(2)
            textInput.send_keys(Keys.RETURN)
        except:
            print('')
    except:
        print('Not clickable')
        driver.execute_script("window.scrollTo(0, 150)")  
    driver.get("Change to MAIN PAGE")

# cookies = driver.get_cookies()
# print(cookies)

