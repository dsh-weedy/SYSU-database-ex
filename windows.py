from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
import pandas as pd
import numpy as np

import edit
import func
import inquire
import my_func
from ui.login import Ui_Login
from ui.user_main import Ui_User_main
from ui.user_person import Ui_User_person
from ui.buy import Ui_Buy
from ui.lease import Ui_Lease
from ui.manager_check import Ui_Manager_check
from ui.add_car import Ui_Add_car


class Login(QtWidgets.QWidget, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class User_main(QtWidgets.QWidget, Ui_User_main):
    def __init__(self, conn):
        super().__init__()
        self.setupUi(self)

        self.car_list = inquire.inquire_all(conn, 'car')
        self.show_index = 0
        self.label_page.setText('-第' + str(self.show_index+1) + '页-')
        self.buy_button = [
            self.pushButton_buy1,
            self.pushButton_buy2,
            self.pushButton_buy3,
            self.pushButton_buy4,
            self.pushButton_buy5,
            self.pushButton_buy6,
        ]
        self.lease_button = [
            self.pushButton_lease1,
            self.pushButton_lease2,
            self.pushButton_lease3,
            self.pushButton_lease4,
            self.pushButton_lease5,
            self.pushButton_lease6,
        ]
        self.car_label = [
            self.label_1,
            self.label_2,
            self.label_3,
            self.label_4,
            self.label_5,
            self.label_6,
        ]
        self.graphics = [
            self.graphicsView_1,
            self.graphicsView_2,
            self.graphicsView_3,
            self.graphicsView_4,
            self.graphicsView_5,
            self.graphicsView_6,
        ]

    def update_page(self, conn, user_id):
        print('update_page')

        date = my_func.get_time(conn)
        self.label_time.setText(date[:4] + '/' + date[4:6] + '/' + date[6:])

        available = self.check_available(conn, user_id)     # 看看是不是老赖

        self.car_list = inquire.inquire_all(conn, 'car')
        for i in range(6):
            if self.show_index * 6 + i >= len(self.car_list):
                scene = QtWidgets.QGraphicsScene()
                self.graphics[i].setScene(scene)
                self.car_label[i].setText('car-')
                self.buy_button[i].setEnabled(False)
                self.lease_button[i].setEnabled(False)
            else:
                frame = QtGui.QImage('./img/car_default.jpg')
                pix = QtGui.QPixmap.fromImage(frame).scaled(self.graphics[i].width() - 2,
                                                            self.graphics[i].height() - 2)
                item = QtWidgets.QGraphicsPixmapItem(pix)
                scene = QtWidgets.QGraphicsScene()
                scene.addItem(item)
                self.graphics[i].setScene(scene)
                if self.car_list[self.show_index * 6 + i][5] == 2:
                    self.car_label[i].setText(
                        'car' + str(self.car_list[self.show_index * 6 + i][1]) + self.car_list[self.show_index * 6 + i][4])
                    if available:
                        self.buy_button[i].setEnabled(True)
                        self.lease_button[i].setEnabled(True)
                    else:
                        self.buy_button[i].setEnabled(False)
                        self.lease_button[i].setEnabled(False)
                elif self.car_list[self.show_index * 6 + i][5] == 1:
                    self.car_label[i].setText(
                        'car' + str(self.car_list[self.show_index * 6 + i][1]) + self.car_list[self.show_index * 6 + i][4] + ' 已租出')
                    self.buy_button[i].setEnabled(False)
                    self.lease_button[i].setEnabled(False)
                elif self.car_list[self.show_index * 6 + i][5] == 0:
                    self.car_label[i].setText(
                        'car' + str(self.car_list[self.show_index * 6 + i][1]) + self.car_list[self.show_index * 6 + i][4] + ' 已卖出')
                    self.buy_button[i].setEnabled(False)
                    self.lease_button[i].setEnabled(False)

        self.label_page.setText('-第' + str(self.show_index + 1) + '页-')
        # print(self.pushButton_lease2.isEnabled())

    def operation(self, conn, i, op, user_id, emp_id, begin_date='', end_date=''):
        car_list = inquire.inquire_all(conn, 'car')
        car_id = int(car_list[i][1])
        print('operation', i, op, car_id, emp_id)
        if op == 'buy':
            func.purchase_car(user_id, emp_id, car_id, conn)
            self.buy_button[i % 6].setEnabled(False)
            self.lease_button[i % 6].setEnabled(False)
        elif op == 'lease':
            print('begin_date:', begin_date, 'end_date:', end_date)
            if begin_date == '' or end_date == '': return
            func.rent_car(user_id, emp_id, car_id, begin_date, end_date, conn)
            self.buy_button[i % 6].setEnabled(False)
            self.lease_button[i % 6].setEnabled(False)

    def check_available(self, conn, user_id):
        lease_list = my_func.get_user_leaselist(conn, user_id)
        for i in lease_list:
            if i[8] == 3:
                return False
        return True


class User_person(QtWidgets.QWidget, Ui_User_person):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_userid(self, user_id, conn):
        date = my_func.get_time(conn)
        self.label_time.setText(date[:4] + '/' + date[4:6] + '/' + date[6:])

        info = func.check_cus_detail(user_id, conn)
        self.user_info = '姓名：' + info[0] + '\n邮箱：' + info[1]
        self.label_info.setText(self.user_info)

        frame = QtGui.QImage('./img/default.jpg')
        pix = QtGui.QPixmap.fromImage(frame).scaled(self.graphicsView.width()-2, self.graphicsView.height()-2)
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.graphicsView.setScene(scene)

        buy_list = my_func.get_user_buylist(conn, user_id)
        self.listWidget_1.clear()
        for i in buy_list:
            tmp = 'id:' + str(i[0]) + '\tcar_id:' + str(i[2]) + '\temp_id:' + str(i[3]) \
                  + '\tpirce:' + str(i[4]) + '\tdate:' + str(i[5])
            self.listWidget_1.addItem(tmp)

        lease_list = my_func.get_user_leaselist(conn, user_id)
        self.listWidget_2.clear()
        for i in lease_list:
            tmp = 'id:' + str(i[0]) + '  car_id:' + str(i[2]) + '  emp_id:' + str(i[3]) \
                   + '  rent:' + str(i[4]) + '  ' + str(i[5]) + '-' + str(i[6]) \
                  + '  return_date:' + str(i[7]) + '  state:' + str(i[8])
            self.listWidget_2.addItem(tmp)

        fine_list = my_func.get_user_finelist(conn, user_id)
        self.listWidget_fine.clear()
        for i in fine_list:
            tmp = 'lease:' + str(i[0]) + '  car:' + str(i[2]) + '  fine:' + str(i[1])
            self.listWidget_fine.addItem(QListWidgetItem(tmp))

    def return_car(self, conn, user_id):
        date = int(my_func.get_time(conn))
        if self.listWidget_2.currentRow() == -1: return
        line_list = self.listWidget_2.currentItem().text().split()
        state = int(line_list[-1].split(':')[1])
        if state == 2: return
        lease_id = int(line_list[0].split(':')[1])
        car_id = int(line_list[1].split(':')[1])
        # print(car_id, lease_id, date)

        func.return_car(conn, car_id, lease_id, date)

        lease_list = my_func.get_user_leaselist(conn, user_id)
        self.listWidget_2.clear()
        for i in lease_list:
            tmp = 'id:' + str(i[0]) + '  car_id:' + str(i[2]) + '  emp_id:' + str(i[3]) \
                  + '  rent:' + str(i[4]) + '  ' + str(i[5]) + '-' + str(i[6]) \
                  + '  return_date:' + str(i[7]) + '  state:' + str(i[8])
            self.listWidget_2.addItem(tmp)
            
        fine_list = my_func.get_user_finelist(conn, user_id)
        self.listWidget_fine.clear()
        for i in fine_list:
            tmp = 'lease:' + str(i[0]) + '  car:' + str(i[2]) + '  fine:' + str(i[1])
            self.listWidget_fine.addItem(QListWidgetItem(tmp))


class Buy(QtWidgets.QWidget, Ui_Buy):
    def __init__(self, conn):
        super().__init__()
        self.setupUi(self)

        emp_list = inquire.inquire_all(conn, 'employees')
        self.comboBox.addItems([str(emp[0]) + ' ' + emp[1] for emp in emp_list])
        self.comboBox.setCurrentIndex(0)
        self.i = 0

    def update_info(self, i, car_info, conn):
        print(i, 'update')
        date = my_func.get_time(conn)
        self.label_time.setText(date[:4] + '/' + date[4:6] + '/' + date[6:])

        self.comboBox.clear()
        emp_list = inquire.inquire_all(conn, 'employees')
        self.comboBox.addItems([str(emp[0]) + ' ' + emp[1] for emp in emp_list])
        self.comboBox.setCurrentIndex(0)
        self.i = i      # 根据索引更新页面信息
        write = 'image:' + str(car_info[0]) + '\ncar_idL' + str(car_info[1]) + '\nprice:' + str(car_info[2]) \
              + '\nmodel:' + str(car_info[4]) + '\ndescription:' + str(car_info[6])
        print(write)
        self.label_info.setText(write)

class Lease(QtWidgets.QWidget, Ui_Lease):
    def __init__(self, conn):
        super().__init__()
        self.setupUi(self)

        emp_list = inquire.inquire_all(conn, 'employees')
        self.comboBox.addItems([str(emp[0]) + ' ' + emp[1] for emp in emp_list])
        self.comboBox.setCurrentIndex(0)
        self.i = 0

    def update_info(self, i, car_info, conn):
        print(i, 'update')
        date = my_func.get_time(conn)
        self.label_time.setText(date[:4] + '/' + date[4:6] + '/' + date[6:])

        self.comboBox.clear()
        emp_list = inquire.inquire_all(conn, 'employees')
        self.comboBox.addItems([str(emp[0]) + ' ' + emp[1] for emp in emp_list])
        self.comboBox.setCurrentIndex(0)
        self.i = i
        write = 'image:' + str(car_info[0]) + '\ncar_idL' + str(car_info[1]) + '\nrent:' + str(car_info[3]) \
              + '\nmodel:' + str(car_info[4]) + '\ndescription:' + str(car_info[6])
        print(write)
        self.label_info.setText(write)


class Manager_check(QtWidgets.QWidget, Ui_Manager_check):
    def __init__(self, conn):
        super().__init__()
        self.setupUi(self)
        frame = QtGui.QImage('./img/user_default.jpg')
        pix = QtGui.QPixmap.fromImage(frame).scaled(self.graphicsView.width() - 2, self.graphicsView.height() - 2)
        item = QtWidgets.QGraphicsPixmapItem(pix)
        scene = QtWidgets.QGraphicsScene()
        scene.addItem(item)
        self.graphicsView.setScene(scene)

        date = my_func.get_time(conn)
        self.label_time.setText(date[:4] + '/' + date[4:6] + '/' + date[6:])

    def update_customer(self, conn):
        self.pushButton_add.setEnabled(False)
        self.pushButton_sub.setEnabled(False)
        self.listWidget.clear()

        cus_list = inquire.inquire_all(conn, 'user')
        for i in cus_list:
            tmp = 'user_id:' + str(i[0]) + ' ' + i[1] + '\tage:' + str(i[2]) + '\temail:' + \
                  i[3] + '\tpassword:' + i[4]
            self.listWidget.addItem(QListWidgetItem(tmp))

    def update_car(self, conn):
        self.pushButton_add.setEnabled(True)
        self.pushButton_sub.setEnabled(True)
        self.listWidget.clear()

        car_list = inquire.inquire_all(conn, 'car')
        for i in car_list:
            tmp = 'car_id:' + str(i[1]) + '\tstate:' + str(i[5]) + '\tprice:' + str(i[2]) + \
                  '\trent:' + str(i[3]) + '\tmodel:' + i[4]
            self.listWidget.addItem(QListWidgetItem(tmp))

    def update_buy(self, conn):
        self.pushButton_add.setEnabled(False)
        self.pushButton_sub.setEnabled(False)
        self.listWidget.clear()

        buy_list = inquire.inquire_all(conn, 'purchase')
        for i in buy_list:
            tmp = 'id:' + str(i[0]) + '  user_id:' + str(i[1]) + '  car_id:' + str(i[2]) + '  emp_id:' + str(i[3]) + \
                  '  price:' + str(i[4]) + '  date:' + str(i[5])
            self.listWidget.addItem(QListWidgetItem(tmp))

    def update_lease(self, conn):
        self.pushButton_add.setEnabled(False)
        self.pushButton_sub.setEnabled(False)
        self.listWidget.clear()

        lease_list = inquire.inquire_all(conn, 'lease')
        for i in lease_list:
            tmp = 'id:' + str(i[0]) + '  user_id:' + str(i[1]) + '  car_id:' + str(i[2]) + '  emp_id:' + str(i[3]) + \
                  '  rent:' + str(i[4]) + '  begin_date:' + str(i[5]) + '  end_date:' + str(i[6]) + \
                  '  return_date:' + str(i[7]) + '  state:' + str(i[8])
            self.listWidget.addItem(QListWidgetItem(tmp))

    def update_fine(self, conn):
        self.pushButton_add.setEnabled(False)
        self.pushButton_sub.setEnabled(False)
        self.listWidget.clear()

        fine_list = inquire.inquire_all(conn, 'fine')
        for i in fine_list:
            tmp = 'id:' + str(i[0]) + '  fine:' + str(i[1])
            self.listWidget.addItem(QListWidgetItem(tmp))

    def update_emp(self, conn):
        self.pushButton_add.setEnabled(False)
        self.pushButton_sub.setEnabled(False)
        self.listWidget.clear()

        emp_list = inquire.inquire_all(conn, 'employees')
        for i in emp_list:
            tmp = 'emp:' + str(i[0]) + ' ' + i[1] + '\tage:' + str(i[2]) + '\temail:' + i[3]
            self.listWidget.addItem(QListWidgetItem(tmp))

    def insert_car(self, add_car, conn):
        add_car.next_car_id = inquire.inquire_all(conn, 'car')[-1][1] + 1
        print(add_car.next_car_id)
        tmp = 'car_id:' + add_car.lineEdit_car_id.text() + '\tstate:2' + '\tprice:' + \
              add_car.lineEdit_price.text() + '\trent:' + add_car.lineEdit_rent.text() + \
              '\tmodel:' + add_car.lineEdit_model.text()
        print(tmp)
        self.listWidget.addItem(QListWidgetItem(tmp))
        edit.add_car(conn, add_car.lineEdit_img.text(), int(add_car.lineEdit_car_id.text()),
                     int(add_car.lineEdit_price.text()), int(add_car.lineEdit_rent.text()),
                     add_car.lineEdit_model.text(), 2, add_car.lineEdit_description.text(),
                     int(add_car.lineEdit_deposit.text()))

    def remove_car(self, conn):
        index = self.listWidget.currentRow()
        car_id = int(self.listWidget.currentItem().text().split()[0].split(':')[1])
        self.listWidget.takeItem(index)
        edit.delete_car(conn, car_id)

    def set_time(self, conn, calender):
        year, month, day = self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text()
        y, m, d = int(year), int(month), int(day)
        if year == '' or month == '' or day == '' or y <= 0 or m <= 0 or d <= 0 or m > 12 or d > calender[m]:
            return False

        if len(year) < 4:
            for i in range(4-len(year)):
                year = '0' + year
        month = '0' + month if len(month) == 1 else month
        day = '0' + day if len(day) == 1 else day
        print('time_set:', year, month, day)

        date = int(year + month + day)
        func.setTime(conn, date)

        date = my_func.get_time(conn)
        self.label_time.setText(date[:4] + '/' + date[4:6] + '/' + date[6:])
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()


class Add_car(QtWidgets.QWidget, Ui_Add_car):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.next_car_id = 0














