#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210928-nlp/)
# 
# # day 2: getting started with nlp
# - overview day 2
# - section 2.3.1 python syntax
#     - [variables and data types](#variables)
# - section 2.3.2 functions
#     - [functions and modules](#functions)
# - section 2.3.3 files
#     - [files and directories](#files)
# 
# # section 2.3.1
# - some text
# 
# # section 2.3.2
# - some text
# 
# # section 2.3.3
# - some text

# In[8]:


import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")


# #  NLP Tutorial 8 - Amazon and IMDB Review Sentiment Classification using SpaCy

# #### Watch Full Lesson here:  https://youtu.be/cd51nXNpiiU

# ## What is NLP 

# Natural Language Processing (NLP) is the field of Artificial Intelligence concerned with the processing and understanding of human language. Since its inception during the 1950s, machine understanding of language has played a pivotal role in translation, topic modeling, document indexing, information retrieval, and extraction.

# #### Application of NLP
# - Text Classification
# - Spam Filters
# - Voice text messaging
# - Sentiment analysis
# - Spell or grammar check
# - Chat bot
# - Search Suggestion
# - Search Autocorrect
# - Automatic Review Analysis system
# - Machine translation
# - And so much more

# In[ ]:


# !pip install scikit-learn


# In[ ]:


# !pip install -U spacy


# In[ ]:


# !python -m spacy download en


# In[ ]:


#!python -m spacy download en_core_web_sm


# ### Data Cleaning Options
# - Case Normalization
# - Removing Stop Words
# - Removing Punctuations or Special Symbols
# - Lemmatization or Stemming
# - Parts of Speech Tagging
# - Entity Detection
# - Bag of Words
# - TF-IDF 

# ### Bag of Words - The Simplest Word Embedding Technique

# This is one of the simplest methods of embedding words into numerical vectors. It is not often used in practice due to its oversimplification of language, but often the first embedding technique to be taught in the classroom setting.

# ```
# doc1 = "I am high"
# doc2 = "Yes I am high"
# doc3 = "I am kidding" 
# 
# ```

# ![image.png](attachment:image.png)

# ### Bag of Words and Tf-idf 
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html
# 
# tf–idf for “Term Frequency times Inverse Document Frequency

# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# # Let's Get Started

# In[1]:


import spacy
from spacy import displacy


# In[16]:


nlp = spacy.load('en_core_web_sm')


# In[17]:


text = "Apple, This is first sentence. and Google this is another one. here 3rd one is"


# In[18]:


doc = nlp(text)


# In[19]:


doc


# In[20]:


for token in doc:
    print(token)


# In[21]:


sent = nlp.create_pipe('sentencizer')


# In[22]:


nlp.add_pipe(sent, before='parser')


# In[23]:


doc = nlp(text)


# In[24]:


for sent in doc.sents:
    print(sent)


# In[25]:


from spacy.lang.en.stop_words import STOP_WORDS


# In[26]:


stopwords = list(STOP_WORDS)


# In[27]:


print(stopwords)


# In[28]:


len(stopwords)


# In[30]:


for token in doc:
    if token.is_stop == False:
        print(token)


# ### Lemmatization 

# In[31]:


doc = nlp('run runs running runner')


# In[32]:


for lem in doc:
    print(lem.text, lem.lemma_)


# ### POS 

# In[33]:


doc = nlp('All is well at your end!')


# In[34]:


for token in doc:
    print(token.text, token.pos_)


# In[35]:


displacy.render(doc, style = 'dep')


# ### Entity Detection 

# In[36]:


doc = nlp("New York City on Tuesday declared a public health emergency and ordered mandatory measles vaccinations amid an outbreak, becoming the latest national flash point over refusals to inoculate against dangerous diseases. At least 285 people have contracted measles in the city since September, mostly in Brooklyn’s Williamsburg neighborhood. The order covers four Zip codes there, Mayor Bill de Blasio (D) said Tuesday. The mandate orders all unvaccinated people in the area, including a concentration of Orthodox Jews, to receive inoculations, including for children as young as 6 months old. Anyone who resists could be fined up to $1,000.")


# In[37]:


doc


# In[38]:


displacy.render(doc, style = 'ent')


# ### Text Classification 

# In[3]:


import pandas as pd


# In[4]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# In[41]:


data_yelp = pd.read_csv('datasets/yelp_labelled.txt', sep='\t', header = None)


# In[42]:


data_yelp.head()


# In[43]:


columns_name = ['Review', 'Sentiment']
data_yelp.columns = columns_name


# In[44]:


data_yelp.head()


# In[45]:


data_yelp.shape


# In[49]:


data_amazon = pd.read_csv('datasets/amazon_cells_labelled.txt', sep = '\t', header = None)
data_amazon.columns = columns_name


# In[50]:


data_amazon.head()


# In[51]:


data_amazon.shape


# In[52]:


data_imdb = pd.read_csv('datasets/imdb_labelled.txt', sep = '\t', header = None)


# In[53]:


data_imdb.columns = columns_name


# In[54]:


data_imdb.shape


# In[55]:


data_imdb.head()


# In[56]:


data = data_yelp.append([data_amazon, data_imdb], ignore_index=True)


# In[57]:


data.shape


# In[58]:


data.head()


# In[59]:


data['Sentiment'].value_counts()


# In[60]:


data.isnull().sum()


# ### Tokenization 

# In[61]:


import string


# In[64]:


punct = string.punctuation


# In[65]:


punct


# In[68]:


def text_data_cleaning(sentence):
    doc = nlp(sentence)
    
    tokens = []
    for token in doc:
        if token.lemma_ != "-PRON-":
            temp = token.lemma_.lower().strip()
        else:
            temp = token.lower_
        tokens.append(temp)
    
    cleaned_tokens = []
    for token in tokens:
        if token not in stopwords and token not in punct:
            cleaned_tokens.append(token)
    return cleaned_tokens


# In[70]:


text_data_cleaning("    Hello how are you. Like this video")


# ### Vectorization Feature Engineering (TF-IDF) 

# In[71]:


from sklearn.svm import LinearSVC


# In[72]:


tfidf = TfidfVectorizer(tokenizer = text_data_cleaning)
classifier = LinearSVC()


# In[73]:


X = data['Review']
y = data['Sentiment']


# In[74]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)


# In[75]:


X_train.shape, X_test.shape


# In[77]:


clf = Pipeline([('tfidf', tfidf), ('clf', classifier)])


# In[78]:


clf.fit(X_train, y_train)


# In[79]:


y_pred = clf.predict(X_test)


# In[80]:


print(classification_report(y_test, y_pred))


# In[81]:


confusion_matrix(y_test, y_pred)


# In[85]:


clf.predict(['Wow, this is amzing lesson'])


# In[86]:


clf.predict(['Wow, this sucks'])


# In[87]:


clf.predict(['Worth of watching it. Please like it'])


# In[88]:


clf.predict(['Loved it. amazing'])


# In[ ]:




