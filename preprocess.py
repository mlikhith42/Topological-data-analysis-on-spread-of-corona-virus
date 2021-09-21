import numpy as np
import pandas as  pd
from tqdm import tqdm

from sklearn.preprocessing import normalize

data = pd.read_csv("DataReady.csv")


X = normalize(data)

# print(X[0])

normalized = pd.DataFrame(X,columns=["Latitude","Longitude","Confirmed","Day"])
normalized.to_csv("Normalized.csv",index=False)