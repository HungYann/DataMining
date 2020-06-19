import pathlib
import os

import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State




# app initialize
app = dash.Dash(
    __name__,
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)


server = app.server
app.config["suppress_callback_exceptions"] = True



# Load data
APP_PATH = str(pathlib.Path(__file__).parent.resolve())

FileName=["oilPrice","GoldPrice"]

oilPrice = pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "oil_price.csv")))

gdp= pd.read_csv(os.path.join(APP_PATH, os.path.join("data", "gold_price.csv")))







def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.H6("Crude Oil (petroleum) Annually Price"),
        ],
    )


## graph title
def build_graph_title(title):
    return html.P(className="graph-title", children=title)




app.layout = html.Div(
    children=[
        html.Div(
            id="top-row",
            children=[

                html.Div(
                    className="row",
                    id="top-row-header",

                    children=[

                        html.Div(
                            id="header-container",
                            children=[
                                build_banner(),
                                html.P(
                                    id="instructions",
                                    children="Montoring the oil price, collerate with the variables, and find their pattern",
                                ),

                                build_graph_title(""),

                                html.P(
                                    id="operator-select",
                                    children="",
                                ),

                            
                                
                            ],
                        )

                    ],
                ),

            #---
                html.Div(
                    className="row",
                    id="top-row-graphs",
                    children=[

                        # Ternary map
                        html.Div(
                            id="ternary-map-container",
                            children=[


                                html.Div(
                                    id="ternary-header",
                                    children=[
                                        build_graph_title(
                                            "Oil Price Change Comparison"
                                        )

                                    ],
                                ),


                                dcc.Graph(
                                    id="ternary-map",
                                    figure={
                                        "layout": {
                                            "paper_bgcolor": "#192444",
                                            "plot_bgcolor": "#192444",
                                        }
                                    },
                                    config={
                                        "scrollZoom": True,
                                        "displayModeBar": False,
                                    },
                                ),


                            ],
                        ),


                    ],
                ),
            ],
        ),


        html.Div(
            className="row",
            id="bottom-row",

            children=[
                html.Div(
                    className="row",
                    id="1",
                    children=[

                        # Formation line plots
                        html.Div(
                            id="form-bar-container",
                            className="six columns",
                            children=[
                                build_graph_title("Show Trends for oil price"),
                                dcc.Graph(id="form-by-line"),
                            ],
                        ),

                        html.Div(
                            # Selected well productions
                            id="well-production-container",
                            className="six columns",
                            children=[
                                build_graph_title("Show Trends for gold price"),
                                dcc.Graph(id="production-fig"),
                            ],
                        ),

                    ],
                ),


            #--------------

                html.Div(
                    className="row",
                    id="2",

                    children=[

                        html.Div(
                            id="form-bar-container-1",
                            className="six columns",
                            children=[
                                # build_graph_title("Show relationship for oil price"),
                                dcc.Graph(id="form-by-bar-1"),
                            ],
                        ),

                        html.Div(
                            # Selected well productions
                            id="well-production-container-1",
                            className="six columns",
                            children=[
                                # build_graph_title("show relationship for gold price"),
                                dcc.Graph(id="production-fig-1"),
                            ],
                        ),

                    ],

                ),

            ]

        ),


        #---- bottom ---


        html.Div(
            className="row",
            id="bottom-row-3",

            children=[
                html.Div(
                    className="row",
                    id="3",

                    children=[

                        # Formation line plots
                        html.Div(
                            id="form-bar-container-3",
                            children=[
                                build_graph_title("Data TABLE"),
                                dcc.Graph(id="data-table-3"),
                            ],
                        ),

                    ],
                ),


            #--------------



            ]

        ),

        #---

    ]
)



@app.callback(Output('ternary-map','figure'),
              [ Input('operator-select','value') ])
def toprightlineChart(selectedFile):

    x=oilPrice["Month"];
    y=oilPrice["Change"]

    y1=gdp["Change"]

    data = []

    trace_close = go.Scatter(
        x=x,
        y=y,
        mode='lines+markers',
        name="Oil Price"
    )

    trace_close2 = go.Scatter(
        x=x,
        y=y1,
        mode='lines+markers',
        name="Gold Price"
    )


    data.append(trace_close)
    data.append(trace_close2)
    return {
        'data':data,

        'layout': dict(
            xaxis={'title': 'Year'},
            yaxis={'title': 'Change percentage %'},
        )

    }


@app.callback(Output('form-by-line','figure'),
              [ Input('operator-select','value') ])
def bottomrightlineChart(selectedFile):

    x = oilPrice["Month"];
    y = oilPrice["Price"]

    data = []

    trace_close = go.Scatter(
        x=x,
        y=y,
        mode='lines',
        name="Oil Price"
    )
    data.append(trace_close)

    return {
        'data': data,

        'layout': dict(
            xaxis={'title': 'Month'},
            yaxis={'title': 'Value'},
        )

    }



@app.callback(Output('production-fig', 'figure'),
              [Input('operator-select', 'value')])
def bottomleftlineChart(selectedFile):
    x1 = gdp["Month"]
    y1 = gdp["Price"]

    data = []

    trace_close = go.Scatter(
        x=x1,
        y=y1,
        mode='lines',
        name="Variable"
    )
    data.append(trace_close)

    return {
        'data': data,

        'layout': dict(
            xaxis={'title': 'Month'},
            yaxis={'title': 'Value'},
        )

    }


##----## line 3

@app.callback(Output('form-by-bar-1', 'figure'),
              [Input('operator-select', 'value')])


def bottomleftlineChart(selectedFile):
    x = oilPrice["Month"];
    y = oilPrice["Price"]


    length = len(x.tolist())
    length_value= [i for i in range(length)]

    data = []

    trace_close = go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=dict(size=3,
                    color=length_value)
    )

    data.append(trace_close)

    return {
        'data': data,

        'layout': dict(
            xaxis={'title': 'Month'},
            yaxis={'title': 'Value'},
        )

    }


@app.callback(Output('production-fig-1', 'figure'),
              [Input('operator-select', 'value')])

def bottomleftlineChart(selectedFile):

    x1 = gdp["Month"]
    y1 = gdp["Price"]


    length = len(x1.tolist())
    length_value= [i for i in range(length)]

    data = []

    trace_close = go.Scatter(
        x=x1,
        y=y1,
        mode='markers',
        marker=dict(size=3,
                    color=length_value)
    )

    data.append(trace_close)

    return {
        'data': data,

        'layout': dict(
            xaxis={'title': 'Month'},
            yaxis={'title': 'Value'},
        )

    }



@app.callback(Output('data-table-3', 'figure'),
              [Input('operator-select', 'value')])

def bottomleftlineChart(selectedFile):

    x = oilPrice["Month"];
    y = oilPrice["Price"]

    y1 = gdp["Price"]



    data = []

    trace_close = go.Table(

       header=dict(values=["Year","OilPrice","Gold Price"],
                line_color='darkslategray',
                fill_color='lightskyblue',
                align='left'),

                cells=dict(values=[x,y,y1], line_color='darkslategray',
                fill_color='royalblue',
                font=dict(color='white', size=12),
                height=40
        )
    )



    data.append(trace_close)

    return {
        'data': data,

        'layout': dict(
            xaxis={'title': 'Month'},
            yaxis={'title': 'Value'},
        )

    }





# Running the server
if __name__ == "__main__":
    app.run_server(debug=True)
