# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from settings import Ui_settings_2
from create_profile import Ui_createProfile
from choose_profile import Ui_choose_profile
from defaults import *
import json

#Initailizes Main Menu Screen for application.
class Ui_MainWindow(object):

    #Create UI.
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        #Height is based off Nexus 5X viewport
        MainWindow.resize(WIDTH, HEIGHT)
        MainWindow.setFixedWidth(WIDTH)
        MainWindow.setFixedHeight(HEIGHT)
        MainWindow.setMaximumWidth(WIDTH)
        MainWindow.setMaximumHeight(HEIGHT)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.test1_button = QtWidgets.QPushButton(self.centralwidget)
        self.test1_button.setEnabled(True)
        self.test1_button.setGeometry(QtCore.QRect(60, 220, 301, 91))
        self.test1_button.setStyleSheet("background-color: {};".format(BUTTON_COLOR))
        self.test1_button.setObjectName("test1_button")
        font = QtGui.QFont()
        font.setFamily(FONT)
        font.setPointSize(12)
        self.test1_button.setFont(font)

        self.test1_button.clicked.connect(self.open_choose_profile)

        self.main_menu = QtWidgets.QLabel(self.centralwidget)
        self.main_menu.setGeometry(QtCore.QRect(130, 100, 200, 61))
        font = QtGui.QFont()
        font.setFamily(FONT)
        font.setPointSize(28)
        self.main_menu.setFont(font)
        #Button to create profile
        self.main_menu.setFont(font)
        self.main_menu.setObjectName("main_menu")

        self.test1_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.test1_button_2.setEnabled(True)
        self.test1_button_2.setGeometry(QtCore.QRect(60, 360, 301, 91))
        self.test1_button_2.setStyleSheet("background-color: {};".format(BUTTON_COLOR))
        self.test1_button_2.setObjectName("test1_button_2")
        font.setPointSize(12)
        self.test1_button_2.setFont(font)

        #When Clicked, a new window will pop-up.
        self.test1_button_2.clicked.connect(self.open_create_profile)

        #Button for Settings
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setEnabled(True)
        self.settings_button.setGeometry(QtCore.QRect(60, 500, 301, 91))
        self.settings_button.setObjectName("test1_button_3")
        self.settings_button.setStyleSheet("background-color: {};".format(BUTTON_COLOR))
        self.settings_button.setFont(font)

        #When Clicked, a new window will pop up.
        self.settings_button.clicked.connect(self.open_settings)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Theme of screen is dependent on theme file data.
        #MainWindow.setStyleSheet("background-color: yellow;")
        MainWindow.setStyleSheet("background-color: {};".format(THEME_COLOR))

        MainWindow.setWindowIcon(QtGui.QIcon(ICON))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Menu"))
        self.test1_button.setText(_translate("MainWindow", "Choose Profile"))
        self.main_menu.setText(_translate("MainWindow", "RamFit"))
        self.test1_button_2.setText(_translate("MainWindow", "Create Profile"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))

    #Opens choose_profile.py
    def open_choose_profile(self):
        print ("Deactivating all profiles...")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_choose_profile()
        self.ui.setupUi(self.window)

        #Turns every profile status to "None" or "Not Editable" once clicked
        for i in range(1,5):
            try:
                file_path = f"profiles/mydata{i}.json"
                with open(file_path, 'r') as f:
                    json_object = json.load(f)
                    theme = json_object['status']

                    json_object['status'] = 'None'

                    with open(file_path, 'w') as f:
                        json.dump(json_object, f, indent = 4)
            except FileNotFoundError:
                continue

        self.window.show()

    #Opens create_profile.py
    def open_create_profile(self):
        print("User Creating Profile...")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_createProfile()
        self.ui.setupUi(self.window)
        self.window.show()

    #Opens settings.py
    def open_settings(self):
        print("Opening Settings...")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_settings_2() #calls Ui_settings from another class
        self.ui.setupUi(self.window) #draws window
        #MainWindow.hide() #Hides Window
        self.window.show() #shows window


if __name__ == "__main__":
    import sys
    print("\033[92m \n-Welcome to Ramfit!-\n \033[0m") #Turns the print statement into green using ANSI Sequence
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())