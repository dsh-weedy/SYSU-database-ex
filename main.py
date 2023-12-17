import math
import sys

import pymysql
from PyQt5 import QtWidgets

import func, inquire, edit, my_func
from windows import Login, User_main, User_person, Buy, Lease, Manager_check, Add_car


class SYSU_database():
    def __init__(self):
        super().__init__()

        self.get_windows()
        self.login_bind()
        self.user_main_bind()
        self.user_person_bind()
        self.buy_bind()
        self.lease_bind()
        self.manager_check_bind()
        self.add_car_bind()

        self.user_id = -1

    def get_windows(self):
        self.login = Login()
        self.user_main = User_main(conn)
        self.user_person = User_person()
        self.buy = Buy(conn)
        self.lease = Lease(conn)
        self.manager_check = Manager_check(conn)
        self.add_car = Add_car()


    def login_bind(self):
        self.login.lineEdit_username.setText('1')
        self.login.lineEdit_password.setText('123456')
        self.login.pushButton_login.clicked.connect(self.login_check)

    def user_main_bind(self):
        self.user_main.pushButton_buy1.clicked.connect(lambda: self.user_main2buy(0))
        self.user_main.pushButton_buy2.clicked.connect(lambda: self.user_main2buy(1))
        self.user_main.pushButton_buy3.clicked.connect(lambda: self.user_main2buy(2))
        self.user_main.pushButton_buy4.clicked.connect(lambda: self.user_main2buy(3))
        self.user_main.pushButton_buy5.clicked.connect(lambda: self.user_main2buy(4))
        self.user_main.pushButton_buy6.clicked.connect(lambda: self.user_main2buy(5))
        self.user_main.pushButton_lease1.clicked.connect(lambda: self.user_main2lease(0))
        self.user_main.pushButton_lease2.clicked.connect(lambda: self.user_main2lease(1))
        self.user_main.pushButton_lease3.clicked.connect(lambda: self.user_main2lease(2))
        self.user_main.pushButton_lease4.clicked.connect(lambda: self.user_main2lease(3))
        self.user_main.pushButton_lease5.clicked.connect(lambda: self.user_main2lease(4))
        self.user_main.pushButton_lease6.clicked.connect(lambda: self.user_main2lease(5))
        self.user_main.pushButton_pre.clicked.connect(self.user_main_pre)
        self.user_main.pushButton_next.clicked.connect(self.user_main_next)
        self.user_main.pushButton_person.clicked.connect(self.user_main2person)

    def user_person_bind(self):
        self.user_person.pushButton_signout.clicked.connect(self.user_person2login)
        self.user_person.pushButton_back.clicked.connect(self.user_person2main)
        self.user_person.pushButton_return.clicked.connect(lambda: self.user_person.return_car(conn, self.user_id))

    def buy_bind(self):
        self.buy.pushButton_back.clicked.connect(self.buy2user_main)
        self.buy.pushButton_buy.clicked.connect(lambda: self.customer_buy(self.buy.i))

    def lease_bind(self):
        self.lease.pushButton_back.clicked.connect(self.lease2user_main)
        self.lease.pushButton_lease.clicked.connect(lambda: self.customer_lease(self.lease.i))

    def manager_check_bind(self):
        self.manager_check.pushButton_customer.clicked.connect(lambda: self.manager_check.update_customer(conn))
        self.manager_check.pushButton_car.clicked.connect(lambda: self.manager_check.update_car(conn))
        self.manager_check.pushButton_buy.clicked.connect(lambda: self.manager_check.update_buy(conn))
        self.manager_check.pushButton_lease.clicked.connect(lambda: self.manager_check.update_lease(conn))
        self.manager_check.pushButton_emplyee.clicked.connect(lambda: self.manager_check.update_emp(conn))
        self.manager_check.pushButton_fine.clicked.connect(lambda: self.manager_check.update_fine(conn))
        self.manager_check.pushButton.clicked.connect(self.manager_check2login)
        self.manager_check.pushButton_add.clicked.connect(self.manager_check2add_car)
        self.manager_check.pushButton_sub.clicked.connect(lambda: self.manager_check.remove_car(conn))
        self.manager_check.pushButton_time.clicked.connect(lambda: self.manager_check.set_time(conn, calender))

    def add_car_bind(self):
        self.add_car.pushButton_back.clicked.connect(self.add_car2manager_check)
        self.add_car.pushButton_ack.clicked.connect(lambda: self.manager_check.insert_car(self.add_car, conn))
        self.add_car.pushButton_ack.clicked.connect(self.add_car2manager_check)

    def login_check(self):
        self.user_id = int(self.login.lineEdit_username.text())
        username = int(self.login.lineEdit_username.text())
        password = str(self.login.lineEdit_password.text())
        print('username:', username, 'password:', password)
        login_res = func.usrlogin(username, password, conn)
        if login_res == 0:
            print('连接失败')
        elif login_res == 1:
            self.login.close()
            self.user_person.update_userid(self.user_id, conn)
            self.user_main.show()
            self.user_main.update_page(conn, self.user_id)
            print('customer login')
        elif login_res == 2:
            self.login.close()
            self.manager_check.show()
            print('manager login')
        self.login.lineEdit_username.clear()
        self.login.lineEdit_password.clear()
        self.manager_check.listWidget.clear()

    def user_main2buy(self, i):
        print(self.user_main.show_index * 6 + i)
        if self.user_main.show_index * 6 + i >= len(self.user_main.car_list):
            print('无效车辆')
            return
        self.buy.update_info(self.user_main.show_index * 6 + i,
                             self.user_main.car_list[self.user_main.show_index * 6 + i], conn)
        self.buy.show()

    def user_main2lease(self, i):
        print(self.user_main.show_index * 6 + i)
        if self.user_main.show_index * 6 + i >= len(self.user_main.car_list):
            print('无效车辆')
            return
        self.lease.update_info(self.user_main.show_index * 6 + i,
                               self.user_main.car_list[self.user_main.show_index * 6 + i], conn)
        self.lease.show()

    def user_main_pre(self):
        print('user_main_pre')
        if self.user_main.show_index > 0:
            self.user_main.show_index -= 1
            print(self.user_main.show_index)
            self.user_main.update_page(conn, self.user_id)


    def user_main_next(self):
        print('user_main_next')
        if self.user_main.show_index + 1 < math.ceil((len(self.user_main.car_list)-1) / 6):
            self.user_main.show_index += 1
            print(self.user_main.show_index)
            self.user_main.update_page(conn, self.user_id)

    def user_main2person(self):
        self.user_main.close()
        self.user_person.update_userid(self.user_id, conn)
        self.user_person.show()

    def user_person2login(self):
        self.user_person.close()
        self.login.show()

    def user_person2main(self):
        self.user_person.close()
        self.user_main.update_page(conn, self.user_id)
        self.user_main.show()

    def buy2user_main(self):
        self.buy.close()
        self.user_main.update_page(conn, self.user_id)
        self.user_main.show()

    def customer_buy(self, i):
        # print('buy car:', self.buy.i, 'employee:', self.buy.comboBox.currentText())

        emp_id = int(self.buy.comboBox.currentText().split()[0])
        self.user_main.operation(conn, i, 'buy', self.user_id, emp_id)
        self.buy.close()
        self.user_main.update_page(conn, self.user_id)
        self.user_main.show()


    def lease2user_main(self):
        self.lease.close()
        self.user_main.update_page(conn, self.user_id)
        self.user_main.show()

    def customer_lease(self, i):
        begin_year = self.lease.lineEdit_1_year.text()
        begin_month = self.lease.lineEdit_1_month.text()
        begin_day = self.lease.lineEdit_1_day.text()
        end_year = self.lease.lineEdit_2_year.text()
        end_month = self.lease.lineEdit_2_month.text()
        end_day = self.lease.lineEdit_2_day.text()
        res, begin_date, end_date = self.check_lease_date(begin_year, begin_month, begin_day, end_year, end_month, end_day)
        if res:
            # print('lease car:', self.lease.i, 'employee:', self.buy.comboBox.currentText())
            # print('begin date:', begin_date, 'end date:', end_date)

            emp_id = int(self.lease.comboBox.currentText().split()[0])
            self.user_main.operation(conn, i, 'lease', self.user_id, emp_id, begin_date, end_date)
            self.lease.close()
            self.user_main.update_page(conn, self.user_id)
            self.user_main.show()
        else:
            print('无效日期')

    def check_lease_date(self, y1, m1, d1, y2, m2, d2):
        if y1 == '' or m1 == '' or d1 == '' or y2 == '' or m2 == '' or d2 == '':
            return False, -1, -1
        date0 = inquire.inquire_all(conn, 'global_time')[0]
        y0, m0, d0 = int(date0[1]), int(date0[2]), int(date0[3])
        y1, m1, d1, y2, m2, d2 = int(y1), int(m1), int(d1), int(y2), int(m2), int(d2)
        print(y0, m0, d0, ' ', y1, m1, d1, ' ', y2, m2, d2)
        if y1 < y0 or y2 < y0 or m1 <= 0 or m2 <= 0 or d1 <= 0 or d2 <= 0 or \
                m1 > 12 or m2 > 12 or d1 > calender[m1] or d2 > calender[m2]:
            return False, -1, -1
        else:
            y11, m11, d11 = str(y1), str(m1) if m1 >= 10 else '0' + str(m1), str(d1) if d1 >= 10 else '0' + str(d1)
            y22, m22, d22 = str(y2), str(m2) if m2 >= 10 else '0' + str(m2), str(d2) if d2 >= 10 else '0' + str(d2)
            date00, date11, date22 = str(date0[1]) + str(date0[2]) + str(date0[3]), y11 + m11 + d11, y22 + m22 + d22
            date00, date11, date22 = int(date00), int(date11), int(date22)
            if date00 < date11 < date22:
                return True, date11, date22
        return False, -1, -1

    def manager_check2login(self):
        self.manager_check.close()
        self.login.show()

    def manager_check2add_car(self):
        self.add_car.next_car_id = inquire.inquire_all(conn, 'car')[-1][1] + 1
        self.add_car.lineEdit_car_id.setText(str(self.add_car.next_car_id))
        self.add_car.lineEdit_model.clear()
        self.add_car.lineEdit_img.clear()
        self.add_car.lineEdit_rent.clear()
        self.add_car.lineEdit_price.clear()
        self.add_car.lineEdit_deposit.clear()
        self.add_car.lineEdit_description.clear()
        self.add_car.show()

    def add_car2manager_check(self):
        self.add_car.close()

    def run(self):
        self.login.show()


# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     db = SYSU_database()
#     conn = pymysql.connect(host='localhost', user='root', password='DSHdsh0308!', database='sysu_database', port=3306)
#     db.run()
#     # print(func.check_cus_detail(3, conn))
#     conn.close()
#     sys.exit(app.exec_())

calender = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

app = QtWidgets.QApplication(sys.argv)
conn = pymysql.connect(host='localhost', user='root', password='DSHdsh0308!', database='sysu_database', port=3306)

db = SYSU_database()
db.run()

conn.close()
sys.exit(app.exec_())












