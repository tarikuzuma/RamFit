# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from confirmation import Ui_confirm
from defaults import *
import webbrowser
import subprocess
import json
import sys

#Settings class for defaults modification and profile deletions.
#Named ui_settings_2 because it's a duplicate of an old class that I didn't delete in bin
class Ui_settings_2(object):

    #Initialize UI.
    def setupUi(self, settings_2):

        self.win = settings_2

        settings_2.setObjectName("settings_2")

        settings_2.resize(WIDTH, HEIGHT)
        settings_2.setFixedWidth(WIDTH)
        settings_2.setFixedHeight(HEIGHT)
        settings_2.setMaximumWidth(WIDTH)
        settings_2.setMaximumHeight(HEIGHT)


        font = QtGui.QFont()
        font.setFamily(FONT)
        font.setPointSize(28)

        self.centralwidget = QtWidgets.QWidget(settings_2)
        self.centralwidget.setObjectName("centralwidget")
        self.theme_changer = QtWidgets.QPushButton(self.centralwidget)
        self.theme_changer.setEnabled(True)
        self.theme_changer.setGeometry(QtCore.QRect(60, 140, 301, 91))
        self.theme_changer.setObjectName("theme_changer")
        font.setPointSize(11)
        self.theme_changer.setFont(font)
        self.theme_changer.setStyleSheet("background-color: {};".format(BUTTON_COLOR))

        #When CLicked, changes the theme of the applciation.
        self.theme_changer.clicked.connect(self.edit_theme)

        self.settings = QtWidgets.QLabel(self.centralwidget)
        self.settings.setGeometry(QtCore.QRect(120, 40, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.settings.setFont(font)
        self.settings.setObjectName("settings")

        
        self.delete_data = QtWidgets.QPushButton(self.centralwidget)
        self.delete_data.setEnabled(True)
        self.delete_data.setGeometry(QtCore.QRect(60, 270, 301, 91))
        self.delete_data.setObjectName("delete_data")
        font.setPointSize(12)
        self.delete_data.setFont(font)
        self.delete_data.setStyleSheet("background-color: {};".format(BUTTON_COLOR1))

        #When Clicked, a pop-up will appear that will ask for confirmation.
        self.delete_data.clicked.connect(self.delete_content)

        self.about_us = QtWidgets.QPushButton(self.centralwidget)
        self.about_us.setEnabled(True)
        self.about_us.setGeometry(QtCore.QRect(60, 400, 301, 91))
        self.about_us.setObjectName("about_us")
        font.setPointSize(12)
        self.about_us.setFont(font)
        self.about_us.setStyleSheet("background-color: {};".format(BUTTON_COLOR))

        self.about_us.clicked.connect(self.open_link)

        self.back_main = QtWidgets.QPushButton(self.centralwidget)
        self.back_main.setEnabled(True)
        self.back_main.setGeometry(QtCore.QRect(60, 530, 301, 91))
        self.back_main.setObjectName("back_main")
        font.setPointSize(12)
        self.back_main.setFont(font)
        self.back_main.setStyleSheet("background-color: {};".format(BUTTON_COLOR1))

        #When Clicked, goes back to main
        self.back_main.clicked.connect(self.open_main)

        settings_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(settings_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 26))
        self.menubar.setObjectName("menubar")
        settings_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(settings_2)
        self.statusbar.setObjectName("statusbar")
        settings_2.setStatusBar(self.statusbar)

        settings_2.setStyleSheet("background-color: {};".format(THEME_COLOR))

        self.retranslateUi(settings_2)
        QtCore.QMetaObject.connectSlotsByName(settings_2)

    def retranslateUi(self, settings_2):
        _translate = QtCore.QCoreApplication.translate
        settings_2.setWindowTitle(_translate("settings_2", "Settings"))
        self.theme_changer.setText(_translate("settings_2", "Change Light and Dark Mode"))
        self.settings.setText(_translate("settings_2", "Settings"))
        self.delete_data.setText(_translate("settings_2", "Delete All Data"))
        self.about_us.setText(_translate("settings_2", "About Us"))
        self.back_main.setText(_translate("settings_2", "Back to Main"))

    #Edits the content of json file "theme"
    def edit_theme(self):
        #Reads content of theme.json
        with open("settings/theme.json", 'r') as f:
            json_object = json.load(f) 
            theme = json_object['theme']

            #If condition to see if theme is dark or light, and then converts it to its opposite.
            if theme == "light":
                json_object["theme"] = "dark"
            elif theme == "dark":
                json_object["theme"] = "light"

            #Print what theme it is now
            print ("Theme is now ", json_object['theme'])

            # Write the updated data back to the JSON file
            with open("settings/theme.json", 'w') as f:
                json.dump(json_object, f)

        #Reopens main menu but with different theme
        subprocess.Popen(["python", "main_menu.py"])
        sys.exit()

    #Method to delete all profile data
    def delete_content(self):
        #open window delete content
        print("Delete all profiles?")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_confirm()
        self.ui.setupUi(self.window)
        self.window.show()
        #settings_2.hide()

    def open_link(self):
        webbrowser.open("https://github.com/tarikuzuma/RamFit")
        
    #Method to close settings
    def open_main(self):
        print ("Going back to main menu")
        self.win.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings_2 = QtWidgets.QMainWindow()
    ui = Ui_settings_2()
    ui.setupUi(settings_2)
    settings_2.show()
    sys.exit(app.exec_())