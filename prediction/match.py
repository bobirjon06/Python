import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

barca = pd.read_csv("barca_matches.csv")


racing = pd.read_csv("racing_matches.csv")
# print(barca)
df = pd.DataFrame({
    "Home": barca['Home'],
    "Barca_goals": barca['Scored'],
    "Barca_conceded": barca['Conceded'],
    "Barca_form": barca['Form'],
    "Opponent_goals": racing['Scored'],
    "Opponent_conceded": racing['Conceded'],
    "Opponent_form": racing['Form'],
    "Outcome": barca['Form']
})

# df.to_csv("HeadToHead.csv", index=False)
df = pd.read_csv('HeadToHead.csv')

feature = ['Home', 'Barca_goals', 'Barca_conceded', 'Barca_form', 'Opponent_goals', 'Opponent_conceded', 'Opponent_form']
target = "Outcome"

x = df[feature]

y = df[target]

# print(x.head())
# print(y.head())

x_train, x_test, y_train, y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)
tonight = pd.DataFrame([{
    "Home": 1,             # Barca at home
    "Barca_goals": 3,     # goals in last match
    "Barca_conceded": 2,   # goals conceded in last match
    "Barca_form": 1,       # last match win = 1
    "Opponent_goals": 2,       # Racing last match goals
    "Opponent_conceded": 1,     # Racing last match conceded
    "Opponent_form": 0          # Racing last match not win
}])
model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

# print(y_pred)

proba = model.predict_proba(x_test)
# print(proba)


all_actual = list(y_test)+[None]
all_pred = list(y_pred)+list(model.predict(tonight))

plt.figure(figsize=(6,6))

plt.scatter(range(len(all_pred)-1), y_pred, color='blue', label="Past Predictions")
plt.scatter(len(all_pred)-1, all_pred[-1], color='green', label="Tonight Prediction", s=100)  # highlight tonight

plt.plot([0, len(all_pred)-1], [0,1], color='red', linestyle='--', label="Reference")

plt.xticks(range(len(all_pred)), labels=[f"Match {i+1}" for i in range(len(all_pred))], rotation=45)
plt.yticks([0,1], ["Not Win", "Win"])
plt.ylabel("Outcome")
plt.title("Barca Match Predictions")
plt.legend()
plt.tight_layout()
plt.show()