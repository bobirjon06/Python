from itertools import product

from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QPushButton, QTableWidget, \
    QTableWidgetItem, QGroupBox, QSpinBox, QComboBox
import pandas as pd
import numpy as np

class MainWind(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resize(950, 450)
        self.lst = QTableWidget()
        dt = self.read_data()
        self.lst.setRowCount(dt.shape[0])
        self.lst.setColumnCount(dt.shape[1])
        self.lst.setHorizontalHeaderLabels(dt.columns)
        self.btn = QPushButton("Load All")
        self.grp = QComboBox()
        self.grp.addItems(["All", "Chest", "Back", "Legs", "Shoulders", "Arms", "Full Body"])
        self.btn.clicked.connect(self.load_data)
        v = QVBoxLayout()
        v.addWidget(self.lst)
        v.addWidget(self.btn)
        v.addWidget(self.grp)
        self.setLayout(v)
    def read_data(self):
        df = pd.read_csv("gym_log.csv")
        nums = df[["Sets", "Reps", "Weight"]]
        arr = nums.to_numpy()
        totals = np.prod(arr, axis=1)
        df["TotalWeight"] = totals
        return df
    def load_data(self):
        df = self.read_data()
        self.lst.clear()
        self.lst.setRowCount(df.shape[0])
        self.lst.setColumnCount(df.shape[1])
        self.lst.setHorizontalHeaderLabels(df.columns)
        if self.grp.currentText()=="All":
            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                    # print("===")
                    value = str(df.iloc[i, j])
                    self.lst.setItem(i,j,QTableWidgetItem(value))
                    # print("===")
                    # print(df.loc[i][j])
        else:
            df1 = df[df["Muscle"]==self.grp.currentText()]
            for i in range(df1.shape[0]):
                for j in range(df1.shape[1]):
                    # if df.iloc[i]["Muscle"]==self.grp.currentText():
                        value = str(df.iloc[i, j])
                        self.lst.setItem(i,j,QTableWidgetItem(value))
app = QApplication([])
wind = MainWind()
wind.show()
app.exec_()
