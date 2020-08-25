import re   
import glob
import os
from collections import Counter

dtsetInTxt ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/salida/Tika/convertidos/"
dtsetOutClean ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/salida/Tika/limpiados"
dtsetOutCleanCount ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/salida/Tika/limpiados/Count/"
dtsetOutReferences ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/salida/Tika/References/"
dirPath ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/"   
 


def fileSize(fileIn):
    os.chdir(dtsetInTxt)
    size=os.stat(fileIn).st_size
    return size

def wordsCount(contenido):
    totWwords=str(contenido).split()
    return len(totWwords)

def removewords(pcontenido):
    #print('Antes de hacer la limpieza {}'.format(wordsCount(pcontenido)))
    cleanContenido=[w for w in pcontenido if (w not in setRemovedWords)]
    #print("Tipo de objeto de cleancontenido {} ".format(type(cleanContenido)))
    strcleanContenido=' '.join(cleanContenido)
    strcleanContenido=[w for w in pcontenido if (len(w)>3 & len(w)<26) ]
    strcleanContenido=' '.join(cleanContenido)
    #print('Despues de hacer la limpieza {}'.format(strcleanContenido))
    return strcleanContenido

def cleanWordCount(contenido):
    contenido =re.sub('((f|ht)tp(s?)://)?(.*)[.][a-z]+(((\/.*(\/?)){1,}?)(.*([.].*)?))?',' ',contenido) # Eliminar las URL
    #contenido =re.sub('REFERENCES (\S|\w)+',' ',contenido) # Eliminar la bibliografia
    contenido =re.sub('[a-zA-Z0-9.?{}]+@\w+\.\w+.\w*',' ',contenido) # Eliminar los correos
    contenido =re.sub('\[[a-zA-Z0-9\,\. ]+\]',' ',contenido) # Eliminar cualquier contenido entre corchetes
    #contenido =re.sub('\([a-zA-Z0-9\,\.\- ]+\)',' ',contenido) # Eliminar cualquier contenido entre paréntesis
    contenido =re.sub('\(.+\)',' ',contenido) # Eliminar cualquier contenido entre paréntesis
    contenido =re.sub('((et al\.)|(i\.i\.d\.)|(i\.e\.)|\'|\’|\`)',' ',contenido) # Eliminar abreviaciones y apostrofes 
    contenido =re.sub('(á|à|ä)','a',contenido) # Reemplazar a acentuada
    contenido =re.sub('(é|è|ë)','e',contenido) # Reemplazar e acentuada
    contenido =re.sub('(í|ì|ï)','i',contenido) # Reemplazar i acentuada
    contenido =re.sub('(ó|ò|ö)','o',contenido) # Reemplazar o acentuada
    contenido =re.sub('(ú|ù|ü)','u',contenido) # Reemplazar u acentuada
    contenido =re.sub('(-|\u2212|\u2012|\u2013|\u2014|\u2015)\n',' ',contenido) # Reemplazar el guión para separar una palabra al fin de renglon
    contenido =re.sub('-|\u2212|\u2012|\u2013|\u2014|\u2015',' ',contenido) # Reemplazar el guión
    contenido =re.sub('[^a-zA-Z]',' ',contenido) # Eliminar caracteres que no sean: letra, número o vocales acentuadas
    #contenido =re.sub('[^((a-zA-Z){3,})]',' ',contenido) # Eliminar palabras o números de un caracter de longitud 
    contenido =re.sub('((\w*)?xyz(\w*)?)',' ',contenido) # Eliminar palabras con la cadena xyz
    contenido =re.sub('((\w*?)abc(\w*?))',' ',contenido) # Eliminar palabras con la cadena abc
    contenido =re.sub('((\w*?)shth(\w*?))',' ',contenido) # Eliminar palabras con la cadena shth    
    contenido =re.sub(' +',' ',contenido) # Eliminar espacios en blanco
    contenidoDuplicado =re.findall(r'(\w*?(\w)\2{2,}.*?)',contenido) #Elminar carecteres repetidos
    #|((\w*?)abc(\w*?))|((\w*)?xyz(\w*)?)    
    i=0
    longDuplicados=len(contenidoDuplicado)
    while i <longDuplicados:
         pattern= "\w*?" + contenidoDuplicado [i][0] +"\w*?"
         #print("Patrón {}".format(pattern))
         contenido=re.sub(pattern,' ',contenido) #Eliminar los patrones de caracteres repetidos
         i=i+1
    contenido=contenido.lower()
    contenido1=removewords(contenido.split())
    totWwords=contenido1.split()
    #print("Total de palabras {}".format(len(totWwords)))
    #print("Total de palabras después del pre-procesamiento: {}".format(totWwords))
    return len(totWwords),contenido1
    
def SumWords(pstrcontent):
    totWordDepurado = str(Counter(map(str, pstrcontent.split())))
    totWordDepurado =re.sub('\,','\n',totWordDepurado) 
    ##print("Total de palabras {}".format(totWordDepurado))
    #outputFile1= open(fileCountOut, 'w', encoding='UTF-8')
    #outputFile1.write(totWordDepurado)
    #outputFile1.close()

    #totWwords=contenido.split()
    ##print("Total de palabras {}".format(len(totWwords)))
    ##print("Total de palabras después del pre-procesamiento: {}".format(totWordDepurado))
    #return len(totWwords)
    #totWordDepurado = str(Counter(map(str, contenido.split())))
    #totWordDepurado =re.sub('\,','\n',totWordDepurado) # Eliminar espacios en blanco
    ##print("Total de palabras {}".format(totWordDepurado))
    #fileCountOut = dtsetOutCleanCount + pfile + ".txt"
    #outputFile1= open(fileCountOut, 'w', encoding='UTF-8')
    #outputFile1.write(totWordDepurado)
    #outputFile1.close()

    #totWwords=contenido.split()
    #print("Total de palabras {}".format(len(totWwords)))
    #print("Total de palabras después del pre-procesamiento: {}".format(totWordDepurado))
    return totWordDepurado


os.chdir(dirPath)
inputFileRemoveWords= open("BD_words_to_remove.csv", 'r', encoding='UTF-8')
bdRemovedWords = inputFileRemoveWords.read()
bdRemovedWords= bdRemovedWords.lower()
setRemovedWords= set(bdRemovedWords.split())
inputFileRemoveWords.close()
fileSummary = dirPath + "CleanSummary.csv"
#print("File summary {}".format(fileSummary))
outputFileSummary= open(fileSummary, 'w', encoding='UTF-8')
registro= "Archivo" + ";" + "Tamaño(K)" + ";" + "Cant Palabras Inicial" + ";" + "Cant Palabras depuradas"+ ";" +"Porc Limpieza"+ "\n"
outputFileSummary.write(registro)
os.chdir(dtsetInTxt)
vec_files=[f for f in glob.glob("*.txt")]
for file_i in vec_files:
    name_file,ext_file= file_i.split(".t")
    #tempFile= dtsetInTxt + file_i
    tmpSize=round(fileSize(file_i)/1024,2)
    #Lectura del archivo
    input_file = open(file_i, "r", encoding = 'utf-8')
    contenido = input_file.read()
    input_file.close()
    #Cuenta de palabras iniciales
    tmpWordsOri=wordsCount(contenido)
    pattReference=re.compile('\n *([0-9]*?\.)? *(References|REFERENCES|Bibliography|BIBLIOGRAPHY) *\n')
    if  pattReference.search(contenido,1):
    #if  re.search('\n *([0-9]?*\.?)? *(References|REFERENCES|Bibliography|BIBLIOGRAPHY) *\n',contenido):
        #print("Encontro cadena {}\n".format(pattReference.search(pdfContenido,1)))
        #Se divide el contenido del articulo por las referencias
        textSplited= pattReference.split(contenido,maxsplit=1)   
        contenido=textSplited[0]
        # Se define el patrón para identificar sí el artículo tiene un índice, para eliminarlo de las referencias
        pattIndex=re.compile('\n *([0-9]*?\.)? *(Index|INDEX) *\n')
        if  pattIndex.search(textSplited[3],1):
            referencesSplited= pattIndex.split(textSplited[3],maxsplit=1) 
            references=referencesSplited[0]
            #print('References: {}\n'.format(textSplited[0]))
        else:
            references=textSplited[3]
            # En caso de tener texto de referencia o bibliografía se escribe en un documento en un directorio aparte
        os.chdir(dtsetOutReferences)
        fileOut=  name_file +".txt"
        outputFileReferences= open(fileOut, 'w', encoding='UTF-8')
        outputFileReferences.write(references)
        outputFileReferences.close()
    #Cuenta de palabras despues de la limpieza
    tmpWordsEnd,contenidoLimpio=cleanWordCount(contenido)
    os.chdir(dtsetOutClean)
    fileOut=  name_file +".txt"
    outputFileTxt= open(fileOut, 'w', encoding='UTF-8')
    outputFileTxt.write(contenidoLimpio)
    outputFileTxt.close()
    # Escritura de las referencias del articulo en archivo independiente
    tmpPerClean=round((tmpWordsEnd/tmpWordsOri)*100,2)
    registro= name_file + ";" + str(tmpWordsOri) + ";" + str(tmpWordsEnd)+ ";" + str(tmpPerClean) + "\n"
    outputFileSummary.write(registro)
    os.chdir(dtsetOutCleanCount)
    fileOutCount=  name_file +".txt"
    outputFileCount= open(fileOutCount, 'w', encoding='UTF-8')
    outputFileCount.write(SumWords(contenidoLimpio))
    outputFileCount.close()
outputFileSummary.close()
