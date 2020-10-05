import sqlite3


conn = sqlite3.connect("./FileDBTest.db")
cursor = conn.cursor()

sql = "delete from FileDBTest where file_id=?"
data = ("tt",)
cursor.execute(sql, data)