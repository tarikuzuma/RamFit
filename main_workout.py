# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_workout.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from results import Ui_results 
import time as timer
import json
import sys

class Ui_main_workout(object):
    '''
        Accepts the arguments count, which is the number of times the program needs to keep changing the screen.
            - Count is Equal to the total number of workouts.
            - Filepath stores path where data should go 
            - Workout type (arms, legs, core, cardio)
            - Start_time is the persistent value that will keep running at the background to measure time.
    '''
    def setupUi(self, main_workout, count, filepath, workout_type, start_time):
        self.count = count #Count as persistent
        self.filepath = filepath
        self.workout_type = workout_type 
        self.start_time = start_time #start_time value as persistent

        self.win = main_workout
        self.workout_finished = False 
        self.timer_stop = False

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
        font.setFamily("Poppins")
        self.description.setFont(font)
        #self.description.setPlainText("Hello Test") Old code to display value for description

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 610, 361, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        main_workout.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_workout)
        self.statusbar.setObjectName("statusbar")
        main_workout.setStatusBar(self.statusbar)
        self.init_info(count, filepath, workout_type)

        self.retranslateUi(main_workout)
        QtCore.QMetaObject.connectSlotsByName(main_workout)

    def retranslateUi(self, main_workout):
        _translate = QtCore.QCoreApplication.translate
        main_workout.setWindowTitle(_translate("main_workout", "MainWindow"))
        #self.number.setText(_translate("main_workout", "10")) #Old code to set the total number of exercises to default
        #self.left.setText(_translate("main_workout", "Exercises Left")) #Old code to set exercises to left
        self.finish_workout.setText(_translate("main_workout", "> Finish Workout"))
        #self.exercise_name.setText(_translate("main_workout", "Exercise Name")) #Old code to set name to default
        #self.reps.setText(_translate("main_workout", "Repetition")) #Old code to set reps to default
        self.completed.setText(_translate("main_workout", "Completed"))
    
    #Method to start timer
    def start_timer(self):
        print("Timer Started...")
        self.start_time = timer.time()

    #Method to end timer IF self.timer_stop is TRUE
    def end_timer(self):
        if self.timer_stop:
            print(" \n PASSES \n")
            end_time = timer.time()
            elapsed_time = end_time - self.start_time

            print (f"Timer stopped. Elapsed time: {elapsed_time} seconds.")

            return elapsed_time

    #Open and close window while changing the values depending on count.
    def workout_complete(self):
        self.count += 1
        
        #Stops the program with completion.
        if self.count >= len(self.workout_names): #True Stop
            self.timer_stop = True
            self.time = self.end_timer()

            print("Timer stop: ", self.timer_stop)
            print("Workout Session Done With Completion! Well Done.")

            #Opens results.py window
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_results()
            self.ui.setupUi(self.window, self.filepath, self.workout_type, self.time)
            self.window.show()
            #sys.exit() # FIXME: Is this the right behavior?
            self.win.close()
            return

        self.win.close()
        self.win = QtWidgets.QMainWindow()
        self.ui = Ui_main_workout()
        print(self.count)
        self.ui.setupUi(self.win, self.count, self.filepath, self.workout_type, self.start_time)
        self.win.show()

    #Method to forcefully stop workout
    def workout_finish(self):
        self.workout_finished = True
        self.timer_stop = True
        print("Timer stop: ", self.timer_stop)

        self.time = self.end_timer()

        if self.workout_finished: #Value will only be true when user clicks "Finish Workout."
            print("\nForced Stop...\nWorkout Session Done!")
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_results()
            self.ui.setupUi(self.window, self.filepath,self.workout_type, self.time)
            self.window.show()
            #sys.exit() # FIXME: Is this the right behavior?
            self.win.close()

    #Method to read workout JSON. Accepts the arguments filepath and workout_type.
    def read_workout(self, filepath, workout_type):
        self.workout_names = []
        self.workout_reps = []
        self.workout_image = []
        self.workout_description = []

        with open(filepath, "r") as f:
            json_object = json.load(f)
            #print ("\n",json_object,"\n") #Debug to read what JSON read.
            workout = json_object[workout_type]

            #Equate into a variable certain dta afrom JSON.
            for exercise in workout:
                exercise_name = exercise["name"]
                exercise_reps = exercise["reps"]
                exercise_image = exercise["image"]
                exercise_description = exercise["description"]

                #Appends data gathered from JSON to ff. lists
                self.workout_names.append(exercise_name) 
                self.workout_reps.append(exercise_reps)
                self.workout_image.append(exercise_image)
                self.workout_description.append(exercise_description)

    #This is where we're gonna put all of the interchangable data
    def init_info(self, count, filepath, workout_type):
        print("{" + str(count) + "}")

        #If self count is 0 or just started, initialize timer.
        if self.count == 0:
            self.start_timer()

        print("Timer stop: ", self.timer_stop)

        filepath = self.filepath # Dependent on workout_routine's filepath
        workout_type = self.workout_type # Dependent on workout_type of viewroutine

        # Calls read_workout
        self.read_workout(filepath, workout_type)

        '''
        # For debugging purposes, prints the list.
        print (self.workout_names)
        print (self.workout_reps)
        print (self.workout_image)
        print (self.workout_description)
        '''

        # Block of code to deduct the number of exercises left depending on the length of list workout_names
        number = len(self.workout_names) - count
        number_string = str(number)

        # See if image can be loaded or exist
        try:
            # Load the image file
            image_path = self.workout_image[count]
            pixmap = QPixmap(image_path)

            # Set the loaded image as the background of the QGraphicsView
            scene = QtWidgets.QGraphicsScene()
            scene.addPixmap(pixmap)
            self.graphicsView.setScene(scene)

        except Exception as e:
            print("Error loading image:", str(e))

        # Sets value of labels
        self.number.setText(number_string) # Change the number of exercises left each recursive loop by deducting with 1
        self.exercise_name.setText(self.workout_names[count]) # Access exercise_name from self
        self.reps.setText(self.workout_reps[count]) # Access workout_reps from self
        self.description.setPlainText(self.workout_description[count]) # Access workout_description from self

        if number != 1:
            self.left.setText("Exercises Left")
        else:
            self.left.setText("Exercise Left")

        # Debugging, prints value of lists per index flagged down dependent to value of count
        print (self.workout_names[count])
        print (self.workout_reps[count])
        print (self.workout_image[count])
        print (self.workout_description[count])
#On run, run_window()
if __name__ == "__main__":
    ui = Ui_main_workout()
    ui.run_window()