from PyQt5.QtWidgets import QApplication, QWidget
from matplotlib import pyplot as plt
#
# class MainWindow(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.resize(650,400)
# app = QApplication
#
# window = MainWindow()
# window.show()
# app.exec_()

import pandas as pd
import numpy as np

weeks = np.arange(1, 17)  # Week 1 to 16
exercise = "Bench Press"

weights = 50 + np.cumsum(np.random.randint(1, 3, size=len(weeks)))

reps = 8 + np.random.randint(-1, 2, size=len(weeks))

df = pd.DataFrame({
    "Week": weeks,
    "Exercise": [exercise]*len(weeks),
    "Weight": weights,
    "Reps": reps
})

df["TotalWeight"] = df["Weight"] * df["Reps"]


df.to_csv("data.csv", index=False)

x = df["Week"].values
y = df["Weight"].values

# Fit a line (degree=1)
slope, intercept = np.polyfit(x, y, 1)

# Predict next week
next_week = x[-1] + 1
predicted_weight = slope * next_week + intercept

# --- Plot ---
plt.figure(figsize=(8,5))
plt.plot(x, y, 'o-', label="Actual Weight")
plt.plot(next_week, predicted_weight, 'rx', markersize=10, label=f"Predicted Week {next_week}")
plt.xlabel("Week")
plt.ylabel("Weight (kg)")
plt.title(f"{exercise} Progress Over 16 Weeks")
plt.legend()
plt.grid(True)
plt.show()