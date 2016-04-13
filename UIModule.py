import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

import string

#alpha_numeric = string.ascii_letters + string.digits + string.punctuation
alpha_numeric = string.printable
alpha_numeric_ord = [ord(x) for x in alpha_numeric]

class CustomEdit(QtGui.QTextEdit):
    def __init__(self, queue, parent=None):
        super(QtGui.QTextEdit, self).__init__(parent)
        self.queue = queue

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace:
            print('del')
            pass
        elif event.key() == QtCore.Qt.Key_Enter:
            print('enter')
        else:
            print(ord(event.text()))
            self.queue.put(ord(event.text()))
        super().keyPressEvent(event)

class CustomWindow(QtGui.QMainWindow):

    def __init__(self, queue, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.queue = queue
        self.initUI()

    def initUI(self):
        self.text = CustomEdit(self.queue, self)
        self.setCentralWidget(self.text)

        # x and y coordinates on the screen, width, height
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("VasyEdit.eu")


def start_ui(queue):
    app = QtGui.QApplication(sys.argv)
    win = CustomWindow(queue)
    win.show()
    sys.exit(app.exec_())
