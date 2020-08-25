import tika
tika.initVM()
from tika import parser
import glob
import os
	
dtsetInPdf ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/datasets/papers-pdf/"
dtsetOutTika ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/salida/Tika/convertidos/"
dirPath ="C:/trabajo/2018-2019/Eafit/Procesamiento_Texto/"    

os.chdir(dtsetInPdf)
files="*.pdf"
vec_files=[f for f in glob.glob(files)]
for file_i in vec_files:
    #input_name_file ='0704.3504.pdf'
    name_file,ext_file= file_i.split(".p")
    input_file= dtsetInPdf + file_i
    os.chdir(dtsetInPdf)
    parsedPDF = parser.from_file(input_file)
    pdfContenido = parsedPDF["content"]
    pdfContenido = pdfContenido.replace('(\n +)+','\n')
    pdfContenido = pdfContenido.replace(' +',' ')
    os.chdir(dtsetOutTika)
    fileOut=  name_file +".txt"
    outputFileTxt= open(fileOut, 'w', encoding='UTF-8')
    outputFileTxt.write(pdfContenido)
    outputFileTxt.close()
    
    