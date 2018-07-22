import numpy as np
import pandas as pd

# sklearn preprocessing for dealing with categorical variables
from sklearn.preprocessing import LabelEncoder

# File system manangement
import os

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')

import matplotlib.pyplot as plt
import seaborn as sns

# List files available
os.listdir('../input')
app_train =  pd.read_csv('../input/application_train.csv')
print("training data shape",app_train.shape)
app_train.head()

#TARGETS - is the column where 0 is mentioned for loan paid and 1 for loan not paid

#Examine the Distribution of the Target Column
#The target is what we are asked to predict: either a 0 for the loan was repaid on time, or a 1 indicating the client had payment difficulties.
# We can first examine the number of loans falling into each category.
app_train['TARGET'].value_counts()












