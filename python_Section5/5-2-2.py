import simplejson as json
from tinydb.storages import MemoryStorage
from tinydb import TinyDB, Query

#파일 DB 생성

db = TinyDB('C:/python source/Section5/database/database.db', default_table='users')

#메모리 DB 생성
#db = TinyDB(storage=MemoryStorage, default_table='users')

#테이블 선택
users = db.table("users")
todos = db.table("todos")

#users 테이블 출력
for item in users:
    pass
    print(item['username'], ' : ', item['phone'])

#todos 테이블 출력
for item in todos:
    pass
    print(item['title'], ' : ', item['completed'])

#연결 관계 출력(조건문)
for item in users:
    pass
    print('[',item['username'],']')
    for todo in todos:
        pass
        if todo['userId'] == item['id']:
            print(todo['title'])

#쿼리 객체 사용 조회
#SQL = Query()
Users = Query()
Todos = Query()

#row 수정
users.update({'username': 'kim'}, Users.id == 3)

user_3 = users.search(Users.id == 3)
print(users.search(Users.id ==3)) #>,<,>=,<= 사용 가능
print(user_3)

#row 삭제
users.remove(Users.id == 3)
print(users.search(Users.id ==3))
