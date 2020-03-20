import pandas as pd

kanto = pd.read_csv("./kanto.csv")
kansai = pd.read_csv("./kansai.csv")

kanto_kansai = kanto.append(kansai)
kanto_kansai = kanto_kansai.reset_index(drop=True)

print(kanto_kansai)

kanto_kansai.to_csv("kanto_kansai.csv",index=False)