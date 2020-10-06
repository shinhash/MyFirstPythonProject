import sqlite3


# conn = sqlite3.connect("./FileDBTest.db")
conn = sqlite3.connect("./FileDBTest.db", isolation_level=None)
cursor = conn.cursor()

sql = "update FileDBTest set content=:1  where file_id=:2"
data = ("Rechanged", "1")

cursor.execute(sql, data)
# conn.commit()
