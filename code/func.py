import pymysql


def usrlogin(input_usr_id, input_password, conn):
    # 此函数需要根据输入的usr_id值，在usr表中找到对应的表项，并对比输入的password
    if input_usr_id == 1:
        if input_password == '123456':
            return 2                # 表示当前登入的是manager
        else:
            return False            # manager登入错误

    cursor = conn.cursor()
    cursor.execute("select * from sysu_database.user where usr_id = '%d'" % input_usr_id)
    results = cursor.fetchall()
    if len(results) != 0:
        if input_password == results[0][4]:
            return 1                    # 当前登入的是普通user
        else:
            return False                # 密码错误
    else:
        return False                    # 不存在此用户
