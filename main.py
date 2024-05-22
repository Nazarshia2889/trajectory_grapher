import plotly.graph_objects as go
import numpy as np
import math
import streamlit as st

st.title("Differential Equations Trajectory Grapher")

st.text("Arshia Nayebnazar, Nathan Dai")
st.text("This app graphs the trajectories of a system of differential equations.")
st.text("Play around with the initial conditions to see how the trajectories change.")

n_trajectories = st.slider("Number of Trajectories", 1, 20, 1)

a = np.array([[1, -1],
              [2, 1]])

step = 360/n_trajectories
angle = 0
initial_conditions = []

while angle <= 360:
  radians = angle * (math.pi / 180)
  initial_conditions.append([math.cos(radians), math.sin(radians)])
  angle += step

data = []
for b in initial_conditions:
  x = np.linalg.solve(a, b)
  t = np.arange(-5, 5, 0.01)
  x1 =  x[0] * np.exp(-0.5*t) + x[1] * np.exp(-2 * t)
  x2 =  x[0] *np.exp(-0.5*t) - x[1] * np.exp(-2 * t)
  data.append(go.Scatter(x = x1, y = x2))

f1 = go.Figure(
    data,
    layout = {"xaxis": {"title": "x1"}, "yaxis": {"title": "x2"}, "title": "Trajectories"}
)
f1.update_xaxes(range=[-5, 5])
f1.update_yaxes(range=[-5, 5])

placeholder = st.empty()
placeholder.plotly_chart(f1)