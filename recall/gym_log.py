import pandas as pd

df = pd.read_csv("gym_log.csv")
print(df.head())
print(df.tail(3))
print(df.shape)
print(df.columns)

print(df["Sets"].mean())
print(df["Reps"].max())
print(df["Weight"].mean())
print(df[df["Muscle"]=="Chest"]["Exercise"])
print(df[df["Sets"]>=4])
print(df[df["Weight"]>50])

high = df["HighVolume"] = df["Sets"]*df["Reps"]>=40
w = df["Weighted"] = df["Weight"]>0
print(df.head())

print(df[(df['HighVolume'])&(df['Weighted'])])
print(df[((df['Muscle']=='Back') | (df['Muscle']=="Legs"))&(df['Sets']>=4)])
print(df.sort_values(["Weight"], ascending=False))
print(df.sort_values(["Muscle", "Sets"], ascending=[True, False]))
df[high].to_csv("highvolume.csv", index=False)
df[w].to_csv("weighted.csv", index=False)
print(df.loc[df["Muscle"]=="Chest", ["Exercise", "Sets"]]
)