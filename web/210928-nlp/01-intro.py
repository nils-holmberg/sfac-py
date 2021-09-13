#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210928/)
# 
# # day 2: getting started with nlp
# - overview day 2, table
# 
# ## section 1.1
# - check anaconda installation, create nlp venv
# - conda install spacy, english language models
# - start course jupyter notebook

# In[2]:


import numpy as np
import pandas as pd


# In[1]:


import spacy
#from spacy.lang.sv import Swedish
#nlp = Swedish()  # use directly
#nlp = spacy.blank("sv")  # blank instance


# In[3]:


doc = nlp("jag heter nils")


# In[4]:


doc


# In[5]:


type(doc)


# In[6]:


doc[0]


# In[7]:


t = doc[0]


# In[8]:


from spacy import displacy

displacy.render(doc)


# In[9]:


nlp = spacy.load("en_core_web_sm")


# In[10]:


doc = nlp("my name is nils")


# In[12]:


displacy.render(doc, jupyter=True)


# In[ ]:




