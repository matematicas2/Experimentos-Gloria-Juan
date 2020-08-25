# Proyecto Integrador sobre Procesamiento de Texto

### Equipo de trabajo
Los integrantes del equipo son:
-  Camila Mejía Quintero
-  Sara Mira Puerta
-  Juan David Jurado Tapias
-  Alirio Rodriguez Mesías

# 1. Primera Entrega
## 1.1 Descripción
En este repositorio se encuentra disponibles los archivos con el código y la respectiva documentación que corresponde al Proyecto Integrador de la Maestría en Analítica y Ciencia de Datos de la cohorte 2019-1 en la  Universidad EAFIT.

## 1.2 Descripción del Problema
A partir de un conjunto muy grande (Big data) de documentos tipo texto (Para este proyecto se cuenta con 980 archivos, habiendo quitado un documento escrito en alemán) y los metadatos sobre dichos documentos, realizar un sistema/aplicación para la ingesta, almacenamiento, indexación, búsqueda, recuperación, navegación y visualización de documentos. 
Para implementar la solución se establecieron dos fases:

### 1.2.1 Fase 1: Pre-procesamiento
El objetivo es eliminar de cada archivo de texto la mayor cantidad de información que no agrega valor, depurando los datos que se preservan para la siguiente fase. La sección contiene los siguientes archivos ordenados:

*Directorio dataset*
Se encuentran los 980 archivos en formato txt que se obtienen después de realizar la fase de pre-procesamiento.

*Archivo en formato Jupyter Notebook: preprocessing_data.ipynb*
Contiene:
1. Importación de las librerías necesarias: numpy, re, os y collections. 
2. Llamado de los datos input (datasetIn) y se genera una carpeta de outputs "salida" para guardar los datos de texto de menor dimensión (datasetout).
3. Eliminación de la información innecesaria, para lo que se definieron las siguientes reglas:
     a. Eliminar URL o email.<br>
     b. Eliminar cualquier contenido entre paréntesis o corchetes<br>
     c. Eliminar abreviaciones ("et al.", "i.i.e.","i.e"), apóstrofes y guiones<br>
     d  Eliminar los caracteres que NO sean letras o vocales acentuadas<br>
     e. Eliminar palabras o números de un carácter de longitud 1<br>
     
4. Reconstrucción de los datos en formato .txt para su posterior tratamiento en procesamiento. 
5. Guardado de los nuevos datos en la carpeta de salida.
6. Reducción de la información se puede verificar en el archivo .xls generado. 

*Archivo:CleanSummary.csv*<br>
Para cada archivo de texto, se  estableció:
  a. Tamaño del archivo en KB
  b. El número de palabras al momento de iniciar el proceso, con el respectivo calculo de las palabras del vocabulario inicial
  c. Número de palabras depuradas o eliminadas.
  d. El vocabulario obtenido como resultado de la limpieza.
  Con estos datos se pudo calcular un indicador del porcentaje de limpieza de la fase de preprocesamiento, que en promedio es del 19%.
  
### 1.2.2 Fase 2: Procesamiento
El objetivo es eliminar de cada archivo de texto la mayor cantidad de información que no agrega valor, depurando los datos que se preservan para la construcción del BoW.  

*Archivo: processing_data.ipynb*
Para esto se implementaron las siguientes reglas de procesamiento:
1. Carga de las librerías necesarias para el procesamiento de datos: ntkl, pandas, sklearn, CountVectorizer , pickle. 
2. Formación de las reglas para aplicar la tokenización y eliminación de stopwords, entre otros elementos identificados. 
3. Formación de las reglas para aplicar las tecnicas de stemming y lemmatización. 
4. Lectura de los datos .txt guardados en la carpeta de salida, generada en el pre.procesamiento, se seleccionan los archivos en inglés (existe un documento en alemán). 
5. Implementación de las técnicas de tokenización, stemming y lemmatización a los artículos en inglés, 
6. Construcción del vocabulario.
7. Construcción de la bolsa de palabras (Bag of Words - BoW).

# 2. Segunda Entrega
## 2.1 Descripción de la Solución
Dado que la entrega anterior quedo con el reto de reducir el BoW, se implementaron algunos ajustes a la fase de pre-procesamiento, de forma que se pudiera depurar la información de del contenido de los  artículos, que es el insumo para la construcción del índice invertido, utilizando Meta(https://meta-toolkit.org/) que servirá para la evaluación  del modelo  y utilizando BM25, que sería la técnica implementada en esta segunda entrega. Finalmente se evaluará la sensibilidad del modelo.

### 2.1.1 Fase 1: Pre-procesamiento
*Archivo: simple_conversion_pdf_tika.py*<br>
Para evitar la presencia de caracteres en blanco en medio de palabras, se realizó una conversión de los artículos en formato PDF a formato txt utilizando una libería "Tika (https://tika.apache.org/)", logrando una evitar la pérdida de información.

*Archivo: cleaning_txt.py* <br>
Con los archivos en formato TXT (resultado de la conversión con Tika) se aplica las siguientes reglas:
     a. Eliminar el texto de las referencias bibliográficas, dado que no agrega información en la construcción del BoW.
     b. Eliminar URL o email.<br>
     c. Eliminar cualquier contenido entre paréntesis o corchetes<br>
     d. Eliminar abreviaciones ("et al.", "i.i.e.","i.e"), apóstrofes y guiones<br>
     f  Convertir los caracteres de vocales acentuadas a vocales sin acento<br>
     e.  Eliminar los guiones que se utilizan para dividir palabras (eliminando el guíon) o para componer (dos palabras unidas por guión y se cambia por un espacio en blanco) conceptos
     g. Eliminar palabras que tengan una longitud de caracteres menor a 3 o mayor a 26<br>

*Archivo: BD_words_to_remove.csv*
Contiene un archivo con 17.079 palabras que se identificaron que se pueden eliminar del BoW, dado que no son palabras reconocidas.

*Archivo: CleanSummary.csv*<br>
Para cada archivo de texto, se  estableció:
  a. Tamaño del archivo en KB
  b. El número de palabras al momento de iniciar el proceso, con el respectivo cálculo de las palabras del vocabulario inicial
  c. Número de palabras depuradas o eliminadas.
  d. Volcabulario obtenido como resultado de la limpieza.
  Con estos datos se pudo calcular un indicador del porcentaje de limpieza de la fase de preprocesamiento, que en promedio es del 42%.
  
### 2.1.2 Fase 2: Procesamiento
*Archivo: processing_data.ipynb*<br>
Adicional a las tareas de procesamiento realizadas en la segunda entrega, se complementaron con las siguientes taras:
  * Construcción del archivo cranfield.dat, que en cada registro contiene la información del texto de cada uno de los artículos convertidos con la librería Tika, archivo que se utilizará para la construcción de los índices invertidos utilizando la librería de Metapy.
  * Construcción del archivo "estructuraDatos.sav", que contiene la información del modelo entrenado contruido con la librería de Metapy.
  
  *Archivo: cranfield.toml*<br>
  Contiene los parámetros para que haciendo uso de Meta(https://meta-toolkit.org/) se pueda construir el archivo de los índices invertidos de los artículos, y que será utilizando como datos de referencia para probar el modelo de consulta o búsqueda.
  
  *Archivo: Query.ipynb*<br>
  * Carga los datos del modelo entrenado por Meta y almacenados en el archivo "estructuraDatos.sav".
  * Se ingresan la(s)palabra(s) de la consulta(query) que se utilizaría para establecer el ranquin de documentos que incluyen las palabras de la consulta.
  

# 3. Tercera Entrega
  
## 3.1 Descripción del Problema
A partir del análisis de los campos Título y Descripción de los metadatos de los artículos se deberán implementar dos esquemas de relacionamiento de los artículos una de clasificación (Modelo de Detección de Tópicos- LDA) y otra de agrupación (k-means), no supervisadas, para lo que se deberá utilizar SparkML (https://spark.apache.org/), realizando las tareas de limpieza, tokenización y reducción de la dimensionalidad.

## 3.1 Descripción de la Solución
Tal como se hizo para las primeras dos entredas, se establecera dos fases, tal como se describen a continuación:

### 2.1.1 Fase 1: Pre-procesamiento
En esta fase se implementaron las siguientes tareas:

*Archivo: modelado_topicos_articulos_pyspark.ipynb*
  * Se leyeron los datos de las columnas Título y Descripción del archivo de metadatos de los artículos y se combinaron un en nuevo campo, obteniendo 146.184 palabras. 
  * Se realizó la limpieza de la información, eliminando guiones, caracteres que no sean letras, elimanando stopwords y palabras con  longitud menor a tres carácteres finalmente se realizó el stemming (utilizando la función de Porter Stemmer de la librería NLTK), obteniendo 84.576 palabras y 5483 palabras del vocabulario.
 
 ### 2.1.2 Fase 2: Procesamiento
 Sobre el mismo archivo se implementó:
 
 *Archivo: modelado_topicos_articulos_pyspark.ipynb*
  * Construcción de la matriz dispersa de documentos utilizando la función CountVectorizer de SparkML, en el que se incluyó el parámetro minDF=3, con el que se seleccionarían las palabras que cómo mínimo aparezcan en tres documentos, obteniendo 2252 palabras en el vocabulario de la matríz y logrando na reducción del 59% de la dimensionalidad de los elementos a ser procesados.
  * Construcción del modelo de tópicos, definiendo como parámetros 20 categorías de Tópicos.
  * Construcción del modelo de clustering, definiendo como parámetros K=20 grupos.
  
  *Archivo:clustertable_articles.csv*
  Contiene el listado de los 980 artículos con el número del cluster asignado.
  
   *Archivo: ldaresults_articles.csv*
  Contiene el listado de los 980 artículos con el número del topico asignado.
  
  *Archivo: TerceraEntrega.ipynb*
  Dado que los resultados de la clusterización realizada con Pyspark no suministró una adecuada dispersión de los documentos entre las diferentes clusters, se programó nuevamente el algoritmo de clusterización utilizando la librería de Sklearn (https://scikit-learn.org/), que se combinaron con los tópicos asignados a cada artículo (ldaresults_articles.csv) y el resultado final se presentan un imágenes de nubes de palabras que están disponibles para consulta en el enlace:
  https://app.powerbi.com/view?r=eyJrIjoiMTdjZTk1MWItNjkyMi00OGRjLWE1ZmQtNjcyYzdjODUyNjdlIiwidCI6IjU5YzM4MTgwLThlNmUtNDc2Zi1iNzk3LWZmNjA4NGU0MTkxZSIsImMiOjR9
  
