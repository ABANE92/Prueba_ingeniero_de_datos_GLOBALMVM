# Databricks notebook source
# ============================================================
# Notebook Generador de datos Automático
# ============================================================
# Objetivo:
# DESAFIO #1: Construya un script que genere de forma automática los datos de: 
# departamentos, puestos de trabajo, y empleados.
# ============================================================

from pyspark.sql.functions import *
from pyspark.sql.types import *
import random
from datetime import datetime

# -------------------------------
# 1. Categorias
# -------------------------------
categorias = [
    (1, "Technology"),
    (2, "Business"),
    (3, "Art"),
    (4, "Science"),
    (5, "Health")
]
# -------------------------------
# 2. Niveles
# -------------------------------
niveles = [
    (101, "Beginner"),
    (102, "Intermediate"),
    (103, "Advanced")
]
# -------------------------------
# 3. Empleados generados
# -------------------------------
empleados = []

#Estos son los esquemas de los DataFrames a crear
schema_cat = StructType([
    StructField("category_id", IntegerType()),
    StructField("category_name", StringType())
])
schema_nivel = StructType([
    StructField("level_id", IntegerType()),
    StructField("level_name", StringType())
])
schema_emp = StructType([
    StructField("emp_id", IntegerType()),
    StructField("emp_name", StringType()),
    StructField("category_id", IntegerType()),
    StructField("level_id", IntegerType()),
    StructField("start_date", TimestampType())
])

for i in range(1, 101):
    empleados.append((
        i,
        f"Empleado_{i}",
        random.choice([1,2,3,4,5]),
        random.choice([101,102,103]),
        datetime(2023, random.randint(1,12), random.randint(1,28))
    ))
# Creamos el dataframe de departamentos, puestos y empleados
df_categorias = spark.createDataFrame(categorias, schema_cat)
df_niveles = spark.createDataFrame(niveles, schema_nivel)
df_empleados = spark.createDataFrame(empleados, schema_emp)

#Visualizar los DataFrames
display(df_categorias)
display(df_niveles)
display(df_empleados)

# COMMAND ----------

# ============================================================
# Objetivo
# DESAFIO #2: Guarde los datos simulados en archivos con formato CSV/Parquet. 
# ============================================================

# Directorios base likehouse
raw_path = "/Volumes/prueba_globalmvm/default/prueba_globalmvm/raw"

# Guardar categorías en RAW
df_categorias.write.format("parquet").mode("overwrite").save(f"{raw_path}categorias")
# Guardar niveles en RAW
df_niveles.write.format("parquet").mode("overwrite").save(f"{raw_path}niveles")
# Guardar empleados en RAW
df_empleados.write.format("parquet").mode("overwrite").save(f"{raw_path}empleados")

# Se guarda en formato parquet debido a que Parquet es un formato columnar, 
# comprimido y optimizado para lectura, permite realizar procesos más rápidos,
# ocupa menos espacion de almacenamiento que un archivo CSV y se integra mejor con el lakehouse.



# COMMAND ----------

# ============================================================
# Objetivo
# DESAFIO #3: Implemente un proceso batch para migrar los datos a una base de datos SQL/NoSQL.
# ============================================================


# Directorios base likehouse
raw_path = "/Volumes/prueba_globalmvm/default/prueba_globalmvm/raw"
bronze_path = "Tables/bronze_"  

# Leer RAW
df_cat_bronze = spark.read.parquet(f"{raw_path}categorias")
df_niv_bronze = spark.read.parquet(f"{raw_path}niveles")
df_emp_bronze = spark.read.parquet(f"{raw_path}empleados")

# Guardar como Tablas Delta (BRONZE)
df_cat_bronze.write.format("delta").mode("overwrite").saveAsTable("bronze_categorias")
df_niv_bronze.write.format("delta").mode("overwrite").saveAsTable("bronze_niveles")
df_emp_bronze.write.format("delta").mode("overwrite").saveAsTable("bronze_empleados")


# COMMAND ----------

# ============================================================
# Objetivo
# DESAFIO #4:desarrolle una view/query/report a partir del modelo de datos
#
# ============================================================
spark.sql("""
CREATE OR REPLACE VIEW vw_empleados_full AS
SELECT 
    e.emp_id,
    e.emp_name,
    e.category_id,
    c.category_name,
    e.level_id,
    n.level_name,
    e.start_date
FROM bronze_empleados e
LEFT JOIN bronze_categorias c
    ON e.category_id = c.category_id
LEFT JOIN bronze_niveles n
    ON e.level_id = n.level_id
""")
df_view = spark.sql("SELECT * FROM vw_empleados_full")
display(df_view)