from PyQt5 import QtWidgets

class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle("event_test")
        self.statusBar = self.statusBar()
        self.setMouseTracking(True)
        self.setGeometry(300,300,200,200)
        self.resize(1000,800)
        self.show()
    def keyPressEvent(self, e):
        output = "Press key : {}".format(e.key())
        self.statusBar.showMessage(output)
    def keyReleaseEvent(self,e):
        output = "Out key : {}".format(e.key())
        self.statusBar.showMessage(output)
    def mouseDoubleClickEvent(self, e):
        button = e.button()
        x=e.x()
        y=e.y()
        gx=e.globalX()
        gy=e.globalY()
        output = "Double clicked : {}, x={}, y={}, gx={}, gy={}".format(button,x,y,gx,gy)
        self.statusBar.showMessage(output)

    def mouseMoveEvent(self,e):
        x=e.x()
        y=e.y()
        gx=e.globalX()
        gy=e.globalY()
        output = "Mouse move : x={}, y={}, gx={}, gy={}".format(x,y,gx,gy)
        self.statusBar.showMessage(output)
    def mouseGrabber

app=QtWidgets.QApplication([])
ex=MyApp()
app.exec_()
