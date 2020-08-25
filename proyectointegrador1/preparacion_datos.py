# Preparación de Datos
# Autores: Camila Mejía
#          Sara Mira
#          Juan Jurado
#          Alirio Rodriguez
#Fecha:     12/Abr/2019

import os
import re


#Definiendo variables del entorno de trabajo
dataset ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/papers-txt"
datasetSalida ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/papers_salida"
dirPath ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto"
os.chdir(dirPath)
#allPapers =os.listdir(dataset)
def limpiarContenido(file):
    
    input_file = open(file, "r", encoding='UTF-8')
    texto=input_file.read()
    texto =re.sub('(f|ht)tp(s?)://(.*)[.][a-z]+',' ',texto)
    texto =re.sub('[A-Za-z0-9._%+-]+@(a-z|A-Z|0-9)+\.[A-Z]{2,}\b',' ',texto)
    texto =re.sub('[^A-Za-z0-9.,_%+-\(\)\[\]\´\'\`]',' ',texto)
    texto =re.sub('\[(0-9)+\]',' ',texto)    


    input_file = open("C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/papers-txt/0704.3504.txt", "r", encoding='UTF-8')
texto=input_file.read()
print(texto)
