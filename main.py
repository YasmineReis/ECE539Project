import pandas as pd
import numpy as np
import csv

#read in original dataframe
df =  pd.read_csv(r'autos.csv')

#selecting only the columns we care about
df = df[['price','vehicleType','yearOfRegistration','gearbox','powerPS','model',
        'kilometer','fuelType','brand','notRepairedDamage','dateCreated','postalCode']]

#cleaning data, removing incomplete rows
df = df[df['price']!=0] #removing rows where price is 0
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
lst2=['andere','bus','limousine']
df = df[df.vehicleType.isin(lst2) == False]

#should now be at 127,361 rows
print(df)

#CLEAN, READY TO VISUALIZE







