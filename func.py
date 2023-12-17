
def usrlogin(input_usr_id, input_password, conn):
    conn.ping(reconnect=True)
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
    conn.ping(reconnect=True)
    # 此函数用于查询当前在库中的所有可用的车辆，并返回它们的car_id
    cursor = conn.cursor()
    cursor.execute("select car_id from sysu_database.car where state = 2")
    results = list(cursor.fetchall())
    # 在car表中，state包含0、1、2，分别表示已卖出、被租用、空闲
    # 返回的results是一个car_id的List
    return results


def check_emp(conn):
    conn.ping(reconnect=True)
    # 查询表employee, 返回值为emp_id,name,email
    cursor = conn.cursor()
    cursor.execute("select emp_id, employees.name, email from sysu_database.employees")
    results = list(cursor.fetchall())

    return results


def check_car_detail(input_car_id, conn):
    conn.ping(reconnect=True)
    # 查询数据表car，并根据car_id获得该辆车的详细信息
    cursor = conn.cursor()
    cursor.execute("select image, description, price, model, rent from sysu_database.car where car_id = '%d'" % input_car_id)
    results = list(cursor.fetchall())

    return results


def check_cus_detail(input_usr_id, conn):
    conn.ping(reconnect=True)
    # 查看个⼈信息，根据usr_id查询返回对应用户的name，email
    cursor = conn.cursor()
    cursor.execute("select user.name, email from sysu_database.user where usr_id = '%d'" % input_usr_id)
    results = (cursor.fetchall())[0]

    return results


def purchase_car(input_usr_id, input_emp_id, input_car_id, conn):
    conn.ping(reconnect=True)
    # 买车函数，需要输入为：usr_id(购买车的用户)、emp_id(负责本次购买的员工)、date(购买的日期)、car_id(购买的车辆)
    # 在购买记录中添加一个条目，并修改car表中的对应条目的值
    cursor = conn.cursor()

    cursor.execute("select max(purchase_id) from sysu_database.purchase")
    results = (cursor.fetchall())[0][0]
    if results is None:
        input_purchase_id = 1
    else:
        input_purchase_id = results + 1                       # 获取新增的订单号

    cursor.execute("select price from sysu_database.car where car_id = '%d'" % input_car_id)
    input_price = (cursor.fetchall())[0][0]                                 # 获取汽车的价格

    cursor.execute("select * from sysu_database.global_time")
    nowTime = (cursor.fetchall())[0]
    input_date = nowTime[1]*10000 + nowTime[2]*100 + nowTime[3]

    sql = '''
       insert into sysu_database.purchase(purchase_id, usr_id, car_id, emp_id, price, purchase_date) values(%s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(sql, (input_purchase_id, input_usr_id, input_car_id, input_emp_id, input_price, input_date))
    # 在购买记录purchase中添加一个新条目

    cursor.execute("update sysu_database.car set state = 0 where car_id = '%d'" % input_car_id)
    # 将该辆车的状态修改为“已卖出”

    conn.commit()


def countBegin2End(input_begin_date, input_end_date):
    # 这个函数用于计算开始日期和结束日期之间相差的天数
    input_begin_year = input_begin_date // 10000
    input_begin_month = input_begin_date // 100 % 100
    input_begin_day = input_begin_date % 100

    input_end_year = input_end_date // 10000
    input_end_month = input_end_date // 100 % 100
    input_end_day = input_end_date % 100

    return (input_end_year - input_begin_year) * 365 + (input_end_month - input_begin_month) * 30 + (input_end_day - input_begin_day)


def rent_car(input_usr_id, input_emp_id, input_car_id, input_begin_date, input_end_date, conn):
    conn.ping(reconnect=True)
    # 租车函数，需要输入为：usr_id(租车的用户)、emp_id(负责本次租车的员工)、date(租车的日期)、car_id(租用的车辆)、
    # input_date(租用订单的创建日期)、begin_date(租车的开始日期)、end_date(租车的结束日期)
    cursor = conn.cursor()

    cursor.execute("select max(lease_id) from sysu_database.lease")
    results = (cursor.fetchall())[0][0]
    if results is None:
        input_lease_id = 1
    else:
        input_lease_id = results + 1

    cursor.execute("select rent from sysu_database.car where car_id = '%d'" % input_car_id)
    now_car_rent = (cursor.fetchall())[0][0]

    dateCount = countBegin2End(input_begin_date, input_end_date)
    input_rent_tot = now_car_rent * dateCount

    sql = '''
        insert into sysu_database.lease(lease_id, usr_id, car_id, emp_id, rent_tot, begin_date, end_date, return_date, state) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    cursor.execute(sql, (input_lease_id, input_usr_id, input_car_id, input_emp_id, input_rent_tot, input_begin_date, input_end_date, None, 0))

    # 这里暂时不需要将车辆的状态修改为“被租用”，而是等到开始的那一天到来时，顺序遍历订单，选择被租用的车辆
    # 订单的状态为：0未开始、1进行中、2已结束、3已逾期（逾期的订单需要更新罚款？考虑增加条目）、4被取消（或者可以和2并在一起）
    conn.commit()


def return_car(conn, input_car_id, input_lease_id, input_return_date):
    conn.ping(reconnect=True)
    # 还车函数
    # create cursor
    cursor = conn.cursor()
    print(type(input_car_id), type(input_lease_id), type(input_return_date))
    cursor.execute("update sysu_database.car set state = 2 where car_id = '%d'" % input_car_id)
    sql = '''
        update sysu_database.lease
        set state = 2, return_date = %s
        where lease_id = %s
    '''

    cursor.execute(sql, (input_return_date, input_lease_id))

    conn.commit()


def setTime(conn, input_time):
    conn.ping(reconnect=True)
    # 设置全局时间
    cursor = conn.cursor()

    input_time_year = input_time // 10000
    input_time_month = input_time // 100 % 100
    input_time_day = input_time % 100
    # sql = '''
    #     insert into sysu_database.global_time(time_global, global_year, global_month, global_day) values (1, %s, %s, %s)
    # '''
    sql = '''
            update sysu_database.global_time
            set global_year = %s, global_month = %s, global_day = %s
            where time_global = 0
        '''
    cursor.execute(sql, (input_time_year, input_time_month, input_time_day))
    conn.commit()
