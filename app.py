import csv
from dash import Dash, dcc, html
import plotly.express as px
import os


app = Dash(__name__)

data = []

with open("data/sample.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        
        row["value"] = float(row["value"])
        data.append(row)


x_values = [row["category"] for row in data]
y_values = [row["value"] for row in data]


fig = px.bar(
    x=x_values,
    y=y_values,
    labels={"x": "Category", "y": "Value"},
    title="Sample Dashboard Chart"
)

app.layout = html.Div([
    html.H1("Data Visualization Dashboard"),
    dcc.Graph(figure=fig)
])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host="0.0.0.0", port=port)
