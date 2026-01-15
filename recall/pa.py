import numpy as np
import pandas as pd
# df = pd.DataFrame([[1,2,3],[4,5,6], [7,8,9]], columns=['A', 'B', 'C'])
# print(df.head())
# df = pd.DataFrame([["Alice", 20, 85], ["Bob", 22, 54], ["Charlie", 21, 85]], columns=["Name", "Age", "Score"])
# print(df[["Name", "Score"]])
# print(df["Score"].mean())
# print(df[df["Score"]>80])
# df["Passed"] = df["Score"] >= 80
# print(df)

df = pd.read_csv("students.csv")
# print(df)
# # df.to_csv("output.csv", index=False)
# # df[df["Score"]<80].to_csv("Failed.csv", index=False)
# print(df[["Name", "Major", "Score"]])
print(df.shape)
print(df.columns)
# print(df["Score"].mean())
# print(df["Score"].max())
# print(df["HoursStudied"].mean())
# print(df[df["Score"]>=80])
# print(df[df["Major"]=="CS"])
# print(df[(df["Major"]=="Math") & (df["HoursStudied"]>5)])
df["Passed"] = df["Score"]>=70
df["HardWorker"] = df["HoursStudied"]>=10
# print(df)
# print(df[(df["Passed"])&(df["HardWorker"])])
df[df["Passed"]].to_csv("Passed.csv", index=False)
df[df["Major"]=="CS"].to_csv("CS_Majors.csv", index=False)
# print(df)
# print(df.sort_values(["Score"], ascending=False))
# print(df["Age"])

df["AgeGroup"] = np.where(df["Age"]>20, "Adult", "Young")
avg = df.groupby("AgeGroup")["Score"].mean()
print(avg)
print(df[df["Score"]>avg]["Name"])
