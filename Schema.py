#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyspark
import findspark
findspark.init()
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Example").getOrCreate()


# In[2]:


from pyspark.sql.types import *


# In[3]:


data=[(1,"a",30),(2,"b",32)]
user_schema=StructType([StructField("id",IntegerType()),
                        StructField("name",StringType()),
                        StructField("age",IntegerType())
                       ])


# In[4]:


df=spark.createDataFrame(data,user_schema)


# In[5]:


df.show()


# In[6]:


data2=[
    (1,"Alice",["Reading","Hiking"]),
    (2,"Bob",["Swimming","Gardening","Painting"]),
    (3,"Charlie",["Cooking"]),
    (4,"David",["Photography","Skiing","Cooking"])
]


# In[7]:


schema2 = StructType([
    StructField("id", IntegerType()),
    StructField("name", StringType()),
    StructField("hobbies", ArrayType(StringType()))
])


# In[8]:


df2=spark.createDataFrame(data2,schema2)


# In[9]:


df2.show()


# In[12]:


from pyspark.sql.functions import explode
df2.select("id", "name", explode("hobbies").alias("hobby")).show()


# In[13]:


df2.withColumn("newhobby",explode("hobbies")).show()


# In[15]:


df2.withColumn("hobbies",explode("hobbies")).show()


# In[22]:


from pyspark.sql.functions import *
df3=df2\
.withColumn("hobbies",explode("hobbies"))\
.withColumn("ingestion_data",current_timestamp())
df3.show()


# In[23]:


df3.show(truncate=False)

