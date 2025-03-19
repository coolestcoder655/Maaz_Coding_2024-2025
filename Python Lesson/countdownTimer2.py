import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Sigma-est GUI")
        self.setGeometry(1500, 400, 500, 500)
        self.setWindowIcon(QIcon("GUI_Icon.png"))
        self.label = QLabel("100", self)
        
        
        self.initUI()
    
    def initUI(self):

        
        self.label.setGeometry(200, 150, 150, 150)
        self.label.setStyleSheet("color: #292929; text-align: center; font-size: 40px")
        


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    myTime = int(input("How Many Seconds?"))

    for x in range(myTime, 0, -1):
        seconds = x % 60
        # minutes = int(x / 60) % 60
        # hours = int(x / 3600)
        window.label.setText(f"hours:02:minutes:02:{seconds:02}")
        time.sleep(1)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

