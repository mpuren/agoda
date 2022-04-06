#%%
import os
from jiwer import cer 
import regex as re
import sys
print(os.path.dirname(sys.executable))
#%%
path_gt ="/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/ground-truth/1889-11-27-gt"
path_tess = "/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/tesseract-humanum/1889-11-27-tesseracthn"
path_abby = "/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/abby-humanum/1889-11-27-abbyhn"


date = [date.rsplit("-",1)[0] for date in os.listdir(path_gt)]

corpus_tess = []
corpus_gt = []
corpus_abby=[]
for d in date : 
    with open(os.path.join(path_tess,d+"-tesseracthn.txt")) as f:
        text_tess = f.read()
        corpus_tess.append(text_tess)
        f.close()
        
    with open(os.path.join(path_gt,d+"-gt.txt")) as f:
        text_tess = f.read()
        corpus_gt.append(text_tess)
        f.close()
    
    with open(os.path.join(path_abby,d+"-abbyyhn.txt")) as f:
        text_abby = f.read()
        corpus_abby.append(text_abby)
        f.close()
#%%
CER_1 = []
for i in range(0,len(corpus_gt)) : 
    
    error = cer(corpus_gt[i],corpus_tess[i])
    CER_1.append(error)

#%%
CER_abby = []
for i in range(0,len(corpus_gt)) : 
    
    error = cer(corpus_gt[i],corpus_abby[i])
    CER_abby.append(error)



#%%
corpus_gt_1 = [re.sub("\n"," ",text_gt) for text_gt in corpus_gt]
corpus_tess_1 = [re.sub("\n"," ",text_tess) for text_tess in corpus_tess]
CER_2 = []

for i in range(0,len(corpus_gt_1)) : 
    
    error = cer(corpus_gt_1[i],corpus_tess_1[i])
    CER_2.append(error)




#%%

text_gt = "1° Sur les faits de corruption, la protes- tation affirme que M. Borie aurait semé l'or à pleines mains et dépensé des sommes considérables pour payer des agents élec- toraux."
text_tess = "1° Sur les faits de corruption, la protes- tation affirme que M. Borie aurait semé l\'or à pleines mains et dépensé des sommes considérables pour payer des agents élec- toraux."
error = cer(text_gt,text_tess)
print(error)

#%%
print(set(re.findall("[^a-z\s0-9éèçàùê,;:!)(A-Z\'\.\-ô\?]+"," ".join(corpus_gt))))

#%%
block1 = []
block1 = []

for i , synt in enumerate(re.split("[\s]{5,}",corpus_abby[3])):
    if i%3 == 0:
        print(synt)
#%%
for i , synt in enumerate(re.split("\n",corpus_abby[3])):
    if i%3 == 0:
        print(synt)
    
#%%
lines = re.split("\n",corpus_abby[3])
lines = [re.sub("^[^a-zA-Z0-9éèçàùôîâ]{5,}","",line) for line in lines]
lines = [re.sub("[^a-zA-Z0-9éèçàùôîâ]{5,}$","",line) for line in lines]




#%%


l = [re.findall("^(.*)[\s]{5,}",c) for c in test]
