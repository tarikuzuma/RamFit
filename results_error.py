# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from workout_data import Ui_list_workout_data
from defaults import *


class Ui_results_error(object):
    def setupUi(self, results):

        self.win = results

        results.setObjectName("results")
        results.resize(WIDTH, HEIGHT)
        results.setFixedWidth(WIDTH)
        results.setFixedHeight(HEIGHT)
        results.setMaximumWidth(WIDTH)
        results.setMaximumHeight(HEIGHT)

        results.resize(412, 732)
        self.centralwidget = QtWidgets.QWidget(results)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 60, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.synopsis = QtWidgets.QLabel(self.centralwidget)
        self.synopsis.setGeometry(QtCore.QRect(130, 25, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.synopsis.setFont(font)
        self.synopsis.setObjectName("synopsis")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 140, 411, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.total_time = QtWidgets.QLabel(self.centralwidget)
        self.total_time.setGeometry(QtCore.QRect(30, 100, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.total_time.setFont(font)
        self.total_time.setObjectName("total_time")
        self.total_time_editable = QtWidgets.QLabel(self.centralwidget)
        self.total_time_editable.setGeometry(QtCore.QRect(250, 100, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.total_time_editable.setFont(font)
        self.total_time_editable.setObjectName("total_time_editable")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 260, 376, 218))
        self.calendarWidget.setObjectName("calendarWidget")
        self.total_calories = QtWidgets.QLabel(self.centralwidget)
        self.total_calories.setGeometry(QtCore.QRect(30, 180, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.total_calories.setFont(font)
        self.total_calories.setObjectName("total_calories")
        self.total_calories_editable = QtWidgets.QLabel(self.centralwidget)
        self.total_calories_editable.setGeometry(QtCore.QRect(250, 180, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.total_calories_editable.setFont(font)
        self.total_calories_editable.setObjectName("total_calories_editable")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 220, 411, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 500, 411, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 630, 411, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.height_label = QtWidgets.QLabel(self.centralwidget)
        self.height_label.setGeometry(QtCore.QRect(50, 550, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.height_label.setFont(font)
        self.height_label.setObjectName("height_label")
        self.BMI_label = QtWidgets.QLabel(self.centralwidget)
        self.BMI_label.setGeometry(QtCore.QRect(190, 520, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BMI_label.setFont(font)
        self.BMI_label.setObjectName("BMI_label")
        self.calendar_label = QtWidgets.QLabel(self.centralwidget)
        self.calendar_label.setGeometry(QtCore.QRect(80, 240, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calendar_label.setFont(font)
        self.calendar_label.setObjectName("calendar_label")

        self.calendarWidget.clicked.connect(self.calendar_click)

        self.weight_label = QtWidgets.QLabel(self.centralwidget)
        self.weight_label.setGeometry(QtCore.QRect(50, 580, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.weight_label.setFont(font)
        self.weight_label.setObjectName("weight_label")
        self.bmi_final = QtWidgets.QLabel(self.centralwidget)
        self.bmi_final.setGeometry(QtCore.QRect(220, 600, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bmi_final.setFont(font)
        self.bmi_final.setObjectName("bmi_final")
        self.height_editable = QtWidgets.QLabel(self.centralwidget)
        self.height_editable.setGeometry(QtCore.QRect(190, 550, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.height_editable.setFont(font)
        self.height_editable.setObjectName("height_editable")
        self.weight_editable = QtWidgets.QLabel(self.centralwidget)
        self.weight_editable.setGeometry(QtCore.QRect(190, 580, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.weight_editable.setFont(font)
        self.weight_editable.setObjectName("weight_editable")
        self.button_main = QtWidgets.QPushButton(self.centralwidget)
        self.button_main.setGeometry(QtCore.QRect(262, 660, 121, 28))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.button_main.setFont(font)
        self.button_main.setObjectName("button_main")
        self.button_main.setStyleSheet("background-color: {};".format(BUTTON_COLOR2))
        self.button_main.clicked.connect(self.back_main)

        results.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(results)
        self.statusbar.setObjectName("statusbar")
        results.setStatusBar(self.statusbar)
        results.setStyleSheet("background-color: {};".format(THEME_COLOR))

        self.retranslateUi(results)
        QtCore.QMetaObject.connectSlotsByName(results)

    def retranslateUi(self, results):
        _translate = QtCore.QCoreApplication.translate
        results.setWindowTitle(_translate("results", "MainWindow"))
        self.synopsis.setText(_translate("results", "Workout Synopsis"))
        self.total_time.setText(_translate("results", "Total time of Workout:"))
        self.total_time_editable.setText(_translate("results", "10 Minutes"))
        self.total_calories.setText(_translate("results", "Potential Calories Lost:"))
        self.total_calories_editable.setText(_translate("results", "100 Calories"))
        self.height_label.setText(_translate("results", "Your Height:"))
        self.BMI_label.setText(_translate("results", "BMI:"))
        self.calendar_label.setText(_translate("results", "Calendar of Days Worked Out"))
        self.weight_label.setText(_translate("results", "Your Weight:"))
        self.bmi_final.setText(_translate("results", "= Index / Category"))
        self.height_editable.setText(_translate("results", "Draft"))
        self.weight_editable.setText(_translate("results", "Draft"))
        self.button_main.setText(_translate("results", "Back to Main"))

    def calendar_click(self, date):
        print('Calendar clicked:', date.toString())
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_list_workout_data()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def back_main(self):
        self.win.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    results = QtWidgets.QMainWindow()
    ui = Ui_results_error()
    ui.setupUi(results)
    results.show()
    sys.exit(app.exec_())
