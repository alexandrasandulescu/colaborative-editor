import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, pyqtSlot, SIGNAL, SLOT


class CustomEdit(QtGui.QTextEdit):
    @pyqtSlot()
    def slotTextChanged(self):
        print('new text is : ' + self.toPlainText())

class Main(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.initUI()

    def initUI(self):
        self.text = CustomEdit(self)
        self.setCentralWidget(self.text)

        # x and y coordinates on the screen, width, height
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("VasyEdit.eu")

        self.text.connect(self.text, SIGNAL("textChanged()"),
                self.text, SLOT("slotTextChanged()"))

class UIModule():
    def main():
        app = QtGui.QApplication(sys.argv)
        main = Main()
        main.show()
        sys.exit(app.exec_())
