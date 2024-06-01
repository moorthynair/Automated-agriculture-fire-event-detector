#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 00:26:15 2024

@author: moorthymnair
"""

import argparse
import configparser
import sys
import pandas as pd
import geopandas as gpd
from datetime import datetime
from agrifire_packages import *
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    
    ## input the config.ini path through argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('config_path', help ='Enter the path to config.ini file')
    args = parser.parse_args()
    
    ## Read the config.ini file
    config_path = args.config_path
    config_file = configparser.ConfigParser()
    config_file.read(config_path)
    
    ## user inputs
    repo_path = config_file['repository']['path']
    API_key =  config_file['inputs']['API']
    village_shape = config_file['inputs']['aoi_boundary']
    village_attributes = config_file['inputs']['aoi_attributes']
    date = config_file['inputs']['date']
    date_range = config_file['inputs']['date_range']
    path = config_file['output']['output_path']
    Firms_url = 'https://firms.modaps.eosdis.nasa.gov/api/area/csv/' ##Do not change
    
    ## check for the date
    if str(date) == 'current':
        date = datetime.now().strftime('%Y-%m-%d')
        date_range = 1
        
    ## Print header
    initialiser_agri.header()
    
    ## Step-1
    print('\n')
    Step_1_retreivng_the_fire_data.step_1(village_shape,
                                          Firms_url,API_key,path,date,date_range)
    
    ## Step-2
    print('\n')
    dt = Step_2_merging_of_data.step_2(path, date)
    
    ## Let's break the code if no fire was detected
    if dt.shape[0]==0:    
        sys.exit('\n No fires were observed on {}'.format(date))
    
    ## Step-3
    print('\n')
    Step_3_convert_fire_data_point_to_shapefile.step_3(dt, path, date)
    
    ## Step-4
    print('\n')
    dt_fire_point = Step_4_clip_to_boundary.step_4(path, date,
                                                   village_shape_path = village_shape)
    
    ## Check for confidence
    pd.options.mode.chained_assignment = None ##  supress warnings
    viirs_confidence = config_file['confidence']['viirs']
    modis_confidence = config_file['confidence']['modis']
    
    viirs_dt = dt_fire_point.loc[dt_fire_point['confidence'].isin(viirs_confidence.split(',')), ]
    modis_dt = dt_fire_point[dt_fire_point['instrument'] == 'MODIS'] 
    modis_dt['confidence'] = modis_dt['confidence'].astype('int64')                          
    modis_dt = modis_dt[modis_dt['confidence'] >= int(modis_confidence)]
    
    dt_fire_point = pd.concat([viirs_dt, modis_dt], axis=0).reset_index(drop = True)
    
    ## Step-5
    print('\n')
    dt_agri_fire = Step_5_fine_tunning_by_assigning_land_class.step_5(repository_path = repo_path, non_forest_fires_aoi = dt_fire_point)
    ## Let's break the code if no fire was detected
    print('\n')
    print('-*-'*28)
    if dt_agri_fire.shape[0]==0:    
        sys.exit('\n No fires were observed on {}'.format(date))
    print('\n')
    print('-*-'*28)
        
    ## Step-6
    print('\n')
    Step_6_save_the_results.step_6(dt_agri_fire,date, path, attributes = village_attributes)
    
    
if __name__ == '__main__':
    main()
    





