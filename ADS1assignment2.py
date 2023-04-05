# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:33:31 2023

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def data_climate_change(filename):
    #load the dataset into a pandas dataframe with years as columns
    data = pd.read_csv(filename, skiprows=4)
    data_t = pd.DataFrame.transpose(data)
    data_t = data_t.drop(['Country Code', 'Indicator Code',], axis=0)
    data_t.columns = data_t.iloc[0]
    data_t2 = data_t.iloc[1:]
    
    return data, data_t2
data, data_t2 = data_climate_change('world_climate_data.csv')
print(data)
print(data_t2)

# For this analysis, we will make do with 4 indicators of choice
df_indicators = data[data['Indicator Name'].isin(['Forest area (% of land area)','Urban population',
                                                  'CO2 emissions (kt)','Total greenhouse gas emissions (kt of CO2 equivalent)'])]

print(df_indicators.head())

# for a better analysis i will be transposing the data
data = pd.DataFrame.transpose(df_indicators) 
# then turn the country name as columns.
data.columns=data.iloc[0]
# dropping rows not needed from the data
data = data.drop(['Country Name','Country Code','Indicator Code'])
#selected countries from each continents of the world for the analysis
country = data[['China', 'United States','Australia','Nigeria', 'Germany','Brazil']]
# dropping all missing values from our datasets
country.dropna(inplace=True)
country.index

print(country)


"""
for further accessibilty and ease of data analysis, datasets that combines all 
countries on each indicator will be created in five years increments from 2000 to 2019
"""
# Creating a dataframe for all selected countries on Urban population
df_urban_pop = country.iloc[11:,[0,4,8,12,16,20]]
df_urban_pop = df_urban_pop.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
df_urban_pop.index = pd.to_numeric(df_urban_pop.index) # converting index values to numeric format

"""
Statistical overview for the urban population across selected countries.
Applying Statistical function for the four selected indicators 
across the 7 selected countries.
"""
#statistical function for urban population
print(df_urban_pop.describe())
print(df_urban_pop.mean()) # checking the mean urban population
print(df_urban_pop.median()) # checking the median urban population
print(df_urban_pop.std()) # checking the urban population standard deviation

# Creating a dataframe for all selected countries on Urban population
df_Tot_green_house = country.iloc[11:,[1,5,9,13,17,21]]
df_Tot_green_house = df_Tot_green_house.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
df_Tot_green_house.index = pd.to_numeric(df_Tot_green_house.index) # converting index values to numeric format


"""
Statistical overview for the urban population across selected countries.
Applying Statistical function for the four selected indicators 
across the 7 selected countries.
"""
#statistical function for Total Green House emmision
print(df_Tot_green_house.describe())
print(df_Tot_green_house.mean()) # checking the mean Total Green House emmision
print(df_Tot_green_house.median()) # checking the median Total Green House emmision
print(df_Tot_green_house.std()) # checking the Total Green House emmision standard deviation

# Creating a dataframe for all selected countries on Urban population
df_CO2_emm = country.iloc[11:,[2,6,10,14,18,22]]
df_CO2_emm = df_CO2_emm.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
df_CO2_emm.index = pd.to_numeric(df_CO2_emm.index) # converting index values to numeric format
df_CO2_emm

#statistical function for CO2 emmision
print(df_CO2_emm.describe())
print(df_CO2_emm.mean()) # checking the mean CO2 emmision
print(df_CO2_emm.median()) # checking the median CO2 emmision
print(df_CO2_emm.std()) # checking the CO2 emmision standard deviation

# Creating a dataframe for all selected countries on Forest Area
df_forest_area = country.iloc[11:,[3,7,11,15,19,23]]
df_forest_area = df_forest_area.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
df_forest_area.index = pd.to_numeric(df_forest_area.index) # converting index values to numeric format
df_forest_area


#statistical function for Forest Area
print(df_forest_area.describe())
print(df_forest_area.mean()) # checking the mean Forest Area
print(df_forest_area.median()) # checking the median Forest Area
print(df_forest_area.std()) # checking the Forest Area standard deviation


"""
Plotting a grouped bar of CO2 emission for the 7 nations  in 5 years increments
from the year 1990 to 2010 
"""

df_CO2_emm = df_CO2_emm.iloc[10:, :]
ddf_CO2_emm = df_CO2_emm.apply(pd.to_numeric) # converting to dataframe data type to a numeric format
df_CO2_emm.index = pd.to_numeric(df_CO2_emm.index) # converting index values to numeric format

plt.style.use('default')
df_CO2_emm.T.plot(kind='bar')
plt.title(' nations co2 emission in the last decade increments')
plt.xlabel('Countries')
plt.ylabel('Co2 emission (kt)')
plt.xlim()
plt.show()

plt.figure(figsize=(10,6))
plt.style.use('default')
df_urban_pop.plot()
plt.title('Urban Population Trend for The 6 countries')
plt.xlabel('Year')
plt.ylabel('Urban Population')
plt.xticks([2000,2005,2010,2015,2020])
plt.show()

plt.figure(figsize=(10,6))
plt.style.use('default')
df_forest_area.plot()
plt.title('Forest area (% of land area) Trend for The 6 countries')
plt.xlabel('Year')
plt.ylabel('Forest area (% of land area)')
plt.xticks([2000,2005,2010,2015,2020])
plt.legend(loc='best')
plt.show()

df_Tot_green_house = df_Tot_green_house.iloc[10:, :]
df_Tot_green_house = df_Tot_green_house.apply(pd.to_numeric)

plt.style.use('default')
df_Tot_green_house.T.plot(kind='bar')
plt.title(' Country Total Green House emission in the last decade')
plt.xlabel('Countries')
plt.ylabel('Total greenhouse gas emissions (kt of CO2 equivalent)')
plt.show()

