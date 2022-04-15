from ipaddress import collapse_addresses
from numpy import dtype
import pandas as pd
from sqlalchemy import column
# import openpyxl

# d = pd.read_excel("./sample.xls")
# # d = pd.read_csv("./age.csv")
# df = pd.DataFrame(d)
# print(df)
# print(df[0])

# data = openpyxl.load_workbook("./sample.xlsx")

# s = data.active


# for i in range(1, s.max_row +1):
    
#     for j in range(1, s.max_column+1):
#         cell = s.cell(row=i, column=j)
#         print(cell.value, end=" ")
#     print()
    

# df = pd.DataFrame(d)

# print(s.map({10:25, 30:35, 50:55}))

# print(s.name)
# print(s.array)
# print(s.values)
# print(s.index)
# print(s.dtype)
# print(s.ndim)
# print(s.nbytes)
# print(s.memory_usage(index=False))
# print(s.empty)
# print(s)

# s = pd.Series([10,20,30,40,50])
# s1 = pd.Series([20,22,25,33,43])
# print(s.add(s1))

# d = pd.read_excel("./sample.xls")

# df = pd.DataFrame(d)
# print(df.describe())
# print(df.columns)

# print(df.shape)
# print(df[["Age","Id","First Name"]].head())

# print(df[1:10:2])

# print(df[df["Age"] > 25])

# print(df.loc[1])

# for index, row in df.iterrows():
#     print(index, row[['First Name', "Last Name"]])

# print(df.loc[df["First Name"] == "Dulce"])

# print(df.sort_values(["First Name", "Age"], ascending=[1,0]))

# df["Full Name"]=df["First Name"] +" "+ df["Last Name"]
# print(df)

# df = df.drop(columns="Full Name")
# print(df)

# df.to_excel("/home/vy/new.xlsx")

# print(df.loc[0:3, "First Name": "Age"])



# d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
#    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

# df = pd.DataFrame(d)
# print(df)






# d = pd.read_excel("./sample.xls")
# df = pd.DataFrame(d)
#selecting specific columns from the dataframe, this is one way of doing it by using column names. 
# print(df[["First Name", "Age"]].head())

#selecting specific columns based on str methods
# print(df.loc[:, df.columns.str.endswith("e")])


# renaming multiple columns at once by using rename() method
# df = df.rename(
#     columns={
#         "First Name" : "First_Name",
#         "Last Name" : "Last_Name"
#     }
# )

# print(df)

d = pd.read_excel("./sample.xls", parse_dates=["Date"])
df = pd.DataFrame(d)
print(df[df["Date"] =="2016-08-16" & df["Date"]=="2017-10-15"])


# group_data = df.groupby("Country")

# for a, b in group_data:
#     print(a)
#     print(b)


