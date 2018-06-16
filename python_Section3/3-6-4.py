import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


#chrome_options = Options()
#chrome_options.add_argument("--headless") #CLI 모드 실행

#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\\python source\\Section3\\webdriver\\chrome\\geckodriver.exe")
driver = webdriver.Chrome('C:\\python source\\Section3\\webdriver\\chorme\\chromedriver.exe')
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F')
driver.save_screenshot("C:\\python source\\Section3\\download\\ff1.png")
time.sleep(5)

driver.find_element_by_name('log').send_keys('')
driver.find_element_by_name('pwd').send_keys('')
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()

# #driver.implicitly_wait(5)
# driver.get('https://www.daum.net')
# driver.save_screenshot("C:\\python source\\Section3\\download\\ff2.png")
# #time.sleep(5)
# driver.quit()
# print('스크린샷 완료')
