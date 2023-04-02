
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


#read in original dataframe
df =  pd.read_csv(r'autos.csv')

#selecting only the columns we care about
df = df[['price','vehicleType','yearOfRegistration','gearbox','powerPS','model',
        'kilometer','fuelType','brand','notRepairedDamage','dateCreated','postalCode']]

#cleaning data, removing incomplete rows
df = df[df['price']>500] #removing rows where price less than $10
df = df[df['price']<100000] #removing price outliers over $100k
df = df[df['powerPS']!=0] #removing rows where horsepower is 0
df = df.dropna() #removing all NaN values

#should now be at 257,567 rows
#print(df)


#removing unpopular car brands
#print(df['brand'].unique())
lst = ['skoda','seat','daewoo','trabant','lada','opel']
df = df[df.brand.isin(lst) == False]

#should now be at 213,740 rows
#print(df)

#removing buses and "andere"(other) from car type
#print(df['vehicleType'].unique())
lst2=['andere','bus']
df = df[df.vehicleType.isin(lst2) == False]

#should now be at 184,096 rows
#print(df)
#CLEAN, READY TO VISUALIZE

#scatterplot of price vs year of registration
#df.plot.scatter(x = "price", y = "yearOfRegistration")
#plt.show()

#df.plot.scatter(x = "brand", y = "price")
#plt.show()


