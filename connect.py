import pymysql
import inquire
import sys

sys.path.append("/SYSU-database-ex")

def connect_db():
    db = pymysql.connect(host = "localhost", user = "root", password = "123456",database = "sysu_database", port = 3306)
    return db



db = connect_db()


result = inquire.inquire_all(db,"employees")
print(result)

db.close()