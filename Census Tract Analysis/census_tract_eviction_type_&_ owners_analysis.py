# Author: Binan Zhang
# This file summarizes the eviction type and house owner information for each census tract for furthur demographic analysis

import pandas as pd

# load eviction data as pd dataframe and remove rows with empty 'geometry'
df=pd.read_csv("eviction_with_census_tract.csv")

# clean those without a census tract
df = df.dropna(subset=['NAME'])

# select useful columns
df=df[['NAME','initiating','owner_name']]
count_census=df[['NAME']].groupby(['NAME']).size().sort_values(ascending=False)

print(count_census)

# tract by tract summary of number of evictions by owner and by eviction type
count_owner=df.groupby(['NAME','owner_name']).size().sort_values(ascending=False)
count_ini=df.groupby(['NAME','initiating']).size().sort_values(ascending=False)

print(count_owner)
print(count_ini)

# Analysis for the top 5 largest number of eviction cases census tracts
count_owner1=df[df['NAME']==7317.00].groupby(['NAME','owner_name']).size().sort_values(ascending=False)
count_ini1=df[df['NAME']==7317.00].groupby(['NAME','initiating']).size().sort_values(ascending=False)

count_owner2=df[df['NAME']==7304.01].groupby(['NAME','owner_name']).size().sort_values(ascending=False)
count_ini2=df[df['NAME']==7304.01].groupby(['NAME','initiating']).size().sort_values(ascending=False)

count_owner3=df[df['NAME']==6421.00].groupby(['NAME','owner_name']).size().sort_values(ascending=False)
count_ini3=df[df['NAME']==6421.00].groupby(['NAME','initiating']).size().sort_values(ascending=False)

count_owner4=df[df['NAME']==3840.02].groupby(['NAME','owner_name']).size().sort_values(ascending=False)
count_ini4=df[df['NAME']==3840.02].groupby(['NAME','initiating']).size().sort_values(ascending=False)

count_owner5=df[df['NAME']==3835.01].groupby(['NAME','owner_name']).size().sort_values(ascending=False)
count_ini5=df[df['NAME']==3835.01].groupby(['NAME','initiating']).size().sort_values(ascending=False)

print(count_owner1)
print(count_ini1)

print(count_owner2)
print(count_ini2)

print(count_owner3)
print(count_ini3)

print(count_owner4)
print(count_ini4)

print(count_owner5)
print(count_ini5)