##
import numpy as np
import kmapper as km
import  pandas as pd
import sklearn
from sklearn.preprocessing import normalize


# df = pd.read_csv("Normalized.csv")
# X = np.array(df)

label_load = pd.read_csv("FINAL_DATA_cleaned.csv")
# JAN - MAR
# start = 158513-2 # Jan
# end = 217359-3 #jan-mar

# #JAN - APR
# start = 158513-2 # Jan
# end = 236979-3 #Jan-Aprl

start = 2-2 # Jan
# NOV - MAY
# start = 118676-2 # Jan
end = 259871-3 #Jan-May

label_load = label_load.loc[start:end,["District","State","Date","Confirmed"]]
# print("Stage 1 passed..!\n")


label_load["Labels"] = label_load["District"]+","+label_load["State"]+","+label_load["Date"]+","+np.array(label_load["Confirmed"]).astype(str)+";\n"
# del semi
labels =np.array(label_load["Labels"])
# print(label_load.head())
# print(labels)
print("Stage 2 passed..!\n")
##
start = 2-2 # Jan
# NOV - MAY
# start = 118676-2 # Jan
end = 259871-3 #Ja
data = pd.read_csv("DataReady.csv")

# day selection
data =data.loc[start:end,:]
X = np.array(data)
X = normalize(X, axis=0)
##

print("Stage 3 passed..!\n")


# Init
mapper = km.KeplerMapper(verbose=1)

# Project
lens = mapper.fit_transform(X, projection=[0,1,2,3])

# Create the simplicial complex


epsilon = 0.02
min_sample = 8
graph = mapper.map(
    lens,
    X,
    clusterer=sklearn.cluster.DBSCAN(eps=epsilon,min_samples=min_sample),
    cover=km.Cover(10, perc_overlap=0.08),
)



# # Visualization
mapper.visualize(
    graph,
    path_html="Nov_may.html",
    title="COVID DATA from Nov to May",
    custom_tooltips=labels,
)
