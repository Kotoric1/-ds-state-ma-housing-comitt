import pandas as pd
import scipy
import numpy as np
import matplotlib.pyplot as plt

#penelope fiaschetti's work (pennifer)
dataf = pd.read_csv("eviction_with_census_tract.csv")

dataf['gateway'] = ((dataf['property_a'].str.lower() == 'brockton') | (dataf['property_a'].str.lower() == 'fall river') | (dataf['property_a'].str.lower == 'fitchburg') | (dataf['property_a'].str.lower() == 'haverhill') | (dataf['property_a'].str.lower() == 'holyoke') | (dataf['property_a'].str.lower() == 'lawrence') | (dataf['property_a'].str.lower() == 'lowell') | (dataf['property_a'].str.lower() == 'new bedford') | (dataf['property_a'].str.lower() == 'pittsfield')| (dataf['property_a'].str.lower() == 'springfield')| (dataf['property_a'].str.lower() == 'worcester'))
#plot1 = dataf['gateway'].value_counts().plot.bar(rot = 0)
#plt.title('Eviction Filings')
#plt.xlabel('Property is in a Gateway City')
#plt.ylabel('Filing Count')
filtered = dataf[dataf['gateway'] == True]
plot1 = filtered['Corp'].value_counts().plot.bar(rot = 0)
plt.title('Eviction Filings in Gateway Cities')
plt.xlabel('Owner is a Corporation')
plt.ylabel('Filing Count')
plt.show()
