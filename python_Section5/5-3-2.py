import sqlite3

#DB 생성
conn = sqlite3.connect('C:/python source/Section5/database/sqllite1.db')

#커서 바인딩
c = conn.cursor()

#데이터 조회(전체)
c.execute("SELECT * FROM users")

#1개 로우 선택
# print(c.fetchone())

#지정 로우 선택
# print(c.fetchmany(size=4))

#전체 로우 선택
# print(c.fetchall())

#순회1
# rows = c.fetchall()
# for row in rows:
#     print('usage1 > ',row)

#순회2
# for row in c.fetchall():
#     print('usage2 > ',row)

#순회2
# for row in c.execute("select * from users"):
#     print('usage3 > ',row)

#조건 조회1
param1 = (1,)
c.execute("select * from users where id=?",param1)
print(c.fetchall())

#조건 조회2
param2 = 1
c.execute("select * from users where id='%s'"%param2) #%s, %d, %f %o
print(c.fetchall())

#조건 조회3
c.execute("select * from users where id=:id",{"id":1})
print(c.fetchall())

#조건 조회4
param4 = (1,4)
c.execute("select * from users where id in (?,?)",param4)
print(c.fetchall())

#조건 조회5
c.execute("select * from users where id=:id1 or id=:id2",{"id1":1,"id2":2})
print(c.fetchall())

#dump
with conn:
    #dump 출력
    with open('C:/python source/Section5/data/test.dump','w') as f:
        for line in conn.iterdump():
            f.write('%s\n' %line)
        print("dump write complete!")


conn.commit()

conn.close()
