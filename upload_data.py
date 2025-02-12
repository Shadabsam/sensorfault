from pymongo.mongo_client import MongoClient
import pandas as pd
import json

url="mongodb+srv://shadab:12345@cluster0.97tbl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client=MongoClient(url)

DATABASE_NAME="DB"
COLLECTION_NAME="waferfault"

df=pd.read_csv('C:\Users\shada\OneDrive\Desktop\Sensor Fault Detection\notebooks\wafer_23012020_041211.csv')

df=df.drop('Unnamed: 0',axis=1)

json_record=list(json.loads(df.T.to_json()).values())
