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

## Before Initiating set 5, let us retrive the raster Landuse Landcover file and do the pre-requistes

## Convert the retreived LULC from HDF to tiff format

landuse_landcover = 'C:/Users/HP/Desktop/Fire_analysis/Fires_Kharif_2022/LU_LC_Raster/MCD12Q1.A2020001.h25v06.006.2021360043257.hdf'

if not os.path.exists(landuse_landcover):
    hdflayer = gdal.Open(landuse_landcover, gdal.GA_ReadOnly)
    ## I choose Land Cover Type 1: Annual International Geosphere-Biosphere Programme (IGBP) classification 
    rlayer = gdal.Open(hdflayer.GetSubDatasets()[0][0], gdal.GA_ReadOnly)

    os.chdir('C:/Users/HP/Desktop/Fire_analysis/Fires_Kharif_2022/LU_LC_Raster')
    rastername = 'MCD12Q1_2021360043257.tiff'
    gdal.Warp(rastername,rlayer, dstSRS='EPSG:4326')
