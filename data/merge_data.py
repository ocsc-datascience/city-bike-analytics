#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np

infilelist = [
    "201711-citibike-tripdata.csv.zip",
    "201712-citibike-tripdata.csv.zip",
    "201801-citibike-tripdata.csv.zip",
    "201802-citibike-tripdata.csv.zip",
    "201803-citibike-tripdata.csv.zip",
    "201804-citibike-tripdata.csv.zip",
    "201805-citibike-tripdata.csv.zip",
    "201806-citibike-tripdata.csv.zip",
    "201807-citibike-tripdata.csv.zip",
    "201808-citibike-tripdata.csv.zip",
    "201809-citibike-tripdata.csv.zip",
    "201810-citibike-tripdata.csv.zip",
]

infilelist = [
    "201307-citibike-tripdata.zip",
    "201407-citibike-tripdata.zip",
    "201507-citibike-tripdata.zip",
    "201607-citibike-tripdata.zip",
    "201707-citibike-tripdata.csv.zip",
    "201807-citibike-tripdata.csv.zip",
    ]


dflist = []
for infile in infilelist:
    xdf = pd.read_csv(infile)
    print(xdf.columns)
    xdf['starttime'] = pd.to_datetime(xdf['starttime'])
    xdf['stoptime'] = pd.to_datetime(xdf['stoptime'])
    xdf['birth year'] = xdf['birth year'].fillna(0.0)
    xdf['birth year'] = xdf['birth year'].apply(lambda x: int(x) if x != '\\N' else 0)
    dflist.append(xdf)

df = dflist[0]
for i in range(1,len(dflist)):
    df = df.append(dflist[i])


df = df.dropna()
    
df.to_csv("combined.csv")
