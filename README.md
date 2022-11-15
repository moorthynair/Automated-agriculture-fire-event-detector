# Automated-Agriculture-fire-event-detector
I managed to develop set of codes that can download and process agriculture fire events for any area of interest. Lets check out the code step by step

Pre-requistes
1. Generate a API from NASA FIRMS that lets you download near real time and past (upto 10 days) fire event dataset. [Click here](https://firms.modaps.eosdis.nasa.gov/api/area/) to access website to generate one
![image](https://user-images.githubusercontent.com/83420459/201974345-2780ca02-5577-4e28-aea3-4e09582b02bb.png)

2. We shall be filtering the agriculture fire events using Landuse Landcover dataset. If you have one of your own , then well and good. or else download the MODIS LULC (MCD12Q1 V006) by access the website [clicking here](https://lpdaac.usgs.gov/products/mcd12q1v006/)
3. All the essential python libraries. 

# Lets check out the code step by step
Step 1: [Retreiving the fire data.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_1_Retreivng%20the%20fire%20data.py) The generated API, area of Interset, date, date range and path to store the data are the user input here. The dataset shall be downloaded from 3 different sensors.

Step2: [Merging the fire data.](https://github.com/moorthynair/Automated-Agriculture-fire-event-detector/blob/main/Step_2_merging%20of%20data.py) The fire ebvent data retreived from 3 sensors are merged here.
