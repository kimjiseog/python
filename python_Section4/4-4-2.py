import simplejson as json
#import json

#dict(json) 선언

data={}
data['people'] = []
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'from':'seoul',
    'grade':[95,77,89,91]
})
data['people'].append({
    'name':'park',
    'website':'google.com',
    'from':'busan',
    'grade':[85,67,100,93]
})
data['people'].append({
    'name':'lee',
    'website':'daum.net',
    'from':'iechone',
    'grade':[98,79,99,92]
})

#print(data)

#json 파일쓰기(dump)

with open('C:/python source/Section4/member.json','w') as outfile:
    json.dump(data,outfile,indent=4)

with open('C:/python source/Section4/member.json','r') as infile:
    r = json.load(infile)
    # print(type(r))
    # print(r)
    print("==========")
    for p in r['people']:
        print('name: ' +p['name'])
        print('website: ' +p['website'])
        print('from: ' +p['from'])
        grade = ''
        for g in p['grade']:
            grade = grade + ' ' + str(g)
        print('grade:',grade.lstrip())
        print('')
