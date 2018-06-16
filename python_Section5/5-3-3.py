import sqlite3

#DB 생성
conn = sqlite3.connect('C:/python source/Section5/database/sqllite1.db')

#커서 바인딩
c = conn.cursor()

#데이터 수정1
c.execute("update users set username =? where id=?",('niceman',1))

#데이터 수정2
c.execute("update users set username= :name where id=:id",{"name":'goodboy',"id":2})

#데이터 수정3
c.execute("update users set username= '%s' where id='%s'"%('cuteboy',3))

#데이터 삭제1
c.execute("delete from users where id=?",(1,))

#데이터 삭제2
c.execute("delete from users where id=:id",{"id":2})

#데이터 삭제3
c.execute("delete from users where id='%s'"%(3))

#중간 데이터 확인
for user in c.execute("select * from users"):
    print(user)

conn.commit()

conn.close()
