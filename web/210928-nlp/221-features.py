#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210928-nlp/)
# 
# # day 2: getting started with nlp
# - overview day 2
# - section 2.2.1 python syntax
#     - [variables and data types](#variables)
# - section 2.2.2 functions
#     - [functions and modules](#functions)
# - section 2.2.3 files
#     - [files and directories](#files)
# 
# # section 2.2.1
# - some text
# 
# # section 2.2.2
# - some text
# 
# # section 2.2.3
# - some text

# In[4]:


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

# In[6]:


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

# In[7]:


for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)


# In[9]:


displacy.render(doc, style='dep', jupyter=True)


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

# In[10]:


for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


# In[11]:


text = """Apple decided to fire Tim Cook and hire somebody called John Doe as the new CEO.
They also discussed a merger with Google. On the long run it seems more likely that Apple
will merge with Amazon and Microsoft with Google. The companies will all relocate to
Austin in Texas before the end of the century. John Doe bought a Prosche."""

doc = nlp(text)
displacy.render(doc, style='ent', jupyter=True)


# ### Word vectors and similarity 
# 
# To learn more about word vectors, how to **customize them** and how to load
# **your own vectors** into spaCy, see the usage guide on
# [using word vectors and semantic similarities](/usage/linguistic-features#vectors-similarity).
# 

# In[1]:


#from textblob import TextBlob


# ## Word vectors and similarity

# To use vectors in spaCy, you might consider installing the larger models for the particular language. The common module and language packages only come with the small models. The larger models can be installed as described on the [spaCy vectors page](https://spacy.io/usage/vectors-similarity):
# 
#     python -m spacy download en_core_web_lg
# 
# The large model *en_core_web_lg* contains more than 1 million unique vectors.

# Let us restart all necessary modules again, in particular spaCy:

# In[2]:


import spacy


# We can now import the English NLP pipeline to process some word list. Since the small models in spacy only include context-sensitive tensors, we should use the dowloaded large model for better word vectors. We load the large model as follows:

# In[3]:


nlp = spacy.load('en_core_web_lg')
#nlp = spacy.load("en_core_web_sm")


# We can process a list of words by the pipeline using the *nlp* object:

# In[4]:


tokens = nlp(u'dog poodle beagle cat banana apple')


# As described in the spaCy chapter *[Word Vectors and Semantic Similarity](https://spacy.io/usage/vectors-similarity)*, the resulting elements of *Doc*, *Span*, and *Token* provide a method *similarity()*, which returns the similarities between words: 

# In[5]:


for token1 in tokens:
    for token2 in tokens:
        print(token1, token2, token1.similarity(token2))


# We can access the *vectors* of these objects using the *vector* attribute:

# In[6]:


tokens = nlp(u'dog cat banana grungle')

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)


# The attribute *has_vector* returns a boolean depending on whether the token has a vector in the model or not. The token *grungle* has no vector. It is also out-of-vocabulary (OOV), as the fourth column shows. Thus, it also has a norm of $0$, that is, it has a length of $0$.

# Here the token vector has a length of $300$. We can print out the vector for a token:

# In[7]:


n = 0
print(tokens[n].text, len(tokens[n].vector), tokens[n].vector)


# Here just another example of similarities for some famous words:

# In[8]:


tokens = nlp(u'queen king chef')

for token1 in tokens:
    for token2 in tokens:
        print(token1, token2, token1.similarity(token2))


# ### Similarities in Context

# In spaCy parsing, tagging and NER models make use of vector representations of contexts that represent the *meaning of words*. A text *meaning representation* is represented as an array of floats, i.e. a tensor, computed during the NLP pipeline processing. With this approach words that have not been seen before can be typed or classified. SpaCy uses a 4-layer convolutional network for the computation of these tensors. In this approach these tensors model a context of four words left and right of any given word.

# Let us use the example from the spaCy documentation and check the word *labrador*:

# In[9]:


tokens = nlp(u'labrador')

for token in tokens:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)


# We can now test for the context:

# In[10]:


doc1 = nlp(u"The labrador barked.")
doc2 = nlp(u"The labrador swam.")
doc3 = nlp(u"The people on Labrador are Canadians.")

dog = nlp(u"dog")

count = 0
for doc in [doc1, doc2, doc3]:
    lab = doc
    count += 1
    print(str(count) + ":", lab.similarity(dog))


# Using this strategy we can compute document or text similarities as well:

# In[11]:


docs = ( nlp(u"Paris is the largest city in France."),
        nlp(u"Vilnius is the capital of Lithuania."),
        nlp(u"An emu is a large bird.") )

for x in range(len(docs)):
    zset = set(range(len(docs)))
    zset.remove(x)
    for y in zset:
        print(x, y, docs[x].similarity(docs[y]))


# We can vary the word order in sentences and compare them:

# In[12]:


docs = [nlp(u"dog bites man"), nlp(u"man bites dog"),
        nlp(u"man dog bites"), nlp(u"cat eats mouse")]

for doc in docs:
    for other_doc in docs:
        print('"' + doc.text + '"', '"' + other_doc.text + '"', doc.similarity(other_doc))


# ### Custom Models

# In[ ]:




