import pandas as pd
import plotly.express as px

df = pd.read_csv('covid_stats_csv.csv')
print(df)

fig = px.scatter(x=df.date, y=df.cases, color=df.country)
fig.show()
