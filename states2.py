from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-1', value='Montreal', type='text'),
    dcc.Input(id='input-2', value='Canada', type='text'),
    html.Button(id='botao1', children='Submit'),
    html.Div(id="number_output"),
])

@app.callback(
    Output('number_output', 'children'),
    Input('botao1', 'n_clicks'),
    State('input-1', 'value'),
    State('input-2', 'value'),)

def update_output(n_clicks,input1, input2):
    return f'Input 1 is: {input1}\nInput 2 is: {input2}'

if __name__ == '__main__':
    app.run_server(debug=True)

