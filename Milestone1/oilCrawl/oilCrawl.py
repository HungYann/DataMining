#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:47:52 2020

@author: Gunasegarran
"""

import requests
import requests.cookies
import json
import time
import pandas as pd
from bs4 import BeautifulSoup


url='https://www.macrotrends.net/2516/wti-crude-oil-prices-10-year-daily-chart'
res = requests.get(url)

df = pd.read_html(res.text)
pan = pd.DataFrame(df[0])
d={'Year':pan.iloc[:,0],'AverageClosing Price':pan.iloc[:,1],'Year Open':pan.iloc[:,2],'Year High':pan.iloc[:,3],'Year Low':pan.iloc[:,4],'Year Close':pan.iloc[:,5],'Annual% Change':pan.iloc[:,6]}
df = pd.DataFrame(data=d)
df.to_csv('oilCrawl.csv')
df