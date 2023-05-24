

def cas_particuliers(data):
    
        for i in range(len(data)):
            
            if "comment" in data[i]:
                
                if data[i]['comment'] == 'quote seg':
                    # Ajouter un élément 'quote seg' avec un élément 'seg' contenant le contenu de la clé 'text_ocr'
                    global seg
                    seg = ET.SubElement(body, "seg")
                    quote_seg = ET.SubElement(seg, "quote")
                    quote_seg.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'quote-beginning seg':
                    # Ajouter un élément 'quote-beginning seg' avec un élément 'seg' contenant le contenu de la clé 'text_ocr'
                    quote_beg_seg = ET.SubElement(body, "quote")
                    quote_beg_seg.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'quote-end seg':
                    # Ajouter un élément 'quote-end seg' avec un élément 'seg' contenant le contenu de la clé 'text_ocr'
                    quote_end_seg = ET.SubElement(body, "quote")
                    quote_end_seg.text = data[i]['text_ocr']          

                elif data[i]['comment'] == 'incident':
                    # Ajouter un élément 'incident' avec un élément 'seg' contenant le contenu de la clé 'text_ocr'
                    u_element = ET.SubElement(body, "u")
                    incident = ET.SubElement(u_element, "seg")
                    incident.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'incident-beginning':
                    # Ajouter un élément 'incident-beginning' avec un élément 'seg' contenant le contenu de la clé 'text_ocr'
                    incident_beginning = ET.SubElement(incident, "incident-beginning")            
                    incident_beginning.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'incident-end':
                    # Ajouter un élément 'incident-end' avec un élément 'seg' contenant le contenu de la clé 'text_ocr'
                    incident_end = ET.SubElement(incident, "incident-end")            
                    incident_end.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'table':
                    # Ajouter un élément 'table' avec le contenu de la clé 'text_ocr'
                    table = ET.SubElement(body, "table")
                    row = ET.SubElement(table, "row")
                    cell = ET.SubElement(row, "cell")
                    cell.text = data[i]['text_ocr'] 

                elif data[i]['comment'] == 'other-sitting':
                    # Ajouter un élément 'other-sitting' avec le contenu de la clé 'text_ocr'
                    div = ET.SubElement(body, "div")
                    div1 = ET.SubElement(div, "div", attrib={"type": "other-sitting"})
                    head = ET.SubElement(div1, "head")
                    head.text = data[i]['text_ocr']
            pass