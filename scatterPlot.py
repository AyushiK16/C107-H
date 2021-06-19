import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('data.csv')

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

student = df.loc[df['student_id'] == 'TRL_imb']
print(student.groupby('level')['attempt'].mean())

graph = px.scatter(df, x='student_id', y = 'level', 
    size = 'attempt', color = 'level')

graph.show()