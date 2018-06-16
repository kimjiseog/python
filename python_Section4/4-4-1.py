import simplejson as json
#import json

#dict(json) 선언

data={}
data['people'] = []
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'from':'seoul'
})
data['people'].append({
    'name':'park',
    'website':'google.com',
    'from':'busan'
})
data['people'].append({
    'name':'lee',
    'website':'daum.net',
    'from':'iechone'
})

#print(data)

#data ={'people': [{'name': 'kim', 'website': 'naver.com', 'from': 'seoul'}, {'name': 'park', 'website': 'google.com', 'from': 'busan'}, {'name': 'lee', 'website': 'daum.net', 'from': 'iechone'}]}

#dict(json) -> str
e = json.dumps(data, indent=4)
# print(type(e))
# print(e)

#str -> dict(json)
d = json.loads(e)
# print(type(d))
# print(d)

with open('C:/python source/Section4/member.json','w') as outfile:
    outfile.write(e)


with open('C:/python source/Section4/member.json','r') as infile:
    r = json.loads(infile.read())
    print("=====")
    # print(type(r))
    # print(r)
    for p in r['people']:
        print('name: ' +p['name'])
        print('website: ' +p['website'])
        print('from: ' +p['from'])
        print('')
