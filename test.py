from PyQt5 import QtCore, QtGui, QtWidgets
from view_routine import Ui_view_routine

#Screen will not open unless choose a difficulty first
class Ui_program_choose(object):
    def setupUi(self, program_choose, difficulty):
        #Stores the difficulty level from difficulty_choose.py!
        self.difficulty = difficulty

        program_choose.setObjectName("program_choose")
        program_choose.resize(412, 732)
        self.centralwidget = QtWidgets.QWidget(program_choose)
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

        self.arms_button.clicked.connect(lambda:self.program("arms"))

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

        self.legs_button.clicked.connect(lambda:self.program("legs"))

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

        self.core_button.clicked.connect(lambda:self.program("core"))

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

        self.cardio_button.clicked.connect(lambda:self.program("cardio"))

        program_choose.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(program_choose)
        self.statusbar.setObjectName("statusbar")
        program_choose.setStatusBar(self.statusbar)

        self.retranslateUi(program_choose)
        QtCore.QMetaObject.connectSlotsByName(program_choose)

    def retranslateUi(self, program_choose):
        _translate = QtCore.QCoreApplication.translate
        program_choose.setWindowTitle(_translate("program_choose", "Choose a Program"))
        self.arms_button.setText(_translate("program_choose", "Arms"))
        self.legs_button.setText(_translate("program_choose", "Legs"))
        self.core_button.setText(_translate("program_choose", "Core"))
        self.cardio_button.setText(_translate("program_choose", "Cardio"))

    def program(self, program):
        print(self.difficulty, program)  # Print the difficulty and program
        
        #Opens view_routine.py
        self.view_routine_window = QtWidgets.QMainWindow()
        self.view_routine_ui = Ui_view_routine()
        self.view_routine_ui.setupUi(self.view_routine_window)
        self.view_routine_window.show()

        #Closes window of program_choose.py
        self.program_choose.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_program_choose()
    program_choose = QtWidgets.QMainWindow()
    ui.setupUi(program_choose)
    program_choose.show()
    sys.exit(app.exec_())
