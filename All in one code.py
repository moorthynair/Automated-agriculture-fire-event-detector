# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:25:08 2022

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
import matplotlib.pyplot as plt
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning) 
warnings.simplefilter(action='ignore', category=FutureWarning)

#Lets beign
start = time.time()

url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/'
Map_key = 'e8b17bf4e91dce8468083ba236932eaf' ##Key is confidential

##Define the area for monitoring, I Choose Bihar as my study area
West = '82.54688'
South ='22.96283'
East = '89.29688'
North = '28.06316'

##Define the date range
date = '2022-11-15' ##(YYYY-MM-DD format)
date_range = '1'

#date_modified = dt.strptime(date, '%Y-%m-%d') - timedelta (days= int(date_range))
#date = date_modified.strftime('%Y-%m-%d')

## Define path to store your data
path = 'C:/Users/HP/Desktop/Fire_analysis/Fires_Kharif_2022'

##Analysis begins.......


########## Step 1: Retreiving the data #####################################
area = '{},{},{},{}'.format(West,South,East,North)

sensors = {'VIIRS' : '/VIIRS_SNPP_NRT/' , 'NOAA' : '/VIIRS_NOAA20_NRT/', 'MODIS' : '/MODIS_NRT/' }

for index, i in zip(sensors.keys(), sensors.values()):      
    
    final_url = url+Map_key+i+str(area)+'/'+str(date_range)+'/'+str(date)
    data = requests.get(final_url)    
    new_path = os.path.join(path,index)
    
    ##Check if the path exists
    if not os.path.exists(new_path):
        os.mkdir(new_path)
        
    new_path = new_path+'/'+str(date)+'.csv'
      
    ## Write API Results to CSV
    f = open(new_path, "w") 
    f.write(data.text)
    f.close()
##############################End of step 1 ##################################

###################### Step 2: Merging of data ###################################
##Now that we got the fire points from the desired region of intrest, let us initiate GIS analysis
##Let us first read this data and integrate all the data retreived from various sensors into single dataframe

data_integrated = pd.DataFrame()

predefined_cols = ['latitude', 'longitude', 'brightness', 'scan', 'track', 'acq_date',
       'acq_time', 'satellite', 'instrument', 'confidence', 'version',
       'bright_t31', 'frp', 'daynight']

for i in sensors.keys():    
    new_path = os.path.join(path,i)
    data = pd.read_csv(new_path+'/'+str(date)+'.csv')    
    data.columns = predefined_cols
    data_integrated = pd.concat([data_integrated,data],axis=0)

data_integrated.index = np.arange(0,data_integrated.shape[0])

## Let's break the code if no fire was detected
if data_integrated.shape[0]==0:    
    sys.exit('\n No fires were observed on {}'.format(date))

##############################End of step 2 ##################################

###################### Step 3: Convert fire data point to shapefile ###################################
##Let us first convert these information into an point shapefile
fire_points = gpd.GeoDataFrame(data_integrated, geometry = gpd.points_from_xy(data_integrated['longitude'],data_integrated['latitude']))

##Let us visualise it
fire_points.plot(facecolor = 'red', edgecolor = 'black', markersize=20)

##Let us save the shapefile
new_path = os.path.join(path,'Shapefiles')

if not os.path.exists(new_path):
    os.mkdir(new_path)

ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'

fire_points.to_file(new_path+'/'+str(date)+'.shp', driver ='ESRI Shapefile', crs = ESRI_WKT)

##############################End of step 3 ##################################

###################### Step 4: Clipping process ##############################
##Input firepoints
fire_points = gpd.read_file(new_path+'/'+str(date)+'.shp')

##Input Panchayat Boundary
Panchayat_boundary = gpd.read_file('C:/Users/HP/Desktop/data/IND_adm/PF AND PANCHYAT BOUNDARY/PANCHAYAT_BOUND_WITH_FOREST_ATTRIBUTES.shp')

##input Forest Boundary
forest_boundary = gpd.read_file('C:/Users/HP/Desktop/data/IND_adm/PF AND PANCHYAT BOUNDARY/PF_BOUNDARY_2019.shp')
forest_boundary.to_crs('EPSG:4326', inplace=True)

##Clip out the non forest fires initially
non_forest_fires = gpd.overlay(fire_points, forest_boundary, how='difference')
non_forest_fires_bihar = gpd.overlay(non_forest_fires,Panchayat_boundary,how='intersection')

##Let us now plot the non forest fires
fig, ax1 =plt.subplots()
non_forest_fires_bihar.plot(facecolor = 'red', edgecolor = 'black', markersize=20, ax=ax1)
Panchayat_boundary.plot(facecolor ='None', edgecolor = 'black', ax=ax1) 

##check for duplicates and removal of same
duplicate_list = non_forest_fires_bihar[['longitude','latitude']].duplicated().tolist()

if len(set(duplicate_list))>1:    
    indexes = np.where(duplicate_list)[0]
    non_forest_fires_bihar.drop(index=indexes, inplace=True)
    non_forest_fires_bihar.reset_index(inplace=True)

##You can stop here if you dont need further fine tuning

##############################End of step 4 ##################################

## Before Initiating set 5, let us retrive the raster Landuse Landcover file and do the pre-requistes
## Convert the retreived LULC from HDF to tiff format

landuse_landcover = 'C:/Users/HP/Desktop/Fire_analysis/Fires_Kharif_2022/LU_LC_Raster/MCD12Q1.A2020001.h25v06.006.2021360043257.hdf'

if not os.path.exists(landuse_landcover):
    hdflayer = gdal.Open(landuse_landcover, gdal.GA_ReadOnly)
    ## I choose Land Cover Type 1: Annual International Geosphere-Biosphere Programme (IGBP) classification 
    rlayer = gdal.Open(hdflayer.GetSubDatasets()[0][0], gdal.GA_ReadOnly)

    os.chdir('C:/Users/HP/Desktop/Fire_analysis/Fires_Kharif_2022/LU_LC_Raster')
    rastername = 'MCD12Q1_2021360043257.tiff'
    gdal.Warp(rastername,rlayer, dstSRS='EPSG:4326')

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


###################### Step 6: Save the results #############################
cols_selected = ['latitude', 'longitude', 'acq_date','acq_time', 'instrument', 'confidence', 'frp', 'daynight', 'GPNAME_1', 'BLK_NAME', 'DIST_NAM_1', 'Landuse_type']
fires = non_forest_fires_bihar.loc[:,non_forest_fires_bihar.columns.isin(cols_selected)]

folder = 'Analysed Results'
new_path = os.path.join(path,folder)

if not os.path.exists(new_path):
    os.mkdir(new_path)
    
new_path = new_path + '/'+str(date)+'.xlsx'

## If you want to run the program multiple times a day
if os.path.exists(new_path):
    existing_data = pd.read_excel(new_path)
    fires = existing_data.merge(fires, how= 'outer', indicator=True)
    new_fires = fires.loc[fires['_merge']=='right_only', ].drop(columns = ['_merge'])
    
    ##Let us save the new fires identified over the mutiple run
    folder = 'Multiple Run'
    new_path = os.path.join(path,folder)

    if not os.path.exists(new_path):
        os.mkdir(new_path)
    
    new_path = os.path.join(new_path, str(date))
    
    if not os.path.exists(new_path):
        os.mkdir(new_path)
        
    list_dir = os.listdir(new_path)
    count = len(list_dir)+1 
    
    new_path = new_path + '/'+str(date)+'_run_'+str(count)+'.xlsx'
    new_fires.to_excel(new_path, index=False)
    
    print('\n Run number {} has observed {} number of new fires on {}'.format(count,new_fires.shape[0],date))
    
    folder = 'Analysed Results'
    new_path = os.path.join(path,folder)
    new_path = new_path + '/'+str(date)+'.xlsx'
    
    fires.drop(columns = ['_merge'], inplace=True)
    fires.to_excel(new_path, index=False)     
else:
    fires.to_excel(new_path, index=False)
    
end = time.time()

time_taken = end-start

print('\n {} is the total fires obsereved on {} as of now'.format(fires.shape[0],date))   
print('\n{} Seconds is the time taken for executing the program'.format(round(time_taken,2)))

############################End of step 6 #####################################
