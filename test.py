# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_workout.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_main_workout(object):
    def setupUi(self, main_workout):

        self.win = main_workout
        self.workout_finished = False #Set workout_finished to False

        main_workout.setObjectName("main_workout")
        main_workout.resize(412, 732)
        self.centralwidget = QtWidgets.QWidget(main_workout)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 70, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.number = QtWidgets.QLabel(self.centralwidget)
        self.number.setGeometry(QtCore.QRect(60, 20, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins ExtraBold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.number.setFont(font)
        self.number.setObjectName("number")
        self.left = QtWidgets.QLabel(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(110, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(11)
        self.left.setFont(font)
        self.left.setObjectName("left")
        self.finish_workout = QtWidgets.QPushButton(self.centralwidget)
        self.finish_workout.setGeometry(QtCore.QRect(270, 20, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.finish_workout.setFont(font)
        self.finish_workout.setObjectName("finish_workout")

        self.finish_workout.clicked.connect(self.workout_finish)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 100, 391, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.exercise_name = QtWidgets.QLabel(self.centralwidget)
        self.exercise_name.setGeometry(QtCore.QRect(30, 430, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(11)
        self.exercise_name.setFont(font)
        self.exercise_name.setObjectName("exercise_name")
        self.reps = QtWidgets.QLabel(self.centralwidget)
        self.reps.setGeometry(QtCore.QRect(280, 430, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(11)
        self.reps.setFont(font)
        self.reps.setObjectName("reps")
        self.completed = QtWidgets.QPushButton(self.centralwidget)
        self.completed.setGeometry(QtCore.QRect(30, 650, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        self.completed.setFont(font)
        self.completed.setObjectName("completed")

        self.completed.clicked.connect(self.workout_complete)

        self.description = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(20, 470, 381, 121))
        self.description.setObjectName("description")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 610, 361, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        main_workout.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_workout)
        self.statusbar.setObjectName("statusbar")
        main_workout.setStatusBar(self.statusbar)

        self.retranslateUi(main_workout)
        QtCore.QMetaObject.connectSlotsByName(main_workout)

    def retranslateUi(self, main_workout):
        _translate = QtCore.QCoreApplication.translate
        main_workout.setWindowTitle(_translate("main_workout", "MainWindow"))
        self.number.setText(_translate("main_workout", "10"))
        self.left.setText(_translate("main_workout", "Exercises Left"))
        self.finish_workout.setText(_translate("main_workout", "> Finish Workout"))
        self.exercise_name.setText(_translate("main_workout", "Exercise Name"))
        self.reps.setText(_translate("main_workout", "Repetition"))
        self.completed.setText(_translate("main_workout", "Completed"))

    def read_workout(self):
        filepath = "program_files/beginner/arms.json" #Dependent on workout_routine's filepath
        workout_type = "beginner_arms" #Dependent on workout_type of viewroutine
        workout_names = []
        reps = []
        image = []
        description = []
        
        with open(filepath, "r") as f:
            json_object = json.load(f)
            #print ("\n",json_object,"\n") #Debug to read what JSON read.
            workout = json_object[workout_type]

            #Print the name of each exercise in the workout
            for exercise in workout:
                exercise_name = exercise["name"]
                exercise_reps = exercise["reps"]
                exercise_image = exercise["image"]
                exercise_description = exercise["description"]

                #Appends exercises_name to workout_names list
                workout_names.append(exercise_name) 
                reps.append(exercise_reps)
                image.append(exercise_image)
                description.append(exercise_description)

        print (workout_names)
        print(reps)
        print(image)
        print(description)

    #Method to clsoe window when workout is completed
    def workout_complete(self):
        self.win.close()

    #Ultimately stops the workout session when button is clicked
    def workout_finish(self):
        self.workout_finished = True #If workout_finished button is clicked, sets workout_finish to true
        self.win.close()

    @staticmethod
    def test():
        """Test method"""
        instance = Ui_main_workout()
        instance.read_workout()

    #Runs when class is called
    #Method to loop window open and close 10 times
    @staticmethod
    def run_window():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        ui = Ui_main_workout()
        
        #Loops through opening window 10 times
        for _ in range(10):
            main_workout = QtWidgets.QMainWindow()
            ui.setupUi(main_workout)
            main_workout.show()
            app.exec_()
            
            #If workout_finished is clicked, stop loop and ultimateley exit.
            if ui.workout_finished:
                break
       
        print("Workout Session Done!")
        sys.exit()

if __name__ == "__main__":
    ui = Ui_main_workout()
    Ui_main_workout.test()
    ui.run_window()
