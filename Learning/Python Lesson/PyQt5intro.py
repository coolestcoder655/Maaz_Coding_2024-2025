import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Sigma-est GUI")
        self.setGeometry(1500, 400, 500, 500)
        self.setWindowIcon(QIcon("GUI_Icon.png"))
        # self.checkBox = QCheckBox("Do you like food?", self)
        # self.button = QPushButton("Click Me. Now.", self)
        
        self.initUI()
    
    def initUI(self):



        """
        self.checkBox.setGeometry(10, 0, 500, 100)
        self.checkBox.setStyleSheet("font-size: 30px; font-family: Arial")
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.checkBoxChanged)
    
    def checkBoxChanged(self, state):
        if state == Qt.Checked:
            print("You Like Food.")
        else:
            print("You Don't Like Food.")


        
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px")
        self.button.clicked.connect(self.onClick)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px")
        
    def onClick(self):


        self.label.setText("Goodbye!")
        self.button.setDisabled(True)
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)



        """
        label = QLabel("100", self)
        label.setStyleSheet("color: #292929;" "background-color: red;")
        """
        hbox = QGridLayout()

        hbox.addWidget(label1, 0, 0)
        hbox.addWidget(label2, 0, 1)
        hbox.addWidget(label3, 1, 0)
        hbox.addWidget(label4, 1, 1)
        hbox.addWidget(label5, 1, 2)

        centralWidget.setLayout(hbox)

        
        
        picLabel = QLabel(self)
        picLabel.setGeometry(0, 0, 250, 250)
        picLabel.setScaledContents(True)

        pixmap = QPixmap("GUI_Icon.png")
        picLabel.setPixmap(pixmap)

        picLabel.setGeometry((self.width() - picLabel.width()) // 2,
                            (self.height() - picLabel.height()) // 2,
                            picLabel.width(), 
                            picLabel.height())

          label.setAlignment(Qt.AlignTop)   TOP
          label.setAlignment(Qt.AlignBottom)   BOTTOM
          label.setAlignment(Qt.AlignVCenter)   CENTER

          label.setAlignment(Qt.AlignRight)   HORIZONTALLY RIGHT
          label.setAlignment(Qt.AlignHCenter)   HORIZONTALLY CENTER
          label.setAlignment(Qt.AlignLeft)   HORIZONTALLY LEFT

          label.setAlignment(Qt.AlignHCenter | Qt. AlignTop)   CENTER and TOP
          label.setAlignment(Qt.AlignHCenter | Qt. AlignBottom)   CENTER and BOTTOM
          label.setAlignment(Qt.AlignHCenter | Qt. AlignVCenter)   CENTER and CENTER
          label.setAlignment(Qt.AlignCenter)   CENTER and CENTER
        """
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()