# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_User_main(object):
    def setupUi(self, User_main):
        User_main.setObjectName("User_main")
        User_main.resize(1300, 840)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(User_main)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtWidgets.QLabel(User_main)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.label_time = QtWidgets.QLabel(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_time.setFont(font)
        self.label_time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_time.setObjectName("label_time")
        self.horizontalLayout_10.addWidget(self.label_time)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.pushButton_person = QtWidgets.QPushButton(User_main)
        self.pushButton_person.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_person.setFont(font)
        self.pushButton_person.setObjectName("pushButton_person")
        self.horizontalLayout_10.addWidget(self.pushButton_person)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        spacerItem3 = QtWidgets.QSpacerItem(17, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView_1 = QtWidgets.QGraphicsView(User_main)
        self.graphicsView_1.setObjectName("graphicsView_1")
        self.verticalLayout.addWidget(self.graphicsView_1)
        self.label_1 = QtWidgets.QLabel(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.verticalLayout.addWidget(self.label_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButton_buy1 = QtWidgets.QPushButton(User_main)
        self.pushButton_buy1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_buy1.setFont(font)
        self.pushButton_buy1.setObjectName("pushButton_buy1")
        self.horizontalLayout.addWidget(self.pushButton_buy1)
        self.pushButton_lease1 = QtWidgets.QPushButton(User_main)
        self.pushButton_lease1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_lease1.setFont(font)
        self.pushButton_lease1.setObjectName("pushButton_lease1")
        self.horizontalLayout.addWidget(self.pushButton_lease1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView_2 = QtWidgets.QGraphicsView(User_main)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_2.addWidget(self.graphicsView_2)
        self.label_2 = QtWidgets.QLabel(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.pushButton_buy2 = QtWidgets.QPushButton(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_buy2.setFont(font)
        self.pushButton_buy2.setObjectName("pushButton_buy2")
        self.horizontalLayout_2.addWidget(self.pushButton_buy2)
        self.pushButton_lease2 = QtWidgets.QPushButton(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_lease2.setFont(font)
        self.pushButton_lease2.setObjectName("pushButton_lease2")
        self.horizontalLayout_2.addWidget(self.pushButton_lease2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView_3 = QtWidgets.QGraphicsView(User_main)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_3.addWidget(self.graphicsView_3)
        self.label_3 = QtWidgets.QLabel(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.pushButton_buy3 = QtWidgets.QPushButton(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_buy3.setFont(font)
        self.pushButton_buy3.setObjectName("pushButton_buy3")
        self.horizontalLayout_3.addWidget(self.pushButton_buy3)
        self.pushButton_lease3 = QtWidgets.QPushButton(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_lease3.setFont(font)
        self.pushButton_lease3.setObjectName("pushButton_lease3")
        self.horizontalLayout_3.addWidget(self.pushButton_lease3)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacerItem12)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.graphicsView_4 = QtWidgets.QGraphicsView(User_main)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalLayout_4.addWidget(self.graphicsView_4)
        self.label_4 = QtWidgets.QLabel(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.pushButton_buy4 = QtWidgets.QPushButton(User_main)
        self.pushButton_buy4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_buy4.setFont(font)
        self.pushButton_buy4.setObjectName("pushButton_buy4")
        self.horizontalLayout_7.addWidget(self.pushButton_buy4)
        self.pushButton_lease4 = QtWidgets.QPushButton(User_main)
        self.pushButton_lease4.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_lease4.setFont(font)
        self.pushButton_lease4.setObjectName("pushButton_lease4")
        self.horizontalLayout_7.addWidget(self.pushButton_lease4)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.graphicsView_5 = QtWidgets.QGraphicsView(User_main)
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.verticalLayout_5.addWidget(self.graphicsView_5)
        self.label_5 = QtWidgets.QLabel(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.pushButton_buy5 = QtWidgets.QPushButton(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_buy5.setFont(font)
        self.pushButton_buy5.setObjectName("pushButton_buy5")
        self.horizontalLayout_8.addWidget(self.pushButton_buy5)
        self.pushButton_lease5 = QtWidgets.QPushButton(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_lease5.setFont(font)
        self.pushButton_lease5.setObjectName("pushButton_lease5")
        self.horizontalLayout_8.addWidget(self.pushButton_lease5)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem17)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.graphicsView_6 = QtWidgets.QGraphicsView(User_main)
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.verticalLayout_6.addWidget(self.graphicsView_6)
        self.label_6 = QtWidgets.QLabel(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.pushButton_buy6 = QtWidgets.QPushButton(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_buy6.setFont(font)
        self.pushButton_buy6.setObjectName("pushButton_buy6")
        self.horizontalLayout_9.addWidget(self.pushButton_buy6)
        self.pushButton_lease6 = QtWidgets.QPushButton(User_main)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_lease6.setFont(font)
        self.pushButton_lease6.setObjectName("pushButton_lease6")
        self.horizontalLayout_9.addWidget(self.pushButton_lease6)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem20)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_6.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        spacerItem21 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem21)
        self.label_page = QtWidgets.QLabel(User_main)
        self.label_page.setAlignment(QtCore.Qt.AlignCenter)
        self.label_page.setObjectName("label_page")
        self.verticalLayout_8.addWidget(self.label_page)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem22)
        self.pushButton_pre = QtWidgets.QPushButton(User_main)
        self.pushButton_pre.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_pre.setFont(font)
        self.pushButton_pre.setObjectName("pushButton_pre")
        self.horizontalLayout_5.addWidget(self.pushButton_pre)
        spacerItem23 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem23)
        self.pushButton_next = QtWidgets.QPushButton(User_main)
        self.pushButton_next.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_next.setFont(font)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_5.addWidget(self.pushButton_next)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem24)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        spacerItem25 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem25)
        self.horizontalLayout_11.addLayout(self.verticalLayout_8)
        spacerItem26 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem26)

        self.retranslateUi(User_main)
        QtCore.QMetaObject.connectSlotsByName(User_main)

    def retranslateUi(self, User_main):
        _translate = QtCore.QCoreApplication.translate
        User_main.setWindowTitle(_translate("User_main", "Form"))
        self.label.setText(_translate("User_main", "SYSU_Database"))
        self.label_time.setText(_translate("User_main", "time"))
        self.pushButton_person.setText(_translate("User_main", "个人中心"))
        self.label_1.setText(_translate("User_main", "car1"))
        self.pushButton_buy1.setText(_translate("User_main", "购买"))
        self.pushButton_lease1.setText(_translate("User_main", "租借"))
        self.label_2.setText(_translate("User_main", "car2"))
        self.pushButton_buy2.setText(_translate("User_main", "购买"))
        self.pushButton_lease2.setText(_translate("User_main", "租借"))
        self.label_3.setText(_translate("User_main", "car3"))
        self.pushButton_buy3.setText(_translate("User_main", "购买"))
        self.pushButton_lease3.setText(_translate("User_main", "租借"))
        self.label_4.setText(_translate("User_main", "car4"))
        self.pushButton_buy4.setText(_translate("User_main", "购买"))
        self.pushButton_lease4.setText(_translate("User_main", "租借"))
        self.label_5.setText(_translate("User_main", "car5"))
        self.pushButton_buy5.setText(_translate("User_main", "购买"))
        self.pushButton_lease5.setText(_translate("User_main", "租借"))
        self.label_6.setText(_translate("User_main", "car6"))
        self.pushButton_buy6.setText(_translate("User_main", "购买"))
        self.pushButton_lease6.setText(_translate("User_main", "租借"))
        self.label_page.setText(_translate("User_main", "-第i页-"))
        self.pushButton_pre.setText(_translate("User_main", "上一页"))
        self.pushButton_next.setText(_translate("User_main", "下一页"))
