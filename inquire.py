import pymysql
import connect

READY = 1
RENT = 2
SALE = 3

# use usr_id to inquire usr_purchase_id usr_lease_id
def inquire_usr_order(db,usr_id):
    # create cursor
    cursor = db.cursor() 

    # inquire purchase list
    sql = "select *\
          from purchase \
          where usr_id = %d"
    
    # inquire
    values = (usr_id)
    cursor.execute(sql,values)
    usr_purchase = cursor.fetchall()

    # inquire lease list
    sql = "select * \
        from lease \
        where usr_id = %s" 
    
    # inquire
    values = (usr_id)
    cursor.execute(sql,values)
    usr_lease = cursor.fetchall()

    # return usr_purchase_id usr_lease_id
    return usr_purchase,usr_lease


# inquire all item in car, return car with particular car_id
def inquire_usr_detail(db,usr_id):
    # create cursor
    cursor = db.cursor() 

    # inquire usr list
    sql = "select * from usr where usr_id = %d"
    values = (usr_id)
    
    cursor.execute(sql,values)
    result_usr = cursor.fetchall()

    return result_usr

# inquire all item in car, return car
def inquire_car_all(db):
    # create cursor
    cursor = db.cursor() 

    # inquire car list
    sql = "select *\
          from car "
    
    cursor.execute(sql)
    result_car = cursor.fetchall()

    return result_car

# inquire car which is avlible return car_id
def inquire_car_avlible(db):
    # create cursor
    cursor = db.cursor() 

    # inquire car which is avlible
    sql = "select *\
          from car \
          where state = %d"
    
    values = (READY)
    cursor.execute(sql,values)
    result_car_avlible = cursor.fetchall()

    return result_car_avlible

# inquire all item in car, return car with particular car_id
def inquire_car_detail(db,car_id):
    # create cursor
    cursor = db.cursor() 

    # inquire emp list
    sql = "select * from car where car_id = %d"
    values = (car_id)
    
    cursor.execute(sql,values)
    result_car = cursor.fetchall()

    return result_car

# inquire all item in employees, return emp
def inquire_emp_all(db):
    # create cursor
    cursor = db.cursor() 

    # inquire emp list
    sql = "select *\
          from emp "
    
    cursor.execute(sql)
    result_emp = cursor.fetchall()
    
    return result_emp
