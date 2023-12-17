import pymysql
'''
根据用户id返回购买记录
'''
def get_user_buylist(conn, user_id):
    is_connect = conn.ping()
    if is_connect == False:
        print("数据库断开连接")

    cursor = conn.cursor()

    sql = "select * from purchase where usr_id = " + str(user_id)

    cursor.execute(sql)
    result = cursor.fetchall()

    return result

'''
根据用户id返回租借记录
'''
def get_user_leaselist(conn, user_id):
    is_connect = conn.ping()
    if is_connect == False:
        print("数据库断开连接")

    cursor = conn.cursor()

    sql = "select * from lease where usr_id = " + str(user_id)

    cursor.execute(sql)
    result = cursor.fetchall()

    return result

'''
返回时间
'''
def get_time(conn):
    is_connect = conn.ping()
    if is_connect == False:
        print("数据库断开连接")

    cursor = conn.cursor()

    sql = "select * from global_time"

    cursor.execute(sql)
    result = cursor.fetchall()
    year, month, day = result[0][1], result[0][2], result[0][3]
    res = str(year * 10000 + month * 100 + day)

    return res
