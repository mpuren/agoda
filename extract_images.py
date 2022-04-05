from typing import List, TextIO, Dict
from urllib import request, error
import os
from bs4 import BeautifulSoup
import re
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse
import re
import os
import numpy as np
path_data = r'C:\Users\Aurelien Pellet\Desktop\Aurelien\epitech\agoda'
revue = "cb328020951"

def load_notices(start_year: int, end_year: int) -> None:
    print("loading notices")
    for year in range(start_year, end_year+1):
        xml_notices = f"https://gallica.bnf.fr/services/Issues?ark=ark:/12148/{revue}/date&date={year}"
        print(xml_notices)
        if not os.path.isfile(os.path.join(path_data, "notices", f"notices_{year}.xml")):

            try:
                distant_file = request.urlopen(xml_notices)
                xml_document: str = distant_file.read()
                file_notices = open(os.path.join(path_data, "notices", f"notices_{year}.xml"), "wb")
                file_notices.write(xml_document)
            except error.HTTPError as err:
                print(err)
        else:
            print("Année déjà traitée")
    print("notices loaded")
    
    
def load_xmlfiles() -> List[str]:
    print("building list of files")
    notices: List[str] = list()
    dates: List[str] = list()
    for notices_file_adr in os.listdir(os.path.join(path_data, "notices")):
        notices_file: TextIO = open(os.path.join(path_data, "notices", notices_file_adr), "r", encoding="utf-8")
        content_notices: str = notices_file.read()
        notices_file.close()
        notices += re.findall("ark=\"[a-z0-9]+\"", content_notices)
        dates += re.findall(">[0-9]{2} [a-zA-Zéû]+ [0-9]{4}",content_notices)
    notices = [notice[5:-1] for notice in notices]
    print("list built")
    return notices,dates

def jpg(identifier, title="titre", firstpage=1, lastpage=1):
    lastpage+=1
    listpage = range(firstpage, lastpage)
    for page in listpage:
        if not os.path.isfile(os.path.join(path_data, "images",title+"_"+str(page)+".jpg")):
            try :
                jpgfile = title + "_" + str(page) + ".jpg"
                url = 'http://gallica.bnf.fr/iiif/ark:' + identifier + '/f' + str(page) + '/full/3000/0/native.jpg'
                urllib.request.urlretrieve(url, jpgfile)
            except error.HTTPError as err:
                print(err)
                break
        else :print("page déjà traitée")
    return url , jpgfile



#%%
if __name__ == "__main__":
    load_notices(1888, 1893)
    all_notices,all_dates = load_xmlfiles()
    
    
    df=pd.DataFrame({"ark":all_notices,"date":all_dates})
    df.loc[:,["jour","moi","year"]]=df.date.str.strip(">").str.split(" ").apply(lambda x: pd.Series(x)).values
    #df.loc[:,"year"]=df['year'].apply(lambda x:int(x))
    df.loc[:,"moi"]=df["moi"].replace(["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"]
                                  ,["01","02","03","04","05","06","07","08","09","10","11","12"])
    df.loc[:,"date_seance"] = [y+"_"+m+"_"+ d for y , m , d in zip(df.year,df.moi,df.jour)]
    
    df.loc[:,"date_seance_int"] = df.date_seance.apply(lambda x : int(x.replace("_","")))
    df = df.loc[(df.date_seance_int>=18891112)&(df.date_seance_int<=18931014)].reset_index()
#%%

def jpg(identifier, title="titre", firstpage=1, lastpage=1):
    stop = 0    
    while stop==0:
        num_page = np.random.randint(1, 50, size=1, dtype=int)[0]
        if not os.path.isfile(title + "_" + str(num_page) + ".jpg"):
            try :
                jpgfile = title + "_" + str(num_page) + ".jpg"
                url = 'http://gallica.bnf.fr/iiif/ark:' + identifier + '/f' + str(num_page) + '/full/3000/0/native.jpg'
                urllib.request.urlretrieve(url, jpgfile)
                stop = 1
            except error.HTTPError as err:
                print(err)
                continue
        else : print("page déjà sélectionnée")
nb_pages = 0
while nb_pages <= 100 : 
    num_doc =  np.random.randint(df.shape[0], size=1, dtype=int)[0]
    ark = df.ark[num_doc]
    title = os.path.join(path_data,"img_random",f"{df.date_seance[num_doc]}")
    jpg(identifier="/12148/"+ark+"/",title=title)
    nb_pages += 1
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    