# importing packages
import numpy as np
import pandas as pd
from pandas import Series

# Series
# A series is a 1d array with axis labels (an index)
# Creating a series from a list
x = pd.Series([10,20,30,40,50])
# When we print the series, we get the index, the data and the data type
print(x)
# output:
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

# We can access the different components separately:
# Accessing the index
print(x.index) # output = RangeIndex(start=0, stop=5, step=1)
# Accessing the values
print(x.values) # output = [10 20 30 40 50]
# Accessing the data type - note series cannot store multiple data types
print(x.dtype) # output = int64

# Creating a series with an index
data = [450,650,870]
Sales = Series(data, index=['Don', 'Mike', 'Edwin'])
print(Sales)
# output
# Don      450
# Mike     650
# Edwin    870
# dtype: int64

# We can check the type of Sales, which is a Series
print(type(Sales)) # output = <class 'pandas.core.series.Series'>

# When checking the values of the Series we get the values back. This is becasue they are strings and not ints
print(Sales.index) # output = Index(['Don', 'Mike', 'Edwin'], dtype='object')

# Accessing Values

# Accessing a value using a name
print(Sales['Don']) # output = 450
# Accessing values using a potential index
print(Sales[0]) # output = 450

# Checking for conditions

# We can filter our data based on conditions we specify, we can use booleans to do this
# If we want sales greater than 500:
# Note, doing this returns booleans
print(Sales>500)
# Output
# Don      False
# Mike      True
# Edwin     True
# dtype: bool

# What happens when we use these booleans?
# We can use them to filter data and show data that is True
print(Sales[[False, True, True]])
# Output
# Mike     650
# Edwin    870
# dtype: int64

# To return values that are greater than 500, we need to use these booleans
print(Sales[Sales>500])
# Output
# Mike     650
# Edwin    870
# dtype: int64

# Checking names in the index
print('Don' in Sales) # output = True
# Below will not be true as it is not in the Index
print('Sally' in Sales) # output = False
# Below will also be False, it is a value and thus not in the Index
print(450 in Sales) # output = False

# Working with Dictionaries

# Converting a Series to a Dict
sales_dict = Sales.to_dict()
print(sales_dict) # output = {'Don': 450, 'Mike': 650, 'Edwin': 870}

# Converting a Dict to a Series
sales_ser = Series(sales_dict)
print(sales_ser)
# output
# Don      450
# Mike     650
# Edwin    870
# dtype: int64

# Adding entries and working with NaN/null values

# We can create a new Series from already existing Series
# If we specify name sin the Index that were not there already, NaN values will be assigned
# What is NaN? - Not a Number
new_sales = Series(Sales, index=['Don', 'Mike', 'Sally', 'Edwin', 'Lucy'])
print(new_sales)
# output
# Don      450.0
# Mike     650.0
# Sally      NaN
# Edwin    870.0
# Lucy       NaN
# dtype: float64

# Checking if entries are NaN
print(np.isnan(new_sales['Sally'])) # output = True

# NaN is different to None
print(new_sales['Sally'] is None) # output = False

# We can use isnan on the entire Series
print(np.isnan(new_sales))
# output
# Don      False
# Mike     False
# Sally     True
# Edwin    False
# Lucy      True
# dtype: bool

# Checking for null values using pandas
print(pd.isnull(new_sales))
# output
# Don      False
# Mike     False
# Sally     True
# Edwin    False
# Lucy      True
# dtype: bool

# Naming components in a Series

# Naming an Index
Sales.index.name = "Sales person"
print(Sales)
# output
# Sales person
# Don      450
# Mike     650
# Edwin    870
# dtype: int64

# Naming a Series
Sales.name = "Total TV sales"
print(Sales)
# output
# Sales person
# Don      450
# Mike     650
# Edwin    870
# Name: Total TV sales, dtype: int64

# Dataframes






