# app.py
from dash import Dash
import dash_bootstrap_components as dbc
from data_loader import load_data
from layout import create_layout
from callbacks import register_callbacks


app = Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])
app.title = "Car Price Analysis Dashboard"

df = load_data()

app.layout = create_layout(df)

register_callbacks(app, df)

if __name__ == "__main__":
    app.run(debug=True)

