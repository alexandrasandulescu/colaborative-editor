import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt, pyqtSlot, SIGNAL, SLOT

import string

alpha_numeric = string.ascii_letters + string.digits + string.punctuation
alpha_numeric_ord = [ord(x) for x in alpha_numeric]

class CustomEdit(QtGui.QTextEdit):
    #@pyqtSlot()
    #def slotTextChanged(self):
    #    print('new text is : ' + self.toPlainText())
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace:
            print('del')
            pass
        else:
            print(str(event.text()))
        super().keyPressEvent(event)

class CustomWindow(QtGui.QMainWindow):

    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.initUI()

    def initUI(self):
        self.text = CustomEdit(self)
        self.setCentralWidget(self.text)

        # x and y coordinates on the screen, width, height
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("VasyEdit.eu")

        #self.text.connect(self.text, SIGNAL("textChanged()"),
        #        self.text, SLOT("slotTextChanged()"))

def start_ui(queue):
    app = QtGui.QApplication(sys.argv)
    win = CustomWindow()
    win.show()
    sys.exit(app.exec_())
