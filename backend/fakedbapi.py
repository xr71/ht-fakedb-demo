from flask import jsonify
import pandas as pd
import os 

thisfile = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(thisfile, "fakedb.csv")
DATA = pd.read_csv(filepath)

def apifetchall():

    return DATA.to_json(orient="records")

def sendtodom():

    return list(DATA.values)
