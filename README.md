# Online-dating-fraud-classification-and-dataset-shift

## Data Collection and Processing

The data is not included in this repository, due to ethical restrictions of storing the dating profile data. The scripts *dating_real_download.ipynb* and *dating_fraud_download.ipynb* can be used to scrape the relevant data from datingnmore.com and scamdiggers.com. This data can be cleaned using the Python script *clean.py* and then transferred to csv format using *csvise.py*. These scripts were taken from https://github.com/gsuareztangil/automatic-romancescam-digger, with some minor amendments.   

*Tmestamp_code_add.ipynb* is used to add in the most recent activity dates for the real profiles. This comes from a csv file created in *dating_real_download.ipynb*. *Location_detail_add.ipynb* is used to find the **unique** location fields and search for the latitude and longitude using the geopy package. These are stored in *location_list.csv*.

## Classifier and dataset shift evaluation and mitigation

The script *dating_classify.ipynb* is used to build a histogram-gradient boosting classifier, and then use the TESSERACT Python library to evaluate and mitigate the dataset shift. The TESSERACT Python library is the work of Pendlebury et at. (2019) and they can be contacted for access to the library through the following link: https://s2lab.cs.ucl.ac.uk/projects/tesseract/. 

The files *jobs_list.csv* and *marry_list.csv* are used to categorise these fields (occupation and marriage status), whilst the *location_list.csv* is used to look-up the location fields and provide the longitude and latitude for them in the *dating_classify.ipynb* script. 
