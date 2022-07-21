# Supprimer les sauts de ligne et recoller les mots séparés
def nettoyage_saut_ligne(data):
    """
    Suppression des sauts de ligne (\n) et fusion des mots séparés par les sauts de ligne
    :return:
    """
    for i in range(len(data)):
        if "text_ocr" in data[i]:  # Si la valeur "text_ocr" existe dans le dictionnaire actuel i
            data[i]["text_ocr"] = data[i]["text_ocr"].replace('-\n', "")
            data[i]["text_ocr"] = data[i]["text_ocr"].replace('\n', " ")
            # data[i]['text_ocr'] = "".join([data[i]['text_ocr'], ' '])
            # Permet d'ajouter un espace à chaque fin de boxe, mais ne fonctionne pas dans le pipeline général
    return data



# Ne fonctionne pas lorsque le mot séparé est divisé entre deux boxes
# Ajouter un espace entre les boxes
# Ajouter une fonction pour la gestion des caractères spéciaux ? --> unidecode