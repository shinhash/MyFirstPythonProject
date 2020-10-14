import cx_Oracle
import os


os.putenv('NLS_LANG', '.UTF8')

# conn = cx_Oracle.connect('SHS', 'java', 'localhost/xe')
conn = cx_Oracle.connect('SHS/java@localhost:1521/xe')
cursor = conn.cursor()


# java의 prestme와 같다
sql = "insert into FOODSTORE(STORENAME, FOODNAME, FOODPRICE) values(:1, :2, :3)"
data = ('tt1', 'tt2', 1)
for i in range(1,9):
    cursor.execute(sql, data)

# conn.commit()
# for item in data:
#     cursor.execute(sql, data)
    
    
 
cursor.execute('select * from FOODSTORE')
for temp in cursor:
    print(temp)    
    
