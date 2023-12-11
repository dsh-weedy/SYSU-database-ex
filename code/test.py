import pymysql
import func

conn = pymysql.connect(host='localhost', user='root', password='@Zbc0038;', database='sysu_database', port=3306)
print(func.check_cus_detail(3, conn))

