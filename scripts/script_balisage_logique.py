import re

# Ensemble des scripts à tester un à un

def add_structure(data):
    """
    Ajoute les éléments TEI "text" "body" et "back" en fonction des étiquettes "body", "text", "back", "text back"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"body", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<text><body>', data[i]['text_ocr']]) # laisser le texte ? Besoin du n° de page
            elif re.search(r"text", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</div></body></text>'])
            elif re.search(r"back", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div></body><back><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"\btext back\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join('</div></back></text>') # pas besoin d'inclure le texte car info sur l'imprimerie pas importante
            else:
                pass
    return data

def add_division(data):
    """
    Ajoute l'élément TEI "div" pouvant avoir un attribut @type auant pour valeur soit "part", soit "agenda",
    soit "erratum", soit "lists", soit "offices", soit "other-sitting", soit "contents", soit "voting",
    soit "rectification", soit "petition" en fonction des étiquettes "head part", "part", "agenda", "erratum", "lists",
    "offices", "other-sitting", "head contents", "voting1", "voting2" (etc.), "div-end" "rectification" et "petition"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bhead part\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="part"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"part", data[i]["comment"]): # problème car prend tous les "part" même les "head "part" !
                data[i]['text_ocr'] = "".join(['</div><div type="part">', data[i]['text_ocr']])
            elif re.search(r"agenda", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="agenda"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"erratum", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="erratum"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"lists", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="lists"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"offices", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="offices"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"other-sitting", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="other-sitting"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"\bhead contents\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<div type="other-sitting"><head>', data[i]['text_ocr'], '</head><list>'])
            elif re.search(r"\bvoting1\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<div><div type="voting"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"voting", data[i]["comment"]) and not  re.search(r"\bvoting1\b", data[i]["comment"]): # pas trouver de regex permettant d'exclure 1 (tout en permettant d'inclure 10)
                data[i]['text_ocr'] = "".join(['</div><div type="voting"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"rectification", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="rectification"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"petition", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="petition"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"div-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</div>'])
            else:
                pass
    return data

def add_structural_comment(data):
    """
    Ajoute les éléments TEI "note" pouvant avoir un attribut @type ayant pour valeur soit "opening", soit "closing",
    soit "voterslist", soit "numbersannounced" en fonction des étiquettes "opening", "closing", "note",
    "voterslist-beginning", "note-beginning" et "note-end"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"note[^-a-z]", data[i]["comment"]): # obligation de préciser a-z car étiquette "note head" existe ailleurs
                data[i]['text_ocr'] = "".join(['<note>', data[i]['text_ocr'], '</note>'])
            elif re.search(r"voterslist-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="voterslist"><desc>', data[i]['text_ocr'], '</desc>'])
            elif re.search(r"note-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="numbersannouced">', data[i]['text_ocr']])
            elif re.search(r"note-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</note>'])
            else:
                pass
    return data

def add_item(data):
    """
    Ajoute l'élément TEI "item" fonction des étiquettes "item" et "item list"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"item", data[i]["comment"]): #dupplique les item si pas de tiret pour item list
                data[i]['text_ocr'] = "".join(['<item>', data[i]['text_ocr'], '</item>'])
            elif re.search(r"\bitem list\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<item>', data[i]['text_ocr'], '</item></list>'])
            else:
                pass
    return data

def add_additional_title(data):
    """
    Ajoute les éléments TEI "desc" et "note" fonction des étiquettes "desc", "desc-office", "note head"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bdesc[^-]", data[i]["comment"]) or re.search(r"desc-office", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<desc>', data[i]['text_ocr'], '</desc>'])
            elif re.search(r"\bnote head\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note>', data[i]['text_ocr'], '</note></head>'])
            else:
                pass
    return data

def add_table(data):
    """
    Ajoute les éléments TEI "table" "row" et "celle" en fonction de l'étiquette "table"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"table", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<table><row><cell>', data[i]['text_ocr'], '</cell></row></table>'])
            else:
                pass
    return data





