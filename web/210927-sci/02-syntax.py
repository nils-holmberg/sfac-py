#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210927-sci/)
# 
# # day 1: getting started with python
# - overview of day 1
# 
# ## section: 1.2.1: python syntax
# - variables, flow control, con

# In[1]:


print("Hello Jupyter !")


# In Jupyter/Collaboratory, just typing the name of a variable in the cell prints its representation:

# In[2]:


message = "Hello again !"
message


# In[3]:


# A 'hash' symbol denotes a comment
# This is a comment. Anything after the 'hash' symbol on the line is ignored by the Python interpreter

print("No comment")  # comment


# ## Variables and data types
# ### Integers, floats, strings

# In[4]:


a = 5


# In[5]:


a


# In[6]:


type(a)


# Adding a decimal point creates a `float`

# In[7]:


b = 5.0


# In[8]:


b


# In[9]:


type(b)


# `int` and `float` are collectively called 'numeric' types
# 
# (There are also other numeric types like `hex` for hexidemical and `complex` for complex numbers)

# ## Challenge - Types
# 
# What is the **type** of the variable `letters` defined below ?
# 
# `letters = "ABACBS"`
# 
# * A) `int`
# * B) `str`
# * C) `float`
# * D) `text`
# 
# Write some code the outputs the type - paste your answer into the Etherpad.

# ## Solution
# 
# Option B - `str`.

# In[10]:


letters = "ABACBS"
type(letters)


# ### Strings

# In[11]:


some_words = "Python3 strings are Unicode (UTF-8) ❤❤❤ 😸 蛇"


# In[12]:


some_words


# In[13]:


type(some_words)


# The variable `some_words` is of type `str`, short for "string". Strings hold
# sequences of characters, which can be letters, numbers, punctuation
# or more exotic forms of text (even emoji!).

# ## Operators
# 
# We can perform mathematical calculations in Python using the basic operators:
# 
# `+`  `-`  `*`  `/`  `%`  `**`

# In[14]:


2 + 2  # Addition


# In[15]:


6 * 7  # Multiplication


# In[16]:


2 ** 16  # Power


# In[17]:


13 % 5  # Modulo


# In[18]:


# int + int = int
a = 5
a + 1


# In[19]:


# float + int = float
b = 5.0
b + 1


# In[20]:


a + b


# ```python
# some_words = "I'm a string"
# a = 6
# a + some_words
# ```
# 
# 

# Outputs:
# 
# ```
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-1-781eba7cf148> in <module>()
#       1 some_words = "I'm a string"
#       2 a = 6
# ----> 3 a + some_words
# 
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# ```

# In[21]:


str(a) + " " + some_words


# In[22]:


# Shorthand: operators with assignment
a += 1
a

# Equivalent to:
# a = a + 1


# ### Boolean operations
# 
# We can also use comparison and logic operators:
# `<, >, ==, !=, <=, >=` and statements of identity such as
# `and, or, not`. The data type returned by this is
# called a _boolean_.
# 

# In[23]:


3 > 4


# In[24]:


True and True


# In[25]:


True or False


# ## Lists and sequence types

# ### Lists

# In[26]:


numbers = [2, 4, 6, 8, 10]
numbers


# In[27]:


# `len` get the length of a list
len(numbers)


# In[28]:


# Lists can contain multiple data types, including other lists
mixed_list = ["asdf", 2, 3.142, numbers, ['a','b','c']]
mixed_list


# You can retrieve items from a list by their *index*. In Python, the first item has an index of 0 (zero).

# In[29]:


numbers[0]


# In[30]:


numbers[3]


# You can also assign a new value to any position in the list.

# In[31]:


numbers[3] = numbers[3] * 100
numbers


# You can append items to the end of the list.

# In[32]:


numbers.append(12)
numbers


# You can add multiple items to the end of a list with `extend`.

# In[33]:


numbers.extend([14, 16, 18])
numbers


# ### Loops
# 
# A for loop can be used to access the elements in a list or other Python data structure one at a time. We will learn about loops in other lesson.

# In[34]:


for num in numbers:
    print(num)


# **Indentation** is very important in Python. Note that the second line in the
# example above is indented, indicating the code that is the body of the loop.

# To find out what methods are available for an object, we can use the built-in `help` command:

# In[35]:


help(numbers)


# ### Tuples
# 
# A tuple is similar to a list in that it's an ordered sequence of elements.
# However, tuples can not be changed once created (they are "immutable"). Tuples
# are created by placing comma-separated values inside parentheses `()`.

# In[36]:


tuples_are_immutable = ("bar", 100, 200, "foo")
tuples_are_immutable


# In[37]:


tuples_are_immutable[1]


# ```python
# tuples_are_immutable[1] = 666
# ```

# Outputs:
# 
# ```
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-39-c91965b0815a> in <module>()
# ----> 1 tuples_are_immutable[1] = 666
# 
# TypeError: 'tuple' object does not support item assignment
# ```

# ### Dictionaries
# 
# Dictionaries are a container that store key-value pairs. They are unordered. 
# 
# Other programming languages might call this a 'hash', 'hashtable' or 'hashmap'.

# In[38]:


pairs = {'Apple': 1, 'Orange': 2, 'Pear': 4}
pairs


# In[39]:


pairs['Orange']


# In[40]:


pairs['Orange'] = 16
pairs


# The `items` method returns a sequence of the key-value pairs as tuples.
# 
# `values` returns a sequence of just the values.
# 
# `keys` returns a sequence of just the keys.
# 
# ---
# In Python 3, the `.items()`, `.values()` and `.keys()` methods return a ['dictionary view' object](https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects) that behaves like a list or tuple in for loops but doesn't support indexing. 'Dictionary views' stay in sync even when the dictionary changes.
# 
# You can turn them into a normal list or tuple with the `list()` or `tuple()` functions.

# In[41]:


pairs.items()
# list(pairs.items())


# In[42]:


pairs.values()
# list(pairs.values())


# In[43]:


pairs.keys()
# list(pairs.keys())


# In[44]:


len(pairs)


# In[45]:


dict_of_dicts = {'first': {1:2, 2: 4, 4: 8, 8: 16}, 'second': {'a': 2.2, 'b': 4.4}}
dict_of_dicts


# ## Challenge - Dictionaries
# 
# Given the dictionary:
# 
# ```python
# jam_ratings = {'Plum': 6, 'Apricot': 2, 'Strawberry': 8}
# ```
# 
# How would you change the value associated with the key `Apricot` to `9`.
# 
# A) `jam_ratings = {'apricot': 9}`
# 
# B) `jam_ratings[9] = 'Apricot'`
# 
# C) `jam_ratings['Apricot'] = 9`
# 
# D) `jam_ratings[2] = 'Apricot'`

# ## Solution - Dictionaries
# 
# The correct answer is **C**.
# 
# **A** assigns the name `jam_ratings` to a new dictionary with only the key `apricot` - not only are the other jam ratings now missing, but strings used as dictionary keys are *case sensitive* - `apricot` is not the same key as `Apricot`.
# 
# **B** mixes up the value and the key. Assigning to a dictionary uses the form: `dictionary[key] = value`.
# 
# **C** is correct. Bonus - another way to do this would be `jam_ratings.update({'Apricot': 9})` or even `jam_ratings.update(Apricot=9)`.
# 
# **D** mixes up the value and the key (and doesn't actually include the new value to be assigned, `9`, anywhere). `2` is the original *value*, `Apricot` is the key. Assigning to a dictionary uses the form: `dictionary[key] = value`.

# In[ ]:





# ## section: 1.2.2: functions
# - data structures, functions, pkgs
# 
# ## section: 1.2.3: files
# - navigate file system, working dir 
# 

# In[ ]:




