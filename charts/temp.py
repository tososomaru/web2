def display_value(value, start_date, end_date):
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

    if start_date is None:
        start_date = df['datetime'].min()
    if end_date is None:
        end_date = df['datetime'].max()

    data = df[(start_date < df['datetime']) & (df['datetime'] < end_date)]
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
    Output("telemetry-graph", "figure"),
    [Input('dropdown-telemetry', 'drop'),
     Input('datepicker-telemetry', 'start_date'),
     Input('datepicker-telemetry', 'end_date'),
     Input('slider-telemetry', 'value')],
)
def display_value(drop, start_date, end_date, value):
    print(start_date, end_date, value, drop)

    datetime = [datetime[0] for i, datetime in enumerate(Telemetry.objects.values_list('datetime')) if i < 5000]
    machineid = [machineid[0] for i, machineid in enumerate(Telemetry.objects.values_list('machine_id')) if i < 5000]
    volt = [volt[0] for i, volt in enumerate(Telemetry.objects.values_list('volt')) if i < 5000]
    rotate = [rotate[0] for i, rotate in enumerate(Telemetry.objects.values_list('volt')) if i < 5000]
    pressure = [pressure[0] for i, pressure in enumerate(Telemetry.objects.values_list('volt')) if i < 5000]
    vibration = [vibration[0] for i, vibration in enumerate(Telemetry.objects.values_list('volt')) if i < 5000]

    data = {'datetime': datetime, 'machineid': machineid, 'volt': volt,
            'rotate': rotate, 'pressure': pressure, 'vibration': vibration}
    df = pd.DataFrame(data=data)

    if start_date is None: start_date = df.datetime.min()
    if end_date is None: end_date = df.datetime.max()

    df = df[(start_date < df['datetime']) & (df['datetime'] < end_date)]
    df = df[df['machineid'] == value]
    x = df.datetime
    y = df['{}'.format(drop)]

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