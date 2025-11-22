# Prueba_ingeniero_de_datos_GLOBALMVM
Repositorio para una prueba técnica como ingeniero de datos 
# Prueba - Desafíos 1 al 4 (Databricks Free Edition)

Este repositorio documenta la solución de los **Desafíos 1 al 4**, utilizando **Databricks Community Edition**, almacenamiento mediante **Volumes (Catalog/Schema/Volume)** y procesamiento con **PySpark**, siguiendo buenas prácticas del enfoque **Lakehouse**.

Todos los desafíos fueron ejecutados dentro de un único notebook en Databricks, separados lógicamente por secciones.

Desafío #1 — Generación Automática de Datos**

Se desarrolló un script en PySpark que genera automáticamente:

* Tabla de **Categorías** (departmentos analógicos)
* Tabla de **Niveles** (puestos de trabajo analógicos)
* Tabla de **Empleados** con asignación aleatoria

### Datos generados

* 5 categorías
* 3 niveles
* 100 empleados con:

  * ID
  * Nombre
  * Categoría asignada
  * Nivel asignado
  * Fecha de ingreso

Desafío #2 — Guardar los datos en CSV/Parquet y justificar el formato**

Los DataFrames generados se almacenan en la capa RAW usando un **Volume** configurado dentro del catalog.

### Elección del Formato: **Parquet**

Se seleccionó **Parquet** porque:

* Es **columnar**, ideal para analítica
* Comprime de forma eficiente
* Lectura/escritura optimizada
* Menor costo en almacenamiento
* Integración nativa con Databricks y Delta Lake

### Ruta de almacenamiento utilizada

```
/Volumes/prueba_globalmvm/default/prueba_globalmvm/raw
```

---

Desafío #3 — Proceso Batch hacia SQL/NoSQL/Datawarehouse/Datalake**

Los archivos Parquet generados en RAW son leídos y cargados como **Tablas Delta (Bronze)**.

### Tablas generadas

* `bronze_categorias`
* `bronze_niveles`
* `bronze_empleados`

---

Desafío #4 — Vista/Query/Reporte sobre el modelo de datos**

Se desarrolló una **vista analítica** que unifica la dimensión de categorías, niveles y los empleados.

Vista creada: `vw_empleados_full`

Incluye:

* ID de empleado
* Nombre
* Categoría y su descripción
* Nivel y su descripción
* Fecha de ingreso

Configuración del Volume en Databricks

Antes de ejecutar el proyecto, se configuró:

1. **Catalog:** prueba_globalmvm
2. **Schema:** default
3. **Volume:** prueba_globalmvm


Código fuente principal (Notebook)**

El notebook contiene el código dividido por secciones (Desafíos 1 a 4), usando PySpark para procesar los datos.

Puedes encontrar el notebook completo en este repositorio.

---

Cómo ejecutar este proyecto**

1. Crear un **Volume** en Databricks Community Edition
2. Crear un notebook nuevo y copiar el código
3. Configurar las rutas del volume (RAW)
4. Ejecutar cada sección por desafío
5. Validar la vista final desde el notebook creando una query en pyspark 

---
Autor: Ingeniero Alvaro Andres Solano Villegas

