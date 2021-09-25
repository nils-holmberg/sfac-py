#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210928-nlp/)
# 
# # day 2: getting started with nlp
# - overview day 2
# 
# |time  |section |concepts               |outcomes                               |
# |:-----|:-------|:----------------------|:--------------------------------------|
# |09-10 |2.1.1   |[spacy](01-intro.html) |install spacy package to anaconda venv |
# |      |2.1.2   |import text            |                                       |
# |      |2.1.3   |create document        |                                       |
# |      |break   |                       |                                       |
# |10-11 |2.2.1   |clean                  |                                       |
# |      |2.2.2   |tokenize               |                                       |
# |      |2.2.3   |ner                    |                                       |
# |      |break   |                       |                                       |
# |11-12 |2.3.1   |classify               |                                       |
# |      |2.3.2   |                       |                                       |
# |      |2.3.3   |                       |                                       |
# |12-13 |lunch   |                       |                                       |
# 
# 
# ## section 2.1.1
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




