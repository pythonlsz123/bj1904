
import pymysql

import settings

import hashlib

conn = pymysql.Connect(**settings.parameters)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

username = input("请输入用户名：")

sql = "select username from user where username=%s"

res = cursor.execute(sql,[username])

if len(username.strip()) <= 2:
    print('输入有误')
    conn.rollback()

elif res > 0:
    records = cursor.fetchall()
    for rec in records:
        if username == rec['username']:
            print('账号存在')
            conn.rollback()
else:

    password = input("请输入密码：")
    email = input('请输入邮箱:')
    sql = """insert into user(username,password,email) values ('%s',sha1('%s'),'%s')"""%(username,password, email)
    try:

        res = cursor.execute(sql)
        if res:
            conn.commit()
            print('注册成功')


        else:
            conn.rollback()
    except Exception as e:
        print(e)
        conn.rollback()




cursor.close()
conn.close()
