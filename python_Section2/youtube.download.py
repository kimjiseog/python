import pytube
import os
import subprocess

yt = pytube.YouTube("https://youtu.be/aP2PILSAwLs?list=RDaP2PILSAwLs") #다운로드할 주소
videos = yt.streams.all()

#print('videos', videos)

for i in range(len(videos)) :
    print(i,',',videos[i])

cNum = int(input("다운로드 받을 화질은?(0~21입력)"))

down_dir = "C:\\Users\\jskim2-vmware\\Downloads\\youtube"

videos[cNum].download(down_dir)

newFileName = input("변환할 mp3 파일명은?")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg','-i',
    os.path.join(down_dir,oriFileName),
    os.path.join(down_dir,newFileName)
])

print("동영상 다운로드 및 mp3 변환 완료")
