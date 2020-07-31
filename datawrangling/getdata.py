import wbdata
import pandas as pd
import numpy as np
from datetime import datetime

TODAY = datetime.today()

def get_top10():
    data_country = wbdata.get_country()
    country_dict = {x['name']:x['id'] for x in data_country if x['capitalCity'] != ''} # remove aggregates

    # countries GDP today
    df_gdp_today = wbdata.get_dataframe(
        indicators={'NYGDPMKTPSACD':"GDP"},
        data_date=(TODAY),
        country=list(country_dict.values())
    )

    # list of top 10 countries by GDP
    country_top10 = df_gdp_today.sort_values(by='GDP', ascending=False)[:10]
    country_top10['code'] = [country_dict[x] for x in country_top10.index]
    
    return country_top10


def HumanCapital(country_list='all'):
    """
    return the Human Capital Index for 2017 only
    Args:(str)
        list of country codes
    Returns:
        pandas series
    """
    
    indicator = 'HD.HCI.OVRL'
    data = wbdata.get_data(
        indicator=indicator,
        pandas=True,
        column_name='HumanCapitalIndex',
        country=country_list
    )
    
    return data.sort_values()

def GDP(country_list, date = TODAY):
    indicator = 'NYGDPMKTPSACD'
    data = wbdata.get_data(
        indicator=indicator,
        pandas=True,
        column_name='GDP',
        country=country_list,
        data_date = date
    )
    
    return data.reset_index(level=1).sort_values('date')
    

def getEducation(country_list, date = TODAY):
	indicator = 'SE.XPD.PRIM.PC.ZS'
	data = wbdata.get_data(
		indicator=indicator,
		pandas=True,
		column_name='Expenditure_per_student',
		country=country_list,
		data_date=date
	)
	
	return data.reset_index(level=1).sort_values('date')
	