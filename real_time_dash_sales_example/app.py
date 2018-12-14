# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import random
from collections import deque
from datetime import datetime as dt
from dash.dependencies import Output, Event
from db_util import Data 

# The dequeue data scructures to represent the X(time) and Y(Sales) for the realtime timeseries
X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

# Add custom style to the app using css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Creating the app and setting the layout
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(style={'margin':'30px', 'font-family' : "Rajdhani"}, children=[

    html.Div([
        

        html.Div([        
            html.H3(children='Monitoramento Sell-out tempo real', style={'color':'#00B5BD'}),
        ], className="eleven columns"),

        html.Div([
            html.Img(src=app.get_asset_url('logo.png'), height= '50'),
        ], className="one columns"),  
        
    ], className="row"),

    html.Div([
        html.Div([
            html.Label('Produtos'),
            dcc.Dropdown(
                options=[
                    {'label': 'Refrigerante', 'value': 'NYC'},
                    {'label': u'Cigarro', 'value': 'MTL'},
                    {'label': 'Cerveja', 'value': 'SF'}
                ],
                value=['MTL', 'SF'],
                multi=True
            ),
        ], className="three columns"),

        html.Div([
            html.Label('Região'),
            dcc.Dropdown(
                options=[
                    {'label': 'Zona Sul', 'value': 'NYC'},
                    {'label': u'Zona Norte', 'value': 'MTL'},
                    {'label': 'Centro', 'value': 'SF'}
                ],
                value='MTL'
            )
        ], className="three columns"),

    ], className="row", style={'background-color' : '#E6F6EE', 'padding': '10px', 'border-bottom': '3px solid #b2bec3'}),

    html.Div([
        html.Div([
            dcc.Graph(
                animate=True,
                id='live-graph',
            ),
            dcc.Interval(
                id='graph-update',
                interval=1.5*1000
            )
        ], className="eight columns"),

        html.Div([
            html.H5(children='_', style={'color':'#FFF'}),
            html.H6(children='Meta (R$ 10 mil)', style={'color':'#A6A6A6'}),
            html.H3(id='goal-num', children='0.00%', style={'color':'#00B5BD', 'font-weight':'bold'}),
            html.H6(children='Ticket Médio', style={'color':'#A6A6A6'}),
            html.H3(id='tickect-num', children='0.00%', style={'color':'#00B5BD', 'font-weight':'bold'}),
            html.H6(children='Volume de clientes', style={'color':'#A6A6A6'}),
            html.H3(id='users-num', children='0', style={'color':'#00B5BD', 'font-weight':'bold'})
        ], className="four columns")

    ], className='row')
])

# The goal number update callback
@app.callback(Output('goal-num', 'children'), events=[Event('graph-update', 'interval')])
def update_goal():
    num = Y[-1]/10000 * 100
    return '{0:.2f}'.format(num) + '%'

# The tickect number update callback
@app.callback(Output('tickect-num', 'children'), events=[Event('graph-update', 'interval')])
def update_ticket():
    num = Y[-1]/X[-1]
    return 'R$ ' + '{0:.2f}'.format(num)

# The users count number update callback
@app.callback(Output('users-num', 'children'), events=[Event('graph-update', 'interval')])
def update_clients():
    users = random.uniform(10,80)/3 
    return str(int(users))

# The line chart update callback
@app.callback(Output('live-graph', 'figure'), events=[Event('graph-update', 'interval')])
def update_graph_scatter():
    X.append(X[-1]+1)
    rand = random.uniform(10,60)
    Y.append(Y[-1] + round(rand, 2))

    data = go.Scatter(
        x=list(X),
        y=list(Y),
        name='Scatter',
        mode= 'lines+markers',
        line=dict(color = 'rgb(0, 181, 189)')
    )
    layout = {
        'title': 'Vendas acumuladas',
        'font': {
            'family':'Rajdhani'
        },
        'xaxis' : dict(range=[min(X),max(X)]),
        'yaxis' : dict(range=[min(Y),max(Y)], tickprefix="R$ ")
    }

    return {'data': [data],'layout' : layout}

# Main function to start the app and server
if __name__ == '__main__':
    app.run_server(debug=True)