#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210930-vis/)
# 
# # day 4: getting started with data visualization
# - overview day 4
# 
# |time  |section |concepts                      |outcomes                                                       |
# |:-----|:-------|:-----------------------------|:--------------------------------------------------------------|
# |09-10 |2.1.1   |[spacy](211-intro.html)       |install spacy packages to anaconda venv                        |
# |      |2.1.2   |python syntax                 |practice data structures, conditional statements, flow control |
# |      |2.1.3   |nlp doc                       |create our first nlp document                                  |
# |      |break   |                              |                                                               |
# |10-11 |2.2.1   |[features](221-features.html) |applying nlp analyses to extract linguistic features           |
# |      |2.2.2   |part of speech                |analyze syntactic structure, useful for finding e.g. negations |
# |      |2.2.3   |entity recognition            |extract named entities from text, analyze word similarity      |
# |      |break   |                              |                                                               |
# |11-12 |2.3.1   |[classify](231-classify.html) |how to use scikit-learn for sentiment analysis                 |
# |      |2.3.2   |                              |                                                               |
# |      |2.3.3   |                              |                                                               |
# |12-13 |lunch   |                              |                                                               |
# 
# # section 4.1.1
# - check, update anaconda, install new packages to venv
# 
# ```python
# # update anaconda, env packages
# conda update anaconda
# conda update --all
# # install python visualization packages
# conda install -c conda-forge -n base matplotlib seaborn 
# conda install -c conda-forge -n base plotly dash dash-renderer dash-html-components dash-core-components
# # start jupyter notebook
# jupyter notebook
# ```
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

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%matplotlib inline
#%reload_ext autoreload
#%autoreload 2


# In[2]:


#dfc = pd.read_csv('some.csv')
print(sns.get_dataset_names())
df = sns.load_dataset('car_crashes')
df.head()


# In[3]:


sns.displot(df['not_distracted'])


# ## Quickly Creating Summary Counts in Pandas
# 
# We are studying the species and weight of animals caught in plots in our study
# area. The dataset is stored as a `.csv` file: each row holds information for a
# single animal, and the columns represent:
# 
# | Column           | Description                        |
# |------------------|------------------------------------|
# | record_id        | Unique id for the observation      |
# | month            | month of observation               |
# | day              | day of observation                 |
# | year             | year of observation                |
# | site_id          | ID of a particular plot            |
# | species_id       | 2-letter code                      |
# | sex              | sex of animal ("M", "F")           |
# | hindfoot_length  | length of the hindfoot in mm       |
# | weight           | weight of the animal in grams      |
# 
# Let's next count the number of samples for each species. We can do this in a few
# ways, but we'll use `groupby` combined with **a `count()` method**.

# In[4]:


surveys_df = pd.read_csv("../../csv/surveys.csv")

# Count the number of samples by species
species_counts = surveys_df.groupby('species_id')['record_id'].count()
print(species_counts)


# 
# Or, we can also count just the rows that have the species "DO":
# 
# 

# In[5]:


surveys_df.groupby('species_id')['record_id'].count()['DO']


# ## Basic Math Functions
# 
# If we wanted to, we could perform math on an entire column of our data. For
# example let's multiply all weight values by 2. A more practical use of this might
# be to normalize the data according to a mean, area, or some other value
# calculated from our data.
# 
# 

# In[6]:


# Multiply all weight values by 2 but does not change the original weight data
surveys_df['weight']*2


# ## Quick & Easy Plotting Data Using Pandas
# 
# We can plot our summary stats using Pandas, too.
# 
# 

# In[7]:


## To make sure figures appear inside Jupyter Notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Create a quick bar chart
species_counts.plot(kind='bar')


# #### Animals per site plot
# 
# We can also look at how many animals were captured in each site.

# In[8]:


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

# In[9]:


## Solution Plotting Challenge 1
surveys_df.groupby('site_id').mean()["weight"].plot(kind='bar')


# ### _Solution to Extra Plotting Challenge 2_

# In[10]:


# Solution Plotting Challenge 2
## Create plot of total males versus total females for the entire dataset.

surveys_df.groupby('sex').count()["record_id"].plot(kind='bar')


# ### _Solution to Extra Plotting Challenge 3_
# 
# First we group data by site and by sex, and then calculate a total for each site.

# In[13]:


by_site_sex = surveys_df.groupby(['site_id','sex'])
#by_site_sex.head()

site_sex_count = by_site_sex['weight'].sum()
site_sex_count.head()


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

# In[14]:


by_site_sex = surveys_df.groupby(['site_id','sex'])
site_sex_count = by_site_sex['weight'].sum()
site_sex_count.unstack()


# Now, create a stacked bar plot with that data where the weights for each sex are stacked by plot.
# 
# Rather than display it as a table, we can plot the above data by stacking the values of each sex as follows:

# In[15]:


by_site_sex = surveys_df.groupby(['site_id', 'sex'])
site_sex_count = by_site_sex['weight'].sum()
spc = site_sex_count.unstack()
s_plot = spc.plot(kind='bar', stacked=True, title="Total weight by site and sex")
s_plot.set_ylabel("Weight")
s_plot.set_xlabel("Site")


# In[ ]:




