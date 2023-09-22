#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyspark
import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.sql.types import *

 

from pyspark.sql.functions import *

 

from pyspark.sql import SparkSession

 

spark = SparkSession.builder.appName("Example").getOrCreate()


# In[2]:


df = spark.read.option("multiline",True).json("/home/labuser/Nirati/PySpark/pitstop.json")


# In[3]:


df.show()


# In[4]:


df.sort("driverID").show()


# In[ ]:


grouped_df = df.groupBy('stop').count().orderBy('stop')


# In[5]:


import matplotlib.pyplot as plt
pandas_df = grouped_df.toPandas()
plt.figure(figsize=(5,7))
plt.bar(pandas_df["stop"].astype(str), pandas_df["count"], color="Pink", width=0.5)
plt.xlabel("Stop")
plt.ylabel("Count")
plt.title("Count of Stops")
plt.show()


# In[ ]:


import warnings
warnings.filterwarnings("ignore")


# In[ ]:


df_final=df.sort("driverID")


# In[ ]:


df.count()


# In[ ]:


df.groupBy("stop").count()


# In[ ]:


df_stops=df.groupBy("stop").count()


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


df_final.write.mode("overwrite").option("path","/home/labuser/Nirati/PySpark/pitstop.json").saveAsTable("pitlogs")


# In[ ]:


df.sort("driverId").write.mode('overwrite').option("path",'processed_data/pitstops').saveAsTable("pitstops")
df = spark.read.parquet('processed_data/pitstops')
df.show()


# In[ ]:




