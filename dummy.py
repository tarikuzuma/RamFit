import sys
from PyQt5.QtWidgets import QInputDialog, QApplication, QWidget,  QGridLayout, QListWidget,  QPushButton
from PyQt5.QtGui import QIcon
import json

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('My Wish List')
        self.setWindowIcon(QIcon('./assets/wishlist.png'))
        self.setGeometry(100, 100, 400, 100)

        layout = QGridLayout(self)
        self.setLayout(layout)

        self.list_widget = QListWidget(self)
        self.list_widget.addItems([self.read_program()])
        layout.addWidget(self.list_widget, 0, 0, 4, 1)

        # create buttons
        add_button = QPushButton('Add')
        add_button.clicked.connect(self.add)

        insert_button = QPushButton('Insert')
        insert_button.clicked.connect(self.insert)

        remove_button = QPushButton('Remove')
        remove_button.clicked.connect(self.remove)

        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.clear)
        
        read_button = QPushButton('Read')
        read_button.clicked.connect(self.read_program)

        layout.addWidget(add_button, 0, 1)
        layout.addWidget(insert_button, 1, 1)
        layout.addWidget(remove_button, 2, 1)
        layout.addWidget(clear_button, 3, 1)
        layout.addWidget(read_button, 4, 1)

        # show the window
        self.show()

    def add(self):
        text, ok = QInputDialog.getText(self, 'Add a New Wish', 'New Wish:')
        if ok and text:
            self.list_widget.addItem(text)

    def insert(self):
        text, ok = QInputDialog.getText(self, 'Insert a New Wish', 'New Wish:')
        if ok and text:
            current_row = self.list_widget.currentRow()
            self.list_widget.insertItem(current_row+1, text)

    def remove(self):
        current_row = self.list_widget.currentRow()
        if current_row >= 0:
            current_item = self.list_widget.takeItem(current_row)
            del current_item

    def clear(self):
        self.list_widget.clear()

   #Debugging purposes. Check if difficulty and program is readable.
    def read_program(self):

        #List workout_names into the ListView
        workout_names = []
        filepath = None #Flag Case. File path of JSON. Example: "program_files/beginner/arms.json"
        workout_type = None #Flag Case. Type of workout. Example: "beginner_arms"

        difficulty = 1
        program = "arms"

        if difficulty == 1 and program =="arms":
            print("Beginners, arms day")
            workout_type = "beginner_arms"
            filepath = "program_files/beginner/arms.json"
        else:
            print("Unreadable")
            return

        print ("File path: ", filepath, " : ", workout_type)

        try:
            with open(filepath, "r") as f:
                json_object = json.load(f)
                #print ("\n",json_object,"\n") #To read what json read.
                workout = json_object[workout_type]

                #Print the name of each exercise in the workout
                for exercise in workout:
                    exercise_name = exercise["name"]
                    workout_names.append(exercise_name) #Appends exercises_name to workout_names list

        except FileNotFoundError:
            print("File not found:", filepath)

        except json.JSONDecodeError:
            print("Invalid JSON format in file:", filepath)

        print (*workout_names)

        self.list_widget.addItems([*workout_names])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())