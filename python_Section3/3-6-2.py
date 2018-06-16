import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


chrome_options = Options()
chrome_options.add_argument("--headless") #CLI 모드 실행

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:\\python source\\Section3\\webdriver\\chorme\\chromedriver.exe')
#driver.set_window_size(1920,1280)

#driver.implicitly_wait(5)
driver.get('https://google.com')
driver.save_screenshot("C:\\python source\\Section3\\download\\1.png")
#time.sleep(5)

#driver.implicitly_wait(5)
driver.get('https://www.daum.net')
driver.save_screenshot("C:\\python source\\Section3\\download\\2.png")
#time.sleep(5)
driver.quit()
print('스크린샷 완료')
