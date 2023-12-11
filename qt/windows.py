from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem
import os
import pandas as pd
import numpy as np

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
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.car_list = self.get_car_list()
        self.state = self.get_state_list()
        self.show_index = 0
        self.label_page.setText('-第' + str(self.show_index+1) + '页-')

    def update_page(self):

        if self.show_index * 6 + 0 >= len(self.car_list):
            self.label_1.setText('car-')
            self.pushButton_buy1.setEnabled(False)
            self.pushButton_lease1.setEnabled(False)
        else:
            if self.state[self.show_index * 6 + 0] == 2:
                self.label_1.setText('car' + str(self.show_index * 6 + 1))
                self.pushButton_buy1.setEnabled(True)
                self.pushButton_lease1.setEnabled(True)
            elif self.state[self.show_index * 6 + 0] == 1:
                self.label_1.setText('car' + str(self.show_index * 6 + 1) + ' 已租出')
                self.pushButton_buy1.setEnabled(False)
                self.pushButton_lease1.setEnabled(False)
            elif self.state[self.show_index * 6 + 0] == 0:
                self.label_1.setText('car' + str(self.show_index * 6 + 1) + ' 已卖出')
                self.pushButton_buy1.setEnabled(False)
                self.pushButton_lease1.setEnabled(False)

        if self.show_index * 6 + 1 >= len(self.car_list):
            self.label_2.setText('car-')
            self.pushButton_buy2.setEnabled(False)
            self.pushButton_lease2.setEnabled(False)
        else:
            if self.state[self.show_index * 6 + 1] == 2:
                self.label_2.setText('car' + str(self.show_index * 6 + 2))
                self.pushButton_buy2.setEnabled(True)
                self.pushButton_lease2.setEnabled(True)
            elif self.state[self.show_index * 6 + 1] == 1:
                self.label_2.setText('car' + str(self.show_index * 6 + 2) + ' 已租出')
                self.pushButton_buy2.setEnabled(False)
                self.pushButton_lease2.setEnabled(False)
            elif self.state[self.show_index * 6 + 1] == 0:
                self.label_2.setText('car' + str(self.show_index * 6 + 2) + ' 已卖出')
                self.pushButton_buy2.setEnabled(False)
                self.pushButton_lease2.setEnabled(False)

        if self.show_index * 6 + 2 >= len(self.car_list):
            self.label_3.setText('car-')
            self.pushButton_buy3.setEnabled(False)
            self.pushButton_lease3.setEnabled(False)
        else:
            if self.state[self.show_index * 6 + 2] == 2:
                self.label_3.setText('car' + str(self.show_index * 6 + 3))
                self.pushButton_buy3.setEnabled(True)
                self.pushButton_lease3.setEnabled(True)
            elif self.state[self.show_index * 6 + 2] == 1:
                self.label_3.setText('car' + str(self.show_index * 6 + 3) + ' 已租出')
                self.pushButton_buy3.setEnabled(False)
                self.pushButton_lease3.setEnabled(False)
            elif self.state[self.show_index * 6 + 2] == 0:
                self.label_3.setText('car' + str(self.show_index * 6 + 3) + ' 已卖出')
                self.pushButton_buy3.setEnabled(False)
                self.pushButton_lease3.setEnabled(False)

        if self.show_index * 6 + 3 >= len(self.car_list):
            self.label_4.setText('car-')
            self.pushButton_buy4.setEnabled(False)
            self.pushButton_lease4.setEnabled(False)
        else:
            if self.state[self.show_index * 6 + 3] == 2:
                self.label_4.setText('car' + str(self.show_index * 6 + 4))
                self.pushButton_buy4.setEnabled(True)
                self.pushButton_lease4.setEnabled(True)
            elif self.state[self.show_index * 6 + 3] == 1:
                self.label_4.setText('car' + str(self.show_index * 6 + 4) + ' 已租出')
                self.pushButton_buy4.setEnabled(False)
                self.pushButton_lease4.setEnabled(False)
            elif self.state[self.show_index * 6 + 3] == 0:
                self.label_4.setText('car' + str(self.show_index * 6 + 4) + ' 已卖出')
                self.pushButton_buy4.setEnabled(False)
                self.pushButton_lease4.setEnabled(False)

        if self.show_index * 6 + 4 >= len(self.car_list):
            self.label_5.setText('car-')
            self.pushButton_buy5.setEnabled(False)
            self.pushButton_lease5.setEnabled(False)
        else:
            if self.state[self.show_index * 6 + 4] == 2:
                self.label_5.setText('car' + str(self.show_index * 6 + 5))
                self.pushButton_buy5.setEnabled(True)
                self.pushButton_lease5.setEnabled(True)
            elif self.state[self.show_index * 6 + 4] == 1:
                self.label_5.setText('car' + str(self.show_index * 6 + 5) + ' 已租出')
                self.pushButton_buy5.setEnabled(False)
                self.pushButton_lease5.setEnabled(False)
            elif self.state[self.show_index * 6 + 4] == 0:
                self.label_5.setText('car' + str(self.show_index * 6 + 5) + ' 已卖出')
                self.pushButton_buy5.setEnabled(False)
                self.pushButton_lease5.setEnabled(False)

        if self.show_index * 6 + 5 >= len(self.car_list):
            self.label_6.setText('car-')
            self.pushButton_buy6.setEnabled(False)
            self.pushButton_lease6.setEnabled(False)
        else:
            if self.state[self.show_index * 6 + 5] == 2:
                self.label_6.setText('car' + str(self.show_index * 6 + 6))
                self.pushButton_buy6.setEnabled(True)
                self.pushButton_lease6.setEnabled(True)
            elif self.state[self.show_index * 6 + 5] == 1:
                self.label_6.setText('car' + str(self.show_index * 6 + 6) + ' 已租出')
                self.pushButton_buy6.setEnabled(False)
                self.pushButton_lease6.setEnabled(False)
            elif self.state[self.show_index * 6 + 5] == 0:
                self.label_6.setText('car' + str(self.show_index * 6 + 6) + ' 已卖出')
                self.pushButton_buy6.setEnabled(False)
                self.pushButton_lease6.setEnabled(False)

        self.label_page.setText('-第' + str(self.show_index + 1) + '页-')
        print(self.pushButton_lease2.isEnabled())

    def operation(self, i, op):
        # index = self.show_index * 6 + i
        index = i
        # print('operation', index, op)
        if op == 'buy':
            self.state[index] = 0
            if i == 0:
                self.label_1.setText('car' + str(self.show_index * 6 + 1) + ' 已卖出')
                self.pushButton_buy1.setEnabled(False)
                self.pushButton_lease1.setEnabled(False)
            elif i == 1:
                self.label_2.setText('car' + str(self.show_index * 6 + 2) + ' 已卖出')
                self.pushButton_buy2.setEnabled(False)
                self.pushButton_lease2.setEnabled(False)
            elif i == 2:
                self.label_3.setText('car' + str(self.show_index * 6 + 3) + ' 已卖出')
                self.pushButton_buy3.setEnabled(False)
                self.pushButton_lease3.setEnabled(False)
            elif i == 3:
                self.label_4.setText('car' + str(self.show_index * 6 + 4) + ' 已卖出')
                self.pushButton_buy4.setEnabled(False)
                self.pushButton_lease4.setEnabled(False)
            elif i == 4:
                self.label_5.setText('car' + str(self.show_index * 6 + 5) + ' 已卖出')
                self.pushButton_buy5.setEnabled(False)
                self.pushButton_lease5.setEnabled(False)
            elif i == 5:
                self.label_6.setText('car' + str(self.show_index * 6 + 6) + ' 已卖出')
                self.pushButton_buy6.setEnabled(False)
                self.pushButton_lease6.setEnabled(False)
        elif op == 'lease':
            self.state[index] = 1
            if i == 0:
                self.label_1.setText('car' + str(self.show_index * 6 + 1) + ' 已租出')
                self.pushButton_buy1.setEnabled(False)
                self.pushButton_lease1.setEnabled(False)
            elif i == 1:
                self.label_2.setText('car' + str(self.show_index * 6 + 2) + ' 已租出')
                self.pushButton_buy2.setEnabled(False)
                self.pushButton_lease2.setEnabled(False)
            elif i == 2:
                self.label_3.setText('car' + str(self.show_index * 6 + 3) + ' 已租出')
                self.pushButton_buy3.setEnabled(False)
                self.pushButton_lease3.setEnabled(False)
            elif i == 3:
                self.label_4.setText('car' + str(self.show_index * 6 + 4) + ' 已租出')
                self.pushButton_buy4.setEnabled(False)
                self.pushButton_lease4.setEnabled(False)
            elif i == 4:
                self.label_5.setText('car' + str(self.show_index * 6 + 5) + ' 已租出')
                self.pushButton_buy5.setEnabled(False)
                self.pushButton_lease5.setEnabled(False)
            elif i == 5:
                self.label_6.setText('car' + str(self.show_index * 6 + 6) + ' 已租出')
                self.pushButton_buy6.setEnabled(False)
                self.pushButton_lease6.setEnabled(False)

    def get_car_list(self):
        return range(15)

    def get_state_list(self):
        return [2 for i in range(len(self.car_list))]



class User_person(QtWidgets.QWidget, Ui_User_person):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Buy(QtWidgets.QWidget, Ui_Buy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.addItems(['1', '2', '3'])
        self.comboBox.setCurrentIndex(0)
        self.i = 0

    def update_info(self, i):
        print(i, 'update')
        self.comboBox.setCurrentIndex(0)
        self.i = i      # 根据索引更新页面信息


class Lease(QtWidgets.QWidget, Ui_Lease):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.comboBox.addItems(['1', '2', '3'])
        self.comboBox.setCurrentIndex(0)
        self.i = 0

    def update_info(self, i):
        print(i, 'update')
        self.comboBox.setCurrentIndex(0)
        self.i = i


class Manager_check(QtWidgets.QWidget, Ui_Manager_check):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def update_customer(self):
        self.pushButton_add.setEnabled(False)
        self.pushButton_sub.setEnabled(False)
        cus_list = ['cus 1', 'cus 2', 'cus 3']
        self.listWidget.clear()
        for i in cus_list:
            self.listWidget.addItem(QListWidgetItem(i))

    def update_car(self):
        self.pushButton_add.setEnabled(True)
        self.pushButton_sub.setEnabled(True)
        car_list = ['car 1', 'car 2', 'car 3']
        self.listWidget.clear()
        for i in car_list:
            self.listWidget.addItem(QListWidgetItem(i))

    def update_buy(self):
        self.pushButton_add.setEnabled(False)
        self.pushButton_sub.setEnabled(False)
        buy_list = ['buy 1', 'buy 2', 'buy 3']
        self.listWidget.clear()
        for i in buy_list:
            self.listWidget.addItem(QListWidgetItem(i))

    def update_lease(self):
        self.pushButton_add.setEnabled(False)
        self.pushButton_sub.setEnabled(False)
        lease_list = ['lease 1', 'lease 2', 'lease 3']
        self.listWidget.clear()
        for i in lease_list:
            self.listWidget.addItem(QListWidgetItem(i))

    def insert_car(self, model):
        self.listWidget.addItem(QListWidgetItem(model))
        # db_insert()

    def remove_car(self):
        index = self.listWidget.currentRow()
        self.listWidget.takeItem(index)


class Add_car(QtWidgets.QWidget, Ui_Add_car):
    def __init__(self):
        super().__init__()
        self.setupUi(self)














