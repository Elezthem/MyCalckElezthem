# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalcElezthem.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(358, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Text = QtWidgets.QLabel(self.centralwidget)
        self.Text.setGeometry(QtCore.QRect(0, 0, 361, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.Text.setFont(font)
        self.Text.setStyleSheet("background-color: rgb(171, 171, 171);\n"
"color: rgb(255, 255, 255);")
        self.Text.setObjectName("Text")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 320, 150, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_0.setObjectName("btn_0")
        self.Rovno = QtWidgets.QPushButton(self.centralwidget)
        self.Rovno.setGeometry(QtCore.QRect(150, 320, 150, 80))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Rovno.setFont(font)
        self.Rovno.setStyleSheet("background-color: rgb(158, 158, 158);\n"
"color: rgb(255, 255, 255);")
        self.Rovno.setObjectName("Rovno")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 50, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 50, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 50, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_9.setObjectName("btn_9")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 140, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 140, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 140, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_6.setObjectName("btn_6")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 230, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 230, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 230, 100, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(217, 217, 217);\n"
"color: rgb(255, 255, 255);")
        self.btn_3.setObjectName("btn_3")
        self.btn_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_10.setGeometry(QtCore.QRect(299, 50, 61, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_10.setFont(font)
        self.btn_10.setStyleSheet("background-color: rgb(158, 158, 158);\n"
"color: rgb(255, 255, 255);")
        self.btn_10.setObjectName("btn_10")
        self.btn_11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_11.setGeometry(QtCore.QRect(300, 140, 61, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_11.setFont(font)
        self.btn_11.setStyleSheet("background-color: rgb(158, 158, 158);\n"
"color: rgb(255, 255, 255);")
        self.btn_11.setObjectName("btn_11")
        self.btn_12 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_12.setGeometry(QtCore.QRect(300, 230, 61, 90))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_12.setFont(font)
        self.btn_12.setStyleSheet("background-color: rgb(158, 158, 158);\n"
"color: rgb(255, 255, 255);")
        self.btn_12.setObjectName("btn_12")
        self.btn_13 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_13.setGeometry(QtCore.QRect(300, 319, 61, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.btn_13.setFont(font)
        self.btn_13.setStyleSheet("background-color: rgb(158, 158, 158);\n"
"color: rgb(255, 255, 255);")
        self.btn_13.setObjectName("btn_13")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

        self.is_Rovno = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Elezthem - Калькулятор"))
        self.Text.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.Rovno.setText(_translate("MainWindow", "="))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_10.setText(_translate("MainWindow", "+"))
        self.btn_11.setText(_translate("MainWindow", "-"))
        self.btn_12.setText(_translate("MainWindow", "*"))
        self.btn_13.setText(_translate("MainWindow", "/"))

    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_10.clicked.connect(lambda: self.write_number(self.btn_10.text()))
        self.btn_11.clicked.connect(lambda: self.write_number(self.btn_11.text()))
        self.btn_12.clicked.connect(lambda: self.write_number(self.btn_12.text()))
        self.btn_13.clicked.connect(lambda: self.write_number(self.btn_13.text()))

        self.Rovno.clicked.connect(self.results)

    def write_number(self, number):
        if self.Text.text() == "0" or self.is_Rovno:
            self.Text.setText(number)
            self.is_Rovno = False
        else:
            self.Text.setText(self.Text.text() + number)

    def results(self):
        if not self.is_Rovno:
            res = eval(self.Text.text())
            self.Text.setText("Результат: " + str(res))
            self.is_Rovno = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset|QMessageBox.Cancel|QMessageBox.Ok)

            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("Два раза действие не выполнить")
            error.setDetailedText("Детали")

            error.buttonClicked.connect(self.popup_action)

            error.exec_()

    def popup_action(self, btn):
        if btn.text() == "Ok":
            print("Print Ok")
        elif btn.text() == "Reset":
            self.Text.setText("")
            self.Rovno = False




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
