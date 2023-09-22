#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np


# In[7]:


arr=np.array([1,23,33])


# In[8]:


arr


# In[9]:


arr2=np.array([[1,23,33],[2,22,54]])


# In[10]:


arr2


# In[11]:


arr.ndim


# In[12]:


arr2.ndim


# In[13]:


arr3=np.array([[[1,23,33],[2,22,54]],[[34,45,56],[23,22,51]]])


# In[14]:


arr3


# In[15]:


arr3.ndim


# In[16]:


arr


# In[17]:


arr[2]


# In[18]:


arr[0:2]


# In[19]:


arr2


# In[20]:


arr2[0,2]


# In[21]:


arr2[1,1]


# In[22]:


arr2[1,0:2]


# In[23]:


arr3


# In[24]:


arr3[0,1,2]


# In[25]:


arr3[1,0,1]


# In[26]:


arr3[1,1,0:2]


# In[27]:


arr1 = [[1,2],[3,4],[5,6]]
arr2 = [[6,7],[8,9],[10,11]]
res = np.concatenate((arr1, arr2))
print(res)


# In[29]:


arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
res = np.concatenate((arr1, arr2))
print(res)


# In[34]:


temperature_data = [25.3, 26.1, 24.8, 23.5, 27.2]
pressure_data = [101.2, 100.8, 101.5, 100.2, 101.0]
humidity_data = [55.2, 54.8, 56.5, 53.7, 55.9]


# #Calculate a NumPy array from the dataset

# In[35]:


temperature_arr=np.array(temperature_data)
pressure_arr=np.array(pressure_data)
humidity_arr=np.array(humidity_data)


# In[36]:


temperature_arr


# #Calculate the mean (average) of eavh quantity

# In[38]:


temperature_mean=np.mean(temperature_arr)


# In[39]:


temperature_mean


# #Calculate the standard deviation of each quantity

# In[40]:


temperature_std=np.std(temperature_arr)


# In[41]:


temperature_std


# #Calculate maximum and minimum value

# In[42]:


temperature_max=np.max(temperature_arr)


# In[43]:


temperature_min=np.min(temperature_arr)


# In[44]:


temperature_max


# In[45]:


temperature_min

