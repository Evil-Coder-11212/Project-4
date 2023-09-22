import pandas as pd
import plotly.express as px
import numpy

# My new method
df = pd.read_csv("./data.csv")
data = pd.DataFrame(df)
print(data.corr(method="kendall"))
