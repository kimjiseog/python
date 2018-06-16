import pymysql


#mysql connection
conn = pymysql.connect(host='localhost', user='python', password='qwer1234',
                        db='python_app1',charset='utf8')

try:
    with conn.cursor() as c: #conn.cursor(pymysql.cursors.dictcursor) : 디셔너리 형태로 리턴 #
        #데이터 수정1
        c.execute("update users set username = %s where id = %s",('niceman',1))
        #데이터 수정2
        c.execute("update users set username = '%s' where id = '%d'" %('goodboy',2))
        #중간 데이터 확인1
        c.execute("select * from users order by id DESC")
        for row in c.fetchall():
            print('check1 > ',row)

        #데이터 삭제1
        c.execute("delete from users where id = %s",(1,))
        #데이터 삭제2
        c.execute("delete from users where id = '%s'" %(2,))
        c.execute("select * from users order by id DESC")
        for row in c.fetchall():
            print('check2 > ',row)
    conn.commit()
finally:
    conn.close()
