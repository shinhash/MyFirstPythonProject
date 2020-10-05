import cx_Oracle
import os


os.putenv('NLS_LANG', '.UTF8')

# conn = cx_Oracle.connect('SHS', 'java', 'localhost/xe')
conn = cx_Oracle.connect('SHS/java@localhost:1521/xe')
cursor = conn.cursor()


cursor.execute('select * from temp02')
for temp in cursor:
    print(temp)    
    
# java의 prestme와 같다
sql = "update temp02 set col2=:1 where col2=:2"
data = ('시험글작성중', 'test2')
cursor.execute(sql,data)




cursor.execute('select * from temp02')
for temp in cursor:
    print(temp)