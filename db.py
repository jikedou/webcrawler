# coding:utf-8
import MySQLdb

conn = MySQLdb.connect(host="127.0.0.1", port=3306, db="test", user="root", passwd="123456", charset="utf8")
curs = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
insert_sql="""
    insert into stu VALUES ("%s","%s",%d);
"""
result=curs.execute(insert_sql % ("zhangsan",20,1))
conn.commit()

print result
