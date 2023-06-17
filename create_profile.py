# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from confirmation_create import Ui_profile_created
from confirmation_create2 import Ui_profile_createdpy
import json
from pathlib import Path

#Profile Create Class
class Ui_createProfile(object):

    #Initialize UI
    def setupUi(self, createProfile):
        createProfile.setObjectName("createProfile")
        createProfile.resize(412, 732)
        self.centralwidget = QtWidgets.QWidget(createProfile)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_create = QtWidgets.QPushButton(self.centralwidget)
        self.btn_create.setGeometry(QtCore.QRect(240, 590, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_create.setFont(font)
        self.btn_create.setObjectName("btn_create")

        # When Clicked, triggers the confirmation event.
        self.btn_create.clicked.connect(self.show_line)

        # Lambda expression on when clicked, sex = male
        self.rad_male = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.show_line)
        self.rad_male.setGeometry(QtCore.QRect(152, 290, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rad_male.setFont(font)
        self.rad_male.setObjectName("rad_male")

        # Lambda expression on when clicked, sex = female
        self.rad_female = QtWidgets.QRadioButton(self.centralwidget, clicked=lambda: self.show_line)
        self.rad_female.setGeometry(QtCore.QRect(152, 350, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rad_female.setFont(font)
        self.rad_female.setObjectName("rad_female")

        # groups radio buttons female and male into one.
        # Uses the object "button_group"
        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButton(self.rad_male)
        self.button_group.addButton(self.rad_female)
        self.button_group.setExclusive(True)

        self.box_feet = QtWidgets.QLineEdit(self.centralwidget)
        self.box_feet.setGeometry(QtCore.QRect(150, 430, 51, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.box_feet.setFont(font)
        self.box_feet.setObjectName("box_feet")

        self.box_inches = QtWidgets.QLineEdit(self.centralwidget)
        self.box_inches.setGeometry(QtCore.QRect(220, 430, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.box_inches.setFont(font)
        self.box_inches.setObjectName("box_inches")

        self.box_name = QtWidgets.QLineEdit(self.centralwidget)
        self.box_name.setGeometry(QtCore.QRect(152, 84, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.box_name.setFont(font)
        self.box_name.setObjectName("box_name")

        self.box_age = QtWidgets.QSpinBox(self.centralwidget)
        self.box_age.setGeometry(QtCore.QRect(152, 187, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.box_age.setFont(font)
        self.box_age.setObjectName("box_age")

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(60, 90, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")

        self.label_age = QtWidgets.QLabel(self.centralwidget)
        self.label_age.setGeometry(QtCore.QRect(80, 180, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_age.setFont(font)
        self.label_age.setObjectName("label_age")

        self.label_sex = QtWidgets.QLabel(self.centralwidget)
        self.label_sex.setGeometry(QtCore.QRect(80, 290, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_sex.setFont(font)
        self.label_sex.setObjectName("label_sex")

        # Weight Label
        self.label_weight = QtWidgets.QLabel(self.centralwidget)
        self.label_weight.setGeometry(QtCore.QRect(80, 510, 60, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_weight.setFont(font)
        self.label_weight.setObjectName("label_weight")

        self.box_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.box_weight.setGeometry(QtCore.QRect(150, 510, 71, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.box_weight.setFont(font)
        self.box_weight.setObjectName("box_weight")

        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(90, 590, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName("btn_clear")

        # Instance when the button clear is clicked
        self.btn_clear.clicked.connect(self.clear_all)

        self.label_height = QtWidgets.QLabel(self.centralwidget)
        self.label_height.setGeometry(QtCore.QRect(80, 415, 55, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_height.setFont(font)
        self.label_height.setObjectName("label_height")

        createProfile.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(createProfile)
        self.statusbar.setObjectName("statusbar")
        createProfile.setStatusBar(self.statusbar)

        self.retranslateUi(createProfile)
        QtCore.QMetaObject.connectSlotsByName(createProfile)

    def retranslateUi(self, createProfile):
        _translate = QtCore.QCoreApplication.translate
        createProfile.setWindowTitle(_translate("createProfile", "MainWindow"))
        self.btn_create.setText(_translate("createProfile", "Create"))
        self.rad_male.setText(_translate("createProfile", "Male"))
        self.label_name.setText(_translate("createProfile", "Name:"))
        self.label_age.setText(_translate("createProfile", "Age:"))
        self.label_sex.setText(_translate("createProfile", "Sex:"))
        self.rad_female.setText(_translate("createProfile", "Female"))
        self.btn_clear.setText(_translate("createProfile", "Clear"))
        self.label_height.setText(_translate("createProfile", "Height:"))
        self.label_weight.setText(_translate("createProfile", "Weight:"))
        
    # Opens confirmation window
    def confirm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profile_created()
        self.ui.setupUi(self.window)
        self.window.show()

    def confirm2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_profile_createdpy()
        self.ui.setupUi(self.window)
        self.window.show()

    # Method to check if a field in registration is missing
    def isMissing(self):
        fields = [
            {'name': 'Name', 'widget': self.box_name},
            {'name': 'Age', 'widget': self.box_age},
            {'name': 'sex', 'widget': None},
            {'name': 'Feet', 'widget': self.box_feet},
            {'name': 'Inches', 'widget': self.box_inches},
            {'name': 'Weight', 'widget': self.box_weight}  # Added weight field
        ]

        for field in fields:
            if field['widget'] is None:
                if not self.rad_male.isChecked() and not self.rad_female.isChecked():
                    return True
            elif field['widget'].text().strip() == '':
                return True

        return False

    # Event when Submit button is clicked
    def show_line(self):
        try:
            #Code to cehck if json file reaches 4 max profiles.
            def create_json_file(data, directory, base_file_name, counter=1):
                # Create a Path object for the directory
                path = Path(directory)
                
                # Check if the file already exists and the limit is not reached
                file_name = base_file_name if counter == 1 else f"{base_file_name}_{counter}"
                file_path = path / f"{file_name}.json"
                
                if file_path.exists():
                    if counter == 4:
                        print("Limit reached")
                        self.confirm2()
                        return
                    else:
                        return create_json_file(data, directory, base_file_name, counter + 1)
                
                # Convert data to JSON string
                json_string = json.dumps(data, indent=4)
                
                # Write the JSON string to the file
                with open(file_path, 'w') as f:
                    f.write(json_string)
                
                print(f"File '{file_name}.json' created successfully.")
                return

            # Nested function to convert ft to cm
            def convert_to_cm(feet, inches):
                total_inches = feet * 12 + inches
                cm = total_inches * 2.54
                return cm

            if self.isMissing():
                print("MISSING VALUE")
            else:
                print("VALID")

            name = self.box_name.text()
            print(name)

            age = self.box_age.value()
            print(age)

            sex = ""
            if self.rad_male.isChecked():
                sex = "M"
                print("Male")
            elif self.rad_female.isChecked():
                sex ="F"
                print("Female")

            #Used textboxes because of the aestethic.
            #converts string into an int variable
            #converts feet to cm.
            feet = int(self.box_feet.text())
            inches = int(self.box_inches.text())
            result = convert_to_cm(feet, inches) #result is height.
            print(result)

            #Converts String Weight into a float
            weight = float(self.box_weight.text())  # Added weight field
            print(weight)

            QtWidgets.QMessageBox.information(None, 'Success', 'Profile Created!')
            #self.confirm() #Pops up window for confi

            ###THE NEXT FF. Lines is about JSON dictionaries.

            # Specify the file path where the JSON file should be saved
            base_file_name = "mydata"
            directory = "profiles"

            #Dictionary for json:
            mydict = {
                "status": "None",
                "info": {
                    "name": name,
                    "age": age,
                    "sex": sex,
                    "height": result,
                    "weight": weight
                },
                "workout_data": {

                }
            }
            
            # Write the JSON string to the file
            create_json_file(mydict, directory, base_file_name)


        except:
            #Except if error, prints out a red message.
            error_label = QtWidgets.QLabel(self.centralwidget)
            error_label.setGeometry(QtCore.QRect(60, 650, 300, 30))
            font = QtGui.QFont("Arial", 12)
            font.setPointSize(10)
            font.setBold(True)
            error_label.setFont(font)
            error_label.setStyleSheet("color: red")
            error_label.setText("Missing Requirements or Invalid Input")
            error_label.adjustSize()
            error_label.show()

            #Prints the error in terminal and clears all input.
            print("int values only")
            self.clear_all()
    
    #Method to clear all content from boxes
    def clear_all(self):
        self.box_name.clear()
        self.box_age.clear()
        self.box_feet.clear()
        self.box_inches.clear()
        self.box_weight.clear() 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createProfile = QtWidgets.QMainWindow()
    ui = Ui_createProfile()
    ui.setupUi(createProfile)
    createProfile.show()
    sys.exit(app.exec_())