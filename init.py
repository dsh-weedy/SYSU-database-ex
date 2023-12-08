import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", password="DSHdsh0308!", db="tpch")

cursor = db.cursor()

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
db.close()


