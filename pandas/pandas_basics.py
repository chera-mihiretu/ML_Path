import pandas as pd

array  = list(range(4))

# shows index and values in table format
series = pd.Series(array)

print(series)

## this will set the data into table format
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'San Francisco', 'Los Angeles']}

series1 = pd.DataFrame(data)

print(series1)

## this will set the data into table format
new_data = {'Data1' : {"Another Data" : [1, 2, 3, 4], 'Next' : {"Data" : {"Data another": [1,1,1,1]}}}}

series2 = pd.DataFrame(new_data)

print(series2)

######################################################

load_data = pd.read_csv('my_data.csv')

print(load_data)
