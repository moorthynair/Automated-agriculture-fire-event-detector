
# Automated-Agriculture-fire-event-detector
[![Agri-Fire](https://img.shields.io/badge/Agri-Fire-red
)](https://choosealicense.com/licenses/mit/) 
[![Python](https://img.shields.io/badge/Python-blue
)](https://opensource.org/licenses/)
[![Apache License](https://img.shields.io/badge/license-Apache-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

These set of codes can automatically download and process agriculture fire events occurred over an area of interest on an Near Real Time (NRT) basis. The base information/data for analysis are retreived from the National Aeronautics and Space Administration (NASA). NRT information is available on a 3 hour lag basis, user can run the model multiple times a day to track the latest agriculture fire events. 

## Purpose
Burning crop residue is generally discouraged because of the harm it does to soil biodiversity and public health owing to air pollution. The agriculture officials are mandated to monitor such fire activities in order to take appropriate action. Automating this exercise using satellite-retrieved data will optimise the on-ground judgements and actions because performing this activity manually in an agricultural state is difficult and has a high risk of missing out on specific fire activities.
 
**Note:** We are here only retreiving NRT and past data upto 10 days to facilitate officals with immediate information for corrective actions. For retrospective data, one must access the archieve dataset provided in the NASA FIRMS website.



## Installation on local machine

1. Start by creating a new conda environment.
```bash
  conda create -n fire_analysis python==3.10.1
```
2. Activate the environment
 ```bash
  conda activate fire_analysis
```   
3. Clone the project
```bash
  git clone https://github.com/moorthynair/Automated-Agriculture-fire-event-detector.git
``` 
4. Navigate to the 'Automated-Agriculture-fire-event-detector' directory
```bash
  cd Automated-Agriculture-fire-event-detector
``` 
5. Install the dependencies
```bash
  pip install -r requirement.txt
  conda install gdal ## Run this only if the gdal installation fails
  $ pip install .
``` 
    
## Environment Variables

To run this project, you will need to add the following environment variables to your config.ini file

`path` - specify the path to Automated-Agriculture-fire-event-detector directory on the local machine

`aoi_boundary` - specify the path to the area of interest shapefile in .shp format.

`aoi_attributes` - List the attribute names from the AOI file that you wish to retain in the final result, separated by commas. For example: taluka name, district name.

`API` - provide the API generated from NASA FIRMS. Refer documentation section for more information

`date` - Enter a preferred date in the format (YY-MM-DD). If the user prefers to use the current date, simply type 'current' instead of providing a specific date

`date_range` - Enter a value between 1 and 10. This specifies the range of dates from the provided `date` for which the fires will be retrieved for analysis

`viirs` - is the confidence value of the VIIRS satellite retrievals to be retained. Recommeded to leave it as default. Refer documentation section for more

`modis` - is the minimum confidence value of the modis satellite retrievals to be retained. User may enter a custom value or leave it as the default. Refer to the documentation for more details

`output_path` - specify the directory where the final result shall be saved
## Feedback

If you have any feedback, please reach out to me at moorthymnair@yahoo.in

