#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210929/)
# 
# # natural language processing with spacy (210929)
# some line
# 
# ## exercise 1
# some line
# 

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


import spacy
from spacy.lang.sv import Swedish
nlp = Swedish()  # use directly
nlp = spacy.blank("sv")  # blank instance


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


# In[11]:


displacy.render(doc)


# In[ ]:




