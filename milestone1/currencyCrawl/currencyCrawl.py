#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:47:52 2020

@author: Gunasegarran
"""

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import numpy as np
import csv
from pathlib import Path

csvExist = Path('currencyExchange.csv') #creating a file in csv extention
#Only enable when overwriting with new columns
#if csvExist.is_file():
#    pass
#else:
with open ('currencyExchange.csv','wb') as createFile: #This line will create a csv file under name webcrawler
        filewriter = csv.writer(createFile)

url = "https://www.investing.com/currencies/usd-myr-historical-data"
req = urllib.request.Request(url, data=None, headers={'User-Agent': 'Chrome/35.0.1916.47'})

soup = BeautifulSoup(urllib.request.urlopen(req).read(),"lxml")

#extract data 
rows = soup.find('table',{'class': 'genTbl closedTbl historicalTbl'}).findAll('tr')[1:]
data = []
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip(' ') for ele in cols]
    data.append([ele for ele in cols if ele])
 
#extract column names 
colnames = soup.find('table',{'class': 'genTbl closedTbl historicalTbl'}).findAll('tr')[:1]
col_names = []
for col in colnames:
    cols = col.find_all('th')
    cols = [ele.text.strip() for ele in cols]
    col_names.append(cols)
col_names = col_names[0]
    
#Write data to files
df1 = pd.DataFrame(data,columns = col_names)
df1.to_csv('currencyExchange.csv',mode = 'w', index=False)
df1