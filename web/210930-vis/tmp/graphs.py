#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210930/)
# 
# # data visualization using matplotlib, seaborn (210930)
# some line
# 
# ## exercise 1
# some line
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#!pip install seaborn
import seaborn as sns

#%matplotlib inline
#%reload_ext autoreload
#%autoreload 2


# In[2]:


#dfc = pd.read_csv('some.csv')
print(sns.get_dataset_names())
dfc = sns.load_dataset('car_crashes')
dfc.head()


# In[3]:


sns.displot(dfc['not_distracted'])


# In[ ]:




