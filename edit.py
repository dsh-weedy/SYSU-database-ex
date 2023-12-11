import pymysql

import connect
import inquire

# add new car to car list
def add_car(car_id,price,rent,model,state,deposit):
    # create connetion and cursor
    db = connect.connect_db() 
    cursor = db.cursor() 

    # add new car to list
    sql = "insert into car values (%s,%s,%s,%s,%s,%s)"
    values = (car_id,price,rent,model,state,deposit)
    
    affected_rows = cursor.execute(sql, values)

    # comit changes
    db.commit()
    db.close()

    # chek affected_rows to check whether add is success
    if affected_rows > 0:
        return True
    return False

# delete particular car_id from car list
def delete_car(car_id):
    # create connetion and cursor
    db = connect.connect_db() 
    cursor = db.cursor() 

    # delet car to list
    sql = "delete from car where car_id = %s"
    cursor.execute(sql,(car_id))

    # comit changes
    db.commit()

    # inquire again
    car_all = inquire.inquire_car_all()
    db.close()

    return car_all

# add_car("2",2,3,"4",1,100)
delete_car("2")

print(inquire.inquire_car_all())