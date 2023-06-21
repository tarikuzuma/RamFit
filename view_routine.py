
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view_routine.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_view_routine(object):
    def setupUi(self, view_routine, program, difficulty):
        
        #Gets data of difficulty and program
        self.difficulty = difficulty
        self.program = program

        #Assigns view_routine to Ui_view_routine class
        self.win = view_routine

        view_routine.setObjectName("view_routine")
        view_routine.setWindowModality(QtCore.Qt.WindowModal)
        view_routine.resize(412, 732)
        self.centralwidget = QtWidgets.QWidget(view_routine)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 60, 431, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(170, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(10)
        self.main_label.setFont(font)
        self.main_label.setObjectName("main_label")

        # Create a QListWidget
        self.list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.list_widget.setGeometry(QtCore.QRect(0, 60, 412, 561))

        try:
            self.list_widget.addItems([self.read_program()])
        except:
            self.list_widget.addItems(['Error', 'No', 'File', 'Read'])

        self.list_widget.setObjectName("list_widget")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 680, 421, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setGeometry(QtCore.QRect(200, 630, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.proceed.setFont(font)
        self.proceed.setObjectName("proceed")

        self.proceed.clicked.connect(self.printBoth)

        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 650, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.back_button.setFont(font)
        self.back_button.setObjectName("back_button")

        self.back_button.clicked.connect(self.cancel)

        view_routine.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(view_routine)
        self.statusbar.setObjectName("statusbar")
        view_routine.setStatusBar(self.statusbar)

        self.retranslateUi(view_routine)
        QtCore.QMetaObject.connectSlotsByName(view_routine)

    #Method to store the name of each workout in a program_JSON file and add it to list_widget
    def read_program(self):

        #Stores 'names' data in list workout_names
        workout_names = []
        filepath = None #Flag Case. File path of JSON. Example: "program_files/beginner/arms.json"
        workout_type = None #Flag Case. Type of workout. Example: "beginner_arms"
        
        if self.difficulty == 1 and self.program =="arms":
            print("Beginners, arms day")
            workout_type = f"beginner_{self.program}"
            filepath = f"program_files/beginner/{self.program}.json"
        elif self.difficulty == 1 and self.program =="legs":
            print("Beginners, legs day")
            workout_type = f"beginner_{self.program}"
            filepath = f"program_files/beginner/{self.program}.json"
        else:
            print("Unreadable")
            return

        print ("File path: ", filepath, "\nKey:", workout_type)

        try:
            with open(filepath, "r") as f:
                json_object = json.load(f)
                #print ("\n",json_object,"\n") #Debug to read what JSON read.
                workout = json_object[workout_type]

                #Print the name of each exercise in the workout
                for exercise in workout:
                    exercise_name = exercise["name"]
                    workout_names.append(exercise_name) #Appends exercises_name to workout_names list

        except FileNotFoundError:
            print("File not found:", filepath)

        except json.JSONDecodeError:
            print("Invalid JSON format in file:", filepath)

        
        #Adds list of names into list_widget
        print ("Workouts include: ", *workout_names, sep=", ")
        self.list_widget.addItems([*workout_names])
    

    #Debugging purposes: Check if Button works. Check if dififculty and program is recorded
    def printBoth(self):
        self.read_program()
        print("Hello World: ", self.difficulty, self.program)
    
    def cancel(self):
        print("\nGoing back to main menu...\n")
        self.win.close()
        

    def retranslateUi(self, view_routine):
        _translate = QtCore.QCoreApplication.translate
        view_routine.setWindowTitle(_translate("view_routine", "MainWindow"))
        self.main_label.setText(_translate("view_routine", "Workout"))
        self.proceed.setText(_translate("view_routine", "Let\'s Go!"))
        self.back_button.setText(_translate("view_routine", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view_routine = QtWidgets.QMainWindow()
    ui = Ui_view_routine()
    ui.setupUi(view_routine)
    view_routine.show()
    sys.exit(app.exec_())