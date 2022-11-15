# Automated-Agriculture-fire-event-detector
I managed to develop set of codes that can download and process agriculture fire events for any area of interest. Lets check out the code step by step

Pre-requistes
1. Generate a API from NASA FIRMS that lets you download near real time and past (upto 10 days) fire event dataset
2. We shall be filtering the agriculture fire events using Landuse Landcover dataset. If you have one of your own , then well and good. or else download the MODIS LULC (MCD12Q1 V006)
3. All the essential python libraries

# Lets check out the code step by step
Step 1: Download the fire data. The generated API, area of Interset, date, date range and path to store the data are the user input here. The dataset shall be downloaded from 3 different sensors. Explore the codes to know more
Step 2: 
