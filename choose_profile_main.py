from choose_profile import Ui_choose_profile
from PyQt5 import QtCore, QtGui, QtWidgets
import json

#Back-end for choose_profile.py
class chooseProfile(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        #Set up the UI from Ui_choose_profile
        self.ui = Ui_choose_profile()
        self.ui.setupUi(self)

        #Get name from read_profile.
        #Profile[number] gets the name data from "name_number[i]" and then prints it to button.
        name_numbers = self.read_profile()
        profile1 = name_numbers.get("name_number1", "None")
        profile2 = name_numbers.get("name_number2", "None")
        profile3 = name_numbers.get("name_number3", "None")
        profile4 = name_numbers.get("name_number4", "None")
        
        #Set the button labels depending on name of JSON File
        self.ui.pushButton.setText(profile1)
        self.ui.pushButton_2.setText(profile2)
        self.ui.pushButton_3.setText(profile3)
        self.ui.pushButton_4.setText(profile4)
        
        #Connect the button clicked signals to slots
        self.ui.pushButton.clicked.connect(lambda: self.handle_button_click(name_numbers.get("name_number1"), 1))
        self.ui.pushButton_2.clicked.connect(lambda: self.handle_button_click(name_numbers.get("name_number2"), 2))
        self.ui.pushButton_3.clicked.connect(lambda: self.handle_button_click(name_numbers.get("name_number3"), 3))
        self.ui.pushButton_4.clicked.connect(lambda: self.handle_button_click(name_numbers.get("name_number4"), 4))

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
    def handle_button_click(self, index, button_address):
        print(f"Button: {index} clicked")

        #If statemetns to check what button address was pressed. 
        try:
            if button_address == 1:
                self.edit_status(1)
                print("EDIT 1")
            elif button_address == 2:
                self.edit_status(2)
                print("EDIT 2")
            elif button_address == 3:
                self.edit_status(3)
                print("EDIT 3")
            elif button_address == 4:
                self.edit_status(4)
                print("EDIT 4")

        #Except if error, print message in terminal.
        except FileNotFoundError:
            print("File does not exist.")
        

if __name__ == "__main__":
    import sys
    print ("TEST1")

    for i in range(1,5):
        try:
            file_path = f"profiles/mydata{i}.json"
            with open(file_path, 'r') as f:
                json_object = json.load(f)
                theme = json_object['status']

                json_object['status'] = 'None'

                with open(file_path, 'w') as f:
                    json.dump(json_object, f, indent = 4)
        except FileNotFoundError:
            continue

    app = QtWidgets.QApplication(sys.argv)
    choose_profile = chooseProfile()
    choose_profile.show()
    sys.exit(app.exec_())