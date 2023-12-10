# 用于创建数据库的表
import pymysql

try:
    #创建与数据库的连接
    conn = pymysql.connect(host='localhost', user='root', password='@Zbc0038;', database='sysu_database', port=3306)
    # 创建游标
    cursor = conn.cursor()
    #创建表的sql
    sql = '''
        CREATE TABLE `customer`  (
            `cus_id` INT NOT NULL,
            `name` VARCHAR(20) NOT NULL,
            `age` INT NOT NULL,
            `email` VARCHAR(30) NOT NULL,
            `password` VARCHAR(30) NOT NULL,
            `creditcard` VARCHAR(30) NOT NULL,
          -- 定义主键，并使用BTREE索引
          PRIMARY KEY (`cus_id`) USING BTREE
        );
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TABLE `employees`  (
            `emp_id` INT NOT NULL,
            `name` VARCHAR(20) NOT NULL,
            `age` INT NOT NULL,
            `email` VARCHAR(30) NOT NULL,
          -- 定义主键，并使用BTREE索引
          PRIMARY KEY (`emp_id`) USING BTREE
        );
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TABLE `car`  (
            `car_id` INT NOT NULL,
            `price` INT NOT NULL,
            `rent` INT NOT NULL,
            `model` VARCHAR(30) NOT NULL,
            `state` INT NOT NULL,
            `deposit` INT NOT NULL,
            -- 定义复合主键，并使用BTREE索引
         PRIMARY KEY (`car_id`) USING BTREE,
            -- 使用BTREE加速对于dept_no的搜索速度
         INDEX `dept_no_Btree` (`model`) USING BTREE
        );
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TABLE `purchase`  (
            `purchase_id` INT NOT NULL,
            `cus_id` INT NOT NULL,
            `car_id` INT NOT NULL,
            `emp_id` INT NOT NULL,
            `price` INT NOT NULL,
            -- 定义复合主键，并使用BTREE索引
          PRIMARY KEY (`purchase_id`) USING BTREE,
            -- 使用BTREE加速对于dept_no的搜索速度
          INDEX `cus_id_Btree`(`cus_id`) USING BTREE,
          INDEX `car_id_Btree`(`car_id`) USING BTREE,
          INDEX `emp_id_Btree`(`emp_id`) USING BTREE,
          -- 定义外键约束，外键来自于customer中的cus_id，删除采用级联删除，更新采用RESTRICT
          CONSTRAINT `purchase_cus` FOREIGN KEY (`cus_id`) REFERENCES `customer` (`cus_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
          -- 定义外键约束，外键来自于car中的car_id，删除采用级联删除，更新采用RESTRICT
          CONSTRAINT `purchase_car` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
          -- 定义外键约束，外键来自于employees中的emp_id，删除采用级联删除，更新采用RESTRICT
          CONSTRAINT `purchase_emp` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`) ON DELETE CASCADE ON UPDATE RESTRICT
        );
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TABLE `lease`  (
            `lease_id` INT NOT NULL,
            `cus_id` INT NOT NULL,
            `car_id` INT NOT NULL,
            `emp_id` INT NOT NULL,
	        `rent_tot` INT NOT NULL,
	        `begin_date` DATE NOT NULL,
	        `end_date` DATE NOT NULL,
	        `return_date` DATE,
	        `state` INT NOT NULL,
            -- 定义复合主键，并使用BTREE索引
          PRIMARY KEY (`lease_id`) USING BTREE,
          -- 使用BTREE加速对于搜索速度
          INDEX `cus_id_Btree`(`cus_id`) USING BTREE,
          INDEX `car_id_Btree`(`car_id`) USING BTREE,
          INDEX `emp_id_Btree`(`emp_id`) USING BTREE,
          -- 定义外键约束，外键来自于employee中的emp_no，删除采用级联删除，更新采用RESTRICT
          CONSTRAINT `lease_cus` FOREIGN KEY (`cus_id`) REFERENCES `customer` (`cus_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
          -- 定义外键约束，外键来自于departments中的dept_no，删除采用级联删除，更新采用RESTRICT
          CONSTRAINT `lease_car` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
          CONSTRAINT `lease_emp` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`) ON DELETE CASCADE ON UPDATE RESTRICT
        );
    '''
    cursor.execute(sql)
except:
    print('创建表失败')
finally:
    #关闭数据库连接
    conn.close()

# 数据库创建完成
