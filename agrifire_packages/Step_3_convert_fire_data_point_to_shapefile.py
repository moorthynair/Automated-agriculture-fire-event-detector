# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:25:53 2022

@author: HP
"""

##Input the necessary library
import pandas as pd
import numpy as np
import os
import geopandas as gpd
from alive_progress import alive_bar
import time, logging
import warnings
import shapely
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning) 
warnings.simplefilter(action='ignore', category=FutureWarning)

###################### Step 3: Convert fire data point to shapefile ###################################

def step_3(data_integrated, path, date):
    
    with alive_bar(1, title = 'Convert fire points into shapefile') as bar:
    ##Let us first convert these information into an point shapefile
        fire_points = gpd.GeoDataFrame(data_integrated, geometry = gpd.points_from_xy(data_integrated['longitude'],data_integrated['latitude']))
        
        ##Let us save the shapefile
        new_path = os.path.join(path,'Shapefiles')
        
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        
        ESRI_WKT = 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]'
        
        fire_points.set_crs(ESRI_WKT, inplace=True)
        
        fire_points.to_file(new_path+'/'+str(date)+'.shp', driver ='ESRI Shapefile')
        
        bar()
##############################End of step 3 ##################################
