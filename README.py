import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("https://twitter.com/login")

sleep(3)
username = driver.find_element(By.XPATH,"//input[@name='text']")

username.send_keys("arvind_bit")
next_button = driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
next_button.click()


sleep(3)
password = driver.find_element(By.XPATH,"//input[@name='password']")


password.send_keys('xxxx')
log_in = driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
log_in.click()


sleep(3)
driver.get("https://twitter.com/iManasArora")


wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print('\n\n\n\n\n\n\n\n START SCROLLING\n\n')

scrolls = 3
for _ in range(scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    sleep(2)

tweets = driver.find_elements(By.TAG_NAME, 'article')
for tweet in tweets:
    # Process each tweet as desired
    print('\n\n===============================================================================')
    print(tweet.text)

# driver.quit()




