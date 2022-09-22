#
from dash import html, Output, Input, dcc

from layouts.mainDashboard import geo_dropdown

tabTitle = 'Tab content 1'
plotId = ['graph_0', 'graph_11', 'graph_12', 'graph_13']
dropdown = geo_dropdown

def tab_1():
    return html.Div([
        html.H3(tabTitle),
        # Dropdown
        dropdown,
        # Chart
        html.Div([
            dcc.Graph(id=plotId[1])
        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
        # Chart
        html.Div([
            dcc.Graph(id=plotId[2]),
            dcc.Graph(id=plotId[3]),
        ], style={'display': 'inline-block', 'width': '49%'}),
    ])


