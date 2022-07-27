import json, os, re
from lxml import etree
from script_compilation import compilation
from script_nettoyage import clean_xml
from script_metadonnees import var_metadata, build_teiheader

# Chemins vers les fichiers JSON et les fichiers XML
path = os.path.dirname(__file__)
path_to_json = os.path.join(os.path.abspath(os.path.join(path, os.pardir)), "json_data")
path_to_xml = os.path.join(os.path.abspath(os.path.join(path, os.pardir)), "xml_data")

beginning_elements = '<?xml version="1.0" encoding="UTF-8"?> <?xml-model ' \
                     'href="agoda_schema.rng" ' \
                     'type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"?> <?xml-model ' \
                     'href="agoda_schema.rng" ' \
                     'type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"?> <TEI ' \
                     'xmlns="http://www.tei-c.org/ns/1.0" xml:lang="fr"> '
end_elements = '</TEI>'

# Boucle permettant de lire chaque fichier JSON dont le nom finit par ".json" contenu dans un dossier dont le chemin
# est donné

for file_name in sorted([file for file in os.listdir(path_to_json) if file.endswith('.json')]):
    with open(os.path.join(path_to_json, file_name), encoding='utf-8') as json_file:
        data = json.load(json_file)

        # définir zwt
        for i in range(len(data)):
            if "comment" in data[i]:
                if re.search(r"body[^1]", data[i]["comment"]):
                    inc = 0
                    zwt = int(data[i]['text_ocr'].split()[-1])
                elif re.search(r"page-number", data[i]["comment"]) and not re.search(r"body", data[i]["comment"]):
                    data[i]['text_ocr'] = "".join(['<pb n="', str(zwt + inc), '"/>'])
                    inc += 1
                elif re.search(r"page-number-ref", data[i]["comment"]):
                    data[i]['text_ocr'] = "".join(['<ref target="#', str(zwt + inc), '"/>'])
                    inc += 1

        # Application de la fonction main
        compilation(data, zwt, inc)
        date_pub, meetings, meeting_sitting, date_sitting = var_metadata(data)
        header = build_teiheader(date_pub, meetings, meeting_sitting, date_sitting)

        # Création fichier .xml en mode écriture
        for i in range(len(data)):
            if "comment" in data[i]:
                if "body" in data[i]["comment"]:

                    name = json_file
                    file_name1 = re.split(r"_p", file_name)[0]
                    output_xml = open(str(os.path.join(path_to_xml, file_name1 + ".xml")), mode="w")

                    output_xml.write(beginning_elements)
                    output_xml.write(header)

            # Boucle permettant d'écrire dans le fichier .xml tous les text_ocr de data
            if "text_ocr" in data[i]:
                if len(data[i]["text_ocr"]) > 0:
                    output_xml.write(data[i]['text_ocr'])

                    # ajouter espace entre boxes
                    output_xml.write(" ")

        output_xml.write(end_elements)
output_xml.close()

# vérification du schéma TEI --> à gérer


# Nettoyage des fichiers xml

clean_xml(path_to_xml)

# ---------------------------------------------------------------------------------------------------------------------

# Ajout des xi:include dans le teiCorpus

# my_tree = etree.parse(path_to_xml + '/FR_3R_5L.xml')
# my_root = my_tree.getroot()
# namespace = 'http://www.w3.org/2001/XInclude'
#
#
# for file_name in sorted([file for file in os.listdir(path_to_xml) if file.endswith('.xml')]):
#     if len(str(file_name)) > 12:
#         #if not
#
#         # Ajout des xi:include en allant chercher les noms des fichiers xml
#         my_root.append(etree.Element(etree.QName(namespace, 'include'), nsmap={'xi':namespace},
#                                      attrib={'href':str(file_name)}))
#
# # Sauvegarde
# file_to_save = path_to_xml + '/FR_3R_5L.xml'
# my_tree.write(file_to_save, pretty_print=True, encoding='utf-8', xml_declaration=True)

# Vérification du respect du schéma relaxNG

# # Ouverture du fichier rng
# relaxng_doc = etree.parse(path_to_xml + '/agoda_schema.rng')
#
# # Association comme étant un schéma relaxNG
# relaxng = etree.RelaxNG(relaxng_doc)
#
# # Vérification des erreurs sur l'ensemble des fichiers XML
# relaxng.assertValid(my_tree)

# ---------------------------------------------------------------------------------------------------------------------
