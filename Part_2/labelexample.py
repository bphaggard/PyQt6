from PyQt6.QtGui import QFont, QPixmap, QMovie
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)

        '''
        self.setWindowTitle("Python GUI Development")

        label = QLabel("Python GUI Development", self)
        #label.setText("New Text is here")
        label.move(100, 100) #pozice textu
        label.setFont(QFont("Sanserif", 15))
        label.setStyleSheet("color:red")
        
        label.setNum(33) #zobrazí místo textu číslo
        label.clear() #vyčistí label, nic se nezobrazí
        '''

        '''
        label = QLabel(self)
        pixmap = QPixmap("images/python.png") #zobrazí obrázek
        label.setPixmap(pixmap)
        '''

        label = QLabel(self)
        movie = QMovie("images/hacker.gif")
        #movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())