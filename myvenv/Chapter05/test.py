import os
import sqlite3

# 해당 python file의 전체 path를 가져온다.
# ex) c:/users/Desktop/python_advanced/myvenv/Chapter05
path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, 'SQL_DDL.db')
conn = sqlite3.connect(db)

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
CREATE_SQL = """
     CREATE TABLE IF NOT EXISTS Item (
         id integer primary key autoincrement,
         code text not null,
         name text not null,
         price integer not null
     )
"""

# SQL 명령 실행
cur.execute(CREATE_SQL)

# 데이터베이스 닫기
conn.close()