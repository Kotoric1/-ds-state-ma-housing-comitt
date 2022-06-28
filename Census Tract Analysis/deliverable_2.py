import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np

# load eviction data as pd dataframe and remove rows with empty 'geometry'
df=pd.read_csv("ACS_Income.csv", low_memory=False)
num_eviction = pd.read_csv("by_census.csv")

# clean those without a census tract
#df = df.dropna(subset=['NAME'])

# select useful columns
df=df[['NAME','DP03_0119PE']]

# rename poverty rate
df.drop(labels=[0], axis=0, inplace=True)
df.rename(columns={'DP03_0119PE':'poverty_rate'}, inplace=True)

# extract census tract code only
def extract_census_code(c_name):
    m = re.search('Census Tract (.+?),', c_name).group(1)
    m = float(m)
    return m

# perform extraction to every name in df
for i in range(len(df)):
    df.at[i+1,'NAME'] = extract_census_code(df.at[i+1,'NAME'])

# merge and save as csv
merged_dataset = num_eviction.merge(df, on='NAME', how='left')
merged_dataset.to_csv('poverty_rate_of_census.csv')

# plot
x = np.array(merged_dataset['poverty_rate']).astype(float)
y = np.array(merged_dataset['num_eviction'])

plt.scatter(x, y, s=30, alpha=0.5)
plt.xlabel('poverty_rate(%)')
plt.ylabel('num_eviction')
plt.show()


