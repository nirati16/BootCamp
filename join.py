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


df_sales = spark.read.option("header",True).option("inferschema",True).csv("/home/labuser/Nirati/PySpark/sales.csv")
df_sales.show()


# In[3]:


df_product = spark.read.option("header",True).option("inferschema",True).csv("/home/labuser/Nirati/PySpark/product.csv")
df_product.show()


# In[4]:


df = df_sales.join(df_product, df_sales.product_id==df_product.product_id, "inner")
df.show()


# In[5]:


df_sales.join(df_product, df_sales["product_id"]==df_product["product_id"],how="left").show()


# In[6]:


df_sales_product=df_sales.join(df_product,df_sales["product_id"]==df_product["product_id"],how="left")


# In[7]:


df_sales_product.filter("transaction_id=1").show()


# In[8]:


df_sales_product.where("transaction_id=1").show()


# In[9]:


from pyspark.sql.functions import *


# In[10]:


df_sales_product.where(col("transaction_id")==1).show()


# In[11]:


employees = [(1, "Scott", "Tiger", 1000.0, 
                      "united states", "+1 123 456 7890", "123 45 6789"
                     ),
                     (2, "Henry", "Ford", 1250.0, 
                      "India", "+91 234 567 8901", "456 78 9123"
                     ),
                     (3, "Nick", "Junior", 750.0, 
                      "united KINGDOM", "+44 111 111 1111", "222 33 4444"
                     ),
                     (4, "Bill", "Gomes", 1500.0, 
                      "AUSTRALIA", "+61 987 654 3210", "789 12 6118"
                     )
                ]


# In[12]:


employeesDF = spark. \
    createDataFrame(employees,
                    schema="""employee_id INT, first_name STRING, 
                    last_name STRING, salary FLOAT, nationality STRING,
                    phone_number STRING, ssn STRING"""
                   )


# In[13]:


employeesDF.show()


# In[25]:


employeesDF1=employeesDF.withColumn("nationality",upper(col("nationality")).cast("string"))


# In[28]:


#employeesDF1.dtypes
employeesDF1.show()


# In[30]:


employeesDF2=employeesDF1.withColumn("Last 4 SSN",substring(col("ssn"),7,4).cast("int"))


# In[32]:


employeesDF2.show()


# In[34]:


employeesDF3=employeesDF2.withColumn("Country Code",split(col("phone_number")," ")[0].cast("int"))


# In[36]:


employeesDF3.show()


# In[37]:


employeesDF4=employeesDF3.withColumn("Area Code",split(employeesDF["phone_number"]," ")[1].cast("int"))


# In[38]:


employeesDF4.show()


# In[40]:


employeesDF4.dtypes


# In[ ]:


#employeesDF. \
#    withColumn("nationality",upper("nationality")).\
#    withColumn("ssn_last4", substring(col("ssn"), -4, 4).cast("int")).\
#    withColumn("country_code", split("phone_number", " ")[0].cast("int")).\
#    withColumn("area_code", split("phone_number", " ")[1].cast("int")).\
#    show()


# In[ ]:




