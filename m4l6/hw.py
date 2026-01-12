from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QRadioButton, QGroupBox, QHBoxLayout, QGridLayout, \
    QVBoxLayout


class MainWind(QWidget):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(500,500)
        label_name = QLabel("Ism:")
        self.line_name = QLineEdit()
        self.line_name.setPlaceholderText("Ism")
        label_login = QLabel("Login:")
        self.line_login = QLineEdit()
        self.line_login.setPlaceholderText("Login")
        label_pass = QLabel("Parol")
        self.line_pass = QLineEdit()
        self.line_pass.setPlaceholderText("Parol")
        self.group_gen = QGroupBox("Jinsi")
        h = QHBoxLayout()
        self.rbtn_male = QRadioButton("Erkak")
        self.rbtn_female = QRadioButton("Ayol")
        v = QVBoxLayout()
        v.addWidget(label_name)
        v.addWidget(self.line_name)
        v.addWidget(label_login)
        v.addWidget(self.line_login)
        v.addWidget(label_pass)
        v.addWidget(self.line_pass)
        h.addWidget(self.rbtn_male)
        h.addWidget(self.rbtn_female)
        v.addLayout(h)
        self.group_gen.setLayout(h)
        self.setLayout(v)
app = QApplication([])

wind = MainWind()

wind.show()

app.exec_()