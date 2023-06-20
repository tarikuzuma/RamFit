# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'choose_profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_choose_profile(object):
    def setupUi(self, choose_profile):
        choose_profile.setObjectName("choose_profile")
        choose_profile.resize(412, 732)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        choose_profile.setFont(font)
        self.centralwidget = QtWidgets.QWidget(choose_profile)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 640, 394, 16))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 50, 394, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 190, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 190, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 380, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(20)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 380, 151, 121))
        font = QtGui.QFont()
        font.setFamily("Poppins Light")
        font.setPointSize(20)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_4.setObjectName("pushButton_4")
        choose_profile.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(choose_profile)
        self.statusbar.setObjectName("statusbar")
        choose_profile.setStatusBar(self.statusbar)

        self.retranslateUi(choose_profile)
        QtCore.QMetaObject.connectSlotsByName(choose_profile)

        #Back-end implementation of previous file.
        #Profile[number] gets the name data from "name_number[i]" and then prints it to button.
        name_numbers = self.read_profile()
        profile1 = name_numbers.get("name_number1", "None")
        profile2 = name_numbers.get("name_number2", "None")
        profile3 = name_numbers.get("name_number3", "None")
        profile4 = name_numbers.get("name_number4", "None")

        #Set the button labels depending on name of JSON File
        self.pushButton.setText(profile1)
        self.pushButton_2.setText(profile2)
        self.pushButton_3.setText(profile3)
        self.pushButton_4.setText(profile4)

        #Connect the button clicked signals to slots
        self.pushButton.clicked.connect(lambda: self.handle_button_click(name_numbers.get("name_number1"), 1))
        self.pushButton_2.clicked.connect(lambda: self.handle_button_click(name_numbers.get("name_number2"), 2))
        self.pushButton_3.clicked.connect(lambda: self.handle_button_click(name_numbers.get("name_number3"), 3))
        self.pushButton_4.clicked.connect(lambda: self.handle_button_click(name_numbers.get("name_number4"), 4))

    def retranslateUi(self, choose_profile):
        _translate = QtCore.QCoreApplication.translate
        choose_profile.setWindowTitle(_translate("choose_profile", "Choose Profile"))
        self.pushButton.setText(_translate("choose_profile", "profile1"))
        self.pushButton_2.setText(_translate("choose_profile", "profile2"))
        self.pushButton_3.setText(_translate("choose_profile", "profile3"))
        self.pushButton_4.setText(_translate("choose_profile", "profile4"))

    #Not gonna lie, I just used chatgpt to generate the method
    #I only know 35% of the concept in this method HAHA
    #But essentially it stores IDs or name numbers in a dictionary outside of the loop.
    #Easy method for global naming (well, not totally)
    def read_profile(self):
        name_numbers = {}
        for i in range(1, 5):
            file_path = f"profiles/mydata{i}.json"
            try:
                with open(file_path, 'r') as f:
                    json_object = json.load(f)
                    name = json_object['info']['name']
                    print("Name:", name)

                    name_numbers[f"name_number{i}"] = name

            except FileNotFoundError:
                print(f"File {file_path} not found. Continuing to the next file.")
                continue
            
        print ("")

        # Named "None" for debugging purposes
        # Print all name_numbers
        for i in range(1, 5):
            var_name = f"name_number{i}"
            value = name_numbers.get(var_name)
            if value is not None:
                print(f"{var_name}: {value}")
            else:
                value = "None"
                print(f"{var_name} is not defined. Therefore: {value}")

        print ("")
        return name_numbers

    #Method to edit status of JSON file.
    #"Status" is an element in the JSON File that defines it as "active"
    #Meaning that when Status of a JSON is ACTIVE, program will solely edit it.
    def edit_status(self, index):
        file_path = f"profiles/mydata{index}.json"
        with open(file_path, 'r') as f:
            json_object = json.load(f)
            theme = json_object['status']

            json_object['status'] = 'active'

            with open(file_path, 'w') as f:
                json.dump(json_object, f, indent = 4)

    #Instance when button is clicked
    #Accepts arguments index and button_address.
    #Index is the name of the user
    #button_address is the number location of the button in the screen
    def handle_button_click(self, index, button_address):
        print(f"Button: {index} clicked")

        #If statemetns to check what button address was pressed. 
        try:
            if button_address == 1:
                self.edit_status(1)
                print(f"{index} is now in active-editing mode.")
            elif button_address == 2:
                self.edit_status(2)
                print(f"{index} is now in active-editing mode.")
            elif button_address == 3:
                self.edit_status(3)
                print(f"{index} is now in active-editing mode.")
            elif button_address == 4:
                self.edit_status(4)
                print(f"{index} is now in active-editing mode.")

        #Except if error, print message in terminal.
        except FileNotFoundError:
            print("File does not exist.")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    choose_profile = QtWidgets.QMainWindow()
    ui = Ui_choose_profile()
    ui.setupUi(choose_profile)
    choose_profile.show()
    sys.exit(app.exec_())
