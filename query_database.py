import sqlite3
from sqlite3.dbapi2 import connect

conn = sqlite3.connect("db_GV_Mis.db")

c = conn.cursor()

sql_create_table = """
    CREATE TABLE GVs(
    Hoten text,
    Email text,
    Chucvu text,
    SĐT integer
)
"""
sql_insert = 'INSERT INTO GVs VALUES("Nguyễn Thị Yến","yennt@hvnh.edu.vn","Giảng viên",904150682)'


sql_select = """
select * from GVs
"""

try:
    c.execute(sql_insert)
    conn.commit()
    # c.execute(sql_select)
    # print(c.fetchall())
    # print("OK")
except:
    print("Lỗi")
conn.close()