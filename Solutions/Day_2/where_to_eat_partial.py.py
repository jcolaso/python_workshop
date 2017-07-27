# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:55:43 2017

@author: Gunnvant
"""

import os
import requests
import pandas as pd


base_dir='E:\Work\Python\Python Trainings'

os.chdir(base_dir)

key=open('google_places_api.txt','r')
k=key.read()
key.close()

url='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=17.4138,78.4398&radius=500&type=restaurant&key='+k

response=requests.get(url).json()

place_id=[]
name=[]
open_now=[]
rating=[]
types=[]

for i in response['results']:
    try:    
        place_id.append(i['place_id'])
    except:
        place_id.append('None')
    try:
        name.append(i['name'])
    except:
        name.append('None')
    try:
        open_now.append(i['opening_hours']['open_now'])
    except:
        open_now.append('None')
    try:
        rating.append(i['rating'])
    except:
        rating.append('None')
    try:
        types.append(" ".join(i['types']))
    except:
        types.append('None')
        
restaurants=pd.DataFrame({'place_id':place_id,'name':name,'open_now':open_now,'rating':rating,'types':types})

mask=restaurants['types'].apply(lambda x: 'bar' in x)

restaurants[mask]['name']

## PageToken
url='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=17.4138,78.4398&radius=1500&type=restaurant&key='+k

response=requests.get(url).json()

place_id=[]
name=[]
open_now=[]
rating=[]
types=[]

def run_loop():
    for i in response['results']:
        try:    
            place_id.append(i['place_id'])
        except:
            place_id.append('None')
        try:
            name.append(i['name'])
        except:
            name.append('None')
        try:
            open_now.append(i['opening_hours']['open_now'])
        except:
            open_now.append('None')
        try:
            rating.append(i['rating'])
        except:
            rating.append('None')
        try:
            types.append(" ".join(i['types']))
        except:
            types.append('None')

run_loop()

while 'next_page_token' in response.keys():
    u='https://maps.googleapis.com/maps/api/place/nearbysearch/json?pagetoken='+response['next_page_token']+"&key="+k
    response=requests.get(u).json()
    run_loop()
    
restaurants=pd.DataFrame({'place_id':place_id,'name':name,'open_now':open_now,'rating':rating,'types':types})

mask=restaurants['types'].apply(lambda x: 'bar' in x)

restaurants[mask][['name','rating']].sort_values(by='rating',ascending=False)

