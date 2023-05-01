#!/usr/bin/env python
# coding: utf-8

# # NYC TLC Project

# In[31]:


import pandas as pd               #library exercise for buidling dataframes
import numpy as np                #numpy is imported with pandas
import matplotlib.pyplot as plt   #visualization library
import seaborn as sns             #visualization library
from scipy import stats             #stats library

df = pd.read_csv('2017_yellow_taxi_trip_data.csv')
print("done")


# In[2]:


#Understand &  Interpret the Data Table


# In[3]:


df.head(10)


# In[4]:


df.shape


# In[5]:


df.info()


# In[6]:


#Sort variable (trip_distance) from maximum to minimum value. 

df_sort = df.sort_values(by=['trip_distance'],ascending=False) 
df_sort.head(10)


# In[7]:


#Sort variable (total_amaount) from maximum to minimum value. 

df_sort = df.sort_values(by=['total_amount'],ascending=False)
df_sort.head(10)


# In[8]:


#Understand the data

df.describe()


# In[9]:


#Histogram of TOTAL AMOUNT

plt.figure(figsize=(8,6))
plt.xticks(fontsize=14); plt.yticks(fontsize=14)
df = df.sort_values(by='total_amount')
plt.hist(df['total_amount'],bins=[0,20,40,60,80,100])
plt.title('Histogram of Total Amount',fontsize=20)
plt.xticks(fontsize=15); plt.yticks(fontsize=15)
plt.xlabel('$ amount bin',fontsize=20)
plt.ylabel('Count', fontsize=20)


# In[10]:


#Histogram of TRIP DISTANCE

plt.figure(figsize=(8,6))
#plt.xticks(fontsize=14); plt.yticks(fontsize=14)
df = df.sort_values(by='trip_distance')
plt.hist(df['trip_distance'],bins=[0,5,10,20,25])
plt.title('Histogram of Trip Distance',fontsize=20)
plt.xticks(fontsize=15); plt.yticks(fontsize=15)
plt.xlabel('Trip distance bin',fontsize=20)
plt.ylabel('Count', fontsize=20)


# In[11]:


import datetime as dt


# In[12]:


df.info()


# In[13]:


#Checking for outliers using a box plot visualization

'''convert date columns to datetime'''

df['tpep_pickup_datetime']=pd.to_datetime(df['tpep_pickup_datetime'])
df['tpep_dropoff_datetime']=pd.to_datetime(df['tpep_dropoff_datetime'])


# In[14]:


sns.boxplot(data=None, x=df['trip_distance'], fliersize=1)


# In[15]:


sns.boxplot(x=df['total_amount'], fliersize=1)


# In[16]:


sns.boxplot(x=df['trip_distance'], fliersize=1)


# In[17]:


'''Creates a boolean DataFrame where True is assigned to the cells that are equal to 0, and False otherwise. the line of code removes the rows from the 'trip_distance' column of the df DataFrame where all the values are 0, and assigns the resulting Series to a new variable called df_2'''
df_2 = df['trip_distance'].loc[~(df==0).all(axis=1)]
sns.scatterplot(x=df['total_amount'], y=df_2)


# In[18]:


df.groupby('DOLocationID')['trip_distance'].mean()


# In[19]:


sns.barplot(data=df, x=df['DOLocationID'], y=df['trip_distance'])


# In[20]:


df['trip_duration'] = (df['tpep_dropoff_datetime']-df['tpep_pickup_datetime'])
df.head()


# In[21]:


df.head(10)


# In[22]:


df = pd.read_csv("2017_yellow_taxi_trip_data.csv", index_col = 0)


# In[23]:


df.head(10)


# End of Course Project 4: Conduct A/B Testing
#         The goal for this A/B test is to sample data and analyze whether there is a relationship between payment type and fare amount.

# In[28]:


taxi_data = pd.read_csv("2017_yellow_taxi_trip_data.csv", index_col = 0)


# In[29]:


# descriptive stats code for EDA
taxi_data.describe(include='all')


# In[26]:


# what is the average fare amount for each payment type
taxi_data.groupby('payment_type')['total_amount'].mean()


# Step1: State the null and alternative hypothesis.
# 
# 𝐻0: There is no difference in the average total fare amount between customers who use credit cards and customers who use cash.
# 
# 𝐻𝐴: There is a difference in the average total fare amount between customers who use credit cards and customers who use cash.
# 
# Step2: Choose a significance level = 5%

# In[32]:


#hypothesis test, A/B test
#significance level

credit_card = taxi_data[taxi_data['payment_type'] == 1]['total_amount']
cash = taxi_data[taxi_data['payment_type'] == 2]['total_amount']
stats.ttest_ind(a=credit_card, b=cash, equal_var=False)


# Since the p-value is extremely small (much smaller than the significance level of 5%), you reject the null hypothesis. You conclude that there is a statistically significant difference in the average total fare amount between customers who use credit cards and customers who use cash.
# 

# In[ ]:




