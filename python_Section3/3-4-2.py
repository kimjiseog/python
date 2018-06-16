import sys
import io
from bs4 import BeautifulSoup
import requests, json
import os
import urllib.parse as rep
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
savePath = "C:\\Users\\jskim2-vmware\\Downloads\\imagedown\\"
#로그인 유저 정보
LOGIN_INFO = {
    'log': '',
    'pwd': '',
    'user-submit': rep.quote_plus('로그인'),
    'user-cookie': 1
}

#Session 생성, with 구문안에서 유지
with requests.Session() as s:
    login_req = s.post('https://www.inflearn.com/wp-login.php?redirect_to=https%3A%2F%2Fwww.inflearn.com%2F',data=LOGIN_INFO)
    #html 소스확인
    # print('login_req',login_req.text)
    #print('login_req',login_req.text)
    #header 확인
    #print('headers',login_req.headers)
    if login_req.status_code == 200 and login_req.ok:
        post_one = s.get('https://www.inflearn.com/members/hulpei/dashboard/')
        post_one.raise_for_status()
        soup = BeautifulSoup(post_one.text, 'html.parser')
        #print(soup.prettify())
        study = soup.select_one("h2#sidelogo > a > img")


        fullFileName = os.path.join(savePath,'1.jpg')
        req.urlretrieve(study['src'],fullFileName)
