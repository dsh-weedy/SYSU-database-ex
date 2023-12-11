import math
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import pandas as pd
import numpy as np

from windows import Login, User_main, User_person, Buy, Lease, Manager_check, Add_car

users = {'123': ['123', 'cus'], '456': ['456', 'man']}


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


    def get_windows(self):
        self.login = Login()
        self.user_main = User_main()
        self.user_person = User_person()
        self.buy = Buy()
        self.lease = Lease()
        self.manager_check = Manager_check()
        self.add_car = Add_car()


    def login_bind(self):
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

    def buy_bind(self):
        self.buy.pushButton_back.clicked.connect(self.buy2user_main)
        self.buy.pushButton_buy.clicked.connect(lambda: self.customer_buy(self.buy.i))


    def lease_bind(self):
        self.lease.pushButton_back.clicked.connect(self.lease2user_main)
        self.lease.pushButton_lease.clicked.connect(lambda: self.customer_lease(self.lease.i))

    def manager_check_bind(self):
        self.manager_check.pushButton_customer.clicked.connect(self.manager_check.update_customer)
        self.manager_check.pushButton_car.clicked.connect(self.manager_check.update_car)
        self.manager_check.pushButton_buy.clicked.connect(self.manager_check.update_buy)
        self.manager_check.pushButton_lease.clicked.connect(self.manager_check.update_lease)
        self.manager_check.pushButton.clicked.connect(self.manager_check2login)
        self.manager_check.pushButton_add.clicked.connect(self.manager_check2add_car)
        self.manager_check.pushButton_sub.clicked.connect(self.manager_check.remove_car)

    def add_car_bind(self):
        self.add_car.pushButton_back.clicked.connect(self.add_car2manager_check)
        self.add_car.pushButton_ack.clicked.connect(lambda: self.manager_check.insert_car(self.add_car.lineEdit_model.text()))
        self.add_car.pushButton_ack.clicked.connect(self.add_car2manager_check)

    def login_check(self):
        username = self.login.lineEdit_username.text()
        password = self.login.lineEdit_password.text()
        print('username:', username, 'password:', password)
        if username in users.keys():
            if password == users[username][0] and users[username][1] == 'cus':
                print('customer login')
                self.login.close()
                self.user_main.show()
            elif password == users[username][0] and users[username][1] == 'man':
                print('manager login')
                self.login.close()
                self.manager_check.show()
        self.login.lineEdit_username.clear()
        self.login.lineEdit_password.clear()

    def user_main2buy(self, i):
        print(self.user_main.show_index * 6 + i)
        if self.user_main.show_index * 6 + i >= len(self.user_main.car_list):
            print('无效车辆')
            return
        self.buy.update_info(self.user_main.show_index * 6 + i)
        self.buy.show()

    def user_main2lease(self, i):
        print(self.user_main.show_index * 6 + i)
        if self.user_main.show_index * 6 + i >= len(self.user_main.car_list):
            print('无效车辆')
            return
        self.lease.update_info(self.user_main.show_index * 6 + i)
        self.lease.show()

    def user_main_pre(self):
        print('user_main_pre')
        if self.user_main.show_index > 0:
            self.user_main.show_index -= 1
            print(self.user_main.show_index)
            self.user_main.update_page()


    def user_main_next(self):
        print('user_main_next')
        if self.user_main.show_index + 1 < math.ceil((len(self.user_main.car_list)-1) / 6):
            self.user_main.show_index += 1
            print(self.user_main.show_index)
            self.user_main.update_page()

    def user_main2person(self):
        self.user_main.close()
        self.user_person.show()

    def user_person2login(self):
        self.user_person.close()
        self.login.show()

    def user_person2main(self):
        self.user_person.close()
        self.user_main.show()

    def buy2user_main(self):
        self.buy.close()
        self.user_main.show()

    def customer_buy(self, i):
        print('buy car:', self.buy.i, 'employee:', self.buy.comboBox.currentText())
        self.user_main.operation(i, 'buy')
        self.buy.close()
        self.user_main.update_page()
        self.user_main.show()

    def lease2user_main(self):
        self.lease.close()
        self.user_main.show()

    def customer_lease(self, i):
        begin_date = self.lease.lineEdit_1.text()
        end_date = self.lease.lineEdit_2.text()
        if self.check_lease_date(begin_date, end_date):
            print('lease car:', self.lease.i, 'employee:', self.buy.comboBox.currentText())
            print('begin date:', begin_date, 'end date:', end_date)
            self.user_main.operation(i, 'lease')
            self.lease.close()
            self.user_main.update_page()
            self.user_main.show()
        else:
            print('无效日期')

    def check_lease_date(self, begin, end):
        return True

    def manager_check2login(self):
        self.manager_check.close()
        self.login.show()

    def manager_check2add_car(self):
        self.add_car.lineEdit_car_id.clear()
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





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    db = SYSU_database()

    db.run()

    sys.exit(app.exec_())













