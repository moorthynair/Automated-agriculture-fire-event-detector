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
import matplotlib.pyplot as plt
from shapely.errors import ShapelyDeprecationWarning
warnings.filterwarnings("ignore", category=ShapelyDeprecationWarning) 
warnings.simplefilter(action='ignore', category=FutureWarning)

###################### Step 4: Clipping process ##############################

##Input firepoints
fire_points = gpd.read_file(new_path+'/'+str(date)+'.shp') ##Define the path here

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
