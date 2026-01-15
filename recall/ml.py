import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


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

plt.show()