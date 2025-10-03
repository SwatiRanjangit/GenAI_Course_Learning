import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
import pickle

# load dataset
data = pd.read_csv('Churn_Modeling.csv')
print(data.head())