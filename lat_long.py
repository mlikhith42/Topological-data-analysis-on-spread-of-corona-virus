##
import pandas as  pd
from tqdm import tqdm
from datetime import datetime


lookup = pd.read_csv("LookUp.csv")
data = pd.read_csv("districts.csv")

lat =[]
long =[]
state = []
district = []
size = len(data)

date_format = "%Y-%m-%d"


lookup.index = [lookup["State"]+","+lookup["District"]]

lats = {}
longs = {}
day = {}


a = datetime.strptime("2020-04-25", date_format)
##

for index,row in tqdm(data.iterrows()):
    # find lat from look up
    # find long from look up

    lt=lookup.loc[[row["State"]+","+row["District"]],'Latitude']
    lng = lookup.loc[[row["State"]+","+row["District"]], 'Longitude']

    b = datetime.strptime(data["Date"][index], date_format)
    delta = b - a

    # print()
    lats[index]=lt[0]
    # print(type(lt),lats)
    longs[index] = lng[0]

    dt = int(str(delta).split(" ")[0])

    day[index] = dt

print(data.columns)

finals = pd.DataFrame()
finals["Latitude"] =  lats.values()
finals["Longitude"] = longs.values()
finals["Confirmed"] = data["Confirmed"]
finals["Day"] = day.values()


finals.to_csv("DataReady.csv",index=False)
data["Latitude"] = lats.values()
data["Longitude"] = longs.values()
data["Day"] = day.values()

data.to_csv("FINAL_DATA_cleaned.csv",index=False)

