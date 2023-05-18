# necessary imports
from urllib.request import urlopen
import json
import pandas as pd

link = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"

# read data from link as dictonary
response = urlopen(link)  
data_json = json.loads(response.read())
  
#print(data_json)

# create list contain columns names.
columns = data_json['pokemon'][0].keys()


#check if any columns are missing or not if any then add it with value of Nan
for i in range(len(data_json['pokemon'])):
    #print(data_json['pokemon'][i].keys())
    for j in columns:
        if j not in data_json['pokemon'][i].keys():
            data_json['pokemon'][i][j] = "Nan"
            #print(f"{i} : {j}")

#create dataframe from dictonary.
df = pd.DataFrame.from_dict(data_json['pokemon'], orient='columns')

# create excel file from dataframe 
df.to_excel("pokemon.xlsx")