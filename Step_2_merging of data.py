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

###################### Step 2: Integration ###################################
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
data_integrated['confidence'] = data_integrated['confidence'].astype('object')

## Let's break the code if no fire was detected
if data_integrated.shape[0]==0:    
    sys.exit('\n No fires were observed on {}'.format(date))

##############################End of step 2 ##################################
