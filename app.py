import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Maçã", "Banana", "Laranja", "Morango", "Abacaxi", "Uva", "Limão", "Pera", "Melancia", "Cereja"],
    "Amount": [20, 15, 30, 25, 10, 35, 18, 22, 27, 12],
    "City": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Porto Alegre", "Salvador", "Brasília", "Curitiba", "Fortaleza", "Recife", "Manaus"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City")

#=============================================================================
# LAYOUT
app.layout = html.Div(id="div1",
    children=[
        html.H1("Hello Dash", id="h1"),

        html.Div("Dash: o framework para construir aplicativos web"),

        dcc.Graph(figure=fig, id="graph")
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
