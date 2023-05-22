# Automated-Agriculture-fire-event-detector
These set of codes can automatically download and process agriculture fire events occurred over an area of interest with a single click. The base information/data for analysis are retreived from the National Aeronautics and Space Administration (NASA) owned satellites. Since NASA provides data on Near Real Time (NRT) basis (Lag of 1-3 hours of the satellite overpass), one can run the code multiple times a day to track the latest fire events. 

## The purpose
Burning crop residue is generally discouraged because of the harm it does to soil biodiversity and public health owing to air pollution. The agriculture officials are mandated to monitor such illegal activity in order to take appropriate action. Automating this exercise using satellite-retrieved data will optimise the on-ground judgements and actions because performing this activity manually in an agricultural state is difficult and has a high risk of missing out on specific fire activities.
 
**Note:** We are here only retreiving NRT and past data upto 10 days to facilitate officals with immediate information for corrective actions. For retrospective data, one must access the archieve dataset provided in the NASA FIRMS website.

## Pre-requisites
**Req-1:** Generate a API from NASA FIRMS that lets you download NRT and past (upto 10 days) fire event dataset. [Click here](https://firms.modaps.eosdis.nasa.gov/api/area/) to access website and scroll down to generate one

**Req-2:** We shall be filtering the agriculture fire events using Landuse Landcover dataset. If you have one of your own , well and good or else download the MODIS LULC (MCD12Q1 V006) by access the website [clicking here](https://lpdaac.usgs.gov/products/mcd12q1v006/)

**Req-3:** All the essential python libraries for simulating the script mentioned [here](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/requirement.txt)

## what are the user inputs?
1. Generated API (See pre-requisites step 1)
2. Area of Interest for which the fire point has to be downloaded (provide the lat/lon of the geometry bounding box)
3. Date for which the fire event has to be downloaded
4. Date range (1 - 10 days)
5. Path to store the analysed data

## What are the user dataset to be provided?
1. Shapefile of the area of interest
2. Landuse Landcover dataset (Store it in a folder named 'LU_LC_Raster' in the path input by the user) 
3. Other shapefile files such as forest boundary, industrial area boundary for extracting agriculture fire events from other events. See Step 4 below 

# Lets check out the code step by step
Step 1: [Retreiving the fire data.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_1_Retreivng%20the%20fire%20data.py) 

Step2: [Merging the fire data.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_2_merging%20of%20data.py) 

Step 3: [Convert point data to shapefile.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_3_Convert%20fire%20data%20point%20to%20shapefile.py) 

Step 4: [Clip to boundary shapefile.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_4_Clip%20to%20boundary.py) 

To further enhancing agriuclture fire event retrivals, one can use Landuse Landcover dataset. [The processing of MODIS derived LULC is mentioned here.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/LU_LC%20Retreivals.py) one can either continue or skip step 5 and move to step 6. 

Step 5: [Fine tunning using LU-LC dataset.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_5_Fine%20tunning%20by%20assigning%20land%20class.py)

Step 6: [Saving the results/Multiple runs.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_6_Save%20the%20results.py)

------

### Okay Now try running the code all together 
Access to [all in one code.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/All%20in%20one%20code.py)

Have a look at the final informations/folders that shall be generated in the path provided by the user after running the program [Click here](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Final%20Path.png)

Please note that the area of interest, shapefiles used here are pertaining to Bihar State (India). You many modify the area of interest accordingly
