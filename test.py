import pandas as pd

df = pd.read_csv("./school.csv")

print(df)
print("=============================================================================")
df["weight"] = [29,31,33,28,29,31,27]

print(df)
print("=============================================================================")

df.to_csv('school_add_weight.csv',index=False)

df2 = pd.read_csv("./school_add_weight.csv")

print(df2)