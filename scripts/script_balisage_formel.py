import json
import re

#with open("/home/fanny/Documents/AGODA/Docs de travail AGODA Github/Transformations/JSON/FR_3R_5L_1889-11-26.json") as f:
    #x = f.read()
    #print(json.loads(x))

#with open("/home/fanny/Documents/AGODA/Docs de travail AGODA Github/Transformations/JSON/FR_3R_5L_1889-11-26_p178.json") as f:
    #data = json.load(f)


def add_seg(data):
    """
    Ajoute l'élément TEI "seg" pour chacun des paragraphes étiquetés "seg", "seg-beginning", "seg-end"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"seg[^-]|seg$", data[i]["comment"]) and not re.search(r"quote-beginning|quote-end", data[i]["comment"]): # expression régulière : seg pouvant être suivi de n'importe quel caractère sauf le "-", et seg  en fin de ligne
                data[i]['text_ocr'] = "".join(["<seg>", data[i]['text_ocr'], "</seg>"])
            elif re.search(r"seg-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(["<seg>", data[i]['text_ocr']])
            elif re.search(r"seg-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], "</seg>"])
            else:
                pass
    return data

def add_signed(data):
    """
    Ajoute l'élément TEI "signed" pour chaque élément étiqueté "signed"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"signed", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(["<signed>", data[i]['text_ocr'], "</signed>"])
            else:
                pass
    return data

# NE FONCTIONNE PAS : A REPRENDRE
def add_page_beginning(data):
    """
    Ajoute l'élément TEI "pb" lorsqu'il y a l'étiquette "page-number" ou "page-number-ref", "seg-end"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"page-number[^-]|page-number$", data[i]["comment"]): # expression régulière : page-number pouvant être suivi de n'importe quel caractère sauf le "-", et page-number  en fin de ligne
                data[i]['text_ocr'] = "".join(['<pb n="', data[i]['text_ocr'], '"/>'])
            elif re.search(r"page-number-ref", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<ref target="#', data[i]['text_ocr'], '"/>'])
            else:
                pass
    return data