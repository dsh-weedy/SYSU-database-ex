import pymysql
import inquire
import sys

sys.path.append("/SYSU-database-ex")

def connect_db():
    db = pymysql.connect(host = "localhost", user = "root", password = "123456",database = "sysu_database", port = 3306)
    return db



db = connect_db()


result1,result2 = inquire.inquire_usr_order(db,1)

print(result1)
print(result2)

db.close()