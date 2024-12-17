from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

the_url = driver.find_element(By.XPATH, value='//*[@id="web"]/ol/li[1]/div/div[1]/h3/a')

chrome_options.DriverLoc = driver.service.path

print(chrome_options.DriverLoc)
