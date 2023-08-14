import pandas as pd
import numpy as np 

#You can download the used data from this site: https://www.kaggle.com/code/rtatman/data-cleaning-challenge-handling-missing-values/input

Data = pd.read_csv("NFL Play_DataSet.csv")
Data2 = pd.read_csv("Building_Permits.csv")
#---------------------------------------------------------------- Handeling Missing Values -------------------------------------------------------------#
# Counting the number of missing values to more explore
missing_values_count = Data.isnull().sum()

# Getting percentage might be give a better sense
total = np.product(Data.shape)
percentage = missing_values_count.sum() / total * 100

# Techniqes
# The Questions you should ask: Is this value missing becuase it wasn't recorded or becuase it dosen't exist?
# 1.If it doesn't exist => keep it as NaN
# 2.If a value is missing becuase it wasn't recorded, then you can try to guess what it might have been based on the other value

# For example:
Data['TimeSecs'].isnull().sum()
# TimeSecs => Seconds left in game at the time of the play. So, missing values are because of not recording
Data['PenalizedTeam'].isnull().sum()
# PenalizedTeam => Missing values are because of no penalty 

#Dropping Or Filling missing data:
Data_Dropped = Data.dropna(axis=1)
Data.fillna(method = "bfill", axis=0).fillna(0)

#---------------------------------------------------------------- Scaling and Normalization -------------------------------------------------------------#

