#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210927/)
# 
# # python for research using the scipy stack (210927)
# some line
# 
# ## exercise 1
# some line
# 

# In[1]:


import pandas as pd
import seaborn as sns

# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
df = sns.load_dataset('iris')
df.head()


# In[2]:


df.to_csv("csv/iris.csv", sep="\t", header=True, index=False)


# In[ ]:




