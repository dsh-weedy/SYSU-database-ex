# 用于创建数据库的表
import pymysql

try:
    #创建与数据库的连接
    conn = pymysql.connect(host='localhost', user='root', password='@Zbc0038;', database='sysu_database', port=3306)
    # 创建游标
    cursor = conn.cursor()
    #创建表的sql
    sql = '''
        CREATE TABLE `user`  (
            `usr_id` INT NOT NULL,
            `name` VARCHAR(20) NOT NULL,
            `age` INT NOT NULL,
            `email` VARCHAR(30) NOT NULL,
            `password` VARCHAR(30) NOT NULL,
            `creditcard` VARCHAR(30),
          -- 定义主键，并使用BTREE索引
          PRIMARY KEY (`usr_id`) USING BTREE
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
            `image` VARCHAR(50),
            `car_id` INT NOT NULL,
            `price` INT NOT NULL,
            `rent` INT NOT NULL,
            `model` VARCHAR(30) NOT NULL,
            `state` INT NOT NULL,
            `description` VARCHAR(500),
            `deposit` INT,
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
            `usr_id` INT NOT NULL,
            `car_id` INT NOT NULL,
            `emp_id` INT NOT NULL,
            `price` INT NOT NULL,
            `purchase_date` INT NOT NULL,
            -- 定义复合主键，并使用BTREE索引
          PRIMARY KEY (`purchase_id`) USING BTREE,
            -- 使用BTREE加速对于dept_no的搜索速度
          INDEX `usr_id_Btree`(`usr_id`) USING BTREE,
          INDEX `car_id_Btree`(`car_id`) USING BTREE,
          INDEX `emp_id_Btree`(`emp_id`) USING BTREE,
          -- 定义外键约束，外键来自于user中的usr_id，删除采用级联删除，更新采用RESTRICT
          CONSTRAINT `purchase_usr` FOREIGN KEY (`usr_id`) REFERENCES `user` (`usr_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
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
            `usr_id` INT NOT NULL,
            `car_id` INT NOT NULL,
            `emp_id` INT NOT NULL,
	        `rent_tot` INT NOT NULL,
	        `begin_date` INT NOT NULL,
	        `end_date` INT NOT NULL,
	        `return_date` INT,
	        `state` INT NOT NULL,
            -- 定义复合主键，并使用BTREE索引
          PRIMARY KEY (`lease_id`) USING BTREE,
          -- 使用BTREE加速对于搜索速度
          INDEX `usr_id_Btree`(`usr_id`) USING BTREE,
          INDEX `car_id_Btree`(`car_id`) USING BTREE,
          INDEX `emp_id_Btree`(`emp_id`) USING BTREE,
          -- 定义外键约束，外键来自于employee中的emp_no，删除采用级联删除，更新采用RESTRICT
          CONSTRAINT `lease_usr` FOREIGN KEY (`usr_id`) REFERENCES `user` (`usr_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
          -- 定义外键约束，外键来自于departments中的dept_no，删除采用级联删除，更新采用RESTRICT
          CONSTRAINT `lease_car` FOREIGN KEY (`car_id`) REFERENCES `car` (`car_id`) ON DELETE CASCADE ON UPDATE RESTRICT,
          CONSTRAINT `lease_emp` FOREIGN KEY (`emp_id`) REFERENCES `employees` (`emp_id`) ON DELETE CASCADE ON UPDATE RESTRICT
        );
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TABLE `fine` (
            `lease_id` INT NOT NULL,
            `fine_value` INT NOT NULL,
          PRIMARY KEY (`lease_id`)
        );
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TABLE `global_time`  (
            `time_global` INT NOT NULL,
            `global_year` INT NOT NULL,
            `global_month` INT NOT NULL,
            `global_day` INT NOT NULL,
          PRIMARY KEY (`time_global`)
        );
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TRIGGER update_lease_trigger
        BEFORE UPDATE ON global_time
        FOR EACH ROW
        BEGIN
            DECLARE carState INT;
            DECLARE leaseCarId INT;
        
            -- 获取车辆状态和lease表对应的car_id
            SELECT car.state, lease.car_id INTO carState, leaseCarId
            FROM car
            JOIN lease ON car.car_id = lease.car_id
            WHERE lease.begin_date = CONCAT(NEW.global_year, NEW.global_month, NEW.global_day) AND lease.state = 0
            LIMIT 1;
        
            -- 根据车辆状态更新lease表
            UPDATE lease
            SET state = CASE 
                WHEN carState = 2 THEN 1  -- 车辆处于空闲状态，订单进行中
                ELSE 4                     -- 车辆不处于空闲状态，订单取消
            END
            WHERE begin_date = CONCAT(NEW.global_year, NEW.global_month, NEW.global_day) AND state = 0;
        
            -- 更新car表
            IF carState = 2 THEN
                -- 车辆处于空闲状态，将车辆状态置为被租用
                UPDATE car
                SET state = 1
                WHERE car_id = leaseCarId;
            END IF;
        END;
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TRIGGER update_lease_status_trigger
        AFTER UPDATE ON global_time
        FOR EACH ROW
        BEGIN
            UPDATE lease
            SET state = 3
            WHERE state = 1
            AND NEW.global_year * 10000 + NEW.global_month * 100 + NEW.global_day > lease.end_date;
        END;
    '''
    cursor.execute(sql)

    sql = '''
        CREATE TRIGGER check_return_date_trigger
        AFTER UPDATE ON lease
        FOR EACH ROW
        BEGIN
            DECLARE fineValue INT;
            DECLARE rentPerDay INT;
            DECLARE overDueDay INT;
			DECLARE tempOverDue INT;
            IF OLD.return_date IS NULL AND NEW.return_date IS NOT NULL THEN
                -- 获取租赁车辆的rent值
                SELECT rent INTO rentPerDay
                FROM car
                WHERE car_id = NEW.car_id;

                -- 计算逾期的天数
                SET tempOverDue = (NEW.return_date - NEW.end_date) / 10000 * 365 + (((NEW.return_date - NEW.end_date) / 100) % 100) * 30 + (NEW.return_date - NEW.end_date) % 100;
--                 -- 计算罚款值,每天租金的1.5倍率
				SET overDueDay = GREATEST(0, tempOverDue);
                SET fineValue = overDueDay * rentPerDay * 1.5;
                -- 如果是逾期还车，插入fine表中
                IF fineValue > 0 THEN
                  INSERT INTO fine (lease_id, fine_value)
                  VALUES (NEW.lease_id, fineValue);
                END IF;
            END IF;
        END;
    '''
    cursor.execute(sql)

except:
    print('创建表失败')
finally:
    #关闭数据库连接
    conn.close()

# 数据库创建完成
