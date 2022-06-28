import pandas as pd
import scipy
import numpy as np
import matplotlib.pyplot as plt

#penelope fiaschetti's work (pennifer) (some lines copied and edited from lowest_rate.ipynb)
dataf = pd.read_csv("eviction_with_geographic.csv")

dataf['other'] = (dataf['Estimate!!Total:!!Not Hispanic or Latino:!!Some other race alone'] + dataf['Estimate!!Total:!!Not Hispanic or Latino:!!Two or more races:']- dataf['Estimate!!Total:!!Not Hispanic or Latino:!!Two or more races:!!Two races including Some other race'])/dataf['Estimate!!Total:'] * 100
dataf['White'] = dataf['Estimate!!Total:!!Not Hispanic or Latino:!!White alone']/dataf['Estimate!!Total:'] * 100
dataf['Black or African American'] = dataf['Estimate!!Total:!!Not Hispanic or Latino:!!Black or African American alone']/dataf['Estimate!!Total:'] * 100
dataf['Asian'] = dataf['Estimate!!Total:!!Not Hispanic or Latino:!!Asian alone']/dataf['Estimate!!Total:'] * 100
dataf['Native Hawaiian and Other Pacific Islander'] = dataf['Estimate!!Total:!!Not Hispanic or Latino:!!Native Hawaiian and Other Pacific Islander alone']/dataf['Estimate!!Total:'] * 100
dataf['American Indian and Alaska Native'] = dataf['Estimate!!Total:!!Not Hispanic or Latino:!!American Indian and Alaska Native alone']/dataf['Estimate!!Total:'] * 100
dataf['Hispanic or Latino'] = dataf['Estimate!!Total:!!Hispanic or Latino:']/dataf['Estimate!!Total:'] * 100
race_columns=['Muni', 'White', 'Black or African American', 'Asian', 'Native Hawaiian and Other Pacific Islander','American Indian and Alaska Native', 'other', 'Hispanic or Latino']


education = pd.read_csv('2019_5Y_EducationalAttainment.csv',skiprows=1)
income = pd.read_csv('2019_5Y_Income.csv',skiprows=1)


education = education[education['Geographic Area Name'].str.contains('Brockton city')]
education['muni'] = 'Brockton'

education['Less than High School Deploma'] = education['Estimate!!Percent!!AGE BY EDUCATIONAL ATTAINMENT!!Population 25 years and over!!9th to 12th grade, no diploma'].astype('float')
education['High School Deploma'] = education['Estimate!!Percent!!AGE BY EDUCATIONAL ATTAINMENT!!Population 25 years and over!!High school graduate (includes equivalency)'].astype('float')
education['Some college, No degree']= education['Estimate!!Percent!!AGE BY EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Some college, no degree'].astype('float')
education["Associate's degree"] = education["Estimate!!Percent!!AGE BY EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Associate's degree"].astype('float')
education["Bachelor's degree or higher"] = education["Estimate!!Percent!!AGE BY EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Bachelor's degree"].astype('float') + education['Estimate!!Percent!!AGE BY EDUCATIONAL ATTAINMENT!!Population 25 years and over!!Graduate or professional degree'].astype('float')

income = income[income['Geographic Area Name'].str.contains('Brockton city')]
income['muni'] = 'Brockton'

income['Less than $10,000'] = income["Estimate!!Households!!Total!!Less than $10,000"].astype(float)
income['$10,000 to $24,999'] = income['Estimate!!Households!!Total!!$10,000 to $14,999'].astype(float) + income['Estimate!!Households!!Total!!$15,000 to $24,999'].astype(float)
income['$25,000 to $49,999'] = income['Estimate!!Households!!Total!!$25,000 to $34,999'].astype(float) + income['Estimate!!Households!!Total!!$35,000 to $49,999'].astype(float)
income['$50,000 to $99,999'] = income['Estimate!!Households!!Total!!$50,000 to $74,999'].astype(float) + income['Estimate!!Households!!Total!!$75,000 to $99,999'].astype(float)
income['$100,000 to $149,000'] = income['Estimate!!Households!!Total!!$100,000 to $149,999'].astype(float)
income['$150,000 or more'] = income['Estimate!!Households!!Total!!$150,000 to $199,999'].astype(float) + income['Estimate!!Households!!Total!!$200,000 or more'].astype(float)
income['Median Income'] = income['Estimate!!Households!!Median income (dollars)'].astype(str).replace('250,000+', '250000').astype(float)
income['Percent of Income Allocated to Rent'] = income['Estimate!!Households!!PERCENT ALLOCATED!!Household income in the past 12 months'].astype(float)




edu_columns=['muni','Less than High School Deploma', 'High School Deploma','Some college, No degree', "Associate's degree","Bachelor's degree or higher"]
income_columns=['muni','Less than $10,000','$10,000 to $24,999','$25,000 to $49,999','$50,000 to $99,999','$100,000 to $149,000','$150,000 or more']



brack1 = dataf[dataf['Estimate!!Total:'] < 10000]
brack2 = dataf[dataf['Estimate!!Total:'] >= 10000]
brack2 = brack2[brack2['Estimate!!Total:'] < 50000]
brack3 = dataf[dataf['Estimate!!Total:'] >= 50000]
brack3 = brack3[brack3['Estimate!!Total:'] < 90000]
brack4 = dataf[dataf['Estimate!!Total:'] >= 90000]        

brack1.sort_values(by=['Evictions per Rented Households'], ascending= False, inplace = True)
brack2.sort_values(by=['Evictions per Rented Households'], ascending= False, inplace = True)
brack3.sort_values(by=['Evictions per Rented Households'], ascending= False, inplace = True)
brack4.sort_values(by=['Evictions per Rented Households'], ascending= False, inplace = True)

cities = [281, 19, 2, 5]

#city1 = income[income['Geographic Area Name'].str.contains('Rowe town')].filter(income_columns, axis=1)
#city2 = income[income['Geographic Area Name'].str.contains('Randolph Town')].filter(income_columns, axis=1)
#city3 = income[income['Geographic Area Name'].str.contains('Fall River city')].filter(income_columns, axis=1)
city4 = income[income['Geographic Area Name'].str.contains('Brockton city')].filter(income_columns, axis=1)

city4.plot(x='muni', kind='bar', stacked=False)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.ylabel("Percentage")
plt.xlabel("Muni")
plt.title("Income in City with Highest Eviction Rate in Bracket 3")
plt.show()
