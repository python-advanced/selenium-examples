from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = 'chromedriver.exe'

driver = webdriver.Chrome(chromedriver)
driver.get('https://www.google.com')

search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

search.send_keys('曲面螢幕')
search.send_keys(Keys.RETURN)