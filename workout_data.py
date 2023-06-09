# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'workout_data.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from defaults import *
import json

class Ui_list_workout_data(object):
    def setupUi(self, list_workout_data, filename):
        
        self.filename = filename
        self.win = list_workout_data

        list_workout_data.setObjectName("list_workout_data")
        
        list_workout_data.resize(412, 612)
        self.centralwidget = QtWidgets.QWidget(list_workout_data)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 50, 421, 491))
        self.listWidget.setObjectName("listWidget")
        font = QtGui.QFont("Poppins")
        self.listWidget.setFont(font)

        self.listWidget.setStyleSheet("""
                QListWidget {
                    background-color: %s; /* Set the background color of the list */
                    border: none; /* Remove the border */
                    padding: 10px; /* Add padding to the list */
                }

                QListWidget::item {
                    background-color: %s; /* Set the background color of each item */
                    padding: 10px; /* Add padding to each item */
                    border-radius: 5px; /* Add border radius to round the corners */
                }

                QListWidget::item:alternate {
                    background-color: %s; /* Set the alternate background color of each item */
                }

                QListWidget::item:selected {
                    background-color: %s; /* Set the background color of the selected item */
                    color: white; /* Set the text color of the selected item */
                }
            """ % (LIST_COLOR,LIST_COLOR, LIST_COLOR, LIST_HIGHLIGHT))

        workout_data_list = self.append_data(self.filename)
        self.display_workout_data(workout_data_list)

        self.main_back = QtWidgets.QPushButton(self.centralwidget)
        self.main_back.setGeometry(QtCore.QRect(242, 550, 161, 28))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.main_back.setFont(font)
        self.main_back.setObjectName("main_back")
        self.main_back.setStyleSheet("background-color: {};".format(BUTTON_COLOR))
        self.main_back.clicked.connect(self.back_main)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        list_workout_data.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(list_workout_data)
        self.statusbar.setObjectName("statusbar")
        list_workout_data.setStatusBar(self.statusbar)

        list_workout_data.setStyleSheet("background-color: {};".format(THEME_COLOR))

        print(self.append_data(self.filename))

        self.retranslateUi(list_workout_data)
        QtCore.QMetaObject.connectSlotsByName(list_workout_data)
        list_workout_data.setWindowIcon(QtGui.QIcon(ICON))

    def retranslateUi(self, list_workout_data):
        _translate = QtCore.QCoreApplication.translate
        list_workout_data.setWindowTitle(_translate("list_workout_data", "Workout Data"))
        self.main_back.setText(_translate("list_workout_data", "Back to Results"))
        self.label.setText(_translate("list_workout_data", "Workout Data"))

    def back_main(self):
        self.win.close()

    #This method is used to append the workout data to the list.
    def append_data(self, filename):
        filename = self.filename
        workout_data_list = []
        with open(filename, 'r') as f:
            data = json.load(f)
            workout_data = data["workout_data"]
            workout_data_list.extend(workout_data)

        return workout_data_list
    
    #This method is used to display the workout data in the list but seperated with brackets
    def display_workout_data(self, workout_data_list):
        
        #For every lsit of workout data
        for workout_data in workout_data_list:
            for date, data in workout_data.items():
                text = f"Date: {date}\n"
                text += f"Time: {data['Time']}\n"
                text += f"Type: {data['Type']}\n"
                text += f"Duration: {data['Duration']}\n"
                text += f"Calories Burnt: {data['Calories Burnt']}\n"
                text += "------------------------\n"

                item = QtWidgets.QListWidgetItem(text)
                self.listWidget.addItem(item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    list_workout_data = QtWidgets.QMainWindow()
    ui = Ui_list_workout_data()
    ui.setupUi(list_workout_data)
    list_workout_data.show()
    sys.exit(app.exec_())
