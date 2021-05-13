import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print('Start...')
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument("download.default_directory=./")
driver = webdriver.Chrome("./chromedriver", chrome_options=options)
driver.get('https://www.imf.org/external/np/fin/data/rms_sdrv.aspx')
time.sleep(5)
driver.find_element_by_id('lbnTSV').click()
time.sleep(10)
print('Final')

driver.quit()
