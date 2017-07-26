# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:17:12 2017

@author: Gunnvant
"""

import pandas as pd
import os
import numpy as np
os.chdir('E:\Work\Python\Python Trainings\Python Advanced\Data')
data=pd.read_csv('starbucks_final.csv')
query="Calories<=450 & Protein<=14 & Fat <=10 & Carb<=40 & Fiber<=5"
#1
data.query(query)
#2
data.query(query).sort_values(['Carb','Protein'],ascending=[1,0])[['Carb','Protein','Calories','Name']]

## James comey
data=pd.read_csv('E:\Work\Python\Python Trainings\Python Advanced\Data\comey.csv')

data['resp_length']=data['Comey Response'].map(lambda x: len(x))
data['question_length']=data['Full Question'].map(lambda x: len(x))

data[data['Party Affiliation']=='Democrat']['resp_length'].mean()

data.groupby('Party Affiliation',as_index=False).agg({'resp_length':np.mean,'question_length':np.mean})

## Assignment 1
os.chdir('E:\Work\Python\Python Trainings\Python Advanced\Data')
data=pd.read_csv('audit.csv')
data.groupby('Gender')['TARGET_Adjusted'].sum()
data.groupby('Gender').size()
data.groupby('Gender')['TARGET_Adjusted'].sum()/data.groupby('Gender').size()



## Assignment 2
data=pd.read_csv('FlightDelays.csv')
data['date']=pd.to_datetime(data['date'])
#1
mask=data['date'].dt.weekday<5
data[mask].query("delay=='delayed'").shape[0]
#2
mask=data['date'].dt.weekday==4
data[mask].query("delay=='delayed'")['distance'].agg([np.mean,np.sum])
data[mask].query("delay=='delayed'").shape[0]
#3
mask=data['date'].dt.weekday>=5
data[mask].query("delay=='ontime'").shape[0]

mask=data['date'].dt.weekday<5
data[mask].query("delay=='ontime'").shape[0]

data['weekend']=data['date'].map(lambda x: 'Yes' if x.weekday()>=5 else 'No')

data[data['delay']=='ontime']['weekend'].value_counts()

#4
mask=data['date'].dt.weekday<5

data[mask].groupby('dest').size()

#5 
data[mask][data['weather']==1].shape[0]