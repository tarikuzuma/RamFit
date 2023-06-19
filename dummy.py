from PyQt5 import QtCore, QtGui, QtWidgets

class CustomModel(QtCore.QAbstractListModel):
    def __init__(self, data, parent=None):
        super(CustomModel, self).__init__(parent)
        self.data = data

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.data)

    def data(self, index, role):
        if not index.isValid():
            return None

        if role == QtCore.Qt.DisplayRole:
            return self.data[index.row()].text
        elif role == QtCore.Qt.DecorationRole:
            return self.data[index.row()].image

        return None

class ListItem:
    def __init__(self, text, image):
        self.text = text
        self.image = image

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.list_view = QtWidgets.QListView(self)
        self.setCentralWidget(self.list_view)

        items = [
            ListItem("Item 1", QtGui.QIcon("image1.png")),
            ListItem("Item 2", QtGui.QIcon("image2.png")),
            ListItem("Item 3", QtGui.QIcon("image3.png")),
        ]

        model = CustomModel(items)
        self.list_view.setModel(model)

        delegate = QtWidgets.QStyledItemDelegate(self.list_view)
        self.list_view.setItemDelegate(delegate)

        self.setWindowTitle("ListView with Images")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
