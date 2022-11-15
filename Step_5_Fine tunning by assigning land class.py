# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:25:53 2022

@author: HP
"""

##Input the necessary library
import pandas as pd
import numpy as np
import requests
from datetime import datetime as dt
import csv
import os
from datetime import timedelta, date
from datetime import datetime as dt
import geopandas as gpd
import xarray as xr
import gdal
import rasterio as rio
import time
import sys
import warnings
import shapely
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning) 
warnings.simplefilter(action='ignore', category=FutureWarning)

###################### Step 5: Fine tunning by assigning land class ###########

os.chdir('C:/Users/HP/Desktop/Fire_analysis/Fires_Kharif_2022/LU_LC_Raster')
LU_LC = rio.open('MCD12Q1_2021360043257.tiff')
LU_LC_array = LU_LC.read(1)

for index, i in non_forest_fires_bihar.iterrows():
    row_index, col_index = LU_LC.index(i['longitude'], i['latitude'])
    non_forest_fires_bihar.loc[index,'Landuse_type'] = LU_LC_array[row_index, col_index]
    print('{} out of {} completed'.format(index+1,len(non_forest_fires_bihar.index)))
    
## Let us know what the landuse type represents?
#1  -   Evergreen Needleleaf Forests: dominated by evergreen conifer trees (canopy >2m). Tree cover >60%.
#2  -   Evergreen Broadleaf Forests: dominated by evergreen broadleaf and palmate trees (canopy >2m). Tree cover >60%.
#3  -   Deciduous Needleleaf Forests: dominated by deciduous needleleaf (larch) trees (canopy >2m). Tree cover >60%.
#4	-	Deciduous Broadleaf Forests: dominated by deciduous broadleaf trees (canopy >2m). Tree cover >60%.
#5	-	Mixed Forests: dominated by neither deciduous nor evergreen (40-60% of each) tree type (canopy >2m). Tree cover >60%.
#6	-	Closed Shrublands: dominated by woody perennials (1-2m height) >60% cover.
#7	-	Open Shrublands: dominated by woody perennials (1-2m height) 10-60% cover.
#8	-	Woody Savannas: tree cover 30-60% (canopy >2m).
#9	-	Savannas: tree cover 10-30% (canopy >2m).
#10	-	Grasslands: dominated by herbaceous annuals (<2m).
#11	-	Permanent Wetlands: permanently inundated lands with 30-60% water cover and >10% vegetated cover.
#12	-	Croplands: at least 60% of area is cultivated cropland.
#13	-	Urban and Built-up Lands: at least 30% impervious surface area including building materials, asphalt and vehicles.
#14	-	Cropland/Natural Vegetation Mosaics: mosaics of small-scale cultivation 40-60% with natural tree, shrub, or herbaceous vegetation.
#15	-	Permanent Snow and Ice: at least 60% of area is covered by snow and ice for at least 10 months of the year.
#16	-	Barren: at least 60% of area is non-vegetated barren (sand, rock, soil) areas with less than 10% vegetation.
#17	-	Water Bodies: at least 60% of area is covered by permanent water bodies.


## Let us now filter based on landuse type
non_forest_fires_bihar = non_forest_fires_bihar.loc[non_forest_fires_bihar['Landuse_type']==12, ]
non_forest_fires_bihar = non_forest_fires_bihar.sort_values(by ='acq_date')

## Let's break the code if no fire was detected
if non_forest_fires_bihar.shape[0]==0:    
    sys.exit('\n No fires were observed on {}'.format(date))
    
##############################End of step 5 ##################################