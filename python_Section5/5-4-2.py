import pymysql


#mysql connection
conn = pymysql.connect(host='localhost', user='python', password='qwer1234',
                        db='python_app1',charset='utf8')

try:
    with conn.cursor() as c: #conn.cursor(pymysql.cursors.dictcursor) : 디셔너리 형태로 리턴 #
        c.execute("select * from users")
        #1개 로우
        # print(c.fetchone())
        #선택 지정
        # print(c.fetchmany(3))
        #전체 로우
        # print(c.fetchall())
        #순회
        c.execute("select * from users order by id ASC")
        rows = c.fetchall()
        for row in rows:
            print('usage1 > ', row)
        #순회2
        c.execute("select * from users order by id DESC")
        rows = c.fetchall()
        for row in rows:
            print('usage2 > ', row)
        #조건 조회1
        param1 = (1,)
        c.execute("select * from users where id=%s", param1)
        print('param1',c.fetchall())

        #조건 조회2
        param2 = 1
        c.execute("select * from users where id='%d'" %param2)
        print('param1',c.fetchall())

        #조건 조회3
        param3 = 4,5
        c.execute("select * from users where id in(%s,%s)", param3)
        print('param1',c.fetchall())

        #조건 조회3
        c.execute("select * from users where id in('%d','%d')" %(4,5))
        print('param1',c.fetchall())
finally:
    conn.close()
