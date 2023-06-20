# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'difficulty_choose.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from program_choose import Ui_program_choose

#A class where the user can chosoe their difficulty. Indeoendent to "program_choose"
class Ui_difficulty_choose(object):
    def setupUi(self, difficulty_choose):
        difficulty_choose.setObjectName("difficulty_choose")
        difficulty_choose.resize(412, 732)
        self.centralwidget = QtWidgets.QWidget(difficulty_choose)
        self.centralwidget.setObjectName("centralwidget")
        self.easy_button = QtWidgets.QPushButton(self.centralwidget)
        self.easy_button.setGeometry(QtCore.QRect(80, 140, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.easy_button.setFont(font)
        self.easy_button.setIconSize(QtCore.QSize(16, 16))
        self.easy_button.setAutoRepeatDelay(300)
        self.easy_button.setObjectName("easy_button")

        #Intensity = 1, meaning "Beginner Level"
        self.easy_button.clicked.connect(lambda: self.intensity(1))

        self.intermediate_button = QtWidgets.QPushButton(self.centralwidget)
        self.intermediate_button.setGeometry(QtCore.QRect(80, 310, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.intermediate_button.setFont(font)
        self.intermediate_button.setIconSize(QtCore.QSize(16, 16))
        self.intermediate_button.setAutoRepeatDelay(300)
        self.intermediate_button.setObjectName("intermediate_button")

        #Intensity = 2, meaning "Intermediate Level"
        self.intermediate_button.clicked.connect(lambda: self.intensity(2))

        self.advanced_button = QtWidgets.QPushButton(self.centralwidget)
        self.advanced_button.setGeometry(QtCore.QRect(80, 480, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.advanced_button.setFont(font)
        self.advanced_button.setIconSize(QtCore.QSize(16, 16))
        self.advanced_button.setAutoRepeatDelay(300)
        self.advanced_button.setObjectName("advanced_button")

        #Intensity = 3, meaning "Advanced Level"
        self.advanced_button.clicked.connect(lambda: self.intensity(3))

        difficulty_choose.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(difficulty_choose)
        self.statusbar.setObjectName("statusbar")
        difficulty_choose.setStatusBar(self.statusbar)

        self.retranslateUi(difficulty_choose)
        QtCore.QMetaObject.connectSlotsByName(difficulty_choose)


    def retranslateUi(self, difficulty_choose):
        _translate = QtCore.QCoreApplication.translate
        difficulty_choose.setWindowTitle(_translate("difficulty_choose", "Choose Difficulty"))
        self.easy_button.setText(_translate("difficulty_choose", "Beginner"))
        self.intermediate_button.setText(_translate("difficulty_choose", "Intermediate"))
        self.advanced_button.setText(_translate("difficulty_choose", "Advanced"))

    #Accepts the argument "difficulty" which is dependent on what intenisity the exercise the user chose.
    #This method stores difficulty.choose and opens program_choose while saving the user's chosen difficulty.
    #The concept is called "Inter Module Communication."
    #https://www.sdcc.bnl.gov/phobos/Phat/PhatDocumentation/Phat5/node16.html

    def intensity(self, difficulty):
        self.difficulty = difficulty  # Store the difficulty level
        print(self.difficulty)

        #Open program_choose.py
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_program_choose()
        self.ui.setupUi(self.window, self.difficulty)  #Passes the difficulty to program_choose.py
        self.window.show()

        #Closes window of difficulty_choose.py
        difficulty_choose.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    difficulty_choose = QtWidgets.QMainWindow()
    ui = Ui_difficulty_choose()
    ui.setupUi(difficulty_choose)
    difficulty_choose.show()
    sys.exit(app.exec_())
