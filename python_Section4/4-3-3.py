#딕셔너리 자료형(key, value) -> 순서 없음, 중복 안됨, 수정 가능, 삭제 가능튜플 자료형(순서,중복 가능 / 수정,삭제 불가능)
#속도 튜플 > 리스트

#선언
a = {'name' : 'kim', 'phone' : '01077777777','birth':910809}
b = {0:'hello world!'}
c = {'arr':[0,1,2,3]}
print(type(a),a)

#출력
print('a - ',a['name'])
print('a - ',a.get('name'))
#print('a - ',a['address']) #그냥 가져오면 에러가 발생함, get으로 가져와야 none 값을 반환함
print('a - ',a.get('address'))
print('c - ', c.get('arr'))

#딕셔너리 추가
a['address'] = 'Seoul'
print('a - ',a)
a['rank'] = [1,2,3]
print('a - ',a)

print('a - ', a.keys())
print('a - ', list(a.keys()))
print('a - ', a.keys())
print('a - ', list(a.values()))

print('a - ',a.items())
print('a - ', type(list(a.items())[1]))

print('a - ','name' in a)
print('a - ','city' in a)
