#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyspark
import findspark
findspark.init()
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Example").getOrCreate()


# In[2]:


input_files="/home/labuser/Nirati/PySpark/"
df=spark.read.json(f"{input_files}/constructor.json")


# In[3]:


df.show()


# In[11]:


from pyspark.sql.functions import *
from pyspark.sql.types import *
df = df.withColumn("ingestion_date",current_timestamp()).withColumn("path",input_file_name())
df.show(2)


# In[15]:


df.drop("path")


# In[16]:


output_files="/home/labuser/Nirati/PySpark/processed_data/constructor_parquet"


# In[17]:


df.write.parquet(f"{output_files}")


# In[18]:


df.write.mode("overwrite").parquet(f"{output_files}")


# In[20]:


df.write.mode("overwrite").saveAsTable("constructor")


# In[26]:


df.write.mode("overwrite").option("path","/home/labuser/Nirati/PySpark/processed_data/constructor_parquet").saveAsTable("constructor")


# In[25]:


spark.sql("select * from constructor where constructorId=10").show()


# In[21]:


spark.sql("select * from constructor").show()

