import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.H1("Dash App 2", id="h1", style={"color": "blue"}),

        html.Div("Dash: o framework para construir aplicativos web"),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)