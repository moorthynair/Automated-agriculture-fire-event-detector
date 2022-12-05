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

###################### Step 6: Save the results ############################

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
    if (len(fires['instrument'].unique())==1) and (fires['instrument'].unique()[0] == 'MODIS'):
        fires['confidence'] = fires['confidence'].astype('int64')
        fires['Landuse_type'] = fires['Landuse_type'].astype('int64')
        fires['acq_time'] = fires['acq_time'].astype('int64')
        fires = existing_data.merge(fires, how= 'outer', indicator=True)
        new_fires = fires.loc[fires['_merge']=='right_only', ].drop(columns = ['_merge'])
        
    elif (len(existing_data['instrument'].unique())==1) and (existing_data['instrument'].unique()[0] == 'MODIS'):
        existing_data['confidence'] = existing_data['confidence'].astype('object')
        fires['Landuse_type'] = fires['Landuse_type'].astype('int64')
        existing_data['acq_time'] = existing_data['acq_time'].astype('object')
        fires = existing_data.merge(fires, how= 'outer', indicator=True)
        new_fires = fires.loc[fires['_merge']=='right_only', ].drop(columns = ['_merge'])
        
    else:
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
    

print('\n {} is the total fires obsereved on {} as of now'.format(fires.shape[0],date))   
print('\n{} Seconds is the time taken for executing the program'.format(round(time_taken,2)))
    
##############################End of step 6 ##################################
