import pymysql
import connect


def inquire_usr_order(usr_id):
    # create connetion and cursor
    db = connect.connect_db() 
    cursor = db.cursor() 

    # inquire purchase list
    sql = "select *\
          from purchase \
          where cus_id = %s" %(usr_id)
    
    cursor.execute(sql)
    result_purchase = cursor.fetchall()

    # inquire lease list
    sql = "select *\
        from lease \
        where usr_id = %s" %(usr_id)
    
    cursor.execute(sql)
    result_purchase = cursor.fetchall()

