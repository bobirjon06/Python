import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form")
        self.setGeometry(650, 50, 700, 1000)
        self.setWindowIcon(QIcon("../images.jpg"))

        label = QLabel("Enter", self)
        label.setFont(QFont("Arial", 20))
        label.setGeometry(0,0,500,1000)
        label.setStyleSheet("color: black;"
                            "background-color: grey;"
                            "font-style:italic;")
        # label.setAlignment(Qt.AlignTop)
        # label.setAlignment(Qt.AlignHCenter)
        # label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        label.setAlignment(Qt.AlignCenter)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
