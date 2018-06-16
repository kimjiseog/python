import sys
import io
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
savePath = "C:\\Users\\jskim2-vmware\\Downloads\\imagedown\\"
#요청 url
URL = 'https://www.wishket.com/accounts/login/'

#fake_useragent 생성
ua = UserAgent()
# print(ua.ie)
# print(ua.chrome)
# print(ua.random)

with requests.Session() as s:
    #URL 연결
    s.get(URL)
    #로그인정보 payload
    LOGIN_INFO = {
        'identification': '',
        'password': '',
        'csrfmiddlewaretoken': s.cookies['csrftoken']
    }
   # print('headers',s.headers)
   # print('token',s.cookies)
    #요청
    response = s.post(URL, data=LOGIN_INFO,headers={'User-Agent':str(ua.chrome), 'Referer': 'https://www.wishket.com/accounts/login/'})
    #HTML 결과 확인
    #print('response', response.text)
    if response.status_code == 200 and response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        projectlist = soup.select("table.table.table-responsive > tbody > tr")
        for i in projectlist:
            print(i.find('th').string,i.find('td').text)
