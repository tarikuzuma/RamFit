# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confirmation_create2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

#Class that warns the user that number of max profiels reached.
class Ui_profile_createdpy(object):

    def setupUi(self, profile_createdpy):
        profile_createdpy.setObjectName("profile_createdpy")
        profile_createdpy.resize(412, 168)
        self.centralwidget = QtWidgets.QWidget(profile_createdpy)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 321, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.confirm = QtWidgets.QPushButton(self.centralwidget)
        self.confirm.setGeometry(QtCore.QRect(160, 100, 93, 28))
        self.confirm.setObjectName("confirm")

        self.confirm.clicked.connect(lambda: self.confirmation(profile_createdpy))

        profile_createdpy.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(profile_createdpy)
        self.statusbar.setObjectName("statusbar")
        profile_createdpy.setStatusBar(self.statusbar)

        self.retranslateUi(profile_createdpy)
        QtCore.QMetaObject.connectSlotsByName(profile_createdpy)

    def retranslateUi(self, profile_createdpy):
        _translate = QtCore.QCoreApplication.translate
        profile_createdpy.setWindowTitle(_translate("profile_createdpy", "Denied"))
        self.label.setText(_translate("profile_createdpy", "No. of Profiles Reached"))
        self.confirm.setText(_translate("profile_createdpy", "Sad :("))

    #Closes the window
    def confirmation(self, conf_v):
        print("\nMax no. of profiles reached.\n")
        conf_v.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    profile_createdpy = QtWidgets.QMainWindow()
    ui = Ui_profile_createdpy()
    ui.setupUi(profile_createdpy)
    profile_createdpy.show()
    sys.exit(app.exec_())
