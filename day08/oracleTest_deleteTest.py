import cx_Oracle
import os


os.putenv('NLS_LANG', '.UTF8')

# conn = cx_Oracle.connect('SHS', 'java', 'localhost/xe')
conn = cx_Oracle.connect('SHS/java@localhost:1521/xe')
cursor = conn.cursor()


    
# java의 prestme와 같다
sql="delete from TEMP02 where col1=:1"
data=('22',)
cursor.execute(sql,data)

conn.commit()

