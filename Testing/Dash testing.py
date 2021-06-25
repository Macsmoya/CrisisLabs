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


def _create_fig():
    df = pd.read_csv('data.csv') #Data frame
    df.columns=['x','y']
    return go.Figure(
        data=go.Scatter(
            x=df['x'],
            y=df['y']))

first_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Graph", className="card-title"),
            html.P("Enn"),
            dbc.Button("Go somewhere", color="primary"),
        ]
    )
)


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
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
    html.Div(
        [
            html.Div(
                [
                    html.H2("Raspberry shake data"),
                    html.P("By Yohan Kanji, Max Moir, Aston Varga and Dev Shamihoke"),
                ],
                className = "header-left",
                    )
         ]),   
        
    dcc.Graph(
        id='g1',
        figure=_create_fig()),
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    )
])


@app.callback(
    dash.dependencies.Output('g1', 'figure'),
    dash.dependencies.Input('interval-component', 'n_intervals'))

def refresh_data(n_clicks):
    return _create_fig()


if __name__ == "__main__":
    app.run_server(host='127.0.0.1', debug=True, port=8050)
