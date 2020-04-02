import pandas as pd


def read_csv(csv_path):
	df = pd.read_csv(csv_path)
	return df

def fill_zero(df):
	df['id'] = df['id'].astype(str).str.zfill(6)

	return df

def get_stock(df, stock_id):
	"""
	df: pandas dataframe
	col_list: list of column name want to fetch
	"""
	stock = df.loc[df['id'] == stock_id]

	return stock

def select_column(df, col_list):
	"""
	df: pandas dataframe
	col_list: list of column name want to fetch
	"""
	output = pd.DataFrame(stock[col_list[0]])

	for col in col_list[1:]:
		output[col] = stock[col]

	return output

def select_date(df, start='', end='2019-12-31', span=-1):
	"""
	start: start date
	end: end date
	span: fetch how many days before end date. Start date will not be used if span is used
	"""

	df['date'] = pd.to_datetime(df['date'])
	if start != '':
		start_date = pd.to_datetime(start)

	end_date = pd.to_datetime(end)

	if span == -1:
		output = df.loc[(df['date'] > start_date) & (df['date'] <= end_date)]
	else:
		idx = df.index[df['date'] == end_date][0].astype(int)
		import ipdb; ipdb.set_trace()
		output = df.iloc[idx - 29:idx+1]

	return output

if __name__ == '__main__':
	df = read_csv('/Users/haomeng/Workspace/CSCI544GroupProject/CSCI544Project/output.csv')
	df = fill_zero(df)

	stock = get_stock(df, '000001')
	stock = select_column(stock, ['date', 'close', 'id'])
	stock = select_date(stock, span=30)


	print(stock)











