#!/usr/bin/env python
# coding: utf-8

# Functions

# In[1]:


a=10
b=20
print('the sum is ',a+b)
print('the difference is ',a-b)
print('the product is ',a*b)
print('the remainder is ',a%b)


# In[2]:


def my_function():
    print("hello from my_function")
my_function()


# Parameter

# In[3]:


def wish(name):
    print("hello ",name," Good Morning")


# In[4]:


wish("naval")


# Task: Write a function to take a no and print it's square value

# In[5]:


def sq(n):
    print(n*n)


# In[6]:


sq(13)


# In[7]:


def sq(n):
    return n*n


# In[8]:


sq(12)


# Task: Write a function to check whether the given number is even or odd

# In[9]:


def check(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")


# In[10]:


check(14)


# In[11]:


check(19)


# In[12]:


def add(a,b):
    print(a+b)


# In[14]:


add(5,6)


# Type of Arguments:
# 1. Positional Arguments
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable Length Arguments

# In[15]:


def sub(a,b):
    print(a-b)


# In[16]:


sub(10,5)


# In[17]:


sub(13,20)


# In[18]:


sub(b=13,a=20)


# In[19]:


def wish(name,msg):
    print("hello",name,msg)


# In[20]:


wish("Nirati","Good Morning")


# In[21]:


wish(msg="Good morning",name="Nirati")


# In[22]:


wish("Good morning",name="Nirati")


# In[23]:


wish(msg="Good morning","Nirati")


# In[24]:


wish("nirati",msg="good morning")


# In[25]:


def sum(a=2,b=3):
    print(a+b)


# In[26]:


sum(5,7)


# In[27]:


sum()


# In[28]:


sum(4)


# In[29]:


sum(b=4)


# In[30]:


range(10)


# In[31]:


sum=0
for i in range(10):
    sum=sum+i
    print(i)


# In[32]:


print(sum)


# In[33]:


def sum(a,b):
    print(a+b)


# In[34]:


sum(10,20,30,40)


# In[35]:


def add(*n):
    sum=0
    for i in n:
        sum=sum+i
    return sum


# In[36]:


add(10,20)


# In[38]:


add(1,2,3,4,5)


# In[39]:


add(10)


# Keyword Variable Length Argument

# In[43]:


def info(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j)


# In[44]:


info(name="John",Age=30,City="Mumbai")


# In[45]:


info(name="John",Age=30,City="Mumbai",dept="IT")


# In[46]:


def person(name, *arg):
    print(name)
    print(arg)


# In[47]:


person("Paul",20,"IT",777700,"Delhi")


# In[48]:


def person(name, **arg):
    print(name)
    for i,j in arg.items():
        print(i,":",j)


# In[49]:


person("Nirati",Age=21,Location="Ghaziabad",dept="IT")


# In[50]:


def person(name, **arg):
    print(name)
    print(arg)


# In[51]:


person("Nirati",Age=21,Location="Ghaziabad",dept="IT")


# Task: Oil and Gas Equipment and Drilling Site Management System
# 
#  
# 
# You are tasked with developing a Python program for an oil and gas company to manage their drilling equipment and drilling sites. The program should use *args and **kwargs to provide flexibility in adding and searching for equipment and sites. Here are the tasks you need to complete:
# Create a Python script that defines empty lists for drilling equipment and drilling sites.
# 
#  
# 
# Implement a function add_equipment that takes the following parameters:
# 
#  
# 
# equipment_type (string): The type of equipment being added.
# *args (tuple): Additional details about the equipment (e.g., model, power, capacity).
# **kwargs (dictionary): Additional attributes of the equipment (e.g., vendor, power source).
# The function should create a dictionary representing the equipment, including its type, details (from *args), and attributes (from **kwargs). Then, it should append this dictionary to the drilling_equipment list.

# In[62]:


drilling_equipment=[]
def add_equipment(equipment_type,*args,**kwargs):
    print(equipment_type)
    print(args)
    print(kwargs)
add_equipment("Pump","Model X",100,10,vendor="A")


# In[68]:


drilling_equipment=[]
def add_equipment(equipment_type,*args,**kwargs):
    dict={
        "equipment":equipment_type,
        "details":args,
        "attributes":kwargs
    }
    drilling_equipment.append(dict)
add_equipment("Pump","Model X",100,10,vendor="A")


# In[69]:


print(drilling_equipment)


# Implement a function add_drilling_site with similar parameters:
# 
#  
# 
# site_name (string): The name of the drilling site being added.
# *args (tuple): Additional details about the site (e.g., location, depth, terrain).
# **kwargs (dictionary): Additional attributes of the site (e.g., status, operator).
# The function should create a dictionary representing the site, including its name, details (from *args), and attributes (from **kwargs). Then, it should append this dictionary to the drilling_sites list.

# In[70]:


def add_drilling_site(site_name,*args,**kwargs):
    dict={
        "name":site_name,
        "details":args,
        "attributes":kwargs
    }
    drilling_equipment.append(dict)
add_equipment("Motor","Model Z",221,30,vendor="B")


# In[71]:


print(drilling_equipment)


# In[72]:


def f(arg1,arg2,arg3=2,arg4=5):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)


# In[73]:


f(2,3)


# In[74]:


f(arg3=9,4,5)


# In[ ]:




