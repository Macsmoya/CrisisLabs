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
import alarm
alarm.triggerReset()
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
    
def _create_fig(channel, datapoints): #Create graph 
    df = get_dataframe(channel)
    currentDf = df.tail(datapoints)
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
                               figure=_create_fig("ENN", 1000)
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
                            html.Br(),
                            html.H5('Channel', className = "card-subtitle"),
                            dcc.Dropdown(
                                id = "channeldropdown",
                                options=[
                                    {'label': 'EHZ', 'value': 'EHZ'},
                                    {'label': 'ENZ', 'value': 'ENZ'},
                                    {'label': 'ENN', 'value': 'ENN'},
                                    {'label': 'ENE', 'value': 'ENE'},
                                ],
                                value='EHZ',
                                clearable=False,
                            ),
                            html.Br(),
                            html.H5('Update interval', className = "card-subtitle"),
                            dcc.Dropdown(
                                id = "updatedropdown",
                                options=[
                                    {'label': 'Never', 'value': '99999999'},
                                    {'label': 'Half a second', 'value': '500'},
                                    {'label': 'One second', 'value': '1000'},
                                ],
                                value='500',
                                clearable=False,
                            ),
                            
                            html.Br(),
                            html.H5('Number of datapoints', className = "card-subtitle"),
                            dcc.Slider(
                                id='range-slider',
                                min=10,
                                max=10000,
                                step=1,
                                value=1000,
                            ),
                            html.Div(id='slider-output-container'),
                            html.Br(),
                            html.H5('Threshold', className = "card-subtitle"),
                            dcc.Slider(
                                id='threshold-slider',
                                min=10,
                                max=10000000,
                                step=100,
                                value=3000000,
                            ),
                            html.Div(id='threshold-container'),
                            html.Br(),
                           
                        ]),
                        width =5,
                        className = "bg-light border border-dark"
                        ),
                    dbc.Col(
                        html.Div([
                            dcc.Textarea(
                                id='data-output',
                                disabled=True,
                                value='No data yet!',
                                style={'width': '100%', 'height': 400},
                            ),
                        ]),
                        width=2
                    ),
                    dbc.Col(
                        html.Div(id="alert-div"),
                        width=3,
                        className = "bg-light border border-dark"
                     ),
                ]),
                html.Br()
], className = "bg-secondary")

lastquake = []

@app.callback(
    dash.dependencies.Output('interval-component', 'interval'),
    [dash.dependencies.Input('updatedropdown', 'value')])
def refresh_update_speed(value):
    return int(value)

@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('range-slider', 'value')])
def update_output(value):
    return 'Currently selected: {}'.format(value)

@app.callback(
    dash.dependencies.Output('threshold-container', 'children'),
    [dash.dependencies.Input('threshold-slider', 'value')])
def update_output(value):
    return 'Currently selected: {}'.format(value)

last_quake = [20]
@app.callback(
    dash.dependencies.Output('bigGraph', 'figure'),
    dash.dependencies.Output('data-output', 'value'),
    dash.dependencies.Input('interval-component', 'n_intervals'),
    dash.dependencies.Input('range-slider', 'value'),
    dash.dependencies.Input('channeldropdown', 'value'),
    dash.dependencies.Input('threshold-slider', 'value')
    )
def refresh_data(n_clicks, datapoints, channel, threshold):
    last_packet = get_dataframe(channel).tail(25)
    time_since_quake = last_quake[0]
    for val in last_packet['y']:
        if abs(val) > threshold:
            alarm.triggerAlarm()
        else:
            alarm.triggerReset()
            
                
    return _create_fig(channel, datapoints), "      " + str(last_packet)[1:-1]

if __name__ == "__main__":
    app.run_server(host='127.0.0.1', debug=True, port=8040)
