#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark


# In[2]:


findspark.init()


# In[3]:


from pyspark.sql import SparkSession


# In[5]:


#Create a spark session
spark=SparkSession.builder.appName("RDDExample").getOrCreate()


# In[6]:


df=spark.createDataFrame([(1,2,3)])


# In[7]:


df.show()


# In[64]:


from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row

 

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
df


# In[65]:


df.show()


# In[66]:


df2 = spark.createDataFrame([
    (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
], schema='a long, b double, c string, d date, e timestamp')
df2


# In[67]:


df2.show()


# In[68]:


data2=[(1,'a','z',777700,'India'),(2,'b','y',9890,'India')]


# In[69]:


schema="id int,name string,last_name string,mo int,country string"


# In[70]:


shem_list=["id","name","last_name","mo","country"]


# In[71]:


df3=spark.createDataFrame(data2,schema)


# In[72]:


df3


# In[73]:


df3.show()


# In[74]:


df3.dtypes


# In[75]:


df4=spark.createDataFrame(data2,shem_list)


# In[76]:


df4.show()


# In[77]:


df4.dtypes


# In[78]:


df4.printSchema()


# In[79]:


users=[{"id":1,
       "first_name":"a",
       "amount_paid":1000
       },
       {"id":2,
       "first_name":"b",
        "amount_paid":2000
       }
      ]


# In[80]:


df4=spark.createDataFrame(users)


# In[81]:


df4.show()


# In[82]:


df5=spark.read.csv("/home/labuser/Nirati/Datasets for Python/employee.csv")


# In[83]:


df5.show()


# In[84]:


df5.printSchema()


# In[85]:


df5=spark.read.option("header",True).csv("/home/labuser/Nirati/Datasets for Python/employee.csv")


# In[86]:


df5.show()


# In[87]:


df5.printSchema()


# In[105]:


df6=spark.read.option("header",True).option("inferschema", True).csv("/home/labuser/Nirati/Datasets for Python/employee.csv")
df6.printSchema()


# In[106]:


#select columns
df6.select("First Name","Gender").show()


# In[107]:


#change column name
df6.select("First Name".alias("forename"))


# In[108]:


from pyspark.sql.functions import col


# In[109]:


df6.select(col("First Name").alias("forename")).show()


# In[110]:


df6.select("First Name",col("Gender")).show(5)


# In[111]:


df6.select("First Name",col("Gender"),"*").show(5)


# In[112]:


df6.select("First Name",col("Gender"),df6["Team"]).show()


# In[113]:


df6.withColumnRenamed('First Name', 'Name').show(5)


# In[114]:


from pyspark.sql.functions import concat


# In[115]:


df6.concat("Start Date","Last Login Time")


# In[116]:


df6.select(concat('Start Date','Last Login Time')).show()


# In[117]:


from pyspark.sql.functions import *


# In[123]:


df6.select("*",
          concat("Start Date", lit(" "), "Last Login Time")
          .alias("datetime")
          ).show(5)


# In[122]:


dffinal=df6.drop("Start Date","Last Login Time")


# In[120]:


dffinal.show()


# In[124]:


dffinal.write.csv("zSpark_Final_Dataframe.csv")


# In[ ]:




