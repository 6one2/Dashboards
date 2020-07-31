import pandas as pd
import plotly.graph_objs as go
from .getdata import get_top10, HumanCapital, GDP, TODAY, getEducation
from datetime import datetime

TODAY_10ago = TODAY.replace(year=TODAY.year-10)

def return_figures():
    """Creates plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    country  = get_top10()
    country_code = country['code'].tolist()
    country_name = list(country.index)
    
    # first chart: Human Capital Index
    graph_one = []
    data_one = HumanCapital(country_code)

    graph_one.append(
      go.Bar(
      x = list(data_one.index),
      y = list(data_one),
      )
    )

    layout_one = dict(
        title = 'Human Capital Index for the 10 richest countries in 2017',
        xaxis = dict(
            title = 'Country'
        ),
        yaxis = dict(
            title = 'Human Capital Index'
        )
    )
    
    
    # second chart: GDP the past 10 years
    graph_two =[]
    data_two = GDP(country_code, (TODAY_10ago, TODAY))
    
    for name in country_name:
        x_val = data_two.loc[name,'date'].values.tolist()
        y_val = data_two.loc[name,'GDP'].values.tolist()
        graph_two.append(
            go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines+markers',
                name = name
            )
        )
    
    layout_two = dict(
        title = 'Gross Domestic Product over the past 10 years', 
        xaxis = dict(
            title = 'Year', 
            autotick=True, 
            tick0=TODAY_10ago.year), 
        yaxis = dict(title = 'Current USD$')
    )
    
    # third chart: %GDP per student the past 10 years
    graph_three =[]
    data_three = getEducation(country_code, (TODAY_10ago, TODAY))
    
    for name in country_name:
        x_val = data_three.loc[name,'date'].values.tolist()
        y_val = data_three.loc[name,'Expenditure_per_student'].values.tolist()
        graph_three.append(
            go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines+markers',
                name = name
            )
        )
    
    layout_three = dict(
        title = 'Government expenditure per student over the past 10 years', 
        xaxis = dict(
            title = 'Year', 
            autotick=True, 
            tick0=TODAY_10ago.year), 
        yaxis = dict(title = '% GDP per capita')
    )
    
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    
    return figures