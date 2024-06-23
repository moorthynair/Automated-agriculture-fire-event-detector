
# Automated-Agriculture-fire-event-detector
[![Agri-Fire](https://img.shields.io/badge/Agri-Fire-red
)](https://choosealicense.com/licenses/mit/) 
[![Python](https://img.shields.io/badge/Python-magenta
)](https://opensource.org/licenses/)
[![Apache License](https://img.shields.io/badge/license-Apache-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

This set of codes can automatically download and process agricultural fire events occurring over an Area of Interest (AOI) on a Near Real-Time (NRT) basis. The base data for analysis is retrieved from the National Aeronautics and Space Administration (NASA). NRT information is available with a 3-hour delay, allowing users to run the model multiple times a day to track the latest agricultural fire events. 

## Purpose
Burning crop residue is generally discouraged due to its detrimental effects on soil biodiversity and public health, particularly through air pollution. Agriculture officials are required to monitor such fire activities to take appropriate actions. Automating this monitoring process using satellite-retrieved data will optimize on-ground decisions and actions, as manually performing this task in an agricultural state is challenging and poses a high risk of missing specific fire incidents.
 
**Note:** This process retrieves near real-time (NRT) and past data up to 10 days to provide officials with immediate information for corrective actions. For retrospective data, please refer to the archived dataset available on the NASA FIRMS website.



## Installation on local machine

1. Start by creating a new conda environment.
```bash
  conda create -n agri_fire python==3.10.1
```
2. Activate the environment
 ```bash
  conda activate agri_fire
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
  pip install -e .
``` 
    
## Environment Variables

To run this project, you will need to add the following environment variables to your config.ini file. Use any text editor to make changes

* `aoi_boundary` - specify the path to the area of interest shapefile in .shp format.

* `aoi_attributes` - List the attribute names from the AOI file that you wish to retain in the final result, separated by commas. For example: taluka name, district name. User may use 'QGIS' to figure out the attributes

* `API` - provide the API generated from NASA FIRMS. Refer documentation section for more information

* `date` - Enter a preferred date in the format (YYYY-MM-DD). If the user prefers to use the current date, simply type 'current' instead of providing a specific date

* `date_range` - Enter a value between 1 and 10. This specifies the range of dates from the provided `date` for which the fires will be retrieved for analysis

* `viirs` - is the confidence value of the VIIRS satellite retrievals to be retained. Recommeded to leave it as default. Refer documentation section for more

* `modis` - is the minimum confidence value of the modis satellite retrievals to be retained. User may enter a custom value or leave it as the default. Refer to the documentation for more details

* `output_path` - specify the directory where the model outputs shall be saved
## Run Locally

Once users have specified all the environment variables in the config.ini file. Run

```bash
  python main.py config.ini
```



## Documentation

#### Model inputs
| Input variables             | Description                                                                |
| ----------------- | ------------------------------------------------------------------ |
| `API` | Generate API by visitng [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/api/area/) to retreive fire data on NRT basis |
| `aoi_boundary`| Shapefiles in .shp format. Make sure the files are not corrupted. Users may access [Survey of India](https://onlinemaps.surveyofindia.gov.in/) or [gisdata.mapog](https://gisdata.mapog.com/) to download shapefiles|
| `viirs` | Each of the VIIRS retreivals comes with a confidence score. 'l':low; 'n':nominal; 'h':high are among the scores assigned. Default in the model is to retain the retreivals with score 'n' and 'h'|
| `modis` | Similar to VIIRS, the confidence score for MODIS retrievals ranges from 0-100%. The default value in the model is set to 60%, but users may modify it according to their requirements |


#### Model outputs
| Folders             | Description                                                                |
| ----------------- | ------------------------------------------------------------------ |
| MODIS | Contains all the raw extracts from MODIS satellite |
| VIIRS| Contains all the raw extracts from VIIRS-N21 satellite|
| NOAA | Contains all the raw extracts from VIIRS-N20 satellite|
| Shapefiles | All the fire raw extracts compiled in .shp format |
| Analysed Results|Ready to share results in excel format |
| Multiple Run | Captures new results each time the model is run for the same date|

## Check for repo updates

```bash
  git pull origin main
```


## FAQ

#### 1. Is the model applicable to any region of the country?
**Response**: At present, the model is exclusively applicable to regions within India
#### 2. Can the model detect non-agriculture fires such as forest fires?
**Response**: At present, model can extract only the agriculture fires
#### 3. How many times can a user run the model in a day?
**Response**: Currently, there are no limits sets. It is recommeded to run the model at an interval of 3-4 hours
#### 4. Will the user have to perform coding in python to run the model?
**Response**: No. All the instructions are to be executed in the command terminal

## Feedback

If you have any feedback, please reach out to me at moorthymnair@yahoo.in

