#%%
import os
import numpy as np
import pandas as pd
os.chdir("/home/atom/Bureau/Aurelien/epitech/Pyllica")
from pyllicalabspdf import *
path_to_pdf  = "/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/documents_test/pdf"
os.chdir(path_to_pdf)

#pdfpress(url="https://gallica.bnf.fr/ark:/12148/bpt6k6428518m/date", title="debat", year=1893, month=2, day=16, item=3, rate=7)

for title in os.listdir("/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/documents_test/docs_used_gt/img_random") :
    print(title)
    year = int(title.split("_")[0])
    month = int(title.split("_")[1])
    day = int(title.split("_")[2])
    pdfpress("https://gallica.bnf.fr/ark:/12148/cb328020951/date","debat1",year=year,month=month,day=day,item=1,rate=1)
#    url = "https://gallica.bnf.fr/ark:/12148/bpt6k6428518m/date"+title.replace("_","").strip(".jpg")+".pdf"


#%%


#%%
import numpy as np
import pandas as pd
pdfWriter = PdfFileWriter()
df = pd.DataFrame({"year":[],"month" : [],"day":[],"page":[]})
for title in os.listdir("/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/documents_test/docs_used_gt/img_random") :
    
    print(title)
    
    year = title.split("_")[0]
    month = title.split("_")[1]
    day = title.split("_")[2]
    page = re.split("\_|\.",title)[-2]
    pdf_file_path = os.path.join(path_to_pdf,"debat1_"+year+month+day+".pdf")
    try : 
        pdf = PdfFileReader(pdf_file_path)
        pdfWriter.addPage(pdf.getPage(1+int(page)))
        df = df.append({"year":int(year),"month":int(month),"day":int(day),"page":int(page)},ignore_index=True)
    except : 
        pass
with open(os.path.join("/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/documents_test/docs_used_gt/","all_pdf.pdf"),"wb") as f :
    pdfWriter.write(f)
    f.close()
df.to_csv("/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/documents_test/docs_used_gt/list_doc_csv.csv")
