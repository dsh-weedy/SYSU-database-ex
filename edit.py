import pymysql
import inquire

READY = 1
RENT = 2
SALE = 3


# add new car to car list
def add_car(db,image,car_id,price,rent,model,state,description,deposit):
    # create cursor
    cursor = db.cursor() 

    # add new car to list
    sql = "insert into car values (%s,%d,%d,%d,%s,%d,%s,%d)"
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
    # create cursor
    cursor = db.cursor() 

    # delet car to list
    sql = "delete from car where car_id = %d"
    cursor.execute(sql,(car_id))

    # comit changes
    db.commit()

    # inquire again
    car_all = inquire.inquire_car_all()

    return car_all

# return car, edit car state 
def return_car(db,car_id):
    # create cursor
    cursor = db.cursor() 

    # delet car to list
    sql = "update car set state = %d where car_id = %d"
    values = (READY,car_id)
    affected_rows = cursor.execute(sql, values)

    # comit changes
    db.commit()

