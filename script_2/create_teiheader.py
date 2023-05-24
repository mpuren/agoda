class CreateTEIHeader:
    def create_teiheader(self):
        # Code de la méthode create_teiheader
        print("Méthode create_teiheader appelée")

def process_header(create_teiheader_instance):
    # Appel de la méthode create_teiheader de l'instance de CreateTEIHeader
    create_teiheader_instance.create_teiheader()

# Création d'une instance de CreateTEIHeader
teiheader_instance = CreateTEIHeader()

# Appel de la fonction process_header en passant l'instance de CreateTEIHeader
process_header(teiheader_instance)

# Ajout des éléments de la TeiHeader ________________________________________________________________________________

def create_teiheader(data):
    

# fileDesc______________________________________________________________________

    teiHeader = ET.SubElement(root, "teiHeader")
    fileDesc = ET.SubElement(teiHeader , "fileDesc")

    # Titre______________________________________________________________________
    
    global titleStmt
    titleStmt = ET.SubElement(fileDesc , "titleStmt")
    title_fr = ET.SubElement(titleStmt, "title", type ="main")
    title_fr.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "fr"
    title_en = ET.SubElement(titleStmt, "title", type ="main")
    title_en.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "en"

    title_sub_fr = ET.SubElement(titleStmt, "title", type ="sub")
    title_sub_fr.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "fr"
    title_sub_en = ET.SubElement(titleStmt, "title", type ="sub")
    title_sub_en.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "en"         

    # meeting____________________________________________________

        # voir partie Meeting plus bas

    # respStmt________________________________________________________

    personnes = {"Brunel TCHEKELI": "id-hal", "Marie PUREN": "id-hal", "Pierre VERNUS": "id-hal"}

    # Boucle pour créer respStmt pour chaque personne
    for personne, identifiant in personnes.items():
        respStmt = ET.SubElement(titleStmt , "respStmt")
        persName = ET.SubElement(respStmt , "persName")
        forename = ET.SubElement(persName , "forename")
        surname = ET.SubElement(persName , "surname")

        # Définir l'attribut xml:id pour l'élément ptr
        #ptr = ET.SubElement(persName, "ptr")
        #ptr.attrib["type"] = identifiant

         # Définir le texte pour forename et surname
        forename.text = personne.split()[0]  # Utiliser le prénom de la personne
        surname.text = personne.split()[1]  # Utiliser le nom de famille de la personne

        # Vérifier si la personne est "Marie PUREN"
        if personne == "Brunel TCHEKELI":
            # Ajouter l'élément ptr avec les attributs appropriés
            resp_fr = ET.SubElement(respStmt, "resp", {"{http://www.w3.org/XML/1998/namespace}lang": "fr"})                        
            resp_fr.text = "Transformation du JSON en XML-TEI et ajout automatique des balises TEI par des scripts Python"
            resp_en = ET.SubElement(respStmt, "resp", {"{http://www.w3.org/XML/1998/namespace}lang": "en"})
            resp_en.text = "Transformation from JSON to XML-TEI and automatic addition of TEI tags by Python scripts"

        # Vérifier si la personne est "Marie PUREN"
        if personne == "Marie PUREN":
            # Ajouter l'élément ptr avec les attributs appropriés
            ptr = ET.SubElement(persName, "ptr", type= identifiant, target=personne)
            ptr = ET.SubElement(persName, "ptr", type="orcid", target="0000-0001-5452-3913")
            resp_fr = ET.SubElement(respStmt, "resp", {"{http://www.w3.org/XML/1998/namespace}lang": "fr"})                        
            resp_fr.text = "TEI Header"
            resp_en = ET.SubElement(respStmt, "resp", {"{http://www.w3.org/XML/1998/namespace}lang": "en"})
            resp_en.text = "TEI Header"

        else:
            # Ajouter l'élément ptr avec les attributs standard
            ptr = ET.SubElement(persName, "ptr", type=identifiant, target=personne)


    # Création de l'élément funder
    funder = ET.SubElement(titleStmt, "funder")
    # Création des éléments orgName avec les attributs xml:lang correspondants
    orgName_fr = ET.SubElement(funder, "orgName", {"{http://www.w3.org/XML/1998/namespace}lang": "fr"})
    orgName_fr.text = "Bibliothèque nationale de France"
    orgName_en = ET.SubElement(funder, "orgName", {"{http://www.w3.org/XML/1998/namespace}lang": "en"})
    orgName_en.text = "National Library of France"

    # Ajout de extent avec les informations sur le nombre de page, le nombre de mots etc (plus tard)                      

    extent= ET.SubElement(fileDesc, "extent")
    measure_pages_fr = ET.SubElement(extent, "measure",  {"quantity": "counts", "{http://www.w3.org/XML/1998/namespace}lang": "fr"})
    measure_pages_fr.text = "pages"
    measure_pages_en = ET.SubElement(extent, "measure",  {"quantity": "counts", "{http://www.w3.org/XML/1998/namespace}lang": "en"})
    measure_pages_en.text = "pages"

    measure_utterances_sl = ET.SubElement(extent, "measure", {"quantity": "counts", "{http://www.w3.org/XML/1998/namespace}lang": "sl"})
    measure_utterances_sl.text = "énoncés"
    measure_utterances_en = ET.SubElement(extent, "measure",  {"quantity": "counts", "{http://www.w3.org/XML/1998/namespace}lang": "en"})
    measure_utterances_en.text = "utterances"

    measure_words_sl = ET.SubElement(extent, "measure",  {"quantity": "counts", "{http://www.w3.org/XML/1998/namespace}lang": "sl"})
    measure_words_sl.text = "mots"
    measure_words_en = ET.SubElement(extent, "measure", {"quantity": "counts", "{http://www.w3.org/XML/1998/namespace}lang": "en"})
    measure_words_en.text = "words"

    global publicationStmt
    publicationStmt = ET.SubElement(fileDesc , "publicationStmt")
    publisher = ET.SubElement(publicationStmt, "publisher")
    publisher.text = "AGODA"
    authority = ET.SubElement(publicationStmt, "authority")
    authority.text = "Bnf Datalab"
    availability = ET.SubElement(publicationStmt, "availability", status="restricted", n="cc-by")
    licence = ET.SubElement(availability, "licence", target="https://creativecommons.org/licenses/by/4.0/")

    # ajout de la date _________________________________

    now = datetime.datetime.now()
    date = ET.SubElement(publicationStmt, "date", {"when": now.strftime("%Y-%m-%d")})
    # date générée automatiquement en utilisant la méthode now() de la classe datetime.datetime et
    # le format est défini avec strftime() en utilisant le modèle "AAAA-MM-JJ"

     # ajout de la dsourceDesc _________________________________
    sourceDesc = ET.SubElement(fileDesc , "sourceDesc")
    biblFull = ET.SubElement(sourceDesc, "biblFull")
    titleStmt_sDc = ET.SubElement(biblFull, "titleStmt")
    title_sDc = ET.SubElement(titleStmt_sDc, "title")
    title_sDc.text = "A définir"
    
    global publicationStmt_sDc
    publicationStmt_sDc = ET.SubElement(biblFull , "publicationStmt")
    publisher_sDc_fr = ET.SubElement(publicationStmt_sDc, "publisher", {"{http://www.w3.org/XML/1998/namespace}lang": "fr"})
    publisher_sDc_fr.text = " "

    publisher_sDc_en = ET.SubElement(publicationStmt_sDc, "publisher", {"{http://www.w3.org/XML/1998/namespace}lang": "en"})
    publisher_sDc_en.text = " "

    pubPlace_sDc = ET.SubElement(publicationStmt_sDc, "pubPlace")
    location_sDc = ET.SubElement(pubPlace_sDc, "location")
    country_sDc = ET.SubElement(location_sDc, "country", key="FR")
    settlement_sDc = ET.SubElement(location_sDc, "settlement", type="city") # que mettre ? est-ce "Paris" pour tout ?
    settlement_sDc.text = " "
    # date____________(voir partie date-pub plus bas: la date est récupérée dans chaque fichier et est ajouté ici)

    distributor_sDc = ET.SubElement(publicationStmt_sDc, "distributor", facs="https://gallica.bnf.fr/ark:/12148/bpt6k477552f/f1")
    distributor_sDc.text = "Source gallica.bnf.fr / Bibliothèque nationale de France"
    availability_sDc = ET.SubElement(publicationStmt_sDc, "availability")
    licence_sDc = ET.SubElement(availability_sDc, "licence", {"target":"https://gallica.bnf.fr/edit/und/conditions-dutilisation-des-contenus-de-gallica", "{http://www.w3.org/XML/1998/namespace}lang": "fr"})
    licence_sDc_p1 = ET.SubElement(licence_sDc, "p" )
    licence_sDc_p1.text = "Les contenus accessibles sur le site Gallica sont pour la plupart des reproductions numériques d'œuvres tombées dans le domaine public provenant des collections de la BnF."
    licence_sDc_p2 = ET.SubElement(licence_sDc, "p" )
    licence_sDc_p2.text = "Ces contenus sont considérés, en vertu du code des relations entre le public et l’administration, comme étant des informations publiques et leur réutilisation s'inscrit dans le cadre des dispositions prévues aux articles L. 321-1 à L. 327-1 de ce code."

    seriesStmt = ET.SubElement(biblFull, "seriesStmt")
    title_series = ET.SubElement(seriesStmt, "title" )
    title_series.text = "Journal Officiel de la République française"
    biblScope1 = ET.SubElement(seriesStmt, "biblScope")
    biblScope1.text = "Débats parlementaires"
    biblScope2 = ET.SubElement(seriesStmt, "biblScope")
    biblScope2.text = "Chambre des députés"
    idno = ET.SubElement(seriesStmt, "idno" , type="ISSN")
    idno.text = "1270-5942"



# EncodingDesc ______________________________________________________________________

    encodingDesc = ET.SubElement(teiHeader , "encodingDesc")

# profileDesc ______________________________________________________________________
    profileDesc = ET.SubElement(teiHeader , "profileDesc")
    langUsage = ET.SubElement(profileDesc, "langUsage")
    language = ET.SubElement(langUsage, "language", ident="fr")
    language.text = "Français"
    global setting_desc
    settingDesc = ET.SubElement(profileDesc, "settingDesc")
    setting_desc = ET.SubElement(settingDesc, "setting")
    name_desc1 = ET.SubElement(setting_desc, "name", type="")    
    name_desc2 = ET.SubElement(setting_desc, "name", type="")
    name_desc3 = ET.SubElement(setting_desc, "name", type="")
   # date_desc = voir partie date plus bas


# Ajout de la description du projet--------------------------------------------------------
    projetDesc = ET.SubElement(encodingDesc, "projetDesc")
    p1 = ET.SubElement(projetDesc, "p")
    p1.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "fr" # A cause des crochets et trop de "", écrire l'attibut de cette maniène pose moins de problème.
    ref1 = ET.SubElement(p1, "ref", target = "https://www.bnf.fr/fr/les-projets-de-recherche#bnf-agoda")
    ref1.text = "AGODA "           
    ref1.tail = '''est un projet qui a pour objectif de rendre disponible au format XML-TEI les textes de débats parlementaires à la Chambre des députés au cours de la Troisième République, suivant l\''''
    ref2 = ET.SubElement(p1, "ref", target ="https://github.com/mpuren/agoda/blob/ODD/documentation/agoda_odd.xml")
    ref2.text = "ODD "
    ref2.tail = "défini pour le projet à partir des "
    ref3 = ET.SubElement(p1, "ref", target = "https://github.com/clarin-eric/parla-clarin")
    ref3.text =  "recommandations produites par Parla-CLARIN. "
    ref3.tail = ''' Dans une optique de preuve de concept, la phase 1 du projet AGODA se concentre plus particulièrement
    sur la 5ème législature (1889-1893). Les textes encodés sont d'abord extraits des documents numérisés disponibles sur '''
    ref4 = ET.SubElement(p1, "ref", target = "https://gallica.bnf.fr/ark:/12148/cb328020951/date.item")
    ref4.text = "Gallica,"
    ref4.tail = ''' la bibliothèque numérique de la Biliothèque nationale de France, puis ils sont convertis 
    en XML-TEI au moyen de scripts Python.'''

                    # Version anglaise ______________________________________________________________________________

    p2 = ET.SubElement(projetDesc, "p")
    p2.attrib["{http://www.w3.org/XML/1998/namespace}lang"] = "en"
    ref1_2 = ET.SubElement(p2, "ref", target = "https://www.bnf.fr/fr/les-projets-de-recherche#bnf-agoda")
    ref1_2.text = "AGODA "
    ref1_2.tail = '''is a project that aims to make available in XML-TEI format the texts of parliamentary debates in the
    Chamber of Deputies during the Third Republic, following the'''
    ref2_2 = ET.SubElement(p2, "ref", target ="https://github.com/mpuren/agoda/blob/ODD/documentation/agoda_odd.xml")
    ref2_2.text = "ODD "
    ref2_2.tail = " defined for the project from the "
    ref3_2 = ET.SubElement(p2, "ref", target = "https://github.com/clarin-eric/parla-clarin")
    ref3_2.text = " Parla-CLARIN recommendations "
    ref3_2.tail = ''' From a proof-of-concept perspective, phase 1 of the AGODA project focuses more specifically on the
    5th legislature (1889-1893). The encoded texts are first extracted from the digitised documents available on '''
    ref4_2 = ET.SubElement(p2, "ref", target = "https://gallica.bnf.fr/ark:/12148/cb328020951/date.item")
    ref4_2.text = "Gallica,"
    ref4_2.tail = '''  the digital library of the Biliothèque nationale de France, then they are converted into
    XML-TEI using Python scripts.'''    

 # fin de la description du projet--------------------------------------------------------    
