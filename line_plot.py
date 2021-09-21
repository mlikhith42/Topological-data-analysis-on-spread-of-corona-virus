import numpy as np
import pandas as pd
import seaborn as sns

sns.set()
data = pd.read_csv("state_total_final.csv")
mahaX = np.array(data["MH"])
apX = np.array(data["AP"])
tnX = np.array(data["TN"])
klX = np.array(data["KL"])
kaX = np.array(data["KA"])

y = np.array(data["Date"])


import plotly.express as px
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=y , y=mahaX,
                    mode='lines+markers',name='Maharashtra')
                )
fig.add_trace(go.Scatter(x=y , y=tnX,
                    mode='lines+markers',name='TamilNadu'))
fig.add_trace(go.Scatter(x=y , y=klX,
                    mode='lines+markers',name='Kerala'))
fig.add_trace(go.Scatter(x=y , y=kaX,
                    mode='lines+markers',name='Karnataka'))
fig.add_trace(go.Scatter(x=y , y=apX,
                    mode='lines+markers',name='Andhra Pradesh'))

fig.show()

