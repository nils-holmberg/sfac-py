#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210930-vis/)
# 
# # data visualization using matplotlib, seaborn (210930)
# some line
# 
# # section 4.1.1
# some line
# 
# # section 4.1.2
# some line
# 
# # section 4.1.3
# some line
# 

# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#!pip install seaborn
import seaborn as sns

#%matplotlib inline
#%reload_ext autoreload
#%autoreload 2


# In[5]:


#dfc = pd.read_csv('some.csv')
print(sns.get_dataset_names())
dfc = sns.load_dataset('car_crashes')
dfc.head()


# In[6]:


sns.displot(dfc['not_distracted'])


# ## Quickly Creating Summary Counts in Pandas
# 
# Let's next count the number of samples for each species. We can do this in a few
# ways, but we'll use `groupby` combined with **a `count()` method**.

# In[7]:


surveys_df = pd.read_csv("../../csv/surveys.csv")

# Count the number of samples by species
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)


# 
# Or, we can also count just the rows that have the species "DO":
# 
# 

# In[8]:


surveys_df.groupby('species_id')['record_id'].count()['DO']


# ## Basic Math Functions
# 
# If we wanted to, we could perform math on an entire column of our data. For
# example let's multiply all weight values by 2. A more practical use of this might
# be to normalize the data according to a mean, area, or some other value
# calculated from our data.
# 
# 

# In[9]:


# Multiply all weight values by 2 but does not change the original weight data
surveys_df['weight']*2


# ## Quick & Easy Plotting Data Using Pandas
# 
# We can plot our summary stats using Pandas, too.
# 
# 

# In[10]:


## To make sure figures appear inside Jupyter Notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Create a quick bar chart
species_counts.plot(kind='bar')


# #### Animals per site plot
# 
# We can also look at how many animals were captured in each site.

# In[11]:


total_count = surveys_df.groupby('site_id')['record_id'].nunique()
# Let's plot that too
total_count.plot(kind='bar')


# ## _Extra Plotting Challenge_
# 
# 1. Create a plot of average weight across all species per plot.
# 
# 2. Create a plot of total males versus total females for the entire dataset.
#  
# 3. Create a stacked bar plot, with weight on the Y axis, and the stacked variable being sex. The plot should show total weight by sex for each plot. Some tips are below to help you solve this challenge:
# [For more on Pandas plots, visit this link.](http://pandas.pydata.org/pandas-docs/stable/visualization.html#basic-plotting-plot)
# 
# 
# 
# 

# ### _Solution to Extra Plotting Challenge 1_

# In[12]:


## Solution Plotting Challenge 1
surveys_df.groupby('site_id').mean()["weight"].plot(kind='bar')


# ### _Solution to Extra Plotting Challenge 2_

# In[13]:


# Solution Plotting Challenge 2
## Create plot of total males versus total females for the entire dataset.

surveys_df.groupby('sex').count()["record_id"].plot(kind='bar')


# ### _Solution to Extra Plotting Challenge 3_
# 
# First we group data by site and by sex, and then calculate a total for each site.

# In[14]:


by_site_sex = surveys_df.groupby(['site_id','sex'])
site_sex_count = by_site_sex['weight'].sum()


# 
# This calculates the sums of weights for each sex within each plot as a table
# 
# ```
# site  sex
# site_id  sex
# 1        F      38253
#          M      59979
# 2        F      50144
#          M      57250
# 3        F      27251
#          M      28253
# 4        F      39796
#          M      49377
# <other sites removed for brevity>
# ```
# 
# Below we'll use `.unstack()` on our grouped data to figure out the total weight that each sex contributed to each plot.
# 
# 

# In[15]:


by_site_sex = surveys_df.groupby(['site_id','sex'])
site_sex_count = by_site_sex['weight'].sum()
site_sex_count.unstack()


# Now, create a stacked bar plot with that data where the weights for each sex are stacked by plot.
# 
# Rather than display it as a table, we can plot the above data by stacking the values of each sex as follows:

# In[16]:


by_site_sex = surveys_df.groupby(['site_id', 'sex'])
site_sex_count = by_site_sex['weight'].sum()
spc = site_sex_count.unstack()
s_plot = spc.plot(kind='bar', stacked=True, title="Total weight by site and sex")
s_plot.set_ylabel("Weight")
s_plot.set_xlabel("Site")


# In[ ]:





# In[ ]:




