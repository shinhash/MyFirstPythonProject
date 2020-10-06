import sqlite3


# conn = sqlite3.connect("./FileDBTest.db")
conn = sqlite3.connect("./FileDBTest.db", isolation_level=None)
cursor = conn.cursor()

sql = "delete from FileDBTest where file_id=?"
data = ("4",)
cursor.execute(sql, data)
# conn.commit()