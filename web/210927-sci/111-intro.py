#!/usr/bin/env python
# coding: utf-8

# [home](https://nils-holmberg.github.io/sfac-py/web/210927-sci/)
# 
# # day 1: getting started with python
# - overview of day 1
# 
# |time  |section |concepts                        |outcomes                                                            |
# |:-----|:-------|:-------------------------------|:-------------------------------------------------------------------|
# |09-10 |1.1.1   |[anaconda3](01-intro.html)      |understand install location, create and update virtual environments |
# |      |1.1.2   |jupyter                         |download course material, open notebooks, edit in web browser       |
# |      |1.1.3   |testing                         |execute the hello world example in jupyter python env               |
# |      |break   |                                |                                                                    |
# |10-11 |1.2.1   |[python syntax](02-syntax.html) |practice data structures, conditional statements, flow control      |
# |      |1.2.2   |functions                       |understand modules                                                  |
# |      |1.2.3   |files, directories              |navigate the file system, read, write data files                    |
# |      |break   |                                |                                                                    |
# |11-12 |1.3.1   |[tabular data](03-tables.html)  |understand how to read, write, and process survey data              |
# |      |1.3.2   |subset, substitute              |and reshape                                                         |
# |      |1.3.3   |summarize                       |aggregate, combine, join operations                                 |
# |12-13 |lunch   |anaconda, continued             |try to resolve anaconda, psychopy installation problems             |
# 
# - **mindset: excel on steroids**
# 
# <img src="../../fig/Microsoft_Office_Excel_2019_present.svg.png" width="100"/>
# 
# ## section 1.1.1: anaconda
# - check anaconda3 installation (backup with google colab)
# - **anaconda console**, conda update, create venv, install scipy
# - python interpreter prompt, spyder ide, script editor
# 
# ```python
# # update anaconda, spyder
# conda update anaconda
# conda install spyder=5.0.5
# # update packages in env
# conda update --all
# # list envs
# conda env list
# # start jupyter notebook
# jupyter notebook
# ```
# 
# ## section 1.1.2: jupyter
# - download course [github repository](https://github.com/nils-holmberg/sfac-py.git)
# - launch jupyter notebook, connect anaconda python kernel
# 
# ## section 1.1.3: testing
# - test interactive python commands in jupyter notebooks
# - navigate file system, working dir 

# In[2]:


# comment: test anaconda3 and jupyter notebooks
print("hello world")


# ## Interpreter
# 
# Python is an interpreted language[*](https://softwareengineering.stackexchange.com/a/24560) which can be used in two ways:
# 
# * "Interactive" Mode: It functions like an "advanced calculator", executing
#   one command at a time:
#   
# ```bash
# user:host:~$ python
# Python 3.5.1 (default, Oct 23 2015, 18:05:06)
# [GCC 4.8.3] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 2 + 2
# 4
# >>> print("Hello World")
# Hello World
# ```
# 
# * "Scripting" Mode: Executing a series of "commands" saved in text file,
#   usually with a `.py` extension after the name of your file:
# 
# ```bash
# user:host:~$ python my_script.py
# Hello World
# ```
# 
# ## Using interactive Python in Jupyter-style notebooks
# 
# A convenient and powerful way to use interactive-mode Python is via a Jupyter Notebook, or similar browser-based interface.
# 
# This particularly lends itself to data analysis since the notebook records a history of commands and shows output and graphs immediately in the browser.
# 
# There are several ways you can run a Jupyter(-style) notebook - locally installed on your computer or hosted as a service on the web. Today we will use a Jupyter notebook service provided by Google: https://colab.research.google.com (Colaboratory).
# 
# ### Jupyter-style notebooks: a quick tour
# 
# Go to https://colab.research.google.com and login with your Google account.
# 
# Select ***NEW NOTEBOOK → NEW PYTHON 3 NOTEBOOK*** - a new notebook will be created.
# 
# ---
# 
# Type some Python code in the top cell, eg:
# 
# ```python
# print("Hello Jupyter !")
# ```
# 
# ***Shift-Enter*** to run the contents of the cell
# 
# ---
# 
# You can add new cells.
# 
# ***Insert → Insert Code Cell***
# 
# ---
# 
# NOTE: When the text on the left hand of the cell is: `In [*]` (with an asterisk rather than a number), the cell is still running. It's usually best to wait until one cell has finished running before running the next.
# 
# Let's begin writing some code in our notebook.

# In[ ]:




