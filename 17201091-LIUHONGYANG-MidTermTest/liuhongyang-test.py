#!/usr/bin/env python
# coding: utf-8

# ##### Name: LIU,HONGYANG
# 
# ##### Matric Number: 17201091/1
# 
# **Target crawling website:**  https://www.macrotrends.net/2516/wti-crude-oil-prices-10-year-daily-chart

# **1.You are required to write code that will crawl the WWW (your familiar domain) of a particular website and collect data from social media or from report or news and so on and to produce dataset.**

# In[1]:


#crawl oil Price data
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
df.head()


# **2.   After that you are required to write code to modify and/or select your the attributes to perform the following tasks:
# Data Cleaning
# Data Integration 
# Data Transformation
# Data Reduction
# Hint : Make sure that use graph to help you select appropriate attributes to perform the above tasks.**
#                                                                                                     

# #### 2.1 Data Cleaning

# In[2]:


#check missing data
df.isnull().sum().any()


# In[3]:


#check duplicated data
df.loc[df.duplicated(),:]


# In[4]:


#check inconsistent data;
#we can find the type of attributes are inconsistent
df.dtypes


# Consequently, we need use data  cleaning to change the  data types of the attributes and make the data types become numeric.

# #### 2.2 Data Integration

# - we will download another source data from this website: https://datahub.io/core/gdp-us
# 
# - Integrate the two kind of sources into one

# In[5]:


#download and read another data source
AmericaGdp=pd.read_csv('year_csv.csv')

#check the first five rows of data 
AmericaGdp.head()


# In[6]:


#1.rename "data" attributes to "Year"
#2.we will integrate attributes in AmericaGdp datasets with the attributes oilPrice datasets in Question 4;

AmericaGdp=AmericaGdp.rename(columns={'date':'Year'})
AmericaGdp.head()


# After intergration in Question 4:
# the data sets should look like this:
#     
# ![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf130bvmsrj31dc07wgmw.jpg)
#     

# #### 2.3 Transformation

# In[7]:


# check the oilPrice datasets
df.describe()


# In[8]:


# check the AmericaGdp datasets
AmericaGdp.describe()


# 
# **Run the code`AmericaGdp.describe()`, check the standard deviation, we can find the `level-current` `level-chained` columns have very high standard deviation.**
# 
# **we need scale the two attributes in Question 5**
# ![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf12v298gxj30r00bmmyl.jpg)
# 

# #### 2.4 Data Reduction

# In[9]:


# check the AmericaGdp columns
AmericaGdp.columns


# In[10]:


#check the oil price columns
df.columns


# we will delete some unrelated attributes to make datasets that have only two components:
# **features** and **targets**

# In[11]:


#fautures:
features=['level-current','level-chained','change-current','change-chained']

#targets:
targets=['Year Close']


# Finally, we will use PCA to do **reduce features attributes and dimensionality** in Question 6

# **3.You are required to write data cleaning code  using the appropriate attribute (Question 2). In order to achieve the task, you are going to cover the following steps:
# Importing required libraries
# Loading Data
# Before data cleaning, plot your result (attribute)
# Data cleaning
# After data cleaning, plot your result (attribute)**
# 

# In[12]:


# import libraries
import pandas as pd


# before data cleaning

# In[13]:


df.head()


# data cleaning

# In[14]:


# In quesion2, we note that the data is inconsistent because we need remove symbol'$' and '%' 
df.loc[:,['AverageClosing Price','Annual% Change']].head()


# In[15]:


#Removing the symbol '%' and '$'
df['Annual% Change'] = list(map(lambda x: x[:-1], df['Annual% Change'].values))
df['AverageClosing Price'] = list(map(lambda x: x[1:], df['AverageClosing Price'].values))
df['Year Open'] = list(map(lambda x: x[1:], df['Year Open'].values))
df['Year High'] = list(map(lambda x: x[1:], df['Year High'].values))
df['Year Low'] = list(map(lambda x: x[1:], df['Year Low'].values))
df['Year Close'] = list(map(lambda x: x[1:], df['Year Close'].values))


df.head()


# In[16]:


# then, we need solve data inconsistent problem
df.dtypes


# In[17]:


#after the '%' and '$' symbol has been removed
# We note that column values for columns have data types of string
# so we need to convert these to numeric data as follows:
df['Annual% Change'] = [float(x) for x in df['Annual% Change'].values]
df['AverageClosing Price'] = [float(x) for x in df['AverageClosing Price'].values]
df['Year Open'] = [float(x) for x in df['Year Open'].values]
df['Year High'] = [float(x) for x in df['Year High'].values]
df['Year Low'] = [float(x) for x in df['Year Low'].values]
df['Year Close'] = [float(x) for x in df['Year Close'].values]

df.head()


# after data cleaning

# In[18]:


#check the data
df.head()


# In[19]:


#check the data type
df.dtypes


# **4.   You are required to write data integration code  using the appropriate attribute (Question 2). In order to achieve the task, you are going to cover the following steps: 
# Importing required libraries
# Loading Data
# Before data cleaning, plot your result (attribute)
# Data cleaning
# After data cleaning, plot your result (attribute)**

# In[20]:


# import libraries
import pandas as pd


# before integraion

# In[21]:


#oilPrice datasets
df.head()


# In[22]:


#American gdp datasets
AmericaGdp.head()


# integration

# In[23]:


# According to quesiont2.2,we will merge df sets and American GDP sets
#merge two data sources: oldPrice and American GDP, using Year value
integration=pd.merge(df,AmericaGdp,on='Year')


# after integration

# In[24]:


integration.head()


# **5.   You are required to write data transformation code  using the appropriate attribute (Question 2). In order to achieve the task, you are going to cover the following steps:
# Importing required libraries
# Loading Data
# Before data transformation,  plot your result (attributes)
# Data transformation
# After data transformation, plot your result (attributes)
#                                   Hint : Normalization, Aggregation and Generalization**
# 

# In[25]:


# import libraries
import pandas as pd
from sklearn import preprocessing


# before transformation

# In[26]:


#check the value
integration.head()


# In[27]:


#check the specific measures:
integration.describe()


# **we need scale the two attributes**
# 
# ![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf13ptlqhhj31fk0c0tb5.jpg)

# data transformation

# In[28]:


transformation = preprocessing.scale(integration.loc[:,['level-current','level-chained']])
transformation  = pd.DataFrame(transformation,columns=['level-current','level-chained'])


integration['level-current'] = transformation['level-current']
integration['level-chained'] = transformation['level-chained']


# after transformation

# In[29]:


#check the value
integration.head()


# In[30]:


#check the specific measures:
#we can find the attributes have been scaled 
integration.describe()


# From the desceibe() method, we can find the two attributes **level-current** and **level-chained** have been scaled.
# 
# ![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf15m4adnmj31fa0cg0ve.jpg)

# **6.   You are required to write data reduction code  using the appropriate attribute (Question 2). In order to achieve the task, you are going to cover the following steps:
# Importing required libraries
# Loading Data
# Before data reduction,  plot your result (attributes)
# Data reduction
# After data reduction, plot your result (attributes)**
# 

# In[31]:


# import libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# before reduction

# In[32]:


integration.head()


# data reduction

# In[33]:


#fautures:
features=['level-current','level-chained','change-current','change-chained']

#targets:
targets=['Year Close']

# Separating out the features
x = integration.loc[:,features].values
# Separating out the target
y = integration.loc[:,targets].values

# Standardizing the features
x = StandardScaler().fit_transform(x)


# In[34]:


pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])


# In[35]:


#the features have been change from four to two 
finalDf = pd.concat([principalDf, df[targets]], axis = 1)


# after data reduction

# In[36]:


finalDf.head()


# In[37]:


import matplotlib.pyplot as plt

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)


ax.scatter(finalDf.loc[:, 'principal component 1']
               , finalDf.loc[:, 'principal component 2']
               , s = 50)
ax.legend(targets)
ax.grid()


# the four attributes **features=['level-current','level-chained','change-current','change-chained']** 
# have been reduced to two attributes.
