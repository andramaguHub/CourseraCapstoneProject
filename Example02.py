import dash
from dash import dcc, Dash, dash_table
from dash import html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import yfinance as yf
input_stock = "TRQ"
GE = yf.Ticker(input_stock)
df_GE = GE.history(period="max")

trace_close = go.Scatter(x=list(df_GE.index),
                         y=list(df_GE.Close),
                         name="Close",
                         line=dict(color="#f44242"))
data = [trace_close]
layout = dict(title=input_stock, showlegend=False)
fig = dict(data=data, layout=layout)

app = Dash(__name__)

app.layout = html.Div([

    html.Div(html.H1(children="Hello World")),

    html.Label("DASH Graph"),

    html.Div(
        dcc.Input(id="stock-input", placeholder="Enter a Stock to be charter", type="text", value="")
    ),

    html.Div(
        dcc.Dropdown(
            options=[
                {"label": "Candlestick", "value": "Candlestick"},
                {"label": "Line", "value": "Line"}
            ],
            placeholder='select type of chart'
        )
    ),

    html.Div(
        dcc.Graph(id="Stock Chart", figure=fig)
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)





