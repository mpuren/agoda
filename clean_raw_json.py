import os 
import re
from spellchecker import SpellChecker

path_to_agoda = "/home/atom/Bureau/Aurelien/epitech/agoda"
path_to_json = os.path.join(path_to_agoda,"json_data_raw")
# turn off loading a built language dictionary, case sensitive on (if desired)
spell = SpellChecker(language=None, case_sensitive=True)


f = open(os.path.join(path_to_agoda,"dic_etiquettes.txt"))
etiquettes = f.read().split(",")

spell.word_frequency.load_words(etiquettes)

#print(spell.correction("sef"))
import json
for i , file_name in enumerate(sorted([file for file in os.listdir(path_to_json) if file.endswith('.json')])):
	#print(i,file_name)
    with open(os.path.join(path_to_json, file_name), encoding='utf-8') as json_file : 
        data = json.load(json_file)


    for  i , entry in enumerate(data) : 
        if "comment" in entry :
            if len(entry["comment"]) > 0 :
                comment = entry["comment"].split()
                etiquettes_corrected = [spell.correction(word) for word in comment]
                comment_corrected = " ".join(etiquettes_corrected)
				
                if file_name == "zz_27111889_jo_debats_0001.json" :
                    if entry["comment"] == comment_corrected :
                        print(entry["comment"],"|||",comment_corrected)
                    
    date = re.search("[0-9]{8}",file_name)[0]
    yyyy = date[-4:]
    mm = date[2:4]
    dd = date[0:2]
    page = re.findall("([0-9]{4}).json",file_name)[0]
    new_file_name = "FR_3R_5L_"+yyyy+"-"+mm+"-"+dd+"_p"+page+".json"
    print(new_file_name)
   					   
    
    with open(os.path.join(path_to_agoda,"json_data_clean",new_file_name), 'w',encoding="utf-8")as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
  

    #%%
f = open(os.path.join(path_to_agoda,"json_data_clean","FR_3R_5L_1889-11-27_p0012.json"), 'r',encoding="utf-8")
text = f.read().split("\n")
f.close()

f = open(os.path.join("/home/atom/Bureau/Aurelien/epitech/agoda/json_data","FR_3R_5L_1889-11-26_p0186.json"), 'r')
text2 = f.read().split("\n")
#%%
for i , line in enumerate(text) :
    if text[i] != text2[i] :
        print(i)
        print(text[i],"|||||||||||-",text2[i])
#%%
f = open(os.path.join(path_to_agoda,"json_data_clean","FR_3R_5L_1889-11-27_p0001.json"), 'r',encoding="latin1")
text = f.read().split("\n")
f.close()

f = open(os.path.join("/home/atom/Bureau/Aurelien/epitech/agoda/json_data","FR_3R_5L_1889-11-26_p0175.json"), 'r',encoding="latin1")
text2 = f.read().split("\n")



