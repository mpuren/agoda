#%%
import os
from jiwer import cer 
import regex as re
path_gt ="/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/ground-truth/1889-11-27-gt"
path_tess = "/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/tesseract-humanum/1889-11-27-tesseracthn"
path_abby = "/home/atom/Bureau/Aurelien/epitech/agoda/eval-ocr/abby-humanum/1889-11-27-abbyhn"

with open(os.path.join(path_gt,"1889-11-27-2-gt.txt")) as f:
    text_gt = f.read()

with open(os.path.join(path_tess,"1889-11-27-2-tesseracthn.txt")) as f:
    text_tess = f.read()

with open(os.path.join(path_abby,"1889-11-27-2-abbyyhn.txt")) as f:
    text_abby = f.read()

#%%
date = [date.rsplit("-",1)[0] for date in os.listdir(path_gt)]

corpus_tess = []
for d in date : 
    with open(os.path.join(path_tess,d+"-tesseracthn.txt")) as f:
        text_tess = f.read()
        corpus_tess.append(text_tess)
        f.close()
#%%

error = cer(text_gt,text_tess)
print(error)


#%%


text_gt = re.sub("\n"," ",text_gt)
text_tess = re.sub("\n"," ",text_tess)
error = cer(text_gt,text_tess)
print(error)

#%%

text_gt = "1° Sur les faits de corruption, la protes- tation affirme que M. Borie aurait semé l'or à pleines mains et dépensé des sommes considérables pour payer des agents élec- toraux."
text_tess = "1° Sur les faits de corruption, la protes- tation affirme que M. Borie aurait semé l\'or à pleines mains et dépensé des sommes considérables pour payer des agents élec- toraux."
error = cer(text_gt,text_tess)
print(error)