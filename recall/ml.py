import pandas as pd
from scipy.stats import alpha
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("gym_log.csv")
df["HighVolume"] = df["Sets"]*df['Reps']
# print(df['HighVolume'])
x = df[["Sets", "Reps", "Weight"]]
y = df["HighVolume"]

x_train, x_test, y_train, y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)

model = LinearRegression()

model.fit(x_train, y_train)


# print(model.coef_)
# print(model.intercept_)

y_pred = model.predict(x_test)
# print(y_pred[:5])
# print(pd.DataFrame({"A":y_test, "P":y_pred}))

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

r2 = model.score(x_test, y_test)
# print(mae, mse, r2)

plt.figure(figsize=(6,6))
plt.scatter(y_test, y_pred, color='blue', label="Predictions")

plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color='red',linestyle='--', label='perfect fit')

plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("smth")
plt.legend()

# plt.show()

x_simple = df[["Sets", "Reps"]]

x_train_s, x_test_s, y_train_s, y_test_s = train_test_split(
    x_simple, y, test_size=0.2, random_state=42
)

model_simple = LinearRegression()
model_simple.fit(x_train_s, y_train_s)

y_pred_s = model_simple.predict(x_test_s)

maes = mean_absolute_error(y_test_s, y_pred_s)
mses = mean_squared_error(y_test_s, y_pred_s)
r2s = model_simple.score(x_test_s, y_test_s)

plt.figure(figsize=(6,6))
plt.scatter(y_test_s, y_pred_s, color='green', label="Predictions")
plt.plot([y_test_s.min(), y_test_s.max()],
         [y_test_s.min(), y_test_s.max()],
         color='red', linestyle='--', label='Perfect fit'
)

plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.legend()
# plt.show()

# print(r2, r2s)

df["HighVolumeClass"] = (df['HighVolume']>=40).astype(int)

x = df[["Sets", "Reps"]]
y = df["HighVolumeClass"]

x_train, x_test, y_train, y_test = train_test_split(
    x,y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
# print(accuracy)

plt.figure(figsize=(6,6))

plt.scatter(
    x["Sets"],
    x['Reps'],
    c=y,
)

x_min, x_max = x["Sets"].min()-1,x['Sets'].max()+1
y_min, y_max = x['Reps'].min()-1, x['Reps'].max()+1

xx,yy = np.meshgrid(
    np.linspace(x_min, x_max, 200),
    np.linspace(y_min, y_max, 200)
)

grid = np.c_[xx.ravel(), yy.ravel()]
z = model.predict(grid)
z = z.reshape(xx.shape)

plt.contourf(xx,yy,z,alpha=0.3)

plt.xlabel("Sets")
plt.ylabel("Reps")
plt.title("Logistic")

plt.show()