import dash
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import csv
from dash_bootstrap_templates import load_figure_template
import layouts
load_figure_template("lux")
app = dash.Dash(
    __name__,
    update_title=None,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.LUX]
)


def _create_fig(): #Create graph 
    df = pd.read_csv('data/data.csv') #Read data from data.csv
    df.columns=['x','y']         
    layout = go.Layout(
                        title = {
                                 'text':'Graph',
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
                                     x=df['x'],
                                     y=df['y'],
                                     ), 
                     layout = layout
                     )



app.layout = html.Div([
             layouts.navbar,
             html.Br(),
             dbc.Row([
                dbc.Col(html.Div(), width=1),
                dbc.Col(layouts.first_card, width=4),
                dbc.Col(html.Div(), width=2),
                dbc.Col(layouts.first_card, width=4),
                dbc.Col(html.Div(), width=1),
            ]),
            html.Br(),
            dbc.Row([
                dbc.Col(html.Div(), width=1),
                dbc.Col(
                    html.Div([
                        dcc.Graph(
                            id='g1',
                            figure=_create_fig()),
                        dcc.Interval(
                            id='interval-component',
                            interval=1*500, # in milliseconds
                            n_intervals=0
                        ),
                    ]),
                width =10,
                className = "bg-light border border-dark"
                )
            ]),
], className = "bg-secondary")


@app.callback(
    dash.dependencies.Output('g1', 'figure'),
    dash.dependencies.Input('interval-component', 'n_intervals'))

def refresh_data(n_clicks):
    return _create_fig()


if __name__ == "__main__":
    app.run_server(host='127.0.0.1', debug=True, port=8050)
