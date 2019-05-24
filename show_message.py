import pymysql
import settings

conn=pymysql.Connect(**settings.parameters)
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

sql="select username,usertype,password,date_format(regtime,'%Y-%m-%d'),email from user"

res=cursor.execute(sql)

if res > 0:
    records=cursor.fetchall()

    print('{:9} {:^3} {:^48} {:^30} {:^10}'.format('用户名', '用户类型', '密码','注册时间','email'))
    fmt = '{:12} {:^3} {:^65} {:<20} {:<10}'

    for rec in records:
        print(fmt.format(rec['username'],rec['usertype'],rec['password'],rec["date_format(regtime,'%Y-%m-%d')"],rec['email']))

cursor.close()
conn.close()