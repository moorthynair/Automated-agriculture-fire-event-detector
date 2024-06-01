# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:25:53 2022

@author: HP
"""

##Input the necessary library
import pandas as pd
import requests
import os
import geopandas as gpd
from alive_progress import alive_bar
import time, logging
import warnings
import shapely
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning) 
warnings.simplefilter(action='ignore', category=FutureWarning)


########## Step 1: Retreiving the data #####################################

def step_1(village_shape_path,url,Map_key,path,date,date_range):
    
    study_area = gpd.read_file(village_shape_path) ## read the shapefile
    study_area.to_crs('epsg:4326', inplace=True)
    West,South,East,North = study_area.total_bounds
    
    area = '{},{},{},{}'.format(West,South,East,North)
    
    sensors = {'VIIRS' : '/VIIRS_SNPP_NRT/' , 'NOAA' : '/VIIRS_NOAA20_NRT/', 'MODIS' : '/MODIS_NRT/' }
    
    with alive_bar(len(sensors),title = 'Retrieving the fire information', bar ='blocks') as bar:
        
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
            
            bar()
    
##############################End of step 1 ##################################
