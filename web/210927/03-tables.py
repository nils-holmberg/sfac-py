#!/usr/bin/env python
# coding: utf-8

# ## section 3.1: tables
# - **mindset: excel on steroids**
# - file system, folders, csv files
# - checking, cleaning, summarizing 
# - sql-like operations on datasets
# - combination of numeric and text 
# - intro to day 2, nlp and spacy
# 

# In[1]:


import pandas as pd
import seaborn as sns

# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
df = sns.load_dataset('iris')
df.head()


# In[2]:


df.to_csv("csv/iris.csv", sep="\t", header=True, index=False)


# In[3]:


# file path on google colab
fp = '/content/iris.csv'
# file path relative to local working dir
fp = '../../csv/iris.csv'

df = pd.read_csv(fp, sep="\t", header=0)
df.head()


# In[ ]:




