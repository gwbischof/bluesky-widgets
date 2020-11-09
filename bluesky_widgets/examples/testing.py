from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



class QThing(QWidget):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.searches = QtSearches(model)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QtSearches(model, parent=self))
        self.go_button = QPushButton("PUSH ME", self)
        self.go_button.clicked.connect(self.c)
        layout.addWidget(self.go_button)

    @pyqtSlot()
    def c(self):
        raise Exception("Intentional")

    
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def button_clicked(self):
        print("clicked")
        print(type(self))

    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Tech With Tim")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me!")
        self.b1.clicked.connect(self.button_clicked)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
