# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:25:53 2022

@author: HP
"""

##Input the necessary library
import pandas as pd
import numpy as np
import os
from alive_progress import alive_bar
import time, logging
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

###################### Step 2: Integration ###################################
##Now that we got the fire points from the desired region of intrest, let us initiate GIS analysis
##Let us first read this data and integrate all the data retreived from various sensors into single dataframe

def step_2(path, date):
    data_integrated = pd.DataFrame()
        
    predefined_cols = ['latitude', 'longitude', 'brightness', 'scan', 'track', 'acq_date',
               'acq_time', 'satellite', 'instrument', 'confidence', 'version',
               'bright_t31', 'frp', 'daynight']
        
    sensors = {'VIIRS' : '/VIIRS_SNPP_NRT/' , 'NOAA' : '/VIIRS_NOAA20_NRT/', 'MODIS' : '/MODIS_NRT/' }
        
    with alive_bar(len(sensors), title = 'Merging data', bar ='blocks') as bar:
        for i in sensors.keys():    
            new_path = os.path.join(path,i)
            data = pd.read_csv(new_path+'/'+str(date)+'.csv')    
            data.columns = predefined_cols
            data_integrated = pd.concat([data_integrated,data],axis=0)
            bar()
        
    data_integrated.index = np.arange(0,data_integrated.shape[0])
    data_integrated['confidence'] = data_integrated['confidence'].astype('object')
        
    return data_integrated

##############################End of step 2 ##################################
