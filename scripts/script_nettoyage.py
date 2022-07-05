import json
import re

#with open("/home/fanny/Documents/AGODA/Docs de travail AGODA Github/Transformations/pages_corrigées_et_annotées/pages_corrigees/FR_3R_5L_1889-11-26.json") as f:
    #x = f.read()
    #print(json.loads(x))

#with open("/home/fanny/Documents/AGODA/Docs de travail AGODA Github/Transformations/pages_corrigées_et_annotées/pages_corrigees/FR_3R_5L_1889-11-26_p178.json") as f:
    #data = json.load(f)

def nettoyage_saut_ligne(data):
    """
    Suppression des sauts de ligne et fusion des mots séparés par les sauts de ligne
    :return:
    """
    for i in range(len(data)):
        if "text_ocr" in data[i]:  # Si la valeur "comment" existe dans le dictionnaire actuel i
            data[i]["text_ocr"] = data[i]["text_ocr"].replace('-\n', "")
            data[i]["text_ocr"] = data[i]["text_ocr"].replace('\n', " ")

    return data