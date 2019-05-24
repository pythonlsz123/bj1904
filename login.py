import pymysql
import settings
import hashlib
conn=pymysql.Connect(**settings.parameters)

cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

while 1:
    for i in range(3):
        user_name=input("请输入用户名:")
        user_password=input("请输入密码:")
        sql="select username from user where username=%s and password=sha1(%s)"
        res=cursor.execute(sql,[user_name,user_password])
        if not res:
            print("登录失败！")
        else:
            print("登陆成功")
            break;
    break;
cursor.close()
conn.close()