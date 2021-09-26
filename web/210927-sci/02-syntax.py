#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210927-sci/)
# 
# # day 1: getting started with python
# - overview of day 1
# 
# # section: 1.2.1: python syntax
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

# ## Automation with Loops

# ## Instructor notes
# 
# *Estimated teaching time:* 30 min
# 
# *Estimated challenge time:* 0 min
# 
# *Key questions:*
# 
#   - "How can I do the same operations on many different values?""
#     
# *Learning objectives:*
# 
#   - "Explain what a `for` loop does."
#   - "Correctly write `for` loops to repeat simple calculations."
#   - "Trace changes to a loop variable as the loop runs."
#   - "Trace changes to other variables as they are updated by a `for` loop."
# 
# *Key points:*
# 
#   - "Use `for variable in sequence` to process the elements of a sequence one at a time."
#   - "The body of a `for` loop must be indented."
#   - "Use `len(thing)` to determine the length of something that contains other values."
# 
# ---

# An example task that we might want to repeat is printing each character in a
# word on a line of its own.

# In[17]:


word = 'lead'


# We can access a character in a string using its index. For example, we can get the first
# character of the word `'lead'`, by using `word[0]`. One way to print each character is to use
# four `print` statements:

# In[18]:


print(word[0])
print(word[1])
print(word[2])
print(word[3])


# While this works, it's a bad approach for two reasons:
# 
# 1. It doesn't scale:
#    if we want to print the characters in a string that's hundreds of letters long,
#    we'd be better off just typing them in.
# 
# 2. It's fragile:
#    if we give it a longer string,
#    it only prints part of the data,
#    and if we give it a shorter one,
#    it produces an error because we're asking for characters that don't exist.
# 
# 

# Running:
# 
# ```python
# word = 'tin'
# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# ```

# Gives the error:
# 
# ```
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-4-e59d5eac5430> in <module>()
#       3 print(word[1])
#       4 print(word[2])
# ----> 5 print(word[3])
# 
# IndexError: string index out of range
# ```

# 
# 
# Here's a better approach:
# 
# 

# In[19]:


word = 'lead'
for char in word:
    print(char)


# This is shorter --- certainly shorter than something that prints every character in a hundred-letter string --- and
# more robust as well:

# In[20]:


word = 'oxygen'
for char in word:
    print(char)


# The improved version uses a **for loop** to repeat an operation --- in this case, printing --- once for each thing in a sequence.
# The general form of a loop is:
# 
# ```python
# for variable in collection:
#     # do things with variable
# ```

# 
# Using the oxygen example above, the loop might look like this:
# 
# ![loop_image](images/loops_image.png)
# 
# where each character (`char`) in the variable `word` is looped through and printed one character after another.
# The numbers in the diagram denote which loop cycle the character was printed in (1 being the first loop, and 6 being the final loop).
# 
# We can call the **loop variable** anything we like,
# but there must be a colon at the end of the line starting the loop, and we must indent anything we want to run inside the loop. Unlike many other languages, there is no command to signify the end of the loop body (e.g. `end for`); what is indented after the `for` statement belongs to the loop.
# 
# 
# 

# ## What's in a name?
# 
# 
# In the example above, the loop variable was given the name `char` as a mnemonic; it is short for 'character'. 
# We can choose any name we want for variables. We might just as easily have chosen the name `banana` for the loop variable, as long as we use the same name when we invoke the variable inside the loop:
# 
# 

# In[21]:


word = 'oxygen'
for banana in word:
    print(banana)


# It is a good idea to choose variable names that are meaningful, otherwise it would be more difficult to understand what the loop is doing.
# 
# 
# Here's another loop that repeatedly updates a variable:

# In[22]:


length = 0
for vowel in 'aeiou':
    length = length + 1
print('There are', length, 'vowels')


# It's worth tracing the execution of this little program step by step.
# 
# Since there are five characters in `'aeiou'`,
# the statement on line 3 will be executed five times.
# 
# The first time around,
# `length` is zero (the value assigned to it on line 1)
# and `vowel` is `'a'`.
# The statement adds 1 to the old value of `length`,
# producing 1,
# and updates `length` to refer to that new value.
# 
# The next time around,
# `vowel` is `'e'` and `length` is 1,
# so `length` is updated to be 2.
# 
# After three more updates,
# `length` is 5;
# since there is nothing left in `'aeiou'` for Python to process,
# the loop finishes
# and the `print` statement on line 4 tells us our final answer.
# 
# Note that a loop variable `vowel` is just a variable that's being used to record progress in a loop.

# ## Challenge - scope of the loop variable
# 
# 1. In the loop over `"aeiou"` above, does the loop variable `vowel` exist after the loop has finished ?
# 

# In[23]:


length = 0
for vowel in 'aeiou':
    length = length + 1
print('After the loop, `vowel` exists and has the value: ' + vowel)

# The loop variable `vowel` exists after the loop is completed, not only inside the loop


# Note also that finding the length of a string is such a common operation that Python actually has a built-in function to do it called `len`:

# In[24]:


print(len('aeiou'))


# `len` is much faster than any function we could write ourselves,
# and much easier to read than a two-line loop;
# it will also give us the length of many other things that we haven't met yet,
# so we should always use it when we can.

# ## From 1 to N
# 
# Python has a built-in function called `range` that creates a sequence of numbers. `range` can
# accept 1, 2, or 3 parameters.
# 
# * If one parameter is given, `range` creates an array of that length,
#   starting at zero and incrementing by 1.
#   For example, `range(3)` produces the numbers `0, 1, 2`.
# * If two parameters are given, `range` starts at
#   the first and ends just before the second, incrementing by one.
#   For example, `range(2, 5)` produces `2, 3, 4`.
# * If `range` is given 3 parameters,
#   it starts at the first one, ends just before the second one, and increments by the third one.
#   For exmaple `range(3, 10, 2)` produces `3, 5, 7, 9`.
# 
# 

# ## Challenge - loop over a range
# Using `range`,
# write a loop that uses `range` to print the first 3 natural numbers:
# 
# ```
# 1
# 2
# 3
# ```
# 
# 
# 

# ## Solution

# In[25]:


for i in range(1, 4):
   print(i)


# ## Computing Powers With Loops
# 
# Exponentiation is built into Python:

# In[26]:


print(5 ** 3)


# ## Challenge - multiplication in a loop
# 
# Write a loop that calculates the same result as `5 ** 3` using
# multiplication (and without exponentiation).

# ## Solution

# In[27]:


result = 1
for i in range(0, 3):
   result = result * 5
print(result)


# ## Bonus challenge: reverse a string
# 
# Knowing that two strings can be concatenated using the `+` operator,
# write a loop that takes a string
# and produces a new string with the characters in reverse order,
# so `'Newton'` becomes `'notweN'`.

# ## Solution

# In[28]:


newstring = ''
oldstring = 'Newton'
for char in oldstring:
   newstring = char + newstring
print(newstring)


# ## Enumerate
# 
# The built-in function `enumerate` takes a sequence (e.g. a list) and generates a
# new sequence of the same length. Each element of the new sequence is a pair composed of the index
# (0, 1, 2,...) and the value from the original sequence:
# 
# ```
# for i, x in enumerate(xs):
#     # Do something with i and x
# ```
# 
# 
# The code above loops through `xs`, assigning the index to `i` and the value to `x`.

# ## Bonus challenge: enumeration for computing the value of a polynomial
# 
# Suppose you have encoded a polynomial as a list of coefficients in
# the following way: the first element is the constant term, the
# second element is the coefficient of the linear term, the third is the
# coefficient of the quadratic term, etc.
# 
# ```
# x = 5
# cc = [2, 4, 3]
# ```
# 
# 
# ```
# y = cc[0] * x**0 + cc[1] * x**1 + cc[2] * x**2
# y = 97
# ```
# 
# 
# Write a loop using `enumerate(cc)` which computes the value `y` of any
# polynomial, given `x` and `cc`.

# ## Solution

# In[29]:


x = 5
cc = [2, 4, 3]
y = cc[0] * x**0 + cc[1] * x**1 + cc[2] * x**2

y = 0
for i, c in enumerate(cc):
    y = y + x**i * c
    
print(y)


# In[ ]:





# # section: 1.2.2: functions
# - data structures, functions, pkgs

# ## Instructor notes
# 
# *Estimated teaching time:* 30 min
# 
# *Estimated challenge time:* 0 min
# 
# *Key questions:*
# 
# 
#     
# *Learning objectives:*
# 
#   - "Build reusable code in Python."
#   - "Write functions using conditional statements (if, then, else)"
# 
# ---

# ## Functions
# 
# Functions wrap up reusable pieces of code - they help you apply the _Do Not Repeat Yourself_ (DRY) principle.

# In[1]:


def square(x):
    # The body of the function is indicated by indenting by 4 spaces.
    return x**2

square(4)


# In[2]:


def hyphenate(a, b):
    # return statements immediately return a value (or None if no value is given)
    return a + '-' + b
    # Any code in the function after the return statement does not get executed.
    print("We will never get here")

hyphenate('python', 'esque')


# Suppose that separating large data files into individual yearly files is a task that we frequently have to perform. We could write a `for` loop like the one above every time we needed to do it but that would be time consuming and error prone. A more elegant solution would be to create a reusable tool that performs this task with minimum input from the user. To do this, we are going to turn the code we’ve already written into a function.
# 
# Functions are reusable, self-contained pieces of code that are called with a single command. They can be designed to accept arguments as input and return values, but they don’t need to do either. Variables declared inside functions only exist while the function is running and if a variable within the function (a local variable) has the same name as a variable somewhere else in the code, the local variable hides but doesn’t overwrite the other.
# 
# Every method used in Python (for example, `print`) is a function, and the libraries we import (say, `pandas`) are a collection of functions. We will only use functions that are housed within the same code that uses them, but it’s also easy to write functions that can be used by different programs.

# Functions are declared following this general structure:

# ```python
# def this_is_the_function_name(input_argument1, input_argument2):
# 
#     # The body of the function is indented
#     # This function prints the two arguments to screen
#     print('The function arguments are:', input_argument1, input_argument2, '(this is done inside the function!)')
# 
#     # And returns their product
#     return input_argument1 * input_argument2
# ```
# 
# The function declaration starts with the word `def`, followed by the function name and any arguments in parenthesis, and ends in a colon. The body of the function is indented just like loops are. If the function returns something when it is called, it includes a return statement at the end.
# 
# 
# Let's rewrite this function with shorter (but still informative) names so we don't need to type as much:

# In[3]:


def product(a, b):
    print('The function arguments are:', a, b, '(this is done inside the function!)')

    return a * b


# This is how we call the function:

# In[4]:


product_of_inputs = product(2, 5)


# In[5]:


print('Their product is:', product_of_inputs, '(this is done outside the function!)')


# ## Challenge - Functions
# 
# 1. Change the values of the input arguments in the function and check its output.
# 
# 2. Try calling the function by giving it the wrong number of arguments (not 2) or not assigning the function call to a variable (no `product_of_inputs =`).
# 
# ### Bonus challenges
# 
# 3. Declare a variable inside the function and test to see where it exists (Hint: can you print it from outside the function?).
# 
# 4. Explore what happens when a variable both inside and outside the function have the same name. What happens to the global variable when you change the value of the local variable?

# ## Solutions - Functions

# In[6]:


# Challenge part 1
product_of_inputs = product(2, 6)
print(product_of_inputs)


# Challenge part 2:
# 
# ```python
# product(2, 6, "nope")
# ```

# ```python
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-12-fe9d9cd35fe2> in <module>()
#       1 # 2
# ----> 2 this_is_the_function_name(2, 6, "nope")
# 
# TypeError: this_is_the_function_name() takes 2 positional arguments but 3 were given
# ```

# Challenge part 3:
# 
# ```python
# def product(a, b):
#     
#     inside_fun = "existential crisis"
#     print('The function arguments are:', a, b, '(this is done inside the function!)')
#     
#     return a * b
# 
# product(2, 5)
# print(inside_fun)
# ```

# ```python
# The function arguments are: 2 5 (this is done inside the function!)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-13-e7a0563b00a6> in <module>()
#      12 
#      13 this_is_the_function_name(2, 5)
# ---> 14 print(inside_fun)
# 
# NameError: name 'inside_fun' is not defined
# ```

# In[7]:


# Challenge part 4
outside = "unchanged"
def product(a, b):
    
    outside = "I'm being manipulated"
    print('The function arguments are:', a, b, '(this is done inside the function!)')

    return a * b

product(2, 5)
print(outside)


# Say we had some code for taking our `survey.csv` data and splitting it out into one file for each year:
# 
# ```python
# # First let's make sure we've read the survey data into a pandas DataFrame.
# import pandas as pd
# all_data = pd.read_csv("surveys.csv")
# 
# this_year = 2002
# # Select data for just that year
# surveys_year = all_data[all_data.year == this_year]
# 
# # Write the new DataFrame to a csv file
# filename = 'surveys' + str(this_year) + '.csv'
# surveys_year.to_csv(filename)
# ```
# 
# There are many different "chunks" of this code that we can turn into functions, and we can even create functions that call other functions inside them. Let’s first write a function that separates data for just one year and saves that data to a file:

# In[8]:


def year_to_csv(year, all_data):
    """
    Writes a csv file for data from a given year.

    year --- year for which data is extracted
    all_data --- DataFrame with multi-year data
    """

    # Select data for the year
    surveys_year = all_data[all_data.year == year]

    # Write the new DataFrame to a csv file
    filename = 'function_surveys' + str(year) + '.csv'
    surveys_year.to_csv(filename)


# The text between the two sets of triple double quotes is called a _docstring_ and contains the documentation for the function. It does nothing when the function is running and is therefore not necessary, but it is good practice to include docstrings as a reminder of what the code does. Docstrings in functions also become part of their ‘official’ documentation:

# In[9]:


get_ipython().run_line_magic('pinfo', 'year_to_csv')


# **Signature:** `year_to_csv(year, all_data)`
# 
# ***Docstring:***
# ```
# Writes a csv file for data from a given year.
# 
# year --- year for which data is extracted
# all_data --- DataFrame with multi-year data
# ```
# 
# ***File:***      `~/devel/python-workshop-base/workshops/docs/modules/notebooks/<ipython-input-16-978149c5937c>`
# 
# ***Type:***      `function`

# In[10]:


# Read the survey data into a pandas DataFrame.
# (if you are jumping in to just this lesson and don't yet have the surveys.csv file yet, 
#  see the "Data analysis in Python with Pandas" `working_with_data` module)
import pandas as pd
surveys_df = pd.read_csv("surveys.csv")

year_to_csv(2002, surveys_df)


# ### Aside - listing files and the `os` module
# 
# Google Collaboratory and Juypter Notebooks have a built-in file browser, however, you can list the files and directories in the current directory ("folder") with Python code like:
# 
# ```python
# import os
# 
# print(os.listdir())
# ```
# 
# You'll see a Python list, a bit like:
# 
# ```
# ['surveys.csv','function_surveys2002.csv']
# ```
# 
# (you may have additional files listed here, generated in previous lessons)
# 
# The [os](https://docs.python.org/3/library/os.html) module contains, among other things, a bunch of useful functions for working with the filesystem and file paths.
# 
# Two other useful examples (hint - these might help in a upcoming challenge):
# 
# ```python
# # This returns True if the file or directory specified exists
# os.path.exists('surveys.csv')
# ```
# 
# ```python
# # This creates empty (nested) directories based on a path (eg in a 'path' each directory is separated by slashes)
# os.makedirs('data/csvs/')
# ```
# 
# If a directory already exists, `os.makedirs` fails and produces an error message (in Python terminology we might say it 'raises an exception' ).
# 
# We can avoid this by using `os.path.exists` and `os.makedirs` together like:
# ```python
# if not os.path.exists('data/csvs/'):
#     os.makedirs('data/csvs/')
# ```

# What we really want to do, though, is create files for multiple years without having to request them one by one. Let’s write another function that uses a `for` loop over a sequence of years and repeatedly calls the function we just wrote, `year_to_csv`:

# In[11]:


def create_csvs_by_year(start_year, end_year, all_data):
    """
    Writes separate CSV files for each year of data.

    start_year --- the first year of data we want
    end_year --- the last year of data we want
    all_data --- DataFrame with multi-year data
    """

    # "end_year" is the last year of data we want to pull, so we loop to end_year+1
    for year in range(start_year, end_year+1):
        year_to_csv(year, all_data)


# Because people will naturally expect that the end year for the files is the last year with data, the `for` loop inside the function ends at `end_year + 1`. By writing the entire loop into a function, we’ve made a reusable tool for whenever we need to break a large data file into yearly files. Because we can specify the first and last year for which we want files, we can even use this function to create files for a subset of the years available. This is how we call this function:

# In[12]:


# Create CSV files, one for each year in the given range
create_csvs_by_year(1977, 2002, surveys_df)


# ## Challenge - More Functions
# 
# 1. How could you use the function `create_csvs_by_year` to create a CSV file for only one year ? (Hint: think about the syntax for range)
# 
# 2. Modify `year_to_csv` so that it has two additional arguments, `output_path` (the path of the directory where the files will be written) and `filename_prefix` (a prefix to be added to the start of the file name). Name your new function `year_to_csv_at_path`. Eg, `def year_to_csv_at_path(year, all_data, output_path, filename_prefix):`. Call your new function to create a new file with a different name in a different directory. ... **Hint:** You could manually create the target directory before calling the function using the Collaboratory / Jupyter file browser, *or* for bonus points you could do it in Python inside the function using the `os` module.
# 
# 3. Create a new version of the `create_csvs_by_year` function called `create_csvs_by_year_at_path` that also takes the additional arguments `output_path` and `filename_prefix`. Internally `create_csvs_by_year_at_path` should pass these values to `year_to_csv_at_path`. Call your new function to create a new set of files with a different name in a different directory.
# 
# 4. Make these new functions return a list of the files they have written. There are many ways you can do this (and you should try them all!): you could make the function print the filenames to screen, or you could use a `return` statement to make the function produce a list of filenames, or you can use some combination of the two. You could also try using the `os` library to list the contents of directories.

# ## Solutions - More Functions

# In[13]:


# Solution - part 1
create_csvs_by_year(2002, 2002, surveys_df)


# In[14]:


# Solution - part 2 and 3
import os

def year_to_csv_at_path(year, all_data, output_path, filename_prefix):
    """
    Writes a csv file for data from a given year.

    year --- year for which data is extracted
    all_data --- DataFrame with multi-year data
    output_path --- The output path for the generated file
    filename_prefix --- Output filename will be of the form "{filename_prefix}{year}.csv"
    """

    # Select data for the year
    surveys_year = all_data[all_data.year == year]

    # Create directories if required
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Write the new DataFrame to a csv file
    filename = output_path + '/' + filename_prefix + str(year) + '.csv'
    surveys_year.to_csv(filename)

def create_csvs_by_year_at_path(start_year, end_year, all_data, output_path, filename_prefix):
    """
    Writes separate CSV files for each year of data.

    start_year --- the first year of data we want
    end_year --- the last year of data we want
    all_data --- DataFrame with multi-year data
    output_path --- The output path for the generated file
    filename_prefix --- Output filename will be of the form "{filename_prefix}{year}.csv"
    """

    # "end_year" is the last year of data we want to pull, so we loop to end_year+1
    for year in range(start_year, end_year+1):
        year_to_csv_at_path(year, all_data, output_path, filename_prefix)


# In[15]:


# Solution - part 4

def year_to_csv_return_filenames(year, all_data):
    # Select data for the year
    surveys_year = all_data[all_data.year == year]

    # Write the new DataFrame to a csv file
    filename = 'function_surveys' + str(year) + '.csv'
    surveys_year.to_csv(filename)
    
    # We could just print the filename. We can see the result, but won't capture the value
    # print(filename)
    
    # It's often more useful to return data rather than print it, so we can do something with it
    return filename

def create_csvs_by_year_return_filenames(start_year, end_year, all_data):
    
    generated_files = []
    for year in range(start_year, end_year+1):
        fn = year_to_csv_return_filenames(year, all_data)
        generated_files.append(fn)
        
    return generated_files

print(create_csvs_by_year_return_filenames(2000, 2002, surveys_df))


# The functions we wrote demand that we give them a value for every argument. Ideally, we would like these functions to be as flexible and independent as possible. Let’s modify the function `create_csvs_by_year` so that the `start_year` and `end_year` default to the full range of the data if they are not supplied by the user. 
# 
# Arguments can be given default values with an equal sign in the function declaration - we call these **'keyword'** arguments. Any argument in the function without a default value (here, `all_data`) is a required argument - we call these **'positional'** arguments. Positional arguements MUST come before any keyword arguments. Keyword arguments are optional - if you don't include them when calling the function, the default value is used.

# In[16]:


def keyword_arg_test(all_data, start_year = 1977, end_year = 2002):
    """
    A simple function to demonstrate the use of keyword arguments with defaults !

    start_year --- the first year of data we want --- default: 1977
    end_year --- the last year of data we want --- default: 2002
    all_data --- DataFrame with multi-year data - not actually used
    """

    return start_year, end_year


start,end = keyword_arg_test(surveys_df, 1988, 1993)
print('Both optional arguments:\t', start, end)

start,end = keyword_arg_test(surveys_df)
print('Default values:\t\t\t', start, end)


# The `\t` in the print statements are tabs, used to make the text align and be easier to read.
# 
# What if our dataset doesn’t start in 1977 and end in 2002? We can modify the function so that it looks for the ealiest and latest years in the dataset if those dates are not provided. Let's redefine `csvs_by_year`:

# In[17]:


def csvs_by_year(all_data, start_year = None, end_year = None):
    """
    Writes separate CSV files for each year of data. The start year and end year can 
    be optionally provided, otherwise the earliest and latest year in the dataset are
    used as the range.

    start_year --- the first year of data we want --- default: None - check all_data
    end_year --- the last year of data we want --- default: None - check all_data
    all_data --- DataFrame with multi-year data
    """

    if start_year is None:
        start_year = min(all_data.year)
    if end_year is None:
        end_year = max(all_data.year)

    return start_year, end_year


start,end = csvs_by_year(surveys_df, 1988, 1993)
print('Both optional arguments:\t', start, end)

start,end = csvs_by_year(surveys_df)
print('Default values:\t\t\t', start, end)


# The default values of the `start_year` and `end_year` arguments in this new version of the `csvs_by_year` function are now `None`. This is a built-in constant in Python that indicates the absence of a value - essentially, that the variable exists in the namespace of the function (the directory of variable names) but that it doesn’t correspond to any existing object.

# ## Challenge - Experimenting with keyword arguments
# 
# 1. What type of object corresponds to a variable declared as `None` ? (Hint: create a variable set to None and use the function `type()`)
# 
# 2. Compare the behavior of the function `csvs_by_year` when the keyword arguments have `None` as a default vs. calling the function by supplying (non-default) values to the keyword arguments
# 
# 3. What happens if you only include a value for `start_year` in the function call? Can you write the function call with only a value for `end_year` ? (Hint: think about how the function must be assigning values to each of the arguments - this is related to the need to put the arguments without default values before those with default values in the function definition!)

# ## Solutions - Experimenting with keyword arguments

# In[18]:


# Challenge 1
the_void = None
type(the_void)


# In[19]:


# Challenge 2
print(csvs_by_year(surveys_df))
print(csvs_by_year(surveys_df, start_year=1999, end_year=2001))


# In[20]:


# Challenge 3
print(csvs_by_year(surveys_df, start_year=1999))

# Keyword args are taken in order if there is no keyword used
# Doing this is a bit dangerous (what if you later decide to add more keyword args to the function ?)
print(csvs_by_year(surveys_df, 1999))
print(csvs_by_year(surveys_df, 1999, end_year=2001))

# But keyword args must always come last - this throws an error
# print(csvs_by_year(surveys_df, start_year=1999, 2001))

# We don't need to specify all keyword args, nor do they need to be in order
print(csvs_by_year(surveys_df, end_year=1999))
print(csvs_by_year(surveys_df, end_year=2001, start_year=1999))


# ## Conditionals - `if` statements

# The body of the test function now has two conditionals (`if` statements) that check the values of `start_year` and `end_year`. `if` statements execute a segment of code when some condition is met. They commonly look something like this:

# In[21]:


a = 5

if a < 0:  # Meets first condition?

    # if a IS less than zero
    print('a is a negative number')

elif a > 0:  # Did not meet first condition. meets second condition?

    # if a ISN'T less than zero and IS more than zero
    print('a is a positive number')

else:  # Met neither condition

    # if a ISN'T less than zero and ISN'T more than zero
    print('a must be zero!')


# Change the value of `a` to see how this function works. The statement `elif` means “else if”, and all of the conditional statements must end in a colon.
# 
# The `if` statements in the function `csvs_by_year` check whether there is an object associated with the variable names `start_year` and `end_year`. If those variables are `None`, the `if` statements return the boolean `True` and execute whatever is in their body. On the other hand, if the variable names are associated with some value (they got a number in the function call), the `if` statements return `False` and do not execute. The opposite conditional statements, which would return `True` if the variables were associated with objects (if they had received value in the function call), would be `if start_year` and `if end_year`.
# 
# As we’ve written it so far, the function `csvs_by_year` associates values in the function call with arguments in the function definition just based in their order. If the function gets only two values in the function call, the first one will be associated with `all_data` and the second with `start_year`, regardless of what we intended them to be. We can get around this problem by calling the function using keyword arguments, where each of the arguments in the function definition is associated with a keyword and the function call passes values to the function using these keywords:

# In[22]:


start,end = csvs_by_year(surveys_df)
print('Default values:\t\t\t', start, end)

start,end = csvs_by_year(surveys_df, 1988, 1993)
print('No keywords:\t\t\t', start, end)

start,end = csvs_by_year(surveys_df, start_year = 1988, end_year = 1993)
print('Both keywords, in order:\t', start, end)

start,end = csvs_by_year(surveys_df, end_year = 1993, start_year = 1988)
print('Both keywords, flipped:\t\t', start, end)

start,end = csvs_by_year(surveys_df, start_year = 1988)
print('One keyword, default end:\t', start, end)

start,end = csvs_by_year(surveys_df, end_year = 1993)
print('One keyword, default start:\t', start, end)


# ## Multiple choice challenge
# 
# What output would you expect from the `if` statement (try to figure out the answer without running the code):
# 
# ```python
# pod_bay_doors_open = False
# dave_want_doors_open = False
# hal_insanity_level = 2001
# 
# if not pod_bay_doors_open:
#     print("Dave: Open the pod bay doors please HAL.")
#     dave_wants_doors_open = True
# elif pod_bay_doors_open and hal_insanity_level >= 95:
#     print("HAL: I'm closing the pod bay doors, Dave.")
#     
# if dave_wants_doors_open and not pod_bay_doors_open and hal_insanity_level >= 95:
#     print("HAL: I’m sorry, Dave. I’m afraid I can’t do that.")
# elif dave_wants_doors_open and not pod_bay_doors_open:
#     print("HAL: I'm opening the pod bay doors, welcome back Dave.")
# else:
#     print("... silence of space ...")
# ```
# 
# **a)** "HAL: I'm closing the pod bay doors, Dave.", "... silence of space ..."
# 
# **b)** "Dave: Open the pod bay doors please HAL.", "HAL: I’m sorry, Dave. I’m afraid I can’t do that."
# 
# **c)** "... silence of space ..."
# 
# **d)** "Dave: Open the pod bay doors please HAL.", HAL: "I'm opening the pod bay doors, welcome back Dave."

# **Option (b)**

# ## Bonus Challenge - Modifying functions
# 
# 1. Rewrite the `year_to_csv` and `csvs_by_year` functions to have keyword arguments with default values.
# 
# 2. Modify the functions so that they don’t create yearly files if there is no data for a given year and display an alert to the user (Hint: use conditional statements to do this. For an extra challenge, use `try` statements !).
# 
# 3. The code below checks to see whether a directory exists and creates one if it doesn’t. Add some code to your function that writes out the CSV files, to check for a directory to write to.
# 
# ```python
# import os
# 
# if 'dir_name_here' in os.listdir():
#    print('Processed directory exists')
# else:
#    os.mkdir('dir_name_here')
#    print('Processed directory created')
# ```
# 
# `4.` The code that you have written so far to loop through the years is good, however it is not necessarily reproducible with different datasets. For instance, what happens to the code if we have additional years of data in our CSV files? Using the tools that you learned in the previous activities, make a list of all years represented in the data. Then create a loop to process your data, that begins at the earliest year and ends at the latest year using that list.
# 
# _HINT:_ you can create a loop with a list as follows: `for years in year_list:`

# ## Solutions - Modifying functions

# In[23]:


# Solution - part 1

def year_to_csv(year=None, all_data=None):
    """
    Writes a csv file for data from a given year.

    year --- year for which data is extracted
    all_data --- DataFrame with multi-year data
    """

    if all_data is None:
        all_data = pd.read_csv("surveys.csv")
    
    if year is None:
        year = min(all_data.year)
    
    # Select data for the year
    surveys_year = all_data[all_data.year == year]

    # Write the new DataFrame to a csv file
    filename = 'function_surveys' + str(year) + '.csv'
    surveys_year.to_csv(filename)
    
    
def csvs_by_year(start_year=None, end_year=None, all_data=None):
    """
    Writes separate CSV files for each year of data.

    start_year --- the first year of data we want
    end_year --- the last year of data we want
    all_data --- DataFrame with multi-year data
    """
    
    if all_data is None:
        all_data = pd.read_csv("surveys.csv")
    
    if start_year is None:
        start_year = min(all_data.year)
        
    if end_year is None:
        end_year = max(all_data.year)

    # "end_year" is the last year of data we want to pull, so we loop to end_year+1
    for year in range(start_year, end_year+1):
        year_to_csv(year, all_data)


# In[24]:


# Solution - part 2

def csvs_by_year(start_year=None, end_year=None, all_data=None):
    """
    Writes separate CSV files for each year of data.

    start_year --- the first year of data we want
    end_year --- the last year of data we want
    all_data --- DataFrame with multi-year data
    """
    
    if all_data is None:
        all_data = pd.read_csv("surveys.csv")
    
    if start_year is None:
        start_year = min(all_data.year)
        
    if end_year is None:
        end_year = max(all_data.year)

    # "end_year" is the last year of data we want to pull, so we loop to end_year+1
    for year in range(start_year, end_year+1):
        # print(len(all_data[all_data.year == year]))
        if len(all_data[all_data.year == year]) > 0:
            year_to_csv(year, all_data)
        else:
            print("Skipping: ", year, " - no data points for this year.")

surveys_df = pd.read_csv("surveys.csv")
csvs_by_year(1977, 2002, surveys_df)


# In[25]:


import os

# Solution - part 3
def year_to_csv(year=None, all_data=None, output_dir='output'):
    """
    Writes a csv file for data from a given year.

    year --- year for which data is extracted
    all_data --- DataFrame with multi-year data
    output_dir --- the output directory when CSV files will be written
    """

    if all_data is None:
        all_data = pd.read_csv("surveys.csv")
    
    if year is None:
        year = min(all_data.year)
    
    # Select data for the year
    surveys_year = all_data[all_data.year == year]


    if output_dir in os.listdir('.'):
        print('Processed directory exists: ', output_dir)
    else:
        os.mkdir(output_dir)
        print('Processed directory created: ', output_dir)
    
    # Write the new DataFrame to a csv file
    filename = output_dir + '/' + 'function_surveys' + str(year) + '.csv'
    # The more correct way to create paths is:
    # filename = os.path.join(output_dir, 'function_surveys' + str(year) + '.csv')
    surveys_year.to_csv(filename)
    
year_to_csv(2002, surveys_df)


# In[26]:


# Solution - part 4
def csvs_by_year(all_data):
    """
    Writes separate CSV files for each year of data.

    all_data --- DataFrame with multi-year data
    """

    # We could do this, but missing years will be included in the 'range'
    # start_year = min(all_data.year)
    # end_year = max(all_data.year)
    # year_list = range(start_year, end_year+1)
    
    # Instead, we create an empty list, then loop over all the rows, adding years
    # we haven't seen yet to the list.
    year_list = []
    for year in surveys_df.year:
        if year not in year_list:
            year_list.append(year)
    
    # An elegant alternative is to use a 'set' object.
    # A 'set' is a collection where every value is unique - no duplicates.
    # This ensures no repeated years and has the advantage of also skipping missing years.
    # year_list = set(surveys_df.year)
    
    # "end_year" is the last year of data we want to pull, so we loop to end_year+1
    for year in year_list:
        year_to_csv(year, all_data)
        
# The 'list' of years from each row contains duplicates (we just list the first 20 here)
print(list(surveys_df.year)[0:20])

print()

# Making it a 'set' removes duplicates
print(list(set(surveys_df.year)))


# # section: 1.2.3: files
# - navigate file system, working dir 
# - coming in the tables section 1.3.1

# In[ ]:




