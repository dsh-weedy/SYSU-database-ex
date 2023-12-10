import pymysql

def connect_db():
    db = pymysql.connect(host = "localhost", user = "root", password = "123456",database = "car", port = 3306)
    return db

db = connect_db()
sql = "select * from customer"
cursor = db.cursor()
cursor.execute(sql)

result = cursor.fetchall()
print(result)