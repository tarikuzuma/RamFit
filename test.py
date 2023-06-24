import sys
from PyQt5 import QtWidgets, QtGui, QtCore

class CalendarWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calendar Widget")
        self.resize(300, 200)

        # Create the calendar widget
        self.calendar = QtWidgets.QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.clicked[QtCore.QDate].connect(self.showWorkoutData)

        # Create a layout to hold the calendar widget
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.calendar)

    def showWorkoutData(self, date):
        # Get the selected date as a string
        selected_date = date.toString(QtCore.Qt.ISODate)

        # Perform some logic to retrieve the workout data for the selected date
        workout_data = self.getWorkoutData(selected_date)

        # Create a message box to display the workout data
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Number of Workout Data")
        msg.setText(f"Workout Data for {selected_date}:\n\n{workout_data}")
        msg.exec_()

    def getWorkoutData(self, selected_date):
        # Perform your logic here to retrieve the workout data for the selected date
        # This is just a placeholder, you should replace it with your actual data retrieval logic
        return "List of Workout Data"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = CalendarWidget()
    widget.show()
    sys.exit(app.exec_())
