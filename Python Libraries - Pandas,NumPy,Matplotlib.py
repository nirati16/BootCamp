#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


sales_df=pd.read_csv("sales.csv")


# In[4]:


sales_df


# In[6]:


#Data cleaning
#Check for missing value
#Check data type
#remove duplicates


# In[9]:


sales_df.isnull().count()


# In[10]:


sales_df.dtypes


# In[12]:


sales_df["Date"]=pd.to_datetime(sales_df["Date"])


# In[13]:


display(sales_df.drop_duplicates())


# In[ ]:


#Data Exploration
# Total revenue for the entire dataset
# Total quantity sold for each product
# Monthly total revenue
# Monthly average revenue for each product


# In[16]:


display(sales_df["Sales"].sum())


# In[18]:


sales_df.groupby(["Product"])["Sales"].count()


# In[20]:


sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum()


# In[22]:


sales_df.groupby(sales_df["Date"].dt.month)["Sales"].mean().round(2)

