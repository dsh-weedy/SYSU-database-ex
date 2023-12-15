import pymysql
import inquire

READY = 1
RENT = 2
SALE = 3


# add new car to car list
def add_car(db,image,car_id,price,rent,model,state,description,deposit):
    # check whether database is connected
    is_connect = db.ping()
    if is_connect == False:
        print("数据库断开连接")
    # create cursor
    cursor = db.cursor() 

    # add new car to list
    sql = "insert into car values (%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (image,car_id,price,rent,model,state,description,deposit)

    affected_rows = cursor.execute(sql, values)

    # comit changes
    db.commit()

    # chek affected_rows to check whether add is success
    if affected_rows > 0:
        return True
    return False

# delete particular car_id from car list
def delete_car(db,car_id):
    # check whether database is connected
    is_connect = db.ping()
    if is_connect == False:
        print("数据库断开连接")

    # create cursor
    cursor = db.cursor() 

    # delet car to list
    sql = "delete from car where car_id = %s"
    cursor.execute(sql,(car_id))

    # comit changes
    db.commit()

    # inquire again
    car_all = inquire.inquire_car_all()

    return car_all

# return car, edit car state 
def return_car(db,car_id):
    # check whether database is connected
    is_connect = db.ping()
    if is_connect == False:
        print("数据库断开连接")
    
    # create cursor
    cursor = db.cursor() 

    # delet car to list
    sql = "update car set state = %s where car_id = %s"
    values = (READY,car_id)
    affected_rows = cursor.execute(sql, values)

    # comit changes
    db.commit()

# create user account
def add_usr(db,name,age,email,password,creditcard):
    # check whether database is connected
    is_connect = db.ping()
    if is_connect == False:
        print("数据库断开连接")
    # create cursor
    cursor = db.cursor() 

    # delet car to list
    sql = "select usr_id from user"
    affected_rows = cursor.execute(sql)
    print(affected_rows)
    affected_rows += 2

    sql = "insert into user (usr_id,name,age,email,password,creditcard) values (%s,%s,%s,%s,%s,%s)"

    values = (affected_rows, name, age, email, password, creditcard)
    affected = cursor.execute(sql,values)
    # comit changes
    db.commit()

    if affected == 0:
        return 0
    else :
        return affected_rows


