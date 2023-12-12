import pymysql
import func

conn = pymysql.connect(host='localhost', user='root', password='@Zbc0038;', database='sysu_database', port=3306)
func.rent_car(2, 2, 4, 20231212, 20231215, conn)
func.setTime(conn, 20231216)
func.return_car(conn, 4, 1, 20231216)