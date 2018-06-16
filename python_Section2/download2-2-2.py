import sys
import io
import urllib.request as dw


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://post-phinf.pstatic.net/20150527_274/whtjdgus1666_1432689219314TApr5_JPEG/mug_obj_143268921826930359.JPG"
htmlURL = "http://google.com"

home = "C:\\Users\\jskim2-vmware\\Downloads\\"

savePath1 = home+"test1.jpg"
savePath2 = home+"index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL)
saveFile1 = open(savePath1,'wb') # w : write, r : read a : add b: binary
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2.read())

print("다운로드 완료")
