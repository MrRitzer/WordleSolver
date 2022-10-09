from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox() # Use this if you prefer Firefox. 
driver = webdriver.Chrome()

driver.get('http://www.google.com/')

search_input = driver.find_elements_by_css_selector('input.gLFyf.gsfi')[0]
search_input.send_keys('some search string' + Keys.RETURN)