#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


import numpy as np


# In[3]:


x_axis=np.array([1,10])
y_axis=np.array([1,50])


# In[4]:


plt.plot(x_axis,y_axis)


# In[6]:


y_points=np.array([1,10,2,8,5])
plt.plot(y_points)


# In[7]:


plt.plot(y_points,marker='*')


# In[8]:


plt.plot(y_points,marker='o')


# In[12]:


plt.plot(y_points,marker='o')

plt.title("Sample Chart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")


# In[15]:


months=np.array(['January', 'February', 'March', 'April', 'May'])
sales=np.array([2500, 3200, 2800, 4100, 3700])


# Create a bar chart

# In[18]:


plt.bar(months,sales,color="pink",width=0.6)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Data")


# In[19]:


plt.savefig("monthly_sale.png")

