import pymysql


READY = 1
RENT = 2
SALE = 3

# use usr_id to inquire usr_purchase_id usr_lease_id
def inquire_usr_order(db,usr_id):
    # create cursor
    cursor = db.cursor() 

    # inquire purchase list
    sql = "select * from purchase where usr_id = %s"
    
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

# inquire car which is avlible return car_id
def inquire_car_avlible(db):
    # create cursor
    cursor = db.cursor() 

    # inquire car which is avlible
    sql = "select *\
          from car \
          where state = %s"
    
    values = (READY)
    cursor.execute(sql,values)
    result_car_avlible = cursor.fetchall()

    return result_car_avlible

# iniquire all item in table
def inquire_all(db,table):
    # create cursor
    cursor = db.cursor() 

    # inquire emp list
    sql = "select * from " + table
    
    # execute inquiry
    cursor.execute(sql)
    result = cursor.fetchall()
    
    return result


# iniquire particular item in table
def inquire_all(db,table,id):
    # create cursor
    cursor = db.cursor() 

    # inquire emp list
    sql = "select * from " + table + " where "
    
    if table == "car":
        sql += "car_id=%s"
    elif table == "employees":
        sql += "emp_id=%s"
    elif table == "lease":
        sql += "lease=%s"
    elif table == "purchase":
        sql += "purchase_id=%s"
    elif table == "user":
        sql += "usr_id=%s"
    

    values = (id)
    # execute inquiry
    cursor.execute(sql,values)
    result = cursor.fetchall()
    
    return result
