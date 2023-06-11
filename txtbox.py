from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
import sys

class lineEditDemo(QWidget):
        def __init__(self,parent=None):
                super().__init__(parent)
                def txt(self):
                    
                    e4 = QLineEdit()
                    e4.textChanged.connect(self.textchanged)
                    flo = QFormLayout()

                    flo.addRow("Text changed",e4)
                    
                    self.setLayout(flo)
                    self.setWindowTitle("QLineEdit Example")

        def textchanged(self,text):
                print("Changed: " + text)


if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = lineEditDemo()
        win.show()
        sys.exit(app.exec_())
        
