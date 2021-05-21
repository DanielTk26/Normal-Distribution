import plotly.figure_factory as ff
import pandas as pd 
import csv

df = pd.read_csv("data.csv")

figure = ff.create_ditsplot([df["Weight(Pounds)"].tolist()],["Weight"],show_dist = False)

figure.show()