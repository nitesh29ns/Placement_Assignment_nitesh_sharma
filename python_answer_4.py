## necessary imports

import pandas as pd
import json
from urllib.request import urlopen
import datetime

link = "https://data.nasa.gov/resource/y77d-th95.json"

# read data from the url as dictionary
response = urlopen(link)
data_json = json.loads(response.read())

# create list contain keys names.
keys = data_json[0].keys()


#check if any keys are missing or not if any then add it with value of Nan
for i in range(len(data_json)):
    #print(data_json['pokemon'][i].keys())
    for j in keys:
        if j not in data_json[i].keys():
            data_json[i][j] = "Nan"
            

# create a list of dictionary as per the requirements given in the questions
data = []
for i in range(len(data_json)):
    dic = {"Name of Earth Meteorite" :data_json[i]['name'],
           "ID of Earth Meteorite" :int(data_json[i]['id']),
            "nametype" :data_json[i]['nametype'],
            "recclass" :data_json[i]['recclass'],
            "Mass of Earth Meteorite" :float(data_json[i]['mass']),
            "Year at which Earth Meteorite was hit" :data_json[i]['year'],
            "reclat" :float(data_json[i]['reclat']),
            "recclong" :float(data_json[i]['reclong']),
            "point coordinates":[int(data_json[0]['geolocation']['coordinates'][0]),int(data_json[0]['geolocation']['coordinates'][1])]}
    
    data.append(dic)

# create dataframe fromm dictionary
df = pd.DataFrame.from_dict(data, orient="columns")

# change Year at which Earth Meteorite was hit colum in datatime format.
df['Year at which Earth Meteorite was hit'] = pd.to_datetime(df['Year at which Earth Meteorite was hit'],errors = 'coerce')

# create a csv file from the dataframe
df.to_csv("output.csv")