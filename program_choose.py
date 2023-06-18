# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'program_choose.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_difficulty_choose(object):
    def setupUi(self, difficulty_choose):
        difficulty_choose.setObjectName("difficulty_choose")
        difficulty_choose.resize(412, 732)
        self.centralwidget = QtWidgets.QWidget(difficulty_choose)
        self.centralwidget.setObjectName("centralwidget")
        self.arms_button = QtWidgets.QPushButton(self.centralwidget)
        self.arms_button.setGeometry(QtCore.QRect(80, 80, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.arms_button.setFont(font)
        self.arms_button.setIconSize(QtCore.QSize(16, 16))
        self.arms_button.setAutoRepeatDelay(300)
        self.arms_button.setObjectName("arms_button")
        self.legs_button = QtWidgets.QPushButton(self.centralwidget)
        self.legs_button.setGeometry(QtCore.QRect(80, 240, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.legs_button.setFont(font)
        self.legs_button.setIconSize(QtCore.QSize(16, 16))
        self.legs_button.setAutoRepeatDelay(300)
        self.legs_button.setObjectName("legs_button")
        self.core_button = QtWidgets.QPushButton(self.centralwidget)
        self.core_button.setGeometry(QtCore.QRect(80, 400, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.core_button.setFont(font)
        self.core_button.setIconSize(QtCore.QSize(16, 16))
        self.core_button.setAutoRepeatDelay(300)
        self.core_button.setObjectName("core_button")
        self.cardio_button = QtWidgets.QPushButton(self.centralwidget)
        self.cardio_button.setGeometry(QtCore.QRect(80, 560, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.cardio_button.setFont(font)
        self.cardio_button.setIconSize(QtCore.QSize(16, 16))
        self.cardio_button.setAutoRepeatDelay(300)
        self.cardio_button.setObjectName("cardio_button")
        difficulty_choose.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(difficulty_choose)
        self.statusbar.setObjectName("statusbar")
        difficulty_choose.setStatusBar(self.statusbar)

        self.retranslateUi(difficulty_choose)
        QtCore.QMetaObject.connectSlotsByName(difficulty_choose)

    def retranslateUi(self, difficulty_choose):
        _translate = QtCore.QCoreApplication.translate
        difficulty_choose.setWindowTitle(_translate("difficulty_choose", "Choose a Program"))
        self.arms_button.setText(_translate("difficulty_choose", "Arms"))
        self.legs_button.setText(_translate("difficulty_choose", "Legs"))
        self.core_button.setText(_translate("difficulty_choose", "Core"))
        self.cardio_button.setText(_translate("difficulty_choose", "Cardio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    difficulty_choose = QtWidgets.QMainWindow()
    ui = Ui_difficulty_choose()
    ui.setupUi(difficulty_choose)
    difficulty_choose.show()
    sys.exit(app.exec_())
