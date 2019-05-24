import pymysql
import settings

conn = pymysql.Connect(**settings.parameters)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


sql = """
create table if not exists user(uid int primary key auto_increment,username char(10) unique not null,usertype enum('0','1') default '0',password char(100) not null ,regtime timestamp  default now(),email varchar(50) not null
);
"""
# 返回值是受影响行数
res = cursor.execute(sql)

# 5 关闭连接和游标
cursor.close()
conn.close()