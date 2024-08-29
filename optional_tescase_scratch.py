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

sleep (3)

driver.find_element(By.ID, "search") .send_keys('video games')

sleep(3)

driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']") .click()

sleep (3)

driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']")
#once the actual result is in the Expected result it works? for ex: 'tea'...would 'te' work or 't' as long as its within 'tea'?
# or 'video games'
expected_result= driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
actual_result= 'video games'

assert actual_result in expected_result, f"im looking for {expected_result} but instead i got {actual_result}"

print('test is good money!')

driver.quit()


