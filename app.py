import dash
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import csv
from dash_bootstrap_templates import load_figure_template
import layouts
import plotly.express as px
import math as maths
import time as t
load_figure_template("lux")
app = dash.Dash(
    __name__,
    update_title=None,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.LUX]
)


def get_dataframe(channel):
    df = pd.read_csv('data/' + channel + '.csv') #Read data from data.csv
    df.columns=['x','y']
    return df
    
def _create_fig(channel): #Create graph 
    df = get_dataframe(channel)
    currentDf = df.tail(1000)
    layout = go.Layout(
                        title = {
                                 'text':channel,
                                 'xanchor':'center'
                                },
                        xaxis = {
                                 'title':'Time'
                                },
                        yaxis = {
                                 'title':'Counts'
                                },
                        autosize = True
                       )
    return go.Figure(data=go.Scatter(
                                     x=currentDf['x'],
                                     y=currentDf['y'],
                                     ), 
                     layout = layout
                     )

interval = 1000

app.layout = html.Div([
                layouts.navbar,
                html.Br(),
                dbc.Row([
                    dbc.Col(html.Div(), width=1),
                    dbc.Col(
                        html.Div([
                            dcc.Graph(
                                id='bigGraph',
                               figure=_create_fig("ENN")
                            ),
                            dcc.Interval(
                                id='interval-component',
                                interval=1*interval, # in milliseconds
                                    n_intervals=0
                            ),
                        ]),
                        width =10,
                        className = "bg-light border border-dark"
                        )
                ]),
                html.Br(), 
                dbc.Row([
                    dbc.Col(html.Div(), width=1),
                    dbc.Col(
                        html.Div([
                            dcc.Graph(
                                id='g1',
                                figure=_create_fig("ENZ")
                            ),
                        ]),
                        width =5,
                        className = "bg-light border border-dark"
                        ),
                    dbc.Col(
                        html.Div([
                            dcc.Dropdown(
                                id = "updatedropdown",
                                options=[
                                    {'label': 'Never', 'value': '99999999'},
                                    {'label': 'Half a second', 'value': '500'},
                                    {'label': 'One second', 'value': '1000'},
                                ],
                                value='500',
                                clearable=False
                            ),
                            html.Br(),
                            dcc.Textarea(
                                id='data-output',
                                disabled=True,
                                value='No data yet!',
                                style={'width': '100%', 'height': 300},
                            )
                        ]),
                        width=5
                     ),
                ]),
                html.Br(),           
                dbc.Row([
                    dbc.Col(html.Div(), width=1),
                    dbc.Col(
                        html.Div(
                        ),
                        id = 'a',
                        width=5,
                        className = "bg-light border border-dark"
                    ),
                ]),
], className = "bg-secondary")


@app.callback(
    dash.dependencies.Output('interval-component', 'interval'),
    [dash.dependencies.Input('updatedropdown', 'value')])
def refresh_update_speed(value):
    return int(value)

lastquake = []
@app.callback(
    dash.dependencies.Output('bigGraph', 'figure'),
    dash.dependencies.Output('g1', 'figure'),
    dash.dependencies.Output('data-output', 'value'),
    dash.dependencies.Input('interval-component', 'n_intervals')
)

def refresh_data(n_clicks):
    last_packet = get_dataframe('EHZ').tail(25)
    for val in last_packet['y']:
        if val > 20000:
                lastquake.append(last_packet)
            
    return _create_fig('EHZ'), _create_fig('ENZ'), "  " + str(lastquake)[1:-1]

if __name__ == "__main__":
    app.run_server(host='127.0.0.1', debug=True, port=8050)
