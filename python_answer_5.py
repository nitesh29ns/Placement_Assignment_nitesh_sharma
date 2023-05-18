#necessary imports

import pandas as pd
import json
from urllib.request import urlopen
import datetime

link = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"


# read data from the url as dictionary
response = urlopen(link)
data_json = json.loads(response.read())

# extract required data
data = data_json['_embedded']['episodes']

#create a data_list containing all the required records as per the requirements
data_list = []
for i in range(len(data)):
    dic= {"id":int(data[i]['id']),
          "url":str(data[i]['url']),
          "name":str(data[i]['name']),
          "number":int(data[i]['number']),
          "type": str(data[i]['type']),
          "airdate":data[i]['airdate'],
          "airtime":datetime.datetime.strptime(data[i]['airtime'], "%H:%M").strftime("%I:%M %p"),
          "runtime":float(data[i]['runtime']),
          "average rating":float(data[i]['rating']['average']),
          "medium image link":str(data[i]['image']['medium']),
          "Original image link":str(data[0]['image']['original']),
          "summary":str(data[i]['summary'].replace("<p>","").replace("</p>",""))
        }
    data_list.append(dic)



# create dataframe from dictionary.
df = pd.DataFrame.from_dict(data_list, orient='columns')

#change the airdate to datetime format.
df['airdate'] = pd.to_datetime(df['airdate'], errors="coerce")

# create a csv file from the dataframe
df.to_csv("output1.csv")