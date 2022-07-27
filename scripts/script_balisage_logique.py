import re

# Ensemble des scripts à tester un à un


def add_structure(data):
    """
    Ajout des éléments TEI "text" "body" et "back" pour chaque boxe étiquetée "body", "text", "back", "text-back"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bbody\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<text><body>', data[i]['text_ocr']])
            elif re.search(r"body1", data[i]["comment"]):
                data[i]['text_ocr'] = "".join('<text><body><pb n="1"')
            elif re.search(r"text[^-]", data[i]["comment"]):
                data[i]['text_ocr'] = "".join('</div></body></text>')
                #mettre  le texte avant balise ? S'assurer que l'étiquette est sur la phrase "Imp. ..." qui est à supprimer
            elif re.search(r"[^-]back", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div></div></body><back>', data[i]['text_ocr']])
            elif re.search(r"text-back", data[i]["comment"]):
                data[i]['text_ocr'] = "".join('</div></back></text>')
                # pas besoin d'inclure le texte car info sur l'imprimerie pas importante, et texte pas océrisé
            else:
                pass
    return data

def add_division(data):
    """
    Ajout de l'élément TEI "div" pouvant avoir un attribut @type auant pour valeur soit "part", soit "agenda",
    soit "appendices", soit "erratum", soit "lists", soit "offices", soit "sitting", soit "other-sitting",
    soit "contents", soit "voting", soit "rectification", soit "petition" pour chaque boxe étiquetée "part", "part1",
    "agenda", "appendices", "part1-appendices", "erratum", "part1-erratum", "lists", "part1-lists", "offices",
    "part1-offices", "sitting", "other-sitting", "contents", "voting1", "voting", "div-end", "rectification",
    "petition" ou "part1-petition"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"\bpart\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="part">', data[i]['text_ocr']])
            elif re.search(r"part1[^-]", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<div type="part">', data[i]['text_ocr']])
            elif re.search(r"agenda", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="agenda"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"[^-]appendices", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="appendices"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"part1-appendices", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<div type="appendices"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"[^-]erratum", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="erratum"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"part1-erratum", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div type="erratum"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"[^-]lists", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="lists"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"part1-lists", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div type="lists"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"[^-]offices", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['</div><div type="offices"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"part1-offices", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<div type="offices"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"[^-]sitting", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div type="sitting">', data[i]['text_ocr']])
            elif re.search(r"other-sitting", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="other-sitting"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"contents", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div type="contents"><head>', data[i]['text_ocr'], '</head><list>'])
            elif re.search(r"voting1", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div><div type="voting"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"\bvoting\b", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="voting"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"div-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</div>'])
            elif re.search(r"rectification", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="rectification"><head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"[^-]petition", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['</div><div type="petition"><head><label>', data[i]['text_ocr'], '</label>'])
            elif re.search(r"part1-petition", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(
                    ['<div type="petition"><head><label>', data[i]['text_ocr'], '</label>'])
            else:
                pass
    return data

def add_structural_comment(data):
    """
    Ajout de l'élément TEI "note" pour chaque boxe étiquetée "note" et "note-end", et pouvant avoir aussi un attribut
    @type ayant pour valeur soit "voterslist", soit "numbersannounced" pour chaque boxe étiquetée "voterslist-beginning"
    ou "note-beginning"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"note[^-]", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note>', data[i]['text_ocr'], '</note>'])
            elif re.search(r"voterslist-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="voterslist"><desc>', data[i]['text_ocr'], '</desc>'])
            elif re.search(r"note-beginning", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note type="numbersannounced">', data[i]['text_ocr']])
            elif re.search(r"note-end", data[i]["comment"]):
                data[i]['text_ocr'] = "".join([data[i]['text_ocr'], '</note>'])
            else:
                pass
    return data

def add_item(data):
    """
    Ajout de l'élément TEI "item" pour chaque boxe étiquetée "item" ou "item-list"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"item[^-]", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<item>', data[i]['text_ocr'], '</item>'])
            elif re.search(r"item-list", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<item>', data[i]['text_ocr'], '</item></list>'])
            else:
                pass
    return data

def add_title(data):
    """
    Ajout des éléments TEI "head", "desc" et "note" pour chaque boxe étiquetée "head", "desc" ou "note-head"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"[^-]head", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<head>', data[i]['text_ocr'], '</head>'])
            elif re.search(r"desc", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<desc>', data[i]['text_ocr'], '</desc>'])
            elif re.search(r"note-head", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<note>', data[i]['text_ocr'], '</note></head>'])
            else:
                pass
    return data

def add_table(data):
    """
    Ajout des éléments TEI "table" "row" et "cell" pour chaque boxe étiquetée "table"
    :return:
    """
    for i in range(len(data)):
        if "comment" in data[i]:
            if re.search(r"table", data[i]["comment"]):
                data[i]['text_ocr'] = "".join(['<table><row><cell>', data[i]['text_ocr'], '</cell></row></table>'])
            else:
                pass
    return data





