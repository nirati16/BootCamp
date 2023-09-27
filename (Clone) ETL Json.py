# Databricks notebook source
from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/saunextadls/raw/json

# COMMAND ----------

#dbutils.fs.mount(
#  source = "wasbs://raw@saunextadls.blob.core.windows.net",
#  mount_point = "/mnt/saunextadls/raw",
#  extra_configs = {"fs.azure.account.key.saunextadls.blob.core.windows.net":"DsZWJs7JVVHZz1I7GKyclV8ejCdj0V2UkqMlgAp6QyVOw5rvrHvmVTgwcThdHUymWg7MXon65/0z+AStj4Yiug=="})

# COMMAND ----------

df=spark.read.json("dbfs:/mnt/saunextadls/raw/json")

# COMMAND ----------

df.display()

# COMMAND ----------

df1=df.withColumn("ingestiondate",current_timestamp()).withColumn("path",input_file_name())

# COMMAND ----------

df1.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists json

# COMMAND ----------

#Managed Table - as I have not specified the path.
df1.write.mode("overwrite").saveAsTable("bronzejson")

# COMMAND ----------

#External Table - this will be stored in data lake
df1.write.mode("overwrite").option("path","dbfs:/mnt/saunextadls/raw/output/nirati/json").saveAsTable("json.bronze")
#df1.write.mode("append").option("path","dbfs:/mnt/saunextadls/raw/output/nirati/json").saveAsTable("json.bronze")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from json.bronze

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from json.bronze

# COMMAND ----------


