# importing packages
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

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

# Dataframes are 2d, size-mutable, potentially diverse tabular data structures.
# This data structure contains labeled axes (rows and columns)

# Creating Dataframes

# Creating a Dataframe from a list
data = [["Adrian",20], ["Bethany", 23], ["Chloe", 41]]

# As we create a Dataframe, we can specify what column names are, and what the type of data is
df = pd.DataFrame(data, columns=["Name", "Age"], dtype=int)
print(df)
# output
#       Name  Age
# 0   Adrian   20
# 1  Bethany   23
# 2    Chloe   41

# Creating a Dataframe from a Dict
new_dict = {"Name":["Tom", "Jane", "Steve", "Lucy"], "Sales":[250, 300, 350, 400]}
# Note, we are not specifying column names. Column names are automatically assigned from the Keys
df_dict = pd.DataFrame(new_dict)
print(df_dict)
# output
#     Name  Sales
# 0    Tom    250
# 1   Jane    300
# 2  Steve    350
# 3   Lucy    400

# Adding a custom index
# So far we have created Dataframes with a default index
# We can use the index parameter to add an index
df_dict_index = pd.DataFrame(new_dict, index=["rank1", "rank2", "rank3", "rank4"])
print(df_dict_index)
# output
#         Name  Sales
# rank1    Tom    250
# rank2   Jane    300
# rank3  Steve    350
# rank4   Lucy    400

# Creating a Dataframe from a list of Dict's
# This is the same data we had previously, but in a different format
dict_list = [{"Name": "Tom", "Sales": 250}, {"Name": "Jane", "Sales": 300}, {"Name": "Steve", "Sales": 350}, {"Name": "Lucy", "Sales": 400}]
df_dict_list = pd.DataFrame(dict_list)
print(df_dict_list)
# output
#     Name  Sales
# 0    Tom    250
# 1   Jane    300
# 2  Steve    350
# 3   Lucy    400

# Creating a Dataframe from a Dict of Series
east = pd.Series([1000, 1200, 3400], index=["Q1", "Q2", "Q3"])
west = pd.Series([1100, 1300, 2400, 3500], index=["Q1", "Q2", "Q3", "Q4"])
print(east)
print(west)
# Currently output separately

# If we have a Series we want to put into a Dataframe, we can easily combine them together
# If we wanted a Dataframe from a single Series, we can do that by passing in the single Series
df_region = pd.DataFrame({"East": east, "West": west})
print(df_region)
# output
#       East  West
# Q1  1000.0  1100
# Q2  1200.0  1300
# Q3  3400.0  2400
# Q4     NaN  3500

# Once we have a Dataframe, we can easily add Series on:
df_region["North"] = [2000, 3000, 2500, 4000]
df_region["South"] = [2000, 3000, 2500, 4000]
print(df_region)
# output
#    East  West  North  South
# Q1  1000.0  1100   2000   2000
# Q2  1200.0  1300   3000   3000
# Q3  3400.0  2400   2500   2500
# Q4     NaN  3500   4000   4000

# Shifting and changing the Index

# If we make a mistake and need to set a new index, we can add a new column
# And se that new column as the index
years = ["2016", "2017", "2018", "2019"]
df_region["Years"] = years
print(df_region)
# output
#       East  West  North  South years
# Q1  1000.0  1100   2000   2000  2016
# Q2  1200.0  1300   3000   3000  2017
# Q3  3400.0  2400   2500   2500  2018
# Q4     NaN  3500   4000   4000  2019

# We can use set_index to set the index to a different column in the Dataframe
df_region = df_region.set_index("Years") # Beware capitalisation
print(df_region)
# output
#          East  West  North  South
# Years
# 2016   1000.0  1100   2000   2000
# 2017   1200.0  1300   3000   3000
# 2018   3400.0  2400   2500   2500
# 2019      NaN  3500   4000   4000

# To use different index values, we can use reindex
# reindex will shift our index
new_df = df_region.reindex(["2017", "2018", "2019", "2020", "2021"])
print(new_df)
# output
# Years
# 2017   1200.0  1300.0  3000.0  3000.0
# 2018   3400.0  2400.0  2500.0  2500.0
# 2019      NaN  3500.0  4000.0  4000.0
# 2020      NaN     NaN     NaN     NaN
# 2021      NaN     NaN     NaN     NaN

# reindex can also be used on columns
# Columns can be shifted or new columns can be added if we add a name that was not present before
re_indexed = new_df.reindex(columns=["North", "East", "South", "New"])
print(re_indexed)
# output
#         North    East   South  New
# Years
# 2017   3000.0  1200.0  3000.0  NaN
# 2018   2500.0  3400.0  2500.0  NaN
# 2019   4000.0     NaN  4000.0  NaN
# 2020      NaN     NaN     NaN  NaN
# 2021      NaN     NaN     NaN  NaN

# Missing Data

# Filling in missing values
# We may to change all NaN values to 0 (or any specific number)
# This will be espcially useful when working with certain types of algorithm
# Some algorithms cannot deal with NaN values

print(re_indexed.fillna(0)) # Note, we are not actually assigning this to a new Dataframe


# If we don't want to fill with a single value we can change the fill method
# Methods we can pick up from - 'backfill', 'bfill, 'pad', 'ffill'
# These methods will take the last available value and carry it to the next item
print(re_indexed.fillna(method="ffill"))


# We can also use interpolation
# The default method is linear, this can be changed if needed
print(re_indexed.interpolate())

# Dropping items in Dataframes

# If we don't want to fill NaN values, we can drop instead

# dropna() on its own will drop anything that contains any NaN values
# We might not want to do this, we can specify more parameters
# print(re_indexed.dropna())
# output
# Empty DataFrame
# Columns: [North, East, South, New]
# Index: []

# We can specify columns and methods

# axis 1 = columns, axis 0 = rows
# how- "all"=If all values are NA, drop row/column, "any"=If any NA values are present, drop row/column
# print(re_indexed.dropna(axis=1, how="all"))
# output
# Years
# 2017   3000.0  1200.0  3000.0
# 2018   2500.0  3400.0  2500.0
# 2019   4000.0     NaN  4000.0
# 2020      NaN     NaN     NaN
# 2021      NaN     NaN     NaN

# We can also set a threshold: int - replace that many non-NA values
# re_indexed.dropna(thresh=1)
# output
#         North    East   South  New
# Years
# 2017   3000.0  1200.0  3000.0  NaN
# 2018   2500.0  3400.0  2500.0  NaN
# 2019   4000.0  3400.0  4000.0  NaN
# 2020   4000.0  3400.0  4000.0  NaN
# 2021   4000.0  3400.0  4000.0  NaN

# When we set the threshold to 3, 2019 is dropped as it only has 2 non-NA values
# print(re_indexed.dropna(thresh=3))
# output
#         North    East   South  New
# Years
# 2017   3000.0  1200.0  3000.0  NaN
# 2018   2500.0  3400.0  2500.0  NaN

# Dropping based on index
print(re_indexed.drop("2019"))
# output
#         North    East   South  New
# Years
# 2017   3000.0  1200.0  3000.0  NaN
# 2018   2500.0  3400.0  2500.0  NaN
# 2020      NaN     NaN     NaN  NaN
# 2021      NaN     NaN     NaN  NaN

# We can easily check for and remove duplicated rows
# We need to create a Dataframe with duplicates first to demonstrate this
df_dup = DataFrame([["A", 1], ["B", 2], ["A", 1]])
print(df_dup)
# output
#    0  1
# 0  A  1
# 1  B  2
# 2  A  1

# Finding the duplicate rows
# duplicated() returns a boolean series denoting duplicate rows
print(df_dup.duplicated())
# output
# 0    False
# 1    False
# 2     True
# dtype: bool

# By default inplace is False (meaning the DF does not change)
# To change the DF permanently specify inplace = True
# df_dup.drop_duplicates(inplace=True)
# print(df_dup)
# output
#    0  1
# 0  A  1
# 1  B  2

# Selecting entries

# Back to using new_df
print(new_df)
# output
# East    West   North   South
# Years
# 2017   1200.0  1300.0  3000.0  3000.0
# 2018   3400.0  2400.0  2500.0  2500.0
# 2019      NaN  3500.0  4000.0  4000.0
# 2020      NaN     NaN     NaN     NaN
# 2021      NaN     NaN     NaN     NaN

# Select an entire column by using column name
print(new_df["North"])
# output
# Years
# 2017    3000.0
# 2018    2500.0
# 2019    4000.0
# 2020       NaN
# 2021       NaN
# Name: North, dtype: float64

# iloc
# iloc lets us find the a record based on integer indexing - useful if we want to return a row
# In this case, location 2 corresponds to the row of 2019
print(new_df.iloc[2])
# output
# East        NaN
# West     3500.0
# North    4000.0
# South    4000.0
# Name: 2019, dtype: float64

# Using iloc to find specific values
# In this example, the first row (2017) is selected and then the second column (West)
print(new_df.iloc[0, 1]) # output = 1300.0

# We can use slicing with iloc
# In this example we are interested in the Years 2018-2019 (positions 1 and 2)
print(new_df.iloc[1:3])
# output
#          East    West   North   South
# Years
# 2018   3400.0  2400.0  2500.0  2500.0
# 2019      NaN  3500.0  4000.0  4000.0

# Loc
# Loc lets us access a group of rows and columns based on Labels or a boolean array
# This is useful when we know the index name but not the position of the row we are interested in
print(new_df.loc["2019"])
# output
# East        NaN
# West     3500.0
# North    4000.0
# South    4000.0
# Name: 2019, dtype: float64

# We can use loc to select multiple rows
print(new_df.loc[["2018", "2019"]])
# output
#          East    West   North   South
# Years
# 2018   3400.0  2400.0  2500.0  2500.0
# 2019      NaN  3500.0  4000.0  4000.0

# Using boolean arrays with loc
# For each row, we specify True or False depending on whether we want them returned or not
print(new_df.loc[[False, False, True, True, True]])
# output
#        East    West   North   South
# Years
# 2019    NaN  3500.0  4000.0  4000.0
# 2020    NaN     NaN     NaN     NaN
# 2021    NaN     NaN     NaN     NaN

# Data Alignment
# We can add Series and columns in DataFrames together.
# Since Series are made up of singular columns, it is easy to add them togehter, with DataFrames there is an additional step of specifying the column to add.
# These examples will add DataFrame columns (Note that for Series, this will work the same, without having to input the column names).

# Adding two columns in one Dataframe
print(new_df["East"] + new_df["North"])
# Output
# Years
# 2017    4200.0
# 2018    5900.0
# 2019       NaN
# 2020       NaN
# 2021       NaN
# dtype: float64

# We can use .add to be able to specify a fill value for NaN
# 2019 will now have a value because the NaN in one of the columns was filled to 0
# Results of two NaN columns will remain as NaN
print(new_df["East"].add(new_df["North"], fill_value=0))
# Ouput
# Years
# 2017    4200.0
# 2018    5900.0
# 2019    4000.0
# 2020       NaN
# 2021       NaN
# dtype: float64

# Sorting and Ranking

# Sorting by index
# ascending: 1 True, 0 False
print(new_df.sort_index(ascending=0))
#          East    West   North   South
# Years
# 2021      NaN     NaN     NaN     NaN
# 2020      NaN     NaN     NaN     NaN
# 2019      NaN  3500.0  4000.0  4000.0
# 2018   3400.0  2400.0  2500.0  2500.0
# 2017   1200.0  1300.0  3000.0  3000.0

# Sorting by column
# Default is ascending, to change, add the parameter like in the previous example
print(new_df.sort_values(by=["North"]))
# Output
#          East    West   North   South
# Years
# 2018   3400.0  2400.0  2500.0  2500.0
# 2017   1200.0  1300.0  3000.0  3000.0
# 2019      NaN  3500.0  4000.0  4000.0
# 2020      NaN     NaN     NaN     NaN
# 2021      NaN     NaN     NaN     NaN

# Ranking columns
# First we need to specify the column, and then we can apply the rank function to it
print(new_df["North"].rank(ascending=0))
# Output
# Years
# 2017    2.0
# 2018    3.0
# 2019    1.0
# 2020    NaN
# 2021    NaN
# Name: North, dtype: float64

# We can save the rank as a new column if needed
new_df["rank_north"] = new_df["North"].rank(ascending=0)
print(new_df)
# Output
#          East    West   North   South  rank_north
# Years
# 2017   1200.0  1300.0  3000.0  3000.0         2.0
# 2018   3400.0  2400.0  2500.0  2500.0         3.0
# 2019      NaN  3500.0  4000.0  4000.0         1.0
# 2020      NaN     NaN     NaN     NaN         NaN
# 2021      NaN     NaN     NaN     NaN         NaN

# Summary Statistics

# Describe
# Probably the most useful - gives us general summary statistics for entire DataFrame
print(new_df.describe())
# Output
#               East    West        North        South  rank_north
# count     2.000000     3.0     3.000000     3.000000         3.0
# mean   2300.000000  2400.0  3166.666667  3166.666667         2.0
# std    1555.634919  1100.0   763.762616   763.762616         1.0
# min    1200.000000  1300.0  2500.000000  2500.000000         1.0
# 25%    1750.000000  1850.0  2750.000000  2750.000000         1.5
# 50%    2300.000000  2400.0  3000.000000  3000.000000         2.0
# 75%    2850.000000  2950.0  3500.000000  3500.000000         2.5
# max    3400.000000  3500.0  4000.000000  4000.000000         3.0

# Finding the totals of all columns
print(new_df.sum())
# Output
# East          4600.0
# West          7200.0
# North         9500.0
# South         9500.0
# rank_north       6.0
# dtype: float64

# Cumulative Sum
print(new_df.cumsum())
# Output
#          East    West   North   South  rank_north
# Years
# 2017   1200.0  1300.0  3000.0  3000.0         2.0
# 2018   4600.0  3700.0  5500.0  5500.0         5.0
# 2019      NaN  7200.0  9500.0  9500.0         6.0
# 2020      NaN     NaN     NaN     NaN         NaN
# 2021      NaN     NaN     NaN     NaN         NaN

# Minimum values in each column
print(new_df.min())
# Output
# East          1200.0
# West          1300.0
# North         2500.0
# South         2500.0
# rank_north       1.0
# dtype: float64

# Maximum values in each column
print(new_df.max())
# Output
# East          3400.0
# West          3500.0
# North         4000.0
# South         4000.0
# rank_north       3.0
# dtype: float64

# Index Hierarchy

# Creating a DataFrame with a hierarchical index
# We are using numpy arange to create a range of numbers,
# and re-shaping it so that the numbers will fit on a 4x4 grid

df_temp = DataFrame(np.arange(16).reshape(4,4), index = [["2018", "2018", "2019", "2019"], ["Jan", "Feb", "Jan", "Feb"]], columns= [["NY", "NY", "LA", "LA"], ["Cold", "Hot", "Cold", "Hot"]])
print(df_temp)
# Output
#            NY       LA
#          Cold Hot Cold Hot
# 2018 Jan    0   1    2   3
#      Feb    4   5    6   7
# 2019 Jan    8   9   10  11
#      Feb   12  13   14  15

# We can add index and columns names
df_temp.index.names=["Year", "Month"]
df_temp.columns.names=["State", "Temp"]
print(df_temp)
# Output
# State        NY       LA
# Temp       Cold Hot Cold Hot
# Year Month
# 2018 Jan      0   1    2   3
#      Feb      4   5    6   7
# 2019 Jan      8   9   10  11
#      Feb     12  13   14  15

# Using swaplevel to swap levels on a particular axis
# axis - 0 or Ã¢Â€Â˜indexÃ¢Â€Â™, 1 or Ã¢Â€Â˜columnsÃ¢Â€Â™
print(df_temp.swaplevel("State", "Temp", axis=1))
# Output
# Temp       Cold Hot Cold Hot
# State        NY  NY   LA  LA
# Year Month
# 2018 Jan      0   1    2   3
#      Feb      4   5    6   7
# 2019 Jan      8   9   10  11
#      Feb     12  13   14  15

# Sorting based on the first level of the index
print(df_temp.sort_index(level=0))
# Output
# State        NY       LA
# Temp       Cold Hot Cold Hot
# Year Month
# 2018 Feb      4   5    6   7
#      Jan      0   1    2   3
# 2019 Feb     12  13   14  15
#      Jan      8   9   10  11

# Sorting by the second level of the index
print(df_temp.sort_index(level=1))
# Output
# 	State	NY	LA
# Temp	Cold	Hot	Cold	Hot
# Year	Month
# 2018	Feb	4	5	6	7
# 2019	Feb	12	13	14	15
# 2018	Jan	0	1	2	3
# 2019	Jan	8	9	10	11

# Accessing single columns in a multi-index, note there is no comma
print(df_temp["NY"]["Cold"])
# Output
# Year  Month
# 2018  Jan       0
#       Feb       4
# 2019  Jan       8
#       Feb      12
# Name: Cold, dtype: int32

# Accessing single columns
# We can still use iloc with a multi-index
print(df_temp.iloc[0])
# Output
# State  Temp
# NY     Cold    0
#        Hot     1
# LA     Cold    2
#        Hot     3
# Name: (2018, Jan), dtype: int32

# This is how we can use loc
print(df_temp.loc["2018", "Jan"])
# Output
# State  Temp
# NY     Cold    0
#        Hot     1
# LA     Cold    2
#        Hot     3
# Name: (2018, Jan), dtype: int32

# END









