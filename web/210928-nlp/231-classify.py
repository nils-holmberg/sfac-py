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
# - section 2.1.1 python syntax
#     - [variables and data types](#variables)
# - section 2.1.2 functions
#     - [functions and modules](#functions)
# - section 2.1.3 files
#     - [files and directories](#files)
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
# # get trained pipline, language model
# python -m spacy download en_core_web_sm
# # start jupyter notebook
# jupyter notebook
# ```
# 
# # section 2.1.2
# - some text
# 
# # section 2.1.3
# - some text

# In[8]:


import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")


# ### spaCy Features 
# 
# In the documentation, you'll come across mentions of spaCy's features and
# capabilities. Some of them refer to linguistic concepts, while others are
# related to more general machine learning functionality.
# 
# | Name                                  | Description                                                                                                        |
# | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
# | **Tokenization**                      | Segmenting text into words, punctuations marks etc.                                                                |
# | **Part-of-speech** (POS) **Tagging**  | Assigning word types to tokens, like verb or noun.                                                                 |
# | **Dependency Parsing**                | Assigning syntactic dependency labels, describing the relations between individual tokens, like subject or object. |
# | **Lemmatization**                     | Assigning the base forms of words. For example, the lemma of "was" is "be", and the lemma of "rats" is "rat".      |
# | **Sentence Boundary Detection** (SBD) | Finding and segmenting individual sentences.                                                                       |
# | **Named Entity Recognition** (NER)    | Labelling named "real-world" objects, like persons, companies or locations.                                        |
# | **Entity Linking** (EL)               | Disambiguating textual entities to unique identifiers in a knowledge base.                                         |
# | **Similarity**                        | Comparing words, text spans and documents and how similar they are to each other.                                  |
# | **Text Classification**               | Assigning categories or labels to a whole document, or parts of a document.                                        |
# | **Rule-based Matching**               | Finding sequences of tokens based on their texts and linguistic annotations, similar to regular expressions.       |
# | **Training**                          | Updating and improving a statistical model's predictions.                                                          |
# | **Serialization**                     | Saving objects to files or byte strings.                                                                           |
# 
# ### Tokenization
# First, the raw text is split on whitespace characters, similar to
# `text.split(' ')`. Then, the tokenizer processes the text from left to right. On
# each substring, it performs two checks:
# 
# 1. **Does the substring match a tokenizer exception rule?** For example, "don't"
#    does not contain whitespace, but should be split into two tokens, "do" and
#    "n't", while "U.K." should always remain one token.
# 
# 2. **Can a prefix, suffix or infix be split off?** For example punctuation like
#    commas, periods, hyphens or quotes.
# 
# If there's a match, the rule is applied and the tokenizer continues its loop,
# starting with the newly split substrings. This way, spaCy can split **complex,
# nested tokens** like combinations of abbreviations and multiple punctuation
# marks.
# 
# |   0   |  1  |    2    |  3  |   4    |  5   |    6    |  7  |  8  |  9  |   10    |
# | :---: | :-: | :-----: | :-: | :----: | :--: | :-----: | :-: | :-: | :-: | :-----: |
# | Apple | is  | looking | at  | buying | U.K. | startup | for | \$  |  1  | billion |
# 

# In[4]:


doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
    print(token.text)


# ### Linguistic annotations
# 
# spaCy provides a variety of linguistic annotations to give you **insights into a
# text's grammatical structure**. This includes the word types, like the parts of
# speech, and how the words are related to each other. For example, if you're
# analyzing text, it makes a huge difference whether a noun is the subject of a
# sentence, or the object – or whether "google" is used as a verb, or refers to
# the website or company in a specific context.

# In[2]:


doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
    print(token.text, token.pos_, token.dep_)


# ### Part-of-speech tags and dependencies
# 
# After tokenization, spaCy can **parse** and **tag** a given `Doc`. This is where
# the trained pipeline and its statistical models come in, which enable spaCy to
# **make predictions** of which tag or label most likely applies in this context.
# A trained component includes binary data that is produced by showing a system
# enough examples for it to make predictions that generalize across the language –
# for example, a word following "the" in English is most likely a noun.
# 
# Linguistic annotations are available as
# [`Token` attributes](/api/token#attributes). Like many NLP libraries, spaCy
# **encodes all strings to hash values** to reduce memory usage and improve
# efficiency. So to get the readable string representation of an attribute, we
# need to add an underscore `_` to its name:
# 
# To learn more about **part-of-speech tagging** and rule-based morphology, and
# how to **navigate and use the parse tree** effectively, see the usage guides on
# [part-of-speech tagging](/usage/linguistic-features#pos-tagging) and
# [using the dependency parse](/usage/linguistic-features#dependency-parse).
# 
# > - **Text:** The original word text.
# > - **Lemma:** The base form of the word.
# > - **POS:** The simple [UPOS](https://universaldependencies.org/docs/u/pos/)
# >   part-of-speech tag.
# > - **Tag:** The detailed part-of-speech tag.
# > - **Dep:** Syntactic dependency, i.e. the relation between tokens.
# > - **Shape:** The word shape – capitalization, punctuation, digits.
# > - **is alpha:** Is the token an alpha character?
# > - **is stop:** Is the token part of a stop list, i.e. the most common words of
# >   the language?
# 
# | Text    | Lemma   | POS     | Tag   | Dep        | Shape   | alpha   | stop    |
# | ------- | ------- | ------- | ----- | ---------- | ------- | ------- | ------- |
# | Apple   | apple   | `PROPN` | `NNP` | `nsubj`    | `Xxxxx` | `True`  | `False` |
# | is      | be      | `AUX`   | `VBZ` | `aux`      | `xx`    | `True`  | `True`  |
# | looking | look    | `VERB`  | `VBG` | `ROOT`     | `xxxx`  | `True`  | `False` |
# | at      | at      | `ADP`   | `IN`  | `prep`     | `xx`    | `True`  | `True`  |
# | buying  | buy     | `VERB`  | `VBG` | `pcomp`    | `xxxx`  | `True`  | `False` |
# | U.K.    | u.k.    | `PROPN` | `NNP` | `compound` | `X.X.`  | `False` | `False` |
# | startup | startup | `NOUN`  | `NN`  | `dobj`     | `xxxx`  | `True`  | `False` |
# | for     | for     | `ADP`   | `IN`  | `prep`     | `xxx`   | `True`  | `True`  |
# | \$      | \$      | `SYM`   | `$`   | `quantmod` | `$`     | `False` | `False` |
# | 1       | 1       | `NUM`   | `CD`  | `compound` | `d`     | `False` | `False` |
# | billion | billion | `NUM`   | `CD`  | `pobj`     | `xxxx`  | `True`  | `False` |
# 

# In[5]:


for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)


# In[10]:


displacy.render(doc, jupyter=True)


# ### Named Entities 
# 
# To learn more about entity recognition in spaCy, how to **add your own
# entities** to a document and how to **train and update** the entity predictions
# of a model, see the usage guides on
# [named entity recognition](/usage/linguistic-features#named-entities) and
# [training pipelines](/usage/training).
# 
# A named entity is a "real-world object" that's assigned a name – for example, a
# person, a country, a product or a book title. spaCy can **recognize various
# types of named entities in a document, by asking the model for a
# prediction**. Because models are statistical and strongly depend on the
# examples they were trained on, this doesn't always work _perfectly_ and might
# need some tuning later, depending on your use case.
# 
# Named entities are available as the `ents` property of a `Doc`:
# 
# > - **Text:** The original entity text.
# > - **Start:** Index of start of entity in the `Doc`.
# > - **End:** Index of end of entity in the `Doc`.
# > - **Label:** Entity label, i.e. type.
# 
# | Text        | Start | End | Label   | Description                                          |
# | ----------- | :---: | :-: | ------- | ---------------------------------------------------- |
# | Apple       |   0   |  5  | `ORG`   | Companies, agencies, institutions.                   |
# | U.K.        |  27   | 31  | `GPE`   | Geopolitical entity, i.e. countries, cities, states. |
# | \$1 billion |  44   | 54  | `MONEY` | Monetary values, including unit.                     |
# 
# Using spaCy's built-in [displaCy visualizer](/usage/visualizers), here's what
# our example sentence and its named entities look like:

# In[6]:


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


# ### Word vectors and similarity 
# 
# To learn more about word vectors, how to **customize them** and how to load
# **your own vectors** into spaCy, see the usage guide on
# [using word vectors and semantic similarities](/usage/linguistic-features#vectors-similarity).
# 

# In[ ]:




