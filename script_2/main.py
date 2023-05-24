import json
import os
import re
import lxml.etree as ET
#from create_teiheader import create_teiheader
#from grandes_divisions import grandes_divisions
#from paragraphes_divisions import paragraphes_divisions
#from prises_de_parole import prises_de_parole
from specifics_elements import SpecificsElements, process_specifics_elements
#from cas_particuliers import cas_particuliers
#from annexes import annexes
#from generate_id import generate_id 
from baliseur_data import BaliseurData, process_data  
from create_teiheader import CreateTEIHeader, process_header
from write_comment import WriteComment, process_comments

def main():
        
    # Chemin absolu du dossier contenant les fichiers à parcourir
    dossier_json = os.path.join(os.getcwd(), "json_data")
    dossier_xml = os.path.join(os.getcwd(), "xml_data")

    # Créer un pattern regex pour extraire le numéro de page du nom de fichier
    page_number_pattern = re.compile(r'^.*_p(\d+)\.json$')

    # Récupérer la liste des fichiers JSON dans le dossier
    fichiers = [f for f in os.listdir(dossier_json) if f.endswith('.json')]

    # Trier les fichiers JSON en fonction du numéro de page
    fichiers_json_tries = sorted(fichiers, key=lambda x: int(page_number_pattern.match(x).group(1)))

    # Parcourir les fichiers JSON triés
    for index, fichier_json in enumerate(fichiers_json_tries):
        fichier_json = os.path.join(dossier_json, fichier_json)


        # Création de l'élément racine et le squelette du XML
        root = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
        root.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "fr"

        filename = os.path.basename(fichier_json)
        xml_id = os.path.splitext(filename)[0]
        root.attrib["{http://www.w3.org/XML/1998/namespace}id"] = xml_id

        teiHeader = ET.SubElement(root, "teiHeader")
        text_tei = ET.SubElement(root, "text")
        body = ET.SubElement(text_tei, "body")
        page_number = filename.split("_p0")[1].split(".")[0]
        bp_element = ET.SubElement(body, "pb", attrib={"n": "{}".format(page_number)})


        with open(fichier_json, "r", encoding="utf-8") as f:
            # Lire le contenu du fichier JSON
            data = json.load(f)
            
            
            write_comment_instance = WriteComment()
            
            process_comments(write_comment_instance)
            
            baliseur_data_instance = BaliseurData()
            
            process_data(baliseur_data_instance)
        
            if index == 0:
                teiheader_instance = CreateTEIHeader()
                teiheader_instance.create_teiheader()
            
             # Création du fichier XML
    xml_tree = ET.ElementTree(root)
    final_output = filename.split("-")[0] + "_compiled" + ".xml"
    xml_filename = os.path.join(dossier_xml, final_output )

    with open(os.path.join(dossier_xml, xml_filename), "wb") as xml_file:
        root = xml_tree.getroot()

        instruction1 = ' href="agoda_schema.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"'
        model_instr1 = ET.ProcessingInstruction("xml-model", instruction1)
        root.addprevious(model_instr1)

        instruction2 = ' href="agoda_schema.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"'
        model_instr2 = ET.ProcessingInstruction("xml-model", instruction2)
        root.addprevious(model_instr2)

        xml_tree.write(xml_file, encoding="utf-8", xml_declaration=True, pretty_print=True)
        
        # la partie ci dessous du code n'est pas obligatoire. le code sert juste à enregistrer chaque fichier xml séparémment______
            
            
    # Chemin absolu du dossier contenant les fichiers à parcourir
    dossier_json = os.path.join(os.getcwd(), "json_data")
    dossier_xml = os.path.join(os.getcwd(), "xml_data")

    # Créer un pattern regex pour extraire le numéro de page du nom de fichier
    page_number_pattern = re.compile(r'^.*_p(\d+)\.json$')

    # Récupérer la liste des fichiers JSON dans le dossier
    fichiers = [f for f in os.listdir(dossier_json) if f.endswith('.json')]

    # Trier les fichiers JSON en fonction du numéro de page
    fichiers_json_tries = sorted(fichiers, key=lambda x: int(page_number_pattern.match(x).group(1)))

    # Parcourir les fichiers JSON triés
    for index, fichier_json in enumerate(fichiers_json_tries):
        fichier_json = os.path.join(dossier_json, fichier_json)


        # Création de l'élément racine et le squelette du XML
        root = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
        root.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "fr"

        filename = os.path.basename(fichier_json)
        xml_id = os.path.splitext(filename)[0]
        root.attrib["{http://www.w3.org/XML/1998/namespace}id"] = xml_id

        teiHeader = ET.SubElement(root, "teiHeader")
        text_tei = ET.SubElement(root, "text")
        body = ET.SubElement(text_tei, "body")
        page_number = filename.split("_p0")[1].split(".")[0]


        with open(fichier_json, "r", encoding="utf-8") as f:
            # Lire le contenu du fichier JSON
            data = json.load(f)

            # Ajouter le commentaire pour les fichiers suivants
            if index > 0:
                # Créer une instance de la classe WriteComment
                write_comment_instance = WriteComment()

                # Appel de la méthode process_comments en passant l'instance de write_comment_instance
                process_comments(write_comment_instance)

            if index == 0:
                teiheader_instance = CreateTEIHeader()
                teiheader_instance.create_teiheader()

            specifics_elements_instance = SpecificsElements()
            specifics_elements_instance.specifics_elements()
    
            baliseur_data_instance = BaliseurData()            
            process_data(baliseur_data_instance)

            # Création du fichier XML
            xml_tree = ET.ElementTree(root)
            output = xml_id + ".xml"
            xml_filename = os.path.join(dossier_xml, output)

    with open(xml_filename, "wb") as xml_file:
        instruction1 = ' href="agoda_schema.rng" type="application/xml" schematypens="http://purl.oclc.org/dsdl/schematron"'
        model_instr1 = ET.ProcessingInstruction("xml-model", instruction1)
        root.addprevious(model_instr1)

        instruction2 = ' href="agoda_schema.rng" type="application/xml" schematypens="http://relaxng.org/ns/structure/1.0"'
        model_instr2 = ET.ProcessingInstruction("xml-model", instruction2)
        root.addprevious(model_instr2)

        xml_tree.write(xml_file, encoding="utf-8", xml_declaration=True, pretty_print=True)



if __name__ == "__main__":
    main()