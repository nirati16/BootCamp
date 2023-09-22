#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pyspark


# In[8]:


findspark.init('/usr/local/spark')


# In[9]:


from pyspark import SparkContext


# In[10]:


conf=pyspark.SparkConf().setMaster("local").setAppName("first")


# In[11]:


sc=SparkContext(conf=conf)


# In[5]:


sc.stop()


# In[12]:


rdd=sc.parallelize([1,2,3])


# In[13]:


rdd.collect()


# In[14]:


sc


# In[17]:


rdd2=sc.parallelize(["Python","SQL","PySpark"])


# In[18]:


rdd.collect()


# In[19]:


rdd


# In[20]:


display(rdd2)
display(rdd2.collect())
display(type(rdd2))


# In[15]:


rdd3=sc.parallelize([1,2,3,4,5,6,7,8])


# In[16]:


rdd3.collect()


# make the elements inside the list twice of the rdd
# [2,4,6,8,10,12,14,16]

# In[21]:


rdd4=rdd3.map(lambda x:x*2)


# In[22]:


rdd4.collect()


# Task: Save all the even nos in new rdd.

# In[25]:


rdd5=rdd3.filter(lambda x:x%2==0)


# In[26]:


rdd5.collect()


# In[ ]:




