# State of Massachusetts Joint Committee on Housing Evictions Analysis

## Project Description
The goal of this project is to better understand state eviction patterns over the past two years (2020 - 2021). 

## Meeting Schedule
(May vary depending on the circumstances)
- Weekly meeting: Thu 6pm – 7pm (EDT)
- Bi-weekly meeting: Wed 3pm – 4pm (EDT) 

## Project Contacts(Name, Email, Github)
- Binan Zhang,    bzahoka@bu.edu,     BZRG
- YuFan Lin,      eric1025@bu.edu,    Kotoric1
- Jiayu Gu,       jdgu@bu.edu,        GJYCS
- Qiuhao Gu,      guqh6666@bu.edu,    CHARGUis6666

## Data Sources
- Rental Assistance Data - MA Eviction Diversion Initiative Dashboard (state and federal programs only, might need an additional source for local rental assistance, particularly for City of Boston): 
    https://www.mass.gov/info-details/eviction-diversion-initiative-dashboard
- Mass Landlords Data (regular summary statistics on eviction filings)
  - FOIA requests / scraping from trial courts database
- MA Trial Court, Division of Research and Planning - series of Tableau dashboards detailing court hearings, filings for non-payment and any executed judgements: https://public.tableau.com/app/profile/drap4687
- Eviction Lab Data (for comparisons with other states/regions)
- Census Household Pulse Survey (for patterns in fear of eviction and rent payment status): https://www.census.gov/programs-surveys/household-pulse-survey/data.html

## Project Scope
- Look for patterns of eviction cases before the outbreak of covid-19 and after, and figure out the possible impact on the state eviction status.

## Questions to be answered
- What is the profile (race, ethnicity, family composition) of those evicted, what is the profile of those evicting (small landlord, large landlord, etc.), how does this vary by town/city – where are the highest rates, what are the causes of eviction, what is the eviction experience? i.e. who has received notice to quit, etc. How has this been impacted by different moratorium milestones (e.g. CDC expiration, state expiration, city expiration)
- How does Mass data compare to other states e.g. per capita evictions? Big cities in Mass compare to big cities elsewhere?
- How has rental assistance distribution affected this situation? What cities/ towns or census blocks are receiving rental assistance and who isn’t – based on race/ethnicity/etc. Have specific landlords received rental assistance before filings but still evicted, etc. Who is being denied rental assistance and why?

## Methods
- Data cleaning by pandas and numpy.
- Data clustering by sklearn.
- Data visualization by matplotlib(static) and Bokeh/Leaflet(dynamic).

## Limitations
- It would be hard to decide which part of data should be considered as pre-covid or post-covid.
- The large data size might make it harder to do the data cleaning and it might take a great amount of time to apply algorithms to it.
- The ethnicity of each eviction case would be hard to identify.
