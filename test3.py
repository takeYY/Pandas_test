import pandas as pd

df = pd.read_csv("./game2.csv")

drop_ranking_df = df.drop("ranking",axis=1)

fill_0_df = drop_ranking_df.fillna(0)

sort_df = fill_0_df.sort_values("billing_amount(¥)",ascending=False)

formatted_df = sort_df.reset_index(drop=True)

print(formatted_df)

formatted_df.to_csv("game2_formatted.csv",index=False)