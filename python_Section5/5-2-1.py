import simplejson as json
from tinydb.storages import MemoryStorage
from tinydb import TinyDB

#파일 DB 생성

db = TinyDB('C:/python source/Section5/database/database.db', default_table='users')

#메모리 DB 생성
#db = TinyDB(storage=MemoryStorage, default_table='users')

#테이블 선택
users = db.table("users")
todos = db.table("todos")

#테이블 데이터 삽입
# users.insert({'name':'kim', 'email':'test@google.com'})
# todos.insert({'name':'homework', 'complate':'false'})

#테이블 데이터 전체 삽입1
with open('C:/python source/Section5/data/users.json', 'r') as infile:
    r = json.loads(infile.read())
    for u in r:
        users.insert(u)

#테이블 데이터 전체 삽입2
with open('C:/python source/Section5/data/todos.json', 'r') as infile:
    r = json.loads(infile.read())
    for t in r:
        todos.insert(t)

#전체데이터 출력
print(users.all())
print(todos.all())

#테이블 목록
print(db.tables())

#전체 데이터 삭제
#users.purge() #db.purge_table('users') 테이블은 남겨둠
#todos.purge() #db.purge_table('todos')

#db.purge_tables() #테이블까지 삭제

db.close()
