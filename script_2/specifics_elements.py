class SpecificsElements:
    def specifics_elements(self):
       pass

def process_specifics_elements(specifics_elements_instance, data, body, page_number, teiHeader):
    # Appel de la méthode specifics_elements de l'instance de SpecificsElements
    specifics_elements_instance.specifics_elements(data, body, page_number, teiHeader)

# Création d'une instance de SpecificsElements
specifics_elements_instance = SpecificsElements()


def specifics_elements(data, body, page_number, teiHeader):

    for i in range(len(data)):
        if "comment" in data[i]:
            if data[i]['comment'] == "sitting contents":
                # Ajouter un élément 'sitting contents' avec le contenu de la clé 'text_ocr'

                if data[i]['text_ocr'] == "SOMMAIRE" or data[i]['text_ocr'] == "Sommaire":
                    sc_element = ET.SubElement(div_content, "head")
                    sc_element.text = data[i]['text_ocr']
                    div_content.insert(0, sc_element)
                else :
                    sc_element.text = data[i]['text_ocr']
                    div_content.insert(0, sc_element)

            elif data[i]['comment'] == 'body page-number date-pub':
                # Ajouter un élément 'body page-number date-pub' avec le contenu de la clé 'text_ocr'
               
                bp_element = ET.SubElement(body, "pb", attrib={"n": "{}".format(page_number)})
                body.insert(0, bp_element)

            # récupération de la date de publication ___________________________________________________

                texte_date = data[i]['text_ocr'] 

                partie_date = re.search(r'\d{1,2} [a-zA-Z]+ \d{4}', texte_date).group()

                # fonction pour la reconnaissance des dates. 

                parsed_date = dateparser.parse(partie_date, languages=['fr'])
                # Formatter la date 
                formatted_date = parsed_date.strftime('%Y-%m-%d')

                # Création de l'élément date avec l'attribut when
                
                date_sDc = ET.SubElement(publicationStmt_sDc, "date", {"when": formatted_date})
                date_sDc.text = partie_date
                date_desc = ET.SubElement(setting_desc, "date", {"when": formatted_date})
                date_desc.text = partie_date

            elif data[i]['comment'] == 'item':
                # Ajouter un élément 'item' avec le contenu de la clé 'text_ocr'

                item = ET.SubElement(list_item, "item")
                item.text = data[i]['text_ocr']


            elif data[i]['comment'] == 'item-list':
                # Ajouter un élément 'item-list' avec le contenu de la clé 'text_ocr'

                item_list = ET.SubElement(list_item, "item")
                item_list.text = data[i]['text_ocr']
                div_content.insert(-1, sc_element)

            elif data[i]['comment'] == "meeting-session meeting-legislature useless":
                # Ajouter un élément 'meeting-session meeting-legislature' avec le contenu de la clé 'text_ocr'
                meet_session = data[i]['text_ocr']

                # extrait le numéro de session
                num_session = int(meet_session.split(' ')[-1][:-4])
                num_legis = int(meet_session.split(' ')[0][:-1])

                # extrait le texte de la session
                texte_session = "Session " + meet_session.split('Session ')[1]  # ajoute le mot "Sessio
                # extrait la première lettre du mot suivant "Session"
                lettre_session = texte_session.split('Session ')[1][0].upper()

                # créer la balise
                global publicationStmt
                meeting_session = ET.SubElement(publicationStmt, "meeting", n=f"E{num_session}", ana="#parla.lower\n#parla.session") # une autre manière d'écrire les attributs
                meeting_session.text = f"{texte_session}"

                meet_legis = meet_session.split('—')
                meeting_legislature = ET.SubElement(publicationStmt, "meeting", n=f"{num_legis}                                                    L", ana="#parla.lower\n#parla.legislature")
                meeting_legislature.text = meet_legis[0]
                
                global titleStmt
                meeting_session_t = ET.SubElement(titleStmt, "meeting", n=f"E{num_session}", ana="#parla.lower\n#parla.session") # une autre manière d'écrire les attributs
                meeting_session_t.text = f"{texte_session}".strip(".")
                titleStmt.insert(4, meeting_session_t)

                meet_legis = meet_session.split('—')
                meeting_legislature_t = ET.SubElement(titleStmt, "meeting", n=f"{num_legis}L", ana="#parla.lower\n#parla.legislature")
                meeting_legislature_t.text = meet_legis[0].split(".")[0].replace("°", "e")
                titleStmt.insert(5, meeting_legislature_t)

            elif data[i]['comment'] == "meeting-sitting useless" or data[i]['comment'] == "meeting-sitting":
                # Ajouter un élément 'meeting-sitting' avec le contenu de la clé 'text_ocr'
                meet_sit = data[i]['text_ocr'].split('—')
                num_seance = meet_sit[1][0:3]
                meeting_sitting = ET.SubElement(publicationStmt, "meeting", n=f"{num_seance}", ana="#parla.lower\n#parla.sitting")
                meeting_sitting.text = data[i]['text_ocr']
                meeting_sitting_t = ET.SubElement(titleStmt, "meeting", n=f"{num_seance}", ana="#parla.lower\n#parla.sitting")
                meeting_sitting_t.text = data[i]['text_ocr'].split("—")[1].strip(".").replace("°", "e").lower()
                titleStmt.insert(6, meeting_sitting_t)

            elif data[i]['comment'] == 'agenda':
                # Ajouter un élément 'agenda' avec le contenu de la clé 'text_ocr'
                div_agenda = ET.SubElement(body,"div")
                agenda_head = ET.SubElement(div_agenda, "head", type="agenda")
                agenda_head.text = data[i]['text_ocr']
        pass
