import dash
import pandas as pd
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)

def _create_fig():
    df = pd.read_csv('data.csv')
    df.columns=['x','y']
    return go.Figure(
        data=go.Scatter(
            x=df['x'],
            y=df['y']))


app.layout = html.Div([
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
