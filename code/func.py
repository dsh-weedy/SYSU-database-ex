
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


def check_car_available(conn):
    # 此函数用于查询当前在库中的所有可用的车辆，并返回它们的car_id
    cursor = conn.cursor()
    cursor.execute("select car_id from sysu_database.car where state = 2")
    results = list(cursor.fetchall())
    # 在car表中，state包含0、1、2，分别表示已卖出、被租用、空闲
    # 返回的results是一个car_id的List
    return results


def check_emp(conn):
    # 查询表employee, 返回值为emp_id,name,email
    cursor = conn.cursor()
    cursor.execute("select emp_id, employees.name, email from sysu_database.employees")
    results = list(cursor.fetchall())

    return results


def check_car_detail(input_car_id, conn):
    # 查询数据表car，并根据car_id获得该辆车的详细信息
    cursor = conn.cursor()
    cursor.execute("select image, description, price, model, rent from sysu_database.car where car_id = '%d'" % input_car_id)
    results = list(cursor.fetchall())

    return results


def check_cus_detail(input_usr_id, conn):
    # 查看个⼈信息，根据usr_id查询返回对应用户的name，email
    cursor = conn.cursor()
    cursor.execute("select user.name, email from sysu_database.user where usr_id = '%d'" % input_usr_id)
    results = (cursor.fetchall())[0]

    return results