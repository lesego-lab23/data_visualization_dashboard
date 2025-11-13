# callbacks.py
from dash import Input, Output
import plotly.express as px

def register_callbacks(app, df):
    @app.callback(
        [
            Output("avg-price", "children"),
            Output("avg-mileage", "children"),
            Output("avg-year", "children"),
            Output("avg-price-brand", "figure"),
            Output("price-vs-mileage", "figure"),
            Output("price-dist", "figure"),
        ],
        [
            Input("brand-filter", "value"),
            Input("fuel-filter", "value"),
            Input("transmission-filter", "value")
        ]
    )
    def update_dashboard(selected_brands, selected_fuel, selected_transmission):
        filtered_df = df.copy()

        if selected_brands:
            filtered_df = filtered_df[filtered_df['Brand'].isin(selected_brands)]
        if selected_fuel:
            filtered_df = filtered_df[filtered_df['Fuel Type'].isin(selected_fuel)]
        if selected_transmission:
            filtered_df = filtered_df[filtered_df['Transmission'].isin(selected_transmission)]

        # KPIs
        avg_price = f"${filtered_df['Price'].mean():,.0f}"
        avg_mileage = f"{filtered_df['Mileage'].mean():,.0f} km"
        avg_year = f"{filtered_df['Year'].mean():.0f}"

        # Graphs
        fig1 = px.bar(
            filtered_df.groupby('Brand')['Price'].mean().reset_index(),
            x='Brand', y='Price', color='Brand', title="Average Price by Brand"
        )

        fig2 = px.scatter(
            filtered_df, x='Mileage', y='Price', color='Brand',
            hover_data=['Model', 'Year'], title="Price vs Mileage by Brand"
        )

        fig3 = px.histogram(filtered_df, x='Price', nbins=30, title="Distribution of Car Prices")

        return avg_price, avg_mileage, avg_year, fig1, fig2, fig3
