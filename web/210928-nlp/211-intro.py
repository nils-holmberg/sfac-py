#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210928-nlp/)
# 
# # day 2: getting started with nlp
# - overview day 2
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
# # section 2.1.1
# - check, update anaconda installation, create nlp venv
# 
# ```python
# # update anaconda, env packages
# conda update anaconda
# conda update --all
# # install spacy nlp package
# conda install -c conda-forge -n base spacy
# # get trained pipline, language model, small and large
# python -m spacy download en_core_web_sm
# python -m spacy download en_core_web_lg
# # start jupyter notebook
# jupyter notebook
# ```
# 
# # section 2.1.2
# - repetition, python syntax
# - practice data structures, conditional statements, flow control
# 
# # section 2.1.3
# - extend python fuctionality with spacy nlp package
# - create our first basic nlp document

# In[1]:


import spacy
from spacy import displacy
# english language pre-trained model, small
nlp = spacy.load("en_core_web_sm")


# In[28]:


doc = nlp("my name is nils")
type(doc)


# In[29]:


doc
doc[0]


# In[30]:


for token in doc:
    print(token.text, token.pos_, token.dep_)


# In[31]:


displacy.render(doc, jupyter=True)


# ### How about other languages?

# In[32]:


doc = nlp("jag heter nils")
displacy.render(doc, jupyter=True)


# ### test swedish

# In[33]:


from spacy.lang.sv import Swedish
nlp = Swedish()  # use directly
#nlp = spacy.blank("sv")  # blank instance


# ### basic tokenization enabled
# - but not syntactic parsing

# In[34]:


doc = nlp("jag heter nils")
for token in doc:
    print(token.text, token.pos_, token.dep_)
#displacy.render(doc, jupyter=True)


# In[25]:


from spacy.lang.en import English
nlp = English()

doc = nlp("my name is nils")
for token in doc:
    print(token.text, token.pos_, token.dep_)

