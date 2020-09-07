import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
import pandas as pd
from data.models import *
import dash
from datetime import datetime as dt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

style_button = {'border': 'solid 3px #1a2d46',
                'display': 'inline-block', 'padding': '10px 25px',
                'margin': '0 auto', 'cursor': 'pointer',
                'color': '#1a2d46', 'font-size': '0.95rem',
                'background-color': 'white'}

# -----------------------------------------
# App 1

Graph = DjangoDash('Dashboard', external_stylesheets=external_stylesheets)
Graph.layout = html.Div([
    html.Div(className='row',
             style={'display': 'flex'}, children=[
        #Отказы
        html.Div([
            html.H2('Отказы', style={'text-align': 'center', 'color': 'gray', 'font-family': 'Nunito'}),
            dcc.Graph(id='failures-graph', animate=True,
                      style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
            html.Div([
                dcc.Slider(
                    id='slider-failures',
                    marks={i + 1: '{}'.format(i) for i in range(98)},
                    max=98, value=50, step=1,
                    updatemode='drag')],
                style={'margin-top': 20}),
            html.Div(style={'display': 'flex', 'justify-content':'space-evenly'}, children=[
                html.Div(html.Button('Все станки', id='submit-failures', n_clicks=0,
                                 style=style_button,
                                 title='Показать поломки всех станков')),
                html.Div(id='updatemode-output-failures', style={'text-align': 'center', 'margin-top': 10}),
            ]),

            ], style={'width': '33%'}),

        #Ошибки
        html.Div([
            html.H2('Ошибки', style={'text-align': 'center'}),
            dcc.Graph(id='errors-graph', animate=True,
                      style={"backgroundColor": "#1a2d46", 'color': '#ffffff', "height": "40"}),
            html.Div([
                dcc.Slider(
                    id='slider-errors',
                    marks={i: '{}'.format(i) for i in range(101)},
                    max=101,
                    value=50,
                    step=1,
                    updatemode='drag')],
                style={'margin-top': 20}
            ),
            html.Div(style={'display': 'flex', 'justify-content': 'space-evenly'}, children=[
                html.Div(html.Button('Все станки', id='submit-errors', n_clicks=0,
                                     style=style_button,
                                     title='Показать поломки всех станков')),
                html.Div(id='updatemode-output-errors', style={'text-align': 'center', 'margin-top': 10}),
            ])
            ], style={'width': '33%'}),
        #Ремонты
        html.Div([
            html.H2('Ремонты', style={'text-align': 'center'}),
            dcc.Graph(id='comp-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff', "height": "40"}),
            html.Div([
                dcc.Slider(
                    id='slider-comp',
                    marks={i: '{}'.format(i) for i in range(101)},
                    max=101,
                    value=50,
                    step=1,
                    updatemode='drag')],
                style={'margin-top': 20}
            ),
            html.Div(style={'display': 'flex', 'justify-content': 'space-evenly'}, children=[
                html.Div(html.Button('Все станки', id='submit-comp', n_clicks=0,
                                     style=style_button,
                                     title='Показать поломки всех станков')),
                html.Div(id='updatemode-output-comp', style={'text-align': 'center', 'margin-top': 10}),
            ])
            ],style={'width': '33%'}),
    ]),
    #Станки
    html.Div([
        html.H2('Станки', style={'text-align': 'center', 'color': 'gray', 'font-family': 'Nunito'}),
        html.Div(className='row',
                 style={'display': 'flex'}, children=[
                html.Div([
                    dcc.Graph(id='machines-graph', animate=True,
                              style={"backgroundColor": "#1a2d46", 'color': '#ffffff', "height": "40"})
                ], style={'width': '80%'}),
                html.Div([
                    html.Div([
                        dcc.DatePickerRange(
                            id='datepicker-machines',
                            calendar_orientation='vertical',
                            clearable='True',
                            min_date_allowed=dt(2014, 6, 1),
                            max_date_allowed=dt(2017, 6, 1))],
                        style={'width': '20%', 'margin-top': 75}),
                    html.Div(html.Button('Сбросить дату', id='date-clear', n_clicks=0,
                                         style=style_button,
                                         title='Данные за весь период'), style={'margin-top': 30})
                ], style={'class': 'col', 'background': 'rgb(39, 41, 61)', 'color': '#ffffff'})

            ]),

        html.Div([dcc.Dropdown(id='dropdown-machines',
                               options=[{'label': 'Ошибки', 'value': 'errors'},
                                        {'label': 'Ремонт', 'value': 'comp'},
                                        {'label': 'Отказы', 'value': 'failures'}],
                               optionHeight=35, value='errors',
                               disabled=False, multi=False,
                               searchable=True,search_value='',
                               placeholder='Выберите признак...',
                               clearable=True,style={'width':"100%"})],
                 style={'margin-top': 20})
    ]),
    html.Div([
        html.Div(className='row',
                 style={'display': 'flex'}, children=[
                html.Div([
                    html.H2('Телеметрия', style={'text-align': 'center', 'color': 'gray', 'font-family': 'Nunito'}),
                    dcc.Graph(id='telemetry-graph', animate=True,
                              style={"backgroundColor": "#1a2d46", 'color': '#ffffff', "height": "40"})
                ], style={'width': '100%'}),
            ]),

        html.Div([dcc.Dropdown(id='dropdown-telemetry',
                               options=[{'label': 'Напряжение', 'value': 'volt'},
                                        {'label': 'Поворот', 'value': 'rotate'},
                                        {'label': 'Давление', 'value': 'pressure'},
                                        {'label': 'Вибрация', 'value': 'vibration'}],
                               optionHeight=35, value='volt',
                               disabled=False, multi=False,
                               searchable=True, search_value='',
                               placeholder='Выберите параметр...',
                               clearable=True, style={'width': "100%"})],
                 style={'margin-top': 10})]),
        html.Div(style={'display': 'flex', 'justify-content': 'space-evenly'}, children=[
            html.Div([
                dcc.Input(id="input-telemetry", type="number", placeholder="Номер станка",
                          min=0, max=100, value=10, step=1, style={'width': '100%','padding': '12px 20px',
                                                                   'margin': '8px 0','box-sizing':'border-box'})
            ],style={'margin-top': 20}),

            html.Div(id='machine-out', style={'text-align': 'center', 'margin-top': 35, 'margin-left': 20})
        ])

])

@Graph.callback(
    [Output('failures-graph', 'figure'),
     Output('updatemode-output-failures', 'children')],
    [Input('slider-failures', 'value'),
     Input('submit-failures', 'n_clicks')],
)
def display_value(value, btn):
    failures = [failure[0] for failure in Failures.objects.values_list('failure_id')]
    machineid = [failure[0] for failure in Failures.objects.values_list('machine_id')]
    data = {'failures': failures, 'machineid': machineid}
    df_failures = pd.DataFrame(data=data)
    log = 'Текущий станок [{}/{}]'.format(value, len(df_failures['machineid'].unique()))

    try:
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
        if 'submit-failures' in changed_id:
            failure = df_failures['failures'].value_counts()
            log = 'Выбраны все станки'
        else:
            failure = df_failures['failures'][df_failures['machineid'] == value].value_counts()
    except IndexError:
        df_failures = df_failures[df_failures['machineid'] == value]
        failure = df_failures['failures'].value_counts()

    x = [key for key in failure.keys()]
    y = failure.values.tolist()

    graph = go.Bar(
        x=x,
        y=y,
        name='Manipulate Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[0, max(y)]),
        font=dict(color='white'),
    )
    return {'data': [graph], 'layout': layout}, log

@Graph.callback(
    [Output('errors-graph', 'figure'),
     Output('updatemode-output-errors', 'children')],
    [Input('slider-errors', 'value'),
     Input('submit-errors', 'n_clicks')])
def display_value(value, btn):
    errors = [error[0] for error in Errors.objects.values_list('error_id')]
    machineid = [machineid[0] for machineid in Errors.objects.values_list('machine_id')]
    df_errors = pd.DataFrame(data={'errors': errors, 'machineid': machineid})
    log = 'Текущий станок [{}/{}]'.format(value, len(df_errors['machineid'].unique()))

    try:
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
        if 'submit-errors' in changed_id:
            error = df_errors['errors'].value_counts()
            log = 'Выбраны все станки'
        else:
            error = df_errors['errors'][df_errors['machineid'] == value].value_counts()
    except IndexError:
        df_errors = df_errors[df_errors['machineid'] == value]
        error = df_errors['errors'].value_counts()

    x = [key for key in error.keys()]
    y = error.values.tolist()

    graph = go.Bar(
        x=x,
        y=y,
        name='Errors Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[0, max(y)]),
        font=dict(color='white'),

    )
    return {'data': [graph], 'layout': layout}, log

@Graph.callback(
    [Output('comp-graph', 'figure'),
     Output('updatemode-output-comp', 'children')],
    [Input('slider-comp', 'value'),
     Input('submit-comp', 'n_clicks')])

def display_value(value, btn):
    comp = [comp[0] for comp in Maint.objects.values_list('comp_id')]
    machineid = [machineid[0] for machineid in Maint.objects.values_list('machine_id')]
    df_comp = pd.DataFrame(data={'comp': comp, 'machineid': machineid})
    log = 'Текущий станок [{}/{}]'.format(value, len(df_comp['machineid'].unique()))

    try:
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
        if 'submit-comp' in changed_id:
            data_comp = df_comp['comp'].value_counts()
            log = 'Выбраны все станки'
        else:
            data_comp = df_comp['comp'][df_comp['machineid'] == value].value_counts()
    except IndexError:
        data_comp = df_comp['comp'][df_comp['machineid'] == value].value_counts()

    x = [key for key in data_comp.keys()]
    y = data_comp.values.tolist()

    graph = go.Bar(
        x=x,
        y=y,
        name='Comp Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[0, max(y)]),
        font=dict(color='white'),

    )
    return {'data': [graph], 'layout': layout}, log

@Graph.callback(
    Output("machines-graph", "figure"),
    [Input('dropdown-machines', 'value'),
     Input('datepicker-machines', 'start_date'),
     Input('datepicker-machines', 'end_date'),
     Input('date-clear', 'n_clicks')],
)
def display_value(value, start_date, end_date, btn):
    print(value)

    if value == 'errors':
        first = [error[0] for error in Errors.objects.values_list('error_id')]
        machineid = [machineid[0] for machineid in Errors.objects.values_list('machine_id')]
        datetime = [datetime[0] for datetime in Errors.objects.values_list('datetime')]
    elif value == 'comp':
        first = [comp[0] for comp in Maint.objects.values_list('comp_id')]
        machineid = [machineid[0] for machineid in Maint.objects.values_list('machine_id')]
        datetime = [datetime[0] for datetime in Maint.objects.values_list('datetime')]
    else:
        first = [failures[0] for failures in Failures.objects.values_list('failure_id')]
        machineid = [machineid[0] for machineid in Failures.objects.values_list('machine_id')]
        datetime = [datetime[0] for datetime in Failures.objects.values_list('datetime')]

    df = pd.DataFrame(data={'value': first, 'machineid': machineid, 'datetime': datetime})

    try:
        changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
        if 'date-clear' in changed_id:
            start_date = df['datetime'].min()
            end_date = df['datetime'].max()
            print('hel')
    except IndexError:
        pass

    if start_date is None: start_date = df['datetime'].min()
    if end_date is None: end_date = df['datetime'].max()

    data = df[(start_date< df['datetime']) & (df['datetime'] < end_date)]
    del df

    x = data['machineid'].unique()
    y = [val[0] for val in data.groupby('machineid').count().values]

    graph = go.Bar(
        x=x,
        y=y,
        name='Machines Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[0, max(y)]),
        font=dict(color='white'),
    )
    return {'data': [graph], 'layout': layout}


@Graph.callback(
    [Output("telemetry-graph", "figure"),
    Output('machine-out', 'children')],
    [Input('dropdown-telemetry', 'value'),
     Input('input-telemetry', 'value')],
)

def display_value(value, input):
    log = "Выбран станок [{}/{}]".format(input, '100')
    datetime = [datetime[0] for datetime in Telemetry.objects.values_list('datetime').filter(machine_id=input)]
    machineid = [machineid[0] for  machineid in Telemetry.objects.values_list('machine_id').filter(machine_id=input)]
    feature = [feature[0] for  feature in Telemetry.objects.values_list('{}'.format(value)).filter(machine_id=input)]
    # rotate = [rotate[0] for rotate in Telemetry.objects.values_list('rotate').filter(machine_id=input)]
    # pressure = [pressure[0] for pressure in Telemetry.objects.values_list('pressure').filter(machine_id=input)]
    # vibration = [vibration[0] for vibration in Telemetry.objects.values_list('vibration').filter(machine_id=input)]

    data = {'datetime': datetime, 'machineid': machineid, 'feature': feature}
    df = pd.DataFrame(data=data)

    x = df['datetime']
    y = df['feature']

    graph = go.Scatter(
        x=x,
        y=y,
        name='Telemetry Graph'
    )
    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[min(x), max(x)]),
        yaxis=dict(range=[0, max(y)]),
        font=dict(color='white'),

    )
    return {'data': [graph], 'layout': layout}, log

if __name__ == '__main__':
    Graph.run_server(debug=True)