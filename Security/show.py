# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\EP\ELEE_2\UI\show.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShowWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 679)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(150, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 36pt \"MS Shell Dlg 2\";")
        self.title.setObjectName("title")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(180, 90, 221, 141))
        self.plainTextEdit.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(61, 250, 440, 368))
        self.widget.setObjectName("widget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.gridLayout_8.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 2, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name1 = QtWidgets.QLineEdit(self.widget)
        self.name1.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.name1.setText("")
        self.name1.setObjectName("name1")
        self.gridLayout.addWidget(self.name1, 0, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        self.time_1 = QtWidgets.QLineEdit(self.widget)
        self.time_1.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.time_1.setText("")
        self.time_1.setObjectName("time_1")
        self.gridLayout.addWidget(self.time_1, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 4)
        self.gridLayout_8.addLayout(self.gridLayout, 1, 0, 1, 3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.name2 = QtWidgets.QLineEdit(self.widget)
        self.name2.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.name2.setText("")
        self.name2.setObjectName("name2")
        self.gridLayout_2.addWidget(self.name2, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.time2 = QtWidgets.QLineEdit(self.widget)
        self.time2.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.time2.setText("")
        self.time2.setObjectName("time2")
        self.gridLayout_2.addWidget(self.time2, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 4)
        self.gridLayout_8.addLayout(self.gridLayout_2, 2, 0, 1, 3)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.name3 = QtWidgets.QLineEdit(self.widget)
        self.name3.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.name3.setText("")
        self.name3.setObjectName("name3")
        self.gridLayout_3.addWidget(self.name3, 0, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 2, 1, 1)
        self.time3 = QtWidgets.QLineEdit(self.widget)
        self.time3.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.time3.setText("")
        self.time3.setObjectName("time3")
        self.gridLayout_3.addWidget(self.time3, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 4)
        self.gridLayout_8.addLayout(self.gridLayout_3, 3, 0, 1, 3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.name4 = QtWidgets.QLineEdit(self.widget)
        self.name4.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.name4.setText("")
        self.name4.setObjectName("name4")
        self.gridLayout_4.addWidget(self.name4, 0, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_4.addWidget(self.lineEdit_4, 0, 2, 1, 1)
        self.time4 = QtWidgets.QLineEdit(self.widget)
        self.time4.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.time4.setText("")
        self.time4.setObjectName("time4")
        self.gridLayout_4.addWidget(self.time4, 0, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 0, 1, 4)
        self.gridLayout_8.addLayout(self.gridLayout_4, 4, 0, 1, 3)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)
        self.name5 = QtWidgets.QLineEdit(self.widget)
        self.name5.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.name5.setText("")
        self.name5.setObjectName("name5")
        self.gridLayout_5.addWidget(self.name5, 0, 1, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_5.addWidget(self.lineEdit_5, 0, 2, 1, 1)
        self.time5 = QtWidgets.QLineEdit(self.widget)
        self.time5.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.time5.setText("")
        self.time5.setObjectName("time5")
        self.gridLayout_5.addWidget(self.time5, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 1, 0, 1, 4)
        self.gridLayout_8.addLayout(self.gridLayout_5, 5, 0, 1, 3)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)
        self.name6 = QtWidgets.QLineEdit(self.widget)
        self.name6.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.name6.setText("")
        self.name6.setObjectName("name6")
        self.gridLayout_6.addWidget(self.name6, 0, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_6.addWidget(self.lineEdit_6, 0, 2, 1, 1)
        self.time6 = QtWidgets.QLineEdit(self.widget)
        self.time6.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.time6.setText("")
        self.time6.setObjectName("time6")
        self.gridLayout_6.addWidget(self.time6, 0, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem5, 1, 0, 1, 4)
        self.gridLayout_8.addLayout(self.gridLayout_6, 6, 0, 1, 3)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 0, 0, 1, 1)
        self.name7 = QtWidgets.QLineEdit(self.widget)
        self.name7.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.name7.setText("")
        self.name7.setObjectName("name7")
        self.gridLayout_7.addWidget(self.name7, 0, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_7.addWidget(self.lineEdit_7, 0, 2, 1, 1)
        self.time7 = QtWidgets.QLineEdit(self.widget)
        self.time7.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.time7.setText("")
        self.time7.setObjectName("time7")
        self.gridLayout_7.addWidget(self.time7, 0, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 7, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Security Duty"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "\n"
"1                    เวร บก.พัน\n"
"2                    เวร คลังอาวุธ\n"
"3                    เวร ร้อย. 1\n"
"4                    เวร ร้อย. 2\n"
"5                    เวร ร้อย. 3\n"
"6                    เวร สายตรวจ 1\n"
"7                    เวร สายตรวจ 2\n"
""))
        self.label_8.setText(_translate("MainWindow", "                          ชื่อ"))
        self.label_9.setText(_translate("MainWindow", "                 นามสกุล"))
        self.label_10.setText(_translate("MainWindow", "          เวลา"))
        self.label.setText(_translate("MainWindow", "เวร บก.พัน      "))
        self.label_2.setText(_translate("MainWindow", "เวร คลังอาวุธ   "))
        self.label_3.setText(_translate("MainWindow", "เวร ร้อย. 1      "))
        self.label_4.setText(_translate("MainWindow", "เวร ร้อย. 2      "))
        self.label_5.setText(_translate("MainWindow", "เวร ร้อย. 3      "))
        self.label_6.setText(_translate("MainWindow", "เวร สายตรวจ 1"))
        self.label_7.setText(_translate("MainWindow", "เวร สายตรวจ 2"))

        self.name1.setPlaceholderText(name1())
        self.lineEdit.setPlaceholderText(lname1())
        self.time_1.setPlaceholderText(time1())
        
        self.name2.setPlaceholderText(name2())
        self.lineEdit_2.setPlaceholderText(lname2())
        self.time2.setPlaceholderText(time2())
        
        self.name3.setPlaceholderText(name3())
        self.lineEdit_3.setPlaceholderText(lname3())
        self.time3.setPlaceholderText(time3())
        
        self.name4.setPlaceholderText(name4())
        self.lineEdit_4.setPlaceholderText(lname4())
        self.time4.setPlaceholderText(time4())
        
        self.name5.setPlaceholderText(name5())
        self.lineEdit_5.setPlaceholderText(lname5())
        self.time5.setPlaceholderText(time5())
        
        self.name6.setPlaceholderText(name6())
        self.lineEdit_6.setPlaceholderText(lname6())
        self.time6.setPlaceholderText(time6())
        
        self.name7.setPlaceholderText(name7()) 
        self.lineEdit_7.setPlaceholderText(lname7())  
        self.time7.setPlaceholderText(time7())
             
import mysql.connector


def ConnectorMysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12341234",
        database="security",
        # auth_plugin='mysql_native_password'
    )
    # print("db run")
    return mydb

# NAME
def name1():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT fname FROM `securestatus` WHERE position=1'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def name2():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT fname FROM `securestatus` WHERE position=2'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def name3():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT fname FROM `securestatus` WHERE position=3'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def name4():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT fname FROM `securestatus` WHERE position=4'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def name5():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT fname FROM `securestatus` WHERE position=5'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def name6():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT fname FROM `securestatus` WHERE position=6'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def name7():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT fname FROM `securestatus` WHERE position=7'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def lname1():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT sname FROM `securestatus` WHERE position=1'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def lname2():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT sname FROM `securestatus` WHERE position=2'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def lname3():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT sname FROM `securestatus` WHERE position=3'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def lname4():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT sname FROM `securestatus` WHERE position=4'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def lname5():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT sname FROM `securestatus` WHERE position=5'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def lname6():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT sname FROM `securestatus` WHERE position=6'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def lname7():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT sname FROM `securestatus` WHERE position=7'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def time1():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT quater FROM `securestatus` WHERE position=1'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    part_time = {
        "1": "2130-2330",
        "2": "2330-0130",
        "3": "0130-0330",
        "4": "0330-0500"
    }
    time = part_time[x]
    return time

def time2():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT quater FROM `securestatus` WHERE position=2'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    part_time = {
        "1": "2130-2330",
        "2": "2330-0130",
        "3": "0130-0330",
        "4": "0330-0500"
    }
    time = part_time[x]
    return time

def time3():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT quater FROM `securestatus` WHERE position=3'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    part_time = {
        "1": "2130-2330",
        "2": "2330-0130",
        "3": "0130-0330",
        "4": "0330-0500"
    }
    time = part_time[x]
    return time

def time4():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT quater FROM `securestatus` WHERE position=4'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    part_time = {
        "1": "2130-2330",
        "2": "2330-0130",
        "3": "0130-0330",
        "4": "0330-0500"
    }
    time = part_time[x]
    return time

def time5():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT quater FROM `securestatus` WHERE position=5'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    part_time = {
        "1": "2130-2330",
        "2": "2330-0130",
        "3": "0130-0330",
        "4": "0330-0500"
    }
    time = part_time[x]
    return time

def time6():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT quater FROM `securestatus` WHERE position=6'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    part_time = {
        "1": "2130-2330",
        "2": "2330-0130",
        "3": "0130-0330",
        "4": "0330-0500"
    }
    time = part_time[x]
    return time

def time7():
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT quater FROM `securestatus` WHERE position=7'
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    part_time = {
        "1": "2130-2330",
        "2": "2330-0130",
        "3": "0130-0330",
        "4": "0330-0500"
    }
    time = part_time[x]
    return time

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ShowWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
