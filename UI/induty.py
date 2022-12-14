# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\EP\ELEE_2\UI\induty.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_IndutyWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 654)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(90, 30, 291, 51))
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
        self.plainTextEdit.setGeometry(QtCore.QRect(120, 90, 221, 141))
        self.plainTextEdit.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(90, 110, 281, 311))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.in_fname = QtWidgets.QLineEdit(self.widget)
        self.in_fname.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.in_fname.setObjectName("in_fname")
        self.gridLayout.addWidget(self.in_fname, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.in_sname = QtWidgets.QLineEdit(self.widget)
        self.in_sname.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.in_sname.setObjectName("in_sname")
        self.gridLayout.addWidget(self.in_sname, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.in_com = QtWidgets.QLineEdit(self.widget)
        self.in_com.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.in_com.setObjectName("in_com")
        self.gridLayout.addWidget(self.in_com, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.in_platoon = QtWidgets.QLineEdit(self.widget)
        self.in_platoon.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.in_platoon.setObjectName("in_platoon")
        self.gridLayout.addWidget(self.in_platoon, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.in_quater = QtWidgets.QLineEdit(self.widget)
        self.in_quater.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.in_quater.setObjectName("in_quater")
        self.gridLayout.addWidget(self.in_quater, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.in_position = QtWidgets.QLineEdit(self.widget)
        self.in_position.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.in_position.setObjectName("in_position")
        self.gridLayout.addWidget(self.in_position, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 2)
        self.in_send = QtWidgets.QPushButton(self.widget)
        self.in_send.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.in_send.setObjectName("in_send")
        self.gridLayout.addWidget(self.in_send, 7, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 2)
        self.in_show = QtWidgets.QLineEdit(self.widget)
        self.in_show.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.in_show.setObjectName("in_show")
        self.gridLayout.addWidget(self.in_show, 9, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 22))
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
"1    ????????? ??????.?????????\n"
"2    ????????? ???????????????????????????\n"
"3    ????????? ????????????. 1\n"
"4    ????????? ????????????. 2\n"
"5    ????????? ????????????. 3\n"
"6    ????????? ????????????????????? 1\n"
"7    ????????? ????????????????????? 2\n"
""))
        self.label_2.setText(_translate("MainWindow", "Firstname"))
        self.label_3.setText(_translate("MainWindow", "Surname"))
        self.label_7.setText(_translate("MainWindow", "Company"))
        self.label_8.setText(_translate("MainWindow", "Platoon"))
        self.label_4.setText(_translate("MainWindow", "quater"))
        self.label_5.setText(_translate("MainWindow", "Position"))
        self.in_send.setText(_translate("MainWindow", "Check In"))

        self.in_send.clicked.connect(self.checkin)
        
    def checkin(self):
        quater = self.in_quater.text()
        fname = self.in_fname.text()
        sname = self.in_sname.text()
        com = self.in_com.text()
        platoon = self.in_platoon.text()
        position = self.in_position.text()
        onduty = 1
        outduty = 0
        uplogin(quater, position, fname, sname, onduty, outduty)
        checkdata(quater, fname, sname, com, platoon, position)
        self.in_show.setPlaceholderText("complete")

def ConnectorMysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12341234",
        database="testdb",
        # auth_plugin='mysql_native_password'
    )
    print("db run")
    return mydb

def checkdata(quater, fname, sname, com, platoon, position):

    print(quater, fname, sname, com, platoon, position)
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT * FROM securestatus WHERE position="{position}"'
    print("dump databasesuccess!!")
    print(sql)
    cur.execute(sql)
    myresult = cur.fetchall()

    print(myresult)
    if len(myresult) != 0 :
        print("send to update fn")
        upstatus(quater, fname, sname, com, platoon, position)
    else:
        print("send to insert fn")
        insertstatus(quater, fname, sname, com, platoon, position)
        
def upstatus(quater, fname, sname, com, platoon, position):
    print(quater, fname, sname, com, platoon, position)
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = (
        "UPDATE securestatus SET quater = %s ,fname = %s ,sname = %s ,company = %s ,platoon = %s WHERE position = %s")
    print(sql)
    val = (quater, fname, sname, com, platoon, position)
    mycursor.execute(sql, val)
    print('success')
    mydb.commit()
    mycursor.close()
    mydb.close()
            
def insertstatus(quater, fname, sname, com, platoon, position):
    print(quater, fname, sname, com, platoon, position)
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    print("x")
    sql = (
        "INSERT INTO securestatus (`quater`, `position`, `fname`, `sname`, `company`, `platoon`) VALUES (%s , %s , %s , %s , %s , %s) ")
    val = (quater, position, fname, sname, com, platoon)
    mycursor.execute(sql, val)
    print('success')
    mydb.commit()
    mycursor.close()
    mydb.close()
                
def uplogin(quater, position, fname, sname, onduty, outduty):
    mydb = ConnectorMysql()
    mycursor = mydb.cursor()
    sql = (
        "INSERT INTO securelog (`quater`, `position`, `fname`, `sname`, `onduty`, `outduty`) VALUES (%s , %s , %s , %s , %s , %s) ")
    val = (quater, position, fname, sname, onduty, outduty)
    mycursor.execute(sql, val)
    print('success')
    mydb.commit()
    mycursor.close()
    mydb.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_IndutyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
