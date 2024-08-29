from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()

sleep(6)

driver.find_element(By.XPATH, "//span[@class='sc-859e7637-0 hHZPQy']").click()

sleep (6)

driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']")

actual_results= driver.find_element(By.XPATH, "//h1[@class='sc-fe064f5c-0 sc-315b8ab9-2 WObnm gClYfs']").text

expected_results='Sign into your Target account'

assert expected_results in actual_results, f'I expected {actual_results} but i got {expected_results}'

print ("test is good money")

driver.quit()




