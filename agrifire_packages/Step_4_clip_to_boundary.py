# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:25:53 2022

@author: HP
"""

##Input the necessary library
import numpy as np
import os
import geopandas as gpd
import sys
from alive_progress import alive_bar
import time, logging
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

###################### Step 4: Clipping process ##############################

def step_4(path,date,village_shape_path):
    
    with alive_bar(1, title = 'Clipping to boundary') as bar:
        ##Input firepoints
        new_path = os.path.join(path,'Shapefiles')
        fire_points = gpd.read_file(new_path+'/'+str(date)+'.shp') ##Define the path here
        
        ##Input Panchayat Boundary
        study_area = gpd.read_file(village_shape_path) ## read the shapefile
        study_area.to_crs('epsg:4326', inplace=True)
        
        non_forest_fires_aoi = gpd.overlay(fire_points,study_area,how='intersection')
        
        ## Exist if 'Non Forest Fire doesn't exists'
        if non_forest_fires_aoi.shape[0]==0:    
            sys.exit('\n No Non forest fires were observed on {}'.format(date))
            
        ##check for duplicates and removal of same
        duplicate_list = non_forest_fires_aoi[['longitude','latitude']].duplicated().tolist()
        
        if len(set(duplicate_list))>1:    
            indexes = np.where(duplicate_list)[0]
            non_forest_fires_aoi.drop(index=indexes, inplace=True)
            non_forest_fires_aoi.reset_index(inplace=True)
            
        bar()
        
        return non_forest_fires_aoi
    
    ##You can stop here if you dont need further fine tuning

##############################End of step 4 ##################################

        
        

