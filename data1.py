import pandas as pd
import plotly.express as pl
import csv

df = pd.read_csv("data.csv")
student = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()
print(student)

fig = pl.scatter(student,x = "student_id",y = "level",size = "attempt",color = "attempt")
fig.show()