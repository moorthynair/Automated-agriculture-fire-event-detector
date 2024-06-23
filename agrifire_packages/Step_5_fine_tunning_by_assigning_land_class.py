# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:25:53 2022

@author: HP
"""

##Input the necessary library

import os
import rasterio as rio
from alive_progress import alive_bar
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

###################### Step 5: Fine tunning by assigning land class ###########


def step_5(non_forest_fires_aoi):
    
    new_path = os.path.join('landuse_raster')
    raster_file = os.listdir(new_path)
    raster_path = os.path.join(new_path,raster_file[0])
    
    LU_LC = rio.open(raster_path)
    LU_LC_array = LU_LC.read(1)
    
    non_forest_fires_aoi['Landuse_type'] = 0
    
    with alive_bar(len(non_forest_fires_aoi),title = 'Extracting LU_LC information', bar ='blocks') as bar:

        for index, i in non_forest_fires_aoi.iterrows():
            row_index, col_index = LU_LC.index(i['longitude'], i['latitude'])
            non_forest_fires_aoi.loc[index,'Landuse_type'] = LU_LC_array[row_index, col_index]
            bar()
            
        ## Let us know what the landuse type represents?
        #1  -   Evergreen Needleleaf Forests: dominated by evergreen conifer trees (canopy >2m). Tree cover >60%.
        #2  -   Evergreen Broadleaf Forests: dominated by evergreen broadleaf and palmate trees (canopy >2m). Tree cover >60%.
        #3  -   Deciduous Needleleaf Forests: dominated by deciduous needleleaf (larch) trees (canopy >2m). Tree cover >60%.
        #4	-	Deciduous Broadleaf Forests: dominated by deciduous broadleaf trees (canopy >2m). Tree cover >60%.
        #5	-	Mixed Forests: dominated by neither deciduous nor evergreen (40-60% of each) tree type (canopy >2m). Tree cover >60%.
        #6	-	Closed Shrublands: dominated by woody perennials (1-2m height) >60% cover.
        #7	-	Open Shrublands: dominated by woody perennials (1-2m height) 10-60% cover.
        #8	-	Woody Savannas: tree cover 30-60% (canopy >2m).
        #9	-	Savannas: tree cover 10-30% (canopy >2m).
        #10	-	Grasslands: dominated by herbaceous annuals (<2m).
        #11	-	Permanent Wetlands: permanently inundated lands with 30-60% water cover and >10% vegetated cover.
        #12	-	Croplands: at least 60% of area is cultivated cropland.
        #13	-	Urban and Built-up Lands: at least 30% impervious surface area including building materials, asphalt and vehicles.
        #14	-	Cropland/Natural Vegetation Mosaics: mosaics of small-scale cultivation 40-60% with natural tree, shrub, or herbaceous vegetation.
        #15	-	Permanent Snow and Ice: at least 60% of area is covered by snow and ice for at least 10 months of the year.
        #16	-	Barren: at least 60% of area is non-vegetated barren (sand, rock, soil) areas with less than 10% vegetation.
        #17	-	Water Bodies: at least 60% of area is covered by permanent water bodies.
        
        
        ## Let us now filter based on landuse type
        non_forest_fires_aoi = non_forest_fires_aoi.loc[non_forest_fires_aoi['Landuse_type']==12, ]
        non_forest_fires_aoi = non_forest_fires_aoi.sort_values(by ='acq_date')
        
    
    return non_forest_fires_aoi

##############################End of step 5 ##################################