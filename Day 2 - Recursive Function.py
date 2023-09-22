#!/usr/bin/env python
# coding: utf-8

# #Recursive Functions : Function that calls itself

# In[3]:


def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
factorial(5)


# In[6]:


def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
result = fibonacci(7)
print(result) #0,1,1,2,3,5,8


# #Decorator Fucntion

# In[13]:


def div(a,b):
    c=a/b
    return c


# In[14]:


div(10,5)


# In[15]:


def div1(a,b):
    if a<b:
        a,b=b,a
    c=a/b
    return c


# In[16]:


div1(5,10)


# In[17]:


div(5,10)


# Decorator Function

# In[18]:


def og_div(a,b):
    c=a/b
    return c


# In[20]:


og_div(5,10)


# In[19]:


def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


# In[21]:


result = smart_div(og_div)


# In[22]:


result(5,10)


# In[23]:


result(10,5)


# In[60]:


def wish(name):
    print("Hello",name,"Good Morning")


# In[61]:


wish("Nirati")


# In[62]:


def wish_specific(func):
    def inner(n1):
        if(n1=="Robert"):
            print("Hello",n1,"Bad Morning")
        else:
            return func(n1)
    return inner


# In[63]:


result=wish_specific(wish)


# In[66]:


@wish_specific
def wish(name):
    print("Hello",name,"Good Morning")


# In[67]:


result("Robert")


# In[68]:


result("John")


# Task: Logging Decorator
# 
# You are tasked with creating a decorator function called log_function_call that logs when a function is called, along with its arguments, and the result of the function call. You will apply this decorator to two functions.
# 
# Implement a decorator function called log_function_call that takes a function as an argument and wraps it. Inside the decorator, log the function's name, its arguments, and the result of the function call. You can use the logging module for logging.
# 
# Create two functions:
# 
# add(a, b): This function takes two integers, a and b, as arguments and returns their sum.
# multiply(a, b): This function takes two integers, a and b, as arguments and returns their product.
# Apply the log_function_call decorator to both the add and multiply functions.
# 
# Call the decorated add and multiply functions with different arguments to verify that the decorator logs the function calls and results correctly.

# In[71]:


def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def log_function_call(func):
    def inner(a,b):
        return func(a,b)
    return inner
result1 = log_function_call(add)
result2 = log_function_call(multiply)


# In[72]:


result1(2,3)
result2(2,3)


# #Generator Function : uses 'yield' keyword to yield a sequence of value one at a time instead of returning all at once

# In[74]:


def count_up_to(n):
    i=1
    while i<=n:
        yield i
        i=i+1


# In[75]:


count_up_to(10)


# In[76]:


for i in count_up_to(10):
    print(i)


# Task: To generate Fibonacci numbers using generator function

# In[83]:


def FibonacciNos(n):
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        a=0
        b=1
        i=1
        while i<=(n-2):
            c=a+b
            yield c
            a=b
            b=c
            i=i+1
FibonacciNos(5)


# In[84]:


for i in FibonacciNos(5):
    print(i)


# #List Comprehension : 
# list=[expression for items in list if condition]

# In[85]:


nos=[1,2,3,4,5]
square=[x**2 for x in nos]


# In[86]:


print(square)


# In[87]:


s=[x*2 for x in range(10)]
print(s)


# In[90]:


s=[x for x in range(10) if x%2==0]


# In[91]:


print(s)


# In[95]:


l1=["python","sql","azure","power BI"]
print([x[0] for x in l1])


# In[96]:


print([x[0].upper()+x[1:] for x in l1])


# In[100]:


words="the quick brown fox jumps over the lazy dog"
list1 = words.split()
print([[x.upper(),len(x)] for x in list1])


# Lambda Function:
# Anonymous Function: (No name for the function)

# In[103]:


f=lambda i:i*i


# In[102]:


def square(i):
    return i*i


# In[104]:


f(3)


# In[105]:


f1=lambda a,b:a+b


# In[106]:


f1(3,5)


# In[110]:


f2=lambda a,b:max(a,b)


# In[113]:


f2(4,8)


# In[117]:


f3=lambda a,b: a if a>b else b


# In[118]:


f3(4,8)


# Filter, Map Functions

# In[119]:


def evenodd(x):
    if x%2==0:
        return True
    else:
        return False


# In[120]:


evenodd(5)


# In[121]:


l=[0,34,123,45,32,6,12,9]
l1=list(filter(evenodd,l))


# In[122]:


l1


# In[124]:


l2=list(filter(lambda x:x%2==0,l))


# In[125]:


l2


# In[126]:


l=[10,11,12,13,14,15]
def squareit(n):
    return n**2
sq=list(map(squareit,l))
print(sq)


# In[127]:


sq1 = list(map(lambda x:x**2,l))


# In[128]:


sq1


# In[131]:


words=["hello","world","lambda","exercise"]
x1=list(map(lambda x:x.upper(),words))


# In[132]:


x1


# Sort Function

# In[133]:


people=[{'name':'Alice','age':30},{'name':'Bob','age':25},{'name':'Charlie','age':35}]


# In[134]:


sorted(people,key=lambda i:i['age'])


# #Class

# In[135]:


class Computer:
    #Variables
    #Methods(Attributes)(Functions)
    def config(self):
        print("i5, 16Gb")


# In[136]:


comp1=Computer()


# In[137]:


comp1.config()


# In[ ]:




