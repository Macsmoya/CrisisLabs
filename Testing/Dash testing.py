import dash
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import csv
from dash_bootstrap_templates import load_figure_template

load_figure_template("lux")
app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.LUX]
)


def _create_fig(): #Create graph 
    df = pd.read_csv('data.csv') #Read data from data.csv
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

first_card = dbc.Card( 
    dbc.CardBody(
        [
            html.H4("Card ig", className="card-title"),
            html.H6("By WC1", className="card-subtitle"),
            html.P("Enn", className = "card-text"),
        ]
    ),

)


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Github", href="https://github.com/Macsmoya/CrisisLabs")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("follow me on twitter", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Raspberry shake demo",
    brand_href="#",
    color="primary",
    dark=True,
)


app.layout = html.Div([
    navbar,
    html.Br(),
    dbc.Row(
            [
                dbc.Col(html.Div(), width=1),
                dbc.Col(first_card, width=4),
                dbc.Col(html.Div(), width=1),
                dbc.Col(first_card, width=4),
                dbc.Col(html.Div(), width=1),

            ],

        ),
    html.Hr(),
    dbc.Row(
            [
                dbc.Col(html.Div(), width=1),
                dcc.Graph(
                    id='g1',
                    figure=_create_fig()),
                dcc.Interval(
                    id='interval-component',
                    interval=1*1000, # in milliseconds
                    n_intervals=0
                            ),
                dbc.Col(
                    html.Div(
                             
                             ),
                    width=1,
                    style= {"height":"500px"},
                        ),

            ],

        ),
    
])


@app.callback(
    dash.dependencies.Output('g1', 'figure'),
    dash.dependencies.Input('interval-component', 'n_intervals'))

def refresh_data(n_clicks):
    return _create_fig()


if __name__ == "__main__":
    app.run_server(host='127.0.0.1', debug=True, port=8050)
