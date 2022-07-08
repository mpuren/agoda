# Supprimer les sauts de ligne et recoller les mots séparés
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

# Ne fonctionne pas lorsque le mot séparé est divisé entre deux boxes
# Ajouter une fonction pour la gestion des caractères spéciaux ? --> unidecode