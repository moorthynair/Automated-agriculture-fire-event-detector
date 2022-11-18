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

###################### Step 3: Convert fire data point to shapefile ###################################

##Let us first convert these information into an point shapefile
fire_points = gpd.GeoDataFrame(data_integrated, geometry = gpd.points_from_xy(data_integrated['longitude'],data_integrated['latitude']))

##Let us visualise it
ax1= plt.gca()
fire_points.plot(facecolor = 'green', edgecolor = 'black', markersize=20,ax=ax1)

##Let us save the shapefile
new_path = os.path.join(path,'Shapefiles')

if not os.path.exists(new_path):
    os.mkdir(new_path)

ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'

fire_points.to_file(new_path+'/'+str(date)+'.shp', driver ='ESRI Shapefile', crs = ESRI_WKT)

##############################End of step 3 ##################################
