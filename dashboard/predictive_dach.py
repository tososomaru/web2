# import dash
# import dash_table
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd
# import plotly.graph_objs as go
#
# from django_plotly_dash import DjangoDash
# from dash.dependencies import Input, Output
# from datetime import datetime as dt
#
# from data.models import *
# from predictive.models import *
#
#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# style_button = {'border': 'solid 3px #1a2d46',
#                 'display': 'inline-block', 'padding': '10px 25px',
#                 'margin': '0 auto', 'cursor': 'pointer',
#                 'color': '#1a2d46', 'font-size': '0.95rem',
#                 'background-color': 'white'}
#
# ml_algorithms_columns = ['id','Название', 'Описание', 'Код', 'Версия',
#                         'Автор', 'Дата создания', 'Конечная точка']
# columns = ['id','Название', 'Описание', 'Версия',
#                         'Автор', 'Дата создания', 'Конечная точка']
#
# ml_algorithms = [obj for obj in MLAlgorithm.objects.values_list()]
# print(ml_algorithms)
# ml_algorithms_data = pd.DataFrame(ml_algorithms, columns=ml_algorithms_columns)
# del ml_algorithms_data['Код']
#
# Predictive = DjangoDash('Predictive', external_stylesheets=external_stylesheets)
#
# Predictive.layout = dash_table.DataTable(
#     id='table',
#     columns=columns,
#     data=ml_algorithms_data.to_dict(),
# )
#
# if __name__ == '__main__':
#     Predictive.run_server(debug=True)