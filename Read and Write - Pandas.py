#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


emp_df=pd.read_csv("employee.csv")


# In[5]:


emp_df


# In[6]:


emp_df.describe


# In[6]:


emp_df.info


# In[7]:


emp_df.shape


# In[8]:


emp_df.dtypes


# In[9]:


emp_df2=emp_df.convert_dtypes()


# In[11]:


emp_df2.dtypes


# In[17]:


emp_df["Start Date"]=pd.to_datetime(emp_df["Start Date"])


# In[18]:


emp_df.dtypes


# In[19]:


emp_df.nunique()


# In[21]:


emp_df.isnull().sum()


# Fill or replace in gender column by saying NO Gender

# In[22]:


emp_df["Gender"]=emp_df["Gender"].fillna("No Gender")


# In[24]:


emp_df.isnull().sum()


# Group By Gender

# Fill the senior management with the mode value

# Write the emp_df to final_emp_df to csv

# In[30]:


emp_df.groupby(["Gender"]).count()


# In[31]:


emp_df["Senior Management"]=emp_df["Senior Management"].fillna(emp_df["Senior Management"].mode()[0])


# In[32]:


emp_df.isnull().sum()


# In[33]:


emp_df.to_csv("Final_emp_df")

