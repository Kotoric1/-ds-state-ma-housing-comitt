# State of Massachusetts Joint Committee on Housing Evictions Analysis, Team 1 & 3

# Collaborators
Yichen Sun <yichen98@bu.edu>

Merna Alghannam <maalghan@bu.edu>

Penelope Fiaschetti <pmf2022@bu.edu>

Trivikram Ranga <tvranga@bu.edu>

Yufan Lin <eric1025@bu.edu>

Binan Zhang <bzahoka@bu.edu>

# Dataset
Eviction dataset in folder eviction_data

M + 0: only collected the docket information once, the month that the case occurred; 

M + 18: collected the data once during the month of the case, and then 18 months later, to check for missing fields/updates

Please note the output.txt files for details.
Geographic units available are zipcode, municipality, as well as court district.


Municipality profile data in folder Muni_Profile
ACS 5-Year Estimates Subject Tables:
	Link: https://data.census.gov/cedsci

	To better understand how Census Bureau defines Geographic Relationships:
		https://www.census.gov/newsroom/blogs/random-samplings/2014/07/understanding-geographic-relationships-counties-places-tracts-and-more.html
 
Eviction cases by municipality data in folder Eviction_Cases, including normalize by rentals with household information.

Unemployment_2020:
	FROM mass.gov --> Municipal Finance Trend Dashboard --> Category 5: Demographics --> Unemployment Rate --> select 2020
	Link: https://dlsgateway.dor.state.ma.us/reports/rdPage.aspx?rdReport=dashboard.category_5

Census tract data in MA in folder census_tract_data.


# Code
In folder processing_M+0&M+18_datasets, the code generates eviction number for each municipality.

In folder population bracket, the code splits municipalities into 4 brackets with population and analyzes gateway cities.

In folder Poverty and Unemployment Analysis, the code analyzes poverty and unemployment with eviction.

In folder Demographic and Evictions Visualizations - Merna Alghannam - Final, the folder contains code for visualizations: demographics, i.e. race and income profile, geopanda maps, and timeseries trend plots.

In folder utils, there are functions that performed tasks like data cleaning.

In folder brackets analysis, the code analyzes evicted profiles in each brackets.  

In lowest_rate.ipynb -Yufan Lin - the code finds the city which has the lowest rate of eviction in each brackets, and analysis the education, income, and race proportion of each city.


# Work Done By Team 3 Members Before Merging Into Team 1(Binan Zhang & Yufan Lin)  

We performed data cleaning for both eviction datasets(the augmented MassLandlords data and the new massLandlords raw data).  

We added the information of the census tract for each eviction case using GeoPandas to the augmented MassLandlords data.  (census tract analysis folder)

We summarized the number of evictions by each eviction type and the number of evictions by each house owner for each census tract.  

We performed demographic analysis on the 5 census tracts that have the highest number of eviction cases.  

We collected the income datasets for both census tracts and cities.  

We used poverty rates from the census tract income data to perform an analysis on the relationship between poverty rate and the number of eviction cases.  



