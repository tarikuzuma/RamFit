import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        self.button = QPushButton("Open Other Window", self)
        self.button.setGeometry(50, 50, 200, 50)
        self.button.clicked.connect(self.open_other_window)

    def open_other_window(self):
        self.hide()  # Hide the current main window

        other_window = OtherWindow()
        other_window.show()

class OtherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Other Window")

        self.button = QPushButton("Back to Main Window", self)
        self.button.setGeometry(50, 50, 200, 50)
        self.button.clicked.connect(self.back_to_main_window)

    def back_to_main_window(self):
        self.hide()  # Hide the current window

        main_window = MainWindow()
        main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
