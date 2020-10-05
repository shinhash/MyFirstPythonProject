import cx_Oracle
import os


os.putenv('NLS_LANG', '.UTF8')

# conn = cx_Oracle.connect('SHS', 'java', 'localhost/xe')
conn = cx_Oracle.connect('SHS/java@localhost:1521/xe')
cursor = conn.cursor()


# java의 prestme와 같다
sql = "insert into temp02(col1, col2, col3) values(:1, :2, :3)"
data = ('테스트_2321_1', '테스트_2321_2', '테스트_2321_3')
cursor.execute(sql, data)

# conn.commit()
# for item in data:
#     cursor.execute(sql, item)
    
    
 
cursor.execute('select * from temp02')
for temp in cursor:
    print(temp)    
    
