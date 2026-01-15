from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QComboBox
import pandas as pd
import numpy as np

class MainWind(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(950, 450)

        self.table = QTableWidget()

        self.btn_load = QPushButton("Load Data")
        self.btn_save = QPushButton("Save CSV")

        self.filter_box = QComboBox()
        self.filter_box.addItems(["All", "Chest", "Back", "Legs", "Shoulders", "Arms", "Full Body"])

        self.sort_box = QComboBox()
        self.sort_box.addItems(["Default", "Weight Ascending", "Weight Descending"])
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.btn_load)
        layout.addWidget(self.filter_box)
        layout.addWidget(self.sort_box)
        layout.addWidget(self.btn_save)
        self.setLayout(layout)

        self.df = self.read_data()
        self.df_view = self.df.copy()

        self.btn_load.clicked.connect(self.load_data)
        self.filter_box.currentTextChanged.connect(self.load_data)
        self.sort_box.currentTextChanged.connect(self.load_data)
        self.btn_save.clicked.connect(self.save_data)

    def read_data(self):
        df = pd.read_csv("gym_log.csv")
        df["TotalWeight"] = df["Sets"] * df["Reps"] * df["Weight"]
        return df

    def load_data(self):
        df_view = self.df.copy()
        filter_choice = self.filter_box.currentText()
        if filter_choice != "All":
            df_view = df_view[df_view["Muscle"] == filter_choice]

        sort_choice = self.sort_box.currentText().lower()
        if "asc" in sort_choice:
            df_view = df_view.sort_values("Weight", ascending=True)
        elif "desc" in sort_choice:
            df_view = df_view.sort_values("Weight", ascending=False)

        self.df_view = df_view.copy()

        self.table.clear()
        self.table.setRowCount(df_view.shape[0])
        self.table.setColumnCount(df_view.shape[1])
        self.table.setHorizontalHeaderLabels(df_view.columns)

        for i in range(df_view.shape[0]):
            for j in range(df_view.shape[1]):
                value = str(df_view.iloc[i, j])
                self.table.setItem(i, j, QTableWidgetItem(value))

    def save_data(self):
        name = self.filter_box.currentText()
        self.df_view.to_csv(f"{name}.csv", index=False)
        print("Saved filtered & sorted data to filtered_sorted_gym_log.csv")


app = QApplication([])
wind = MainWind()
wind.show()
app.exec_()
