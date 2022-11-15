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

#Lets beign

url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/'
Map_key = 'e####17bf4e#########83ba2eaf' ##Enter the API key generated

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
