# Author: Binan Zhang
# This file merges the census tract information with the provided MassLanlords eviction datasets for each eviction case using GeoPandas
# for furthur census tract analysis

import pandas as pd
import geopandas as gpd
from shapely import wkt
import numpy as np
from shapely.geometry import geo

# load census tract data and make a csv copy
MA_df=gpd.read_file("census_track_data\cb_2018_25_tract_500k.shp")
MA_df.to_csv("census_track_data\census_track_data.csv")

# EPSG:26986 is for MA Coordinate System
# EPSG:4326 is for the standard one
MA_df = MA_df.to_crs("EPSG:26986")

# load eviction data as pd dataframe and remove rows with empty 'geometry'
eviction=pd.read_csv("Eviction Filings thru July2021.csv")
eviction=eviction.dropna(subset=['geometry'])

# convert eviction to gpd dataframe
eviction['geometry'] = gpd.GeoSeries.from_wkt(eviction['geometry'])
eviction=gpd.GeoDataFrame(eviction, crs="EPSG:26986", geometry='geometry')

# merge and save as csv
Spatial_merge_df = eviction.sjoin(MA_df, how='left', predicate='within')
Spatial_merge_df.to_csv("eviction_with_census_tract.csv")
