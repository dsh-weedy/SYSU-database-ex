import pymysql
import inquire
import sys
import edit

sys.path.append("/SYSU-database-ex")

def connect_db():
    db = pymysql.connect(host = "localhost", user = "root", password = "123456",database = "sysu_database", port = 3306)
    return db



db = connect_db()


# result = inquire.inquire_particular(db,"car",4)
result = edit.add_usr(db,"eric",2,"13299939@qq.com","123120","12121-asda-2")
print(result)

db.close()