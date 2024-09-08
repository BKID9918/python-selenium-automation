from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from sample_script import driver

#Amazon logo
driver.find_element(By.CSS_SELECTOR, "[class='a-icon a-icon-logo']")
#Create Account
driver.find_element(By.CSS_SELECTOR, "[class='a-spacing-small']")
#Customer_name _field
driver.find_element(By.CSS_SELECTOR, "[placeholder='First and last name']")
#Customer_email_or_phone_number_field
driver.find_element(By.CSS_SELECTOR, "[id='ap_email']")
#password
driver.find_element(By.CSS_SELECTOR, "[id='ap_password']")
#password_check
driver.find_element(By.CSS_SELECTOR, "[id='ap_password_check']")
#Continue_button
driver.find_element(By.CSS_SELECTOR, "[id='continue']")
#condition_of_use
driver.find_element(By.CSS_SELECTOR, "[href*='notification_condition_of_use']")
#Privacy_notice
driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy_notice']")
#Business_account_link
driver.find_element(By.CSS_SELECTOR, "[id='ab-enhanced-registration-link']")
#Sign_in
driver.find_element(By.CSS_SELECTOR, "[class='a-link-emphasis']")







