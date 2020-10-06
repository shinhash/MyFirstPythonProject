import sqlite3


# conn = sqlite3.connect("./FileDBTest.db")
conn = sqlite3.connect("./FileDBTest.db", isolation_level=None)
cursor = conn.cursor()

sql = "select max(file_id)+1 from FileDBTest"

cursor.execute(sql)

for item in cursor:
    fileId = item[0]

sql = "insert into FileDBTest(file_id, content) values( ? , ? )"
data = (str(fileId), "시험용 작성글")
cursor.execute(sql,data)
# conn.commit()
