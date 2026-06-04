from databricks.connect import DatabricksSession

spark = DatabricksSession.builder.profile("dbw-dev").getOrCreate()
spark.sql("SELECT 1").show()