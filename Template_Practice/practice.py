import pandas as pd
import numpy as np
from datetime import datetime

data = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
                    , index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# print(data[(data['attempts']<2)  & (data['score']>15)])

# print(data['score'].mean())

# data.loc['k'] = [ 'Suresh',15.5,1, 'yes']  #adding row
# data.sort_values(by=['name','score'], ascending=[0, 1])

# data.columns=["col1", "col2","col3","col4"]
# print(data.loc[data["attempts"]== 2])         retrieving particular row
# data.loc["x"] = ["goutham", 44, 1, "yes"]

# d = data.groupby(["name"]).size().reset_index(name='attempts')

# print(data.iloc[::2])         getting alternate rows in the table

# data = data["attempts"].astype(float)
# print(data)

# df = pd.DataFrame([1000, 2000, 3000, -4000, np.inf, -np.inf])  replacing neagtive values from DF

# df.replace([np.inf, -np.inf], np.nan)

# print(df)

# data.insert(loc=0, column='col1', value=[1,2,3,4,5,6,7,8,9,10])  inser

# print(data)

# data = data.groupby('attempts')['name'].apply(list) # grouping attempts column as first col and names as second column 
# print(data)
# col = data.columns
# print(len(col))  #col len
# print(len(data.index)) #row len

# print(data.loc[:,data.columns != "name"]) #displaying data without specified column


# d1 = data.nlargest(4, 'attempts') #to get topmost n records within each group of a DataFrame
# print(d1)


# print(data.add_prefix("A_")) # adding the pefix to our col names
# print(data.add_suffix("_X")) # adding the suffic to our col names

# print(data.loc[:,::-1])  #reverse printing of the columns

# print(data.loc[::-1,:]) #reverse printing of the rows


# print(data.reset_index())

# print(data.select_dtypes(include='object')) #fetching the columns with specified datatypes
# print(data.select_dtypes(include='number'))
# print(data.select_dtypes(include="string"))


# d = data.sample(frac=0.5) 
# print(d)

# print(d.shape)

# data.columns= data.columns.str.capitalize() #captializesing the col names of the DF
# print(data)

# rang = pd.date_range(start="1/2/2022", end="6/6/2022", freq ='B')
# print(rang)



df1 = pd.DataFrame({
    "city": ["new york", "chicago", "texas", "san fransisco"],
    "temparature":[23,24,25, 36]
})

df2 = pd.DataFrame({
    "city":["chicago", "new york", "orlands", "baltimore"],
    "humudity":[65,69,75, 55]
})

# print(df1)
# print(df2)

df3 = pd.merge(df1, df2, on="city")
    # pd.merge(df1, df2, on="city" how="left", indicator = True) common + left df and due to indicator a merge  col gets added in df and tell us the what kind of join has been performed.
    # pd.merge(df1, df2, on="city" how="right") common +right df
    # pd.merge(df1, df2, on="city" how="outer")  both

#if we have same columns we will have suffic of "x" for left df cols and "y" for right df cols

# print(df3)


# with pd.ExcelWriter('testing.xlsx') as writer:  to write the output in mutltiple sheets of excel 
#     df1.to_excel(writer, sheet_name="df1")
#     df2.to_excel(writer, sheet_name="df2")

sr1 = pd.Series(['php', 'python', 'java', 'c#', 'c++'])
sr2 = pd.Series([1, 2, 3, 4, 5])
print(sr1)
# df4 = pd.concat([sr1, sr2], axis=1 )
# print(df4)

df4 = pd.DataFrame({"col1" : sr1, "col2": sr2})
# print(df4)

# df5 = pd.util.testing.makeDataFrame() #deprecated feature but generates same data for 30 rows and 5 colums including an index column
# df6 = pd.util.testing.makeDataFrame()

df4['date'] = pd.date_range(start="1/1/2022", periods=5) #adding column to existing Dataframe. and their are 5 ways to add a column to existing dataframe

# print(df4)
# print(data)

# print(data.interpolate())


t = pd.read_excel("./weather.xls")
t = t.interpolate()
t1 = pd.DataFrame(t)

print(t1)
# t2 = t1.set_index("Age") 
t1.index.name = "index" # giving name to a index column
# print(t1)

# date_of_birth = ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997','11/05/2002','15/09/1997','15/09/1997'] 

# t1.insert(loc=3, column="DOB", value=date_of_birth)
# print(t1)

# t1.drop(['DOB'], axis=1)
# print(t1)

# t1["First Name"] = list(map(lambda x: x.to_lower(), t1["First Name"]))
# print(t1)

# print(t1)


# print(t1.to_string(index=False))

sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'],
          ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]

# print(sales_arrays)
sales_index = pd.MultiIndex.from_arrays(sales_arrays, names=['sales', 'cities'])  #creating multi index for 2 columns

s = pd.Series(np.random.rand(8),   index= sales_index)
# print(s)


# cols = pd.MultiIndex.from_tuples([("a", "x"), ("a", "y"), ("a", "z")])

# df7 = pd.DataFrame([[1,2,3], [3,4,5], [5,6,7]], columns=cols)

# print(df7)

# df7.columns = df7.columns.droplevel(0)
# print(df7)


# print(pd.Timestamp("2022-12-10 12:22").date())

# print(t1)

g = t1.groupby("Country") #works like groupby in sql 

# for a,b in g:     iterate through and get back values
#     print(a)
#     print(b)

india_weather = pd.DataFrame({
    "city" : ["mumbai", "delhi", "banglore"],
    "temperature" : [33,45,30],
    "humidity": [80,60,70] 
})

us_weather = pd.DataFrame({
    "city" : ["new york", "chicago", "orlando"],
    "temperature" : [21,12,35],
    "humidity": [68,65,75] 
})
print(us_weather)
h = pd.concat([india_weather, us_weather], ignore_index=True)#ignore_index is for index continuation
# print(h)

based_on_key = pd.concat([india_weather, us_weather], keys=["india", "us"]) #maintaining an another column based on country which would be helpfu for future filtering

# print(based_on_key.loc["india"])

# print(pd.concat([india_weather, us_weather], axis=1))



