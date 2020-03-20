import pandas as pd

class_df = pd.read_csv("./class.csv")
grade_df = pd.read_csv("./grade.csv")

class_grade = pd.merge(class_df,grade_df,on=["student_number","name"],how="inner")
class_grade = class_grade.reset_index(drop=True)


print(class_grade)

class_grade.to_csv("class_grade.csv",index=False)