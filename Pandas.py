#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


print(pd._version)


# In[4]:


data={
    "names":['a','b','c'],
    "ages":[25,28,21]
}


# In[5]:


df=pd.DataFrame(data)


# In[6]:


df


# In[7]:


print(df)


# In[8]:


df.head(2)


# In[9]:


df.tail(1)


# In[10]:


df.describe()


# In[11]:


df.dtypes


# In[12]:


df.info()


# In[13]:


df


# In[14]:


df.columns=["emp_name","age"]


# In[15]:


df


# In[16]:


df2=df.rename(columns={"emp_name":"emp_firstname","age":"emp_age"})


# In[17]:


df2


# In[18]:


df


# In[19]:


dept=["Sales","Marketing","IT"]


# In[23]:


df2=df.assign(Company=dept)


# In[25]:


df2.dtypes


# In[26]:


df3=df2.convert_dtypes()


# In[29]:


df3.dtypes


# In[30]:


df4=df2.astype({"age":float})


# In[31]:


df4


# In[32]:


df4.dtypes


# In[49]:


print("No. of rows",len(df))


# In[50]:


print("No. of columns",len(df.columns))


# In[43]:


df.shape


# In[44]:


df.shape[0]


# In[45]:


df.shape[1]


# In[48]:


display(df)


# In[54]:


technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,22000,24000],
    'Duration':['30day','40days','35days','40days','60days'],
    'Discount':[1000,2300,1200,2500,2000]
              }


# In[55]:


index_label=['r1','r2','r3','r4','r5']


# In[58]:


cdf=pd.DataFrame(technologies)


# In[59]:


cdf


# In[60]:


cdf=pd.DataFrame(technologies,index=index_label)


# In[61]:


cdf


# df.loc[start:stop:step, start:stop:step]
#          select rows     select columns

# In[63]:


cdf.loc['r1']


# In[64]:


cdf.loc[['r1','r2']]


# In[67]:


cdf.loc[:,["Courses"]]


# In[68]:


cdf.loc[:,["Courses","Fee"]]


# In[69]:


cdf.loc[['r1','r3']]


# In[72]:


cdf.loc['r2':'r4']


# In[73]:


cdf


# In[76]:


cdf.loc[cdf["Fee"]>2200]


# In[77]:


cdf.loc[cdf["Discount"]>1200]


# In[78]:


cdf.query("Courses!='PySpark'")


# In[80]:


cdf.drop(columns=["Discount"])

