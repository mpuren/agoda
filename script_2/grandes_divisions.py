
def grandes_divisions(data, body, filename, page_number, bp_element):
    
    for i in range(len(data)):
        
        if "comment" in data[i]:

            
            if data[i]['comment'] == 'page-number':
                # Ajouter un élément 'page-number' avec le contenu de la clé 'text_ocr'
                pge_number = ET.SubElement(body, "pb", attrib={"n": "{}".format(page_number)})
                pge_number.text = data[i]['text_ocr']
                #body.insert(0, bp_element)


            elif data[i]['comment'] == 'page-number-ref':
                # Ajouter un élément 'page-number-ref' avec le contenu de la clé 'text_ocr'
                incident = ET.SubElement(body, "incident")
                desc = ET.SubElement(incident, "desc")
                page_number_ref = ET.SubElement(desc, "ref", attrib={"target": "#p"} )
                page_number_ref.text = data[i]['text_ocr'] 

            elif data[i]['comment'] == 'part head':
                # Ajouter un élément 'part head' avec le contenu de la clé 'text_ocr'
                div = ET.SubElement(body, "div", attrib={"type": "part", "corresp": "#pv"})
                part_head = ET.SubElement(div, "head" )
                part_head.text = data[i]['text_ocr'] 
                div.addprevious(etree.Comment(generate_id("Partie_")))


            elif data[i]['comment'] == 'opening seg':
                # Ajouter un élément 'opening seg' avec le contenu de la clé 'text_ocr'
                note = ET.SubElement(body, "note", {"type": "opening", "{http://www.w3.org/XML/1998/namespace}id": "ID_" + filename.split("_")[3] + "_" + generate_id("n")})
                opening_seg = ET.SubElement(note, "seg", {"type": "opening", "{http://www.w3.org/XML/1998/namespace}id": generate_id("s")})
                opening_seg.text = data[i]['text_ocr']  

            elif data[i]['comment'] == 'closing seg':
                # Ajouter un élément 'closing seg' avec le contenu de la clé 'text_ocr'
                note = ET.SubElement(body, "note", {"type": "opening", "{http://www.w3.org/XML/1998/namespace}id": generate_id("note")})
                closing_seg = ET.SubElement(note, "seg", {"type": "opening", "{http://www.w3.org/XML/1998/namespace}id": generate_id("s")} )
                closing_seg.text = data[i]['text_ocr'] 

            elif data[i]['comment'] == 'signed seg back':
                # Ajouter un élément 'signed seg back' avec le contenu de la clé 'text_ocr'
                signed = ET.SubElement(body, "signed")
                signed_seg_back = ET.SubElement(signed, "seg")
                signed_seg_back.text = data[i]['text_ocr']  

            elif data[i]['comment'] == 'signed seg div-end':
                # Ajouter un élément 'signed seg div-end' avec le contenu de la clé 'text_ocr'
                signed = ET.SubElement(body, "signed")
                signed_seg_div_end = ET.SubElement(signed, "seg")
                signed_seg_div_end.text = data[i]['text_ocr']  

            elif data[i]['comment'] == 'text':
                # Ajouter un élément 'text' avec le contenu de la clé 'text_ocr'
                text = ET.SubElement(body)
                text.text = data[i]['text_ocr']  

            elif data[i]['comment'] == 'text-back':
                # Ajouter un élément 'text-back' avec le contenu de la clé 'text_ocr'
                div = ET.SubElement(body, "div")
                back = ET.SubElement(div, "back")
                text_back = ET.SubElement(back, "div" )
                text_back.text = data[i]['text_ocr']  
        pass
tag_counts = {}
def generate_id(tag):
    """Génère un identifiant unique pour une balise en fonction de son type."""
    if tag not in tag_counts:
        tag_counts[tag] = 1
    else:
        tag_counts[tag] += 1
    return f"{tag}{tag_counts[tag]}"
