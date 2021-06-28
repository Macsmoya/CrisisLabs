import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash_core_components as dcc

first_card = dbc.Card( 
    dbc.CardBody(
        [
            html.H4("Card ig", className="card-title"),
            html.H6("By WC1", className="card-subtitle"),
            html.P("Enn", className = "card-text"),
        ]
    ),
    color = "dark",
    outline = True
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


