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

