#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#liuhongyang

import requests
import requests.cookies
import json
import time
import pandas as pd
from bs4 import BeautifulSoup

url='https://www.macrotrends.net/2516/wti-crude-oil-prices-10-year-daily-chart'

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

res = requests.get(url,headers=headers)


try:

    df = pd.read_html(res.text)
    pan = pd.DataFrame(df[0])
    d={'Year':pan.iloc[:,0],'AverageClosing Price':pan.iloc[:,1],'Year Open':pan.iloc[:,2],'Year High':pan.iloc[:,3],'Year Low':pan.iloc[:,4],'Year Close':pan.iloc[:,5],'Annual% Change':pan.iloc[:,6]}
    df = pd.DataFrame(data=d)
    df.to_csv('oilCrawl.csv')

except:

    print("The url doesn't work!")