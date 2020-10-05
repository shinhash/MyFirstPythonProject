import sqlite3


conn = sqlite3.connect("./FileDBTest.db")
cursor = conn.cursor()


sql = "select * from FileDBTest"
cursor.execute(sql)

for res in cursor:
    print(res)