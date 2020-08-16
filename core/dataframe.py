import pandas as pd
import calendar
from datetime import datetime


def chart_w_date(column_name, csv_name, date1, date2, chart, file):
	csv_name = pd.read_csv(file)
	csv_name['Start Date'] = csv_name['Start Date'].astype('datetime64[ns]')
	mask = (csv_name['Start Date'] > date1) & (csv_name['Start Date'] <= date2)
	time_period_data = csv_name.loc[mask]
	if chart == 'bar':
		value_columns = time_period_data[column_name].value_counts(
		).rename_axis('unique_values').reset_index(name='counts')
		dict_value_columns = {
			'type': 'column',
			'title': column_name,
			'catogeries': value_columns['unique_values'].tolist(),
			'series': [{'name': coulmn_name,
                            'data': value_columns['counts'].tolist(),
                            'color': 'blue'}]
		}
	if chart == 'pie':
		value_columns = pd.concat([time_period_data['Month'].value_counts().rename_axis(
			'unique_values'), time_period_data['Month'].value_counts(normalize=True).mul(100)], axis=1, keys=('counts', 'percentage'))
		value_columns = value_columns.reset_index()
		dict_value_columns = {
                    'dict_fin': {
                        'type': 'pie',
                        'title': column_name,
                 							'data': value_columns.values.tolist(),
                    }
                }
	return dict_value_columns


def time_series(csv_name, date1, date2):
	csv_name = pd.read_csv("path")
	mask = (csv_name['Start Date'] > date1) & (csv_name['Start Date'] <= date2)
	time_period_data = csv_name.loc[mask]
	time_period_data['Month'] = time_period_data['Start Date'].dt.month
	time_period_data['Month'] = time_period_data['Month'].apply(
		lambda x: calendar.month_abbr[x])
	value_columns = time_period_data['Month'].value_counts(
	).rename_axis('unique_values').reset_index(name='counts')
	dict_value_columns = {
            'type': 'column',
            'title': column_name,
    			 				'catogeries': value_columns['unique_values'].tolist(),
    			 				'series': [{'name': coulmn_name,
                                                            'data': value_columns['counts'].tolist(),
                                                            'color': 'blue'}]
        }
	return dict_value_columns
