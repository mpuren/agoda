import json
import re

#with open("/home/fanny/Documents/AGODA/Docs de travail AGODA Github/Transformations/JSON/FR_3R_5L_1889-11-26.json") as f:
    #x = f.read()
    #print(json.loads(x))

#with open("/home/fanny/Documents/AGODA/Docs de travail AGODA Github/Transformations/JSON/FR_3R_5L_1889-11-26_p178.json") as f:
    #data = json.load(f)

def add_utterance(data):
    """
    Ajoute l'élément TEI "u" pour chacun des paragraphes étiquetés "u", "u-beginning", "u-end"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"u | u$", data[i]["comment"]): # expression régulière : mettre des espaces pour ne pas que ça prenne en compte la lettre u dans un mot
                data[i]['text_ocr'] = "".join(["<u>", data[i]['text_ocr'], "</u>"])
            elif re.search(r"u-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(["<u>", data[i]['text_ocr']])
            elif re.search(r"u-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], "</u>"])
            else:
                pass
    return data

def add_comment(data):
    """
    Ajoute l'élément TEI "note" avec un attribut @type soit de valeur "comment" pour chacun des paragraphes étiquetés "comment",
    "comment-beginning", "comment-end", soit de valeur "result" pour chacun des paragraphes étiquetés "result"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"comment[^-]| comment$", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="comment">', data[i]['text_ocr'], '</note>'])
            elif re.search(r"comment-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="comment">', data[i]['text_ocr']])
            elif re.search(r"comment-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</note>'])
            elif re.search(r"result", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="result">', data[i]['text_ocr'], '</note>'])
            else:
                pass
    return data

def add_incident(data):
    """
    Ajoute l'élément TEI "incident" et "desc" pour chacun des paragraphes étiquetés "incident", "incident-beginning", "incident-end"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"incident[^-]| incident$", data[i]["comment"]):
                #if re.findall("\([^\)]+\)", data[i]["text_ocr"]):
                    #data[i]['text_ocr'] = "".join([re.sub(r'\(', r'<incident><desc>(', data[i]['text_ocr']), re.sub(r'\)', r')</desc></incident>', data[i]['text_ocr'])])
                    #data[i]['text_ocr'] = "".join(re.sub(r'\(', r'<incident><desc>(', data[i]['text_ocr']))
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('(', '<incident><desc>(').replace(')', ')</desc></incident>')
            elif re.search(r"incident-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('(', '<incident><desc>(')
            elif re.search(r"incident-end", data[i]["comment"]):
                data[i]['text_ocr'] = data[i]['text_ocr'].replace(')', ')</desc></incident>')
            else:
                pass
    return data

def add_quote(data):
    """
    Ajoute l'élément TEI "quote" pour chacun des paragraphes étiquetés "quote", "quote-beginning", "quote-end"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"quote[^-]| quote$", data[i]["comment"]):
                #data[i]['text_ocr'] = "".join(re.sub(r'«', r'<quote>«', data[i]['text_ocr']))
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('«', '<quote>«').replace('»', '»</quote>')
            elif re.search(r"quote-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('«', '<quote><seg>«')
            elif re.search(r"quote-end", data[i]["comment"]):
                data[i]['text_ocr'] = data[i]['text_ocr'].replace('»', '»</seg></quote>')
            else:
                pass
    return data