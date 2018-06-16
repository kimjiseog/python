import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


firefox_options = Options()
firefox_options.add_argument("--headless") #CLI 모드 실행

driver = webdriver.Firefox(firefox_options=firefox_options, executable_path="C:\\python source\\Section3\\webdriver\\firefox\\geckodriver.exe")
#driver.set_window_size(1920,1280)

#driver.implicitly_wait(5)
driver.get('https://google.com')
driver.save_screenshot("C:\\python source\\Section3\\download\\ff1.png")
#time.sleep(5)

#driver.implicitly_wait(5)
driver.get('https://www.daum.net')
driver.save_screenshot("C:\\python source\\Section3\\download\\ff2.png")
#time.sleep(5)
driver.quit()
print('스크린샷 완료')
