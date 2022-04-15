import pandas as pd
import numpy as np
import sqlalchemy 

df1 = pd.DataFrame({
    "city": ["new york", "chicago", "texas", "san fransisco"],
    "temparature":[23,24,25, 36]
})

df2 = pd.DataFrame({
    "city":["chicago", "new york", "orlands", "baltimore"],
    "humudity":[65,69,75, 55]
})


weather = pd.DataFrame({
    "city" : ["new york", "new york", "new york", "mumbai", "mumbai", "mumbai", "beijing", "beijing", "beijing"],
    "date" : ["5/1/2017", "5/2/2017", "5/3/2017","5/1/2017", "5/2/2017", "5/3/2017", "5/1/2017", "5/2/2017", "5/3/2017"],
    "temperature" : [65,66,68,75,76,82,80,77,79],
    "humidity" : [56,58,60,80,83,85,26,30,35]
})

# print(weather.pivot(index="date", columns="city", values="humidity")) #we can change column name and observe changes as per requirment


# print(weather.pivot_table( index="city", columns="date")) 
# is same as 
# print(pd.pivot_table(weather, index="city", columns="date", aggfunc="count"))

# weather["date"] = pd.to_datetime(weather["date"])


# print(pd.pivot_table(weather,index=pd.Grouper(freq='M', key="date"), columns="city"))


weather1 = pd.DataFrame({
    "day" : ["Monday", "Tueday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "chicago" : [32,30,28,22,30,20,25],
    "chennai" : [75,77,75,82,83,81,77],
    "berlin" : [41,43,45,38,30,45,47]
})

df1 = (weather1.melt(id_vars=["day"], var_name = "city", value_name="temperature"))
# print(df1)


t = pd.read_excel("./temp.xls")
t1 = pd.DataFrame(t)
print(pd.crosstab(t1.Country, t1.Gender, values=t1.Age, aggfunc=np.average))


engine = sqlalchemy.create_engine("postgresql://postgres:sunny123@localhost:5432/postgre_flask")

df = pd.read_sql_table("user_details", engine)
print(df)