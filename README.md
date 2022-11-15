# Automated-Agriculture-fire-event-detector
I managed to develop set of codes that can download and process agriculture fire events for any area of interest. Since NASA FIRMS provides data on near real time basis, one can run the code multiple times in a day. Lets check out the code step by step

## Pre-requistes
1. Generate a API from NASA FIRMS that lets you download near real time and past (upto 10 days) fire event dataset. [Click here](https://firms.modaps.eosdis.nasa.gov/api/area/) to access website to generate one
![image](https://user-images.githubusercontent.com/83420459/201974345-2780ca02-5577-4e28-aea3-4e09582b02bb.png)

2. We shall be filtering the agriculture fire events using Landuse Landcover dataset. If you have one of your own , well and good or else download the MODIS LULC (MCD12Q1 V006) by access the website [clicking here](https://lpdaac.usgs.gov/products/mcd12q1v006/)
3. All the essential python libraries mentioned [here](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Essential%20Libraries.PNG)

## what are the user inputs?
1. Generate API
2. Area of Interest
3. Date
4. Date range (1 - 10 days)
5. Path to store the data

## What are the user dataset to be provided?
1. Shapefile of the area of interest
2. Landuse Landcover raster data
3. Other shapefile files such as forest boundary, industrial area boundary for extracting agriculture fire events from other events. See Step 4 below 

# Lets check out the code step by step
Step 1: [Retreiving the fire data.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_1_Retreivng%20the%20fire%20data.py) 

Step2: [Merging the fire data.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_2_merging%20of%20data.py) 

Step 3: [Convert point data to shapefile.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_3_Convert%20fire%20data%20point%20to%20shapefile.py) 

Step 4: [Clip to boundary shaepfile.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_4_Clip%20to%20boundary.py) 

To further enhancing agriuclture fire event retrivals, one can use Landuse Landcover dataset. [The processing of MODIS derived LULC is mentioned here.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/LU_LC%20Retreivals.py) one can either continue or skip step 5 and move to step 6. 

Step 5: [Fine tunning using LU-LC dataset.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_5_Fine%20tunning%20by%20assigning%20land%20class.py)

Step 6: [Saving the results/Multiple runs.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_6_Save%20the%20results.py)


## Okay Now try running the code all together. Access to [all in one code.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/All%20in%20one%20code.py)
