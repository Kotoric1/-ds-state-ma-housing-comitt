import pandas as pd
import scipy
import numpy as np
import matplotlib.pyplot as plt


#dataf = pd.read_csv("eviction_with_census_tract.csv")
#plot2 = dataf['poly_typ'].value_counts().plot.bar()
#dataf['count'] = dataf.groupby('owner_name')['owner_name'].transform('count')
#dataf.dropna(subset=['count', 'owner_name'])
#filtered = dataf[dataf['count'] > 20]
#plot1 = filtered['court_divi'].value_counts().plot.bar(rot =0)
#plt.show()
#print(filtered.value_counts(subset = 'owner_name'))


#penelope fiaschetti's work (pennifer)
dataf = pd.read_csv("eviction_with_census_tract.csv")
#plot2 = dataf['Corp'].value_counts().plot.bar()
#plt.title('Eviction Filings')
#plt.xlabel('Owner is a corporation')
#plt.ylabel('Filing Count')
dataf['count'] = dataf.groupby('owner_name')['owner_name'].transform('count')
dataf.dropna(subset=['count', 'owner_name'])
filtered = dataf[dataf['count'] > 20]
#plot1 = filtered['Corp'].value_counts().plot.bar(rot =0)
#plt.title('Eviction Filings by Owners with more than 20 Filings')
#plt.xlabel('Owner is a corporation')
#plt.ylabel('Filing Count')
a = dataf[dataf.Corp == True]
b = dataf[dataf.Corp == False]
histdata = np.array([a['count'].tolist() ,b['count'].tolist()])
plt.hist(histdata, bins = 8, range = (0, 80), label = ['Corporation', 'Not Corporation'])
plt.legend()
plt.title('Eviction Filings Counts by Amount of filings by owner')
plt.xlabel('bins')
plt.ylabel('Count')
plt.show()
#print(filtered.value_counts(subset = 'owner_name'))
