#!/usr/bin/env python
# coding: utf-8

# # Seaborn | Part-1: Loading Datasets:

# When working with Seaborn, we can either use one of the [built-in datasets](https://github.com/mwaskom/seaborn-data) that Seaborn offers or we can load a Pandas DataFrame. Seaborn is part of the [PyData](https://pydata.org/) stack hence accepts Pandas’ data structures.
# 
# Let us begin by importing few built-in datasets but before that we shall import few other libraries as well that our Seaborn would depend upon:  

# In[1]:


# Importing intrinsic libraries:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Once we have imported the required libraries, now it is time to load built-in dataset. The dataset we would be dealing with in this illustration is [Iris Flower Dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set).

# In[2]:


# Loading built-in Datasets:
iris = sns.load_dataset("iris")


# Similarly we may load other dataset as well and for illustration sake, I shall code few of them down here (though won't be referencing to):

# In[3]:


# Refer to 'Dataset Source Reference' for list of all built-in Seaborn datasets.
tips = sns.load_dataset("tips")
exercise = sns.load_dataset("exercise")
titanic = sns.load_dataset("titanic")
flights = sns.load_dataset("flights")


# Let us take a sneak peek as to how this Iris dataset looks like and we shall be using Pandas to do so:

# In[4]:


iris.head(10)


# Iris dataset actually has 50 samples from each of three species of Iris flower (Setosa, Virginica and Versicolor). Four features were measured (in centimetres) from each sample: Length and Width of the Sepals and Petals. Let us try to have a summarized view of this dataset:

# In[5]:


iris.describe()


# `.describe()` is a very useful method in Pandas as it generates descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values. Without getting in-depth into analysis here, let us try to plot something simple from this dataset:

# In[6]:


sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')
# Later in the course I shall explain why above 2 lines of code have been added.

sns.swarmplot(x="species", y="petal_length", data=iris)


# This beautiful representation of data we see above is known as a `Swarm Plot` with minimal parameters. I shall be covering this in detail later on but for now I just wanted you to have a feel of serenity we're getting into. 
# 
# Let us now try to load a random dataset and the one I've picked for this illustration is [PoliceKillingsUS](https://github.com/washingtonpost/data-police-shootings) dataset. This dataset has been prepared by The Washington Post (they keep updating it on runtime) with every fatal shooting in the United States by a police officer in the line of duty since Jan. 1, 2015.

# In[10]:


# Loading Pandas DataFrame:
df = pd.read_csv("C:/Users/Alok/Downloads/PoliceKillingsUS.csv", encoding="windows-1252")


# Just the way we looked into Iris Data set, let us know have a preview of this dataset as well. We won't be getting into deep analysis of this dataset because our agenda is only to visualize the content within. So, let's do this: 

# In[11]:


df.head(10)


# This dataset is pretty self-descriptive and has limited number of features (may read as columns).
# 
# `race`:
# `W`: White, non-Hispanic
# `B`: Black, non-Hispanic
# `A`: Asian
# `N`: Native American
# `H`: Hispanic
# `O`: Other
# `None`: unknown
# 
# And, `gender` indicates:
# `M`: Male
# `F`: Female
# `None`: unknown
# The threat_level column include incidents where officers or others were shot at, threatened with a gun, attacked with other weapons or physical force, etc. The attack category is meant to flag the highest level of threat. The `other` and `undetermined` categories represent all remaining cases. `Other` includes many incidents where officers or others faced significant threats.
# 
# The `threat column` and the `fleeing column` are not necessarily related. Also, `attacks` represent a status immediately before fatal shots by police; while `fleeing` could begin slightly earlier and involve a chase. Latly, `body_camera` indicates if an officer was wearing a body camera and it may have recorded some portion of the incident.
# 
# Let us now look into the descriptive statistics:

# In[12]:


df.describe()


# These stats in particular do not really make much sense. Instead let us try to visualize age of people who were claimed to be armed as per this dataset.
# 
# Quick Note: Two special lines of code that we added earlier won't be required again. As promised, I shall reason that in upcoming lectures.

# In[13]:


sns.stripplot(x="armed", y="age", data=df)


# As you would have guessed by now, this plot is known as a Strip plot and pretty ideal for categorical values. Even this shall be dealt in length later on.
# 
# I hope these sample plots have intrigued you enough to dive deeper into statistical visual inference with Seaborn. And in next lecture, we shall learn to control aesthetics of our plot and few other important aspects.
