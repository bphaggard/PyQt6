from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Button Example")

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Sanserif", 15))
        #line_edit.setText("Default text")
        #line_edit.setPlaceholderText("Enter your name")
        #line_edit.setEnabled(False)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password) #zobrazí tečky místo textu



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())