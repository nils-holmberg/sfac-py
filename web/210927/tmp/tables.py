#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210927/)
# 
# # python for research using the scipy stack (210927)
# some line
# 
# ## overview day 1
# 
# - some intro
# - easy start in google colab
# - variables, flow control, con
# - from ca 11-12 am, install anaconda3
# 
# ## some intro
# 
# - spyder ide, jupyter notebooks
# - data structures, functions, pkgs
# - navigate file system, working dir 
# - **mindset: excel on steroids**
# - file system, folders, csv files
# - checking, cleaning, summarizing 
# - sql-like operations on datasets
# - combination of numeric and text 
# - intro to day 2, nlp and spacy
# 
# <img src="../../fig/Microsoft_Office_Excel_2019_present.svg.png" width="500"/>

# ## exercise 1
# some line
# 
# ![caption](../../fig/612497595dc00-2-612344de79979__700.jpg)

# In[1]:


import pandas as pd
import seaborn as sns

# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
df = sns.load_dataset('iris')
df.head()


# In[2]:


df.to_csv("csv/iris.csv", sep="\t", header=True, index=False)


# In[1]:


import pandas as pd

# file path on google colab
fp = '/content/iris.csv'
# file path relative to local working dir
fp = '../../csv/iris.csv'

df = pd.read_csv(fp, sep="\t", header=0)
df.head()


# In[ ]:




