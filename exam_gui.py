from PyQt5 import QtWidgets
from PyQt5 import QtCore

class MyWindows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Gui")
        self.resize(1920,1080)

        label1 = QtWidgets.QLabel("first label",self)
        label1.setAlignment(QtCore.Qt.AlignCenter)
        label1.resize(60,25)
        
        button = QtWidgets.QPushButton(self)
        button.setText("common button")

        button2 = QtWidgets.QPushButton(self)
        button2.setText("button signal")


        disalbeButton = QtWidgets.QPushButton(self)
        disalbeButton.setText("disable Button")
        disalbeButton.setEnabled(False)

        checkButton = QtWidgets.QPushButton(self)
        checkButton.setText("check Button")
        checkButton.setCheckable(True)
        checkButton.toggle()

        label2 = QtWidgets.QLabel("second label",self)
        label2.setAlignment(QtCore.Qt.AlignCenter)
        label2.setStyleSheet("color:red: font-size:20px:")

        button2.clicked.connect(self.button_clicked)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(button)
        layout.addWidget(disalbeButton)
        layout.addWidget(checkButton)
        layout.addWidget(button2)

        self.setLayout(layout)
        self.show()
    def button_clicked(self):
        send_testmessage = self.sender()
        QtWidgets.QMessageBox.about(self,"test",send_testmessage.text())

app = QtWidgets.QApplication([])
win = MyWindows()
app.exec_()