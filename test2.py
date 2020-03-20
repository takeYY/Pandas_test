import pandas as pd

df = pd.read_csv("./game1.csv")

rename_df = df.rename(columns = {"cellphone":"device_type"})

formatted_df = rename_df.dropna().reset_index(drop=True)

print(formatted_df)

formatted_df.to_csv("game1_formatted.csv",index=False)