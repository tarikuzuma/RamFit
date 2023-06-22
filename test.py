from PyQt5 import QtCore, QtGui, QtWidgets

class TimerWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timer")
        self.resize(400, 100)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setGeometry(QtCore.QRect(30, 30, 340, 30))

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100)  # Update interval in milliseconds
        self.timer.timeout.connect(self.update_progress)

        self.total_time = 10000  # Total time in milliseconds
        self.current_time = 0

    def start_timer(self):
        self.timer.start()

    def update_progress(self):
        self.current_time += self.timer.interval()
        progress = int((self.current_time / self.total_time) * 100)
        self.progress_bar.setValue(progress)

        if self.current_time >= self.total_time:
            self.timer.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = TimerWindow()
    window.show()
    window.start_timer()
    sys.exit(app.exec_())
