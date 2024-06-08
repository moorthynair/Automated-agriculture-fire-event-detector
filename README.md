# Automated-Agriculture-fire-event-detector
These set of codes can automatically download and process agriculture fire events occurred over an area of interest with a single click. The base information/data for analysis are retreived from the National Aeronautics and Space Administration (NASA) owned satellites. Since NASA provides data on Near Real Time (NRT) basis (Lag of 1-3 hours of the satellite overpass), one can run the code multiple times a day to track the latest agriculture fire events. 

## The purpose
Burning crop residue is generally discouraged because of the harm it does to soil biodiversity and public health owing to air pollution. The agriculture officials are mandated to monitor such illegal activity in order to take appropriate action. Automating this exercise using satellite-retrieved data will optimise the on-ground judgements and actions because performing this activity manually in an agricultural state is difficult and has a high risk of missing out on specific fire activities.
 
**Note:** We are here only retreiving NRT and past data upto 10 days to facilitate officals with immediate information for corrective actions. For retrospective data, one must access the archieve dataset provided in the NASA FIRMS website.

## Pre-requisites
**Req-1:** Generate a API from NASA FIRMS that lets you download NRT and past (upto 10 days) fire event dataset. [Click here](https://firms.modaps.eosdis.nasa.gov/api/area/) to access website and scroll down to generate one

**Req-2:** Shapefile of your area of interest. Shapefile can be of any administrative level (state or district) based on requirement. One may explore [Survey of India](https://onlinemaps.surveyofindia.gov.in/Digital_Product_Show.aspx) and [gisdata](https://gisdata.mapog.com/india/States%20level%201)

## Step by step instruction to set up the repository
Let's proceed, assuming 'Anoconda' is installed in the local machine. if not, user may perform simple google search to know how to setup one.
1. Start by creating a new conda environment. I have provided 'fire_analysis' as the environment name. User may provide a preferred name.
   <br/>`conda create -n fire_analysis python==3.10.1`
   
2. Activate the environment.
   <br/>`conda activate fire_analysis`
   
3. Clone the github repository
   <br/>`git clone https://github.com/moorthynair/Automated-Agriculture-fire-event-detector.git`
   
4. Navigate to the 'Automated-Agriculture-fire-event-detector' folder
   <br/>`cd Automated-Agriculture-fire-event-detector`
   
5. Install the supporting libraries to run the model
   <br/>`pip install -r path/to/requirement.txt`
   <br/>`conda install gdal` -- Run this only if gdal installation fails
   <br/>`$ pip install .`
