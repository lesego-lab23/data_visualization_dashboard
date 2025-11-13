# layout.py
from dash import html, dcc
import dash_bootstrap_components as dbc

def create_layout(df):
    layout = dbc.Container([
        html.H1("Car Price Analysis Dashboard", className="text-center my-4 fw-bold"),
        html.P("Explore factors influencing car prices", className="text-center text-muted mb-5"),

        # Filters
        dbc.Row([
            dbc.Col([
                html.Label("Select Brand"),
                dcc.Dropdown(
                    id="brand-filter",
                    options=[{"label": b, "value": b} for b in sorted(df['Brand'].unique())],
                    multi=True,
                    placeholder="Filter by brand..."
                )
            ], width=4),

            dbc.Col([
                html.Label("Select Fuel Type"),
                dcc.Dropdown(
                    id="fuel-filter",
                    options=[{"label": f, "value": f} for f in sorted(df['Fuel Type'].unique())],
                    multi=True,
                    placeholder="Filter by fuel type..."
                )
            ], width=4),

            dbc.Col([
                html.Label("Select Transmission"),
                dcc.Dropdown(
                    id="transmission-filter",
                    options=[{"label": t, "value": t} for t in sorted(df['Transmission'].unique())],
                    multi=True,
                    placeholder="Filter by transmission..."
                )
            ], width=4),
        ], className="mb-4"),

        # KPI Cards
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Average Price", className="card-title text-center"),
                    html.H3(id="avg-price", className="text-center text-primary")
                ])
            ]), width=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Average Mileage", className="card-title text-center"),
                    html.H3(id="avg-mileage", className="text-center text-success")
                ])
            ]), width=4),

            dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5("Average Year", className="card-title text-center"),
                    html.H3(id="avg-year", className="text-center text-info")
                ])
            ]), width=4),
        ], className="mb-5"),

        # Graphs
        dbc.Row([
            dbc.Col(dcc.Graph(id="avg-price-brand"), width=6),
            dbc.Col(dcc.Graph(id="price-vs-mileage"), width=6),
        ]),
        dbc.Row([
            dbc.Col(dcc.Graph(id="price-dist"), width=12)
        ]),

        html.Hr(),
        html.P("📈 Insights: Adjust filters above to explore how different factors such as brand, fuel type, and transmission affect car pricing.",
               className="text-center text-muted mt-4")
    ])

    return layout
