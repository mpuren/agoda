

def annexes(data):
    
        for i in range(len(data)):
            if "comment" in data[i]:
                
                if data[i]['comment'] == 'part1':
                # Ajouter un élément 'part1' avec le contenu de la clé 'text_ocr'
                    div_annexe = ET.SubElement(body, "div", attrib={"type": "part"})
                    div_annexe.text = data[i]['text_ocr']
                    div_annexe.addprevious(etree.Comment(generate_id("Partie_")))

                elif data[i]['comment'] == 'part1 u-beginning seg':
                    # Ajouter un élément 'part1 u-beginning seg' avec le contenu de la clé 'text_ocr'
                    div_annexe = ET.SubElement(body, "div", attrib={"type": "part"})
                    part_u_beg = ET.SubElement(div_annexe, "u")
                    seg_part1 = ET.SubElement(part_u_beg, "seg")
                    seg_part1.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'erratum':
                    # Ajouter un élément 'erratum' avec le contenu de la clé 'text_ocr'
                    div_erratum = ET.SubElement(body, "div", attrib={"type": "erratum"})
                    head_annexe = ET.SubElement(div_erratum, "head")
                    label_annexe = ET.SubElement(head_annexe, "label")
                    label_annexe.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'note-head':
                    # Ajouter un élément 'note-head' avec le contenu de la clé 'text_ocr'
                    div_erratum = ET.SubElement(body, "div", attrib={"type": "erratum"})
                    head_annexe = ET.SubElement(div_erratum, "head")
                    note_head_annexe = ET.SubElement(head_annexe,"note")
                    note_head_annexe.text = data[i]['text_ocr']


                elif data[i]['comment'] == 'lists':
                    # Ajouter un élément 'lists' avec le contenu de la clé 'text_ocr'
                    div_lists = ET.SubElement(body, "div", attrib={"type": "lists"})
                    head_lists = ET.SubElement(div_lists, "head")
                    label_lists = ET.SubElement(head_lists, "label")
                    label_lists.text = data[i]['text_ocr']


                elif data[i]['comment'] == 'offices': 
                    # Ajouter un élément 'offices' avec le contenu de la clé 'text_ocr'
                    div_offices = ET.SubElement(body, "div", attrib={"type": "offices"})
                    head_offices = ET.SubElement(div_offices, "head")
                    head_offices.text = data[i]['text_ocr']     


                elif data[i]['comment'] == 'appendices': 
                    # Ajouter un élément 'appendices' avec le contenu de la clé 'text_ocr'
                    div_appendices = ET.SubElement(body, "div", attrib={"type": "appendices"})
                    head_appendices = ET.SubElement(div_appendices, "head")
                    head_appendices.text = data[i]['text_ocr']


                elif data[i]['comment'] == 'voting1' or data[i]['comment'] == 'voting1': 
                    # Ajouter un élément 'voting1' avec le contenu de la clé 'text_ocr'
                    global div_voting1
                    div_voting1 = ET.SubElement(body, "div", attrib={"type": "voting"})
                    head_voting1 = ET.SubElement(div_voting1, "head")
                    label_voting1 = ET.SubElement(head_voting1, "label")
                    label_voting1.text = data[i]['text_ocr']


                elif data[i]['comment'] == 'result':
                    # Ajouter un élément 'result' avec le contenu de la clé 'text_ocr'
                    note_result = ET.SubElement(div_voting1, "note", attrib={"type": "result"})
                    seg_note_annexe = ET.SubElement(note_result, "seg")
                    seg_note_annexe.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'voterslist-beginning': 
                    # Ajouter un élément 'voterslist-beginning' avec le contenu de la clé 'text_ocr'
                    global note_voterlist
                    note_voterlist = ET.SubElement(div_voting1, "note", attrib={"type": "voterlist"})
                    voterlist = ET.SubElement(note_voterlist, "desc")
                    voterlist.text = data[i]['text_ocr']


                elif data[i]['comment'] == 'desc':  
                    # Ajouter un élément 'desc' avec le contenu de la clé 'text_ocr'
                    voterlist_desc = ET.SubElement(note_voterlist, "desc")
                    voterlist_desc.text = data[i]['text_ocr']


                elif data[i]['comment'] == 'seg note-beginning': 
                    # Ajouter un élément 'seg note-beginning' avec le contenu de la clé 'text_ocr'
                    note_note_beg = ET.SubElement(div_voting1, "note", attrib={"type": "numbersannounced"})
                    seg_note_beg = ET.SubElement(note_note_beg, "seg")
                    seg_note_beg.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'seg note-end' or data[i]['comment'] == 'seg note-end div-end': 
                    # Ajouter un élément 'seg note-end' avec le contenu de la clé 'text_ocr'
                    seg_note_end = ET.SubElement(div_voting1, "seg")
                    seg_note_end.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'rectification':
                    # Ajouter un élément 'rectification' avec le contenu de la clé 'text_ocr'
                    div_rectification = ET.SubElement(body, "div", attrib={"type": "rectification"})
                    head_rectification = ET.SubElement(div_rectification, "head")
                    head_rectification.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'seg comment-beginning': 
                    # Ajouter un élément 'seg comment-beginning' avec le contenu de la clé 'text_ocr'
                    note_com_beg = ET.SubElement(body, "note", attrib={"type": "comment"})
                    seg_com_beg = ET.SubElement(note_com_beg, "seg")
                    seg_com_beg.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'seg note-end':  
                    # Ajouter un élément 'seg note-end' avec le contenu de la clé 'text_ocr'
                    seg_com_end = ET.SubElement(note_com_beg, "seg")
                    seg_com_end.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'petition':
                    # Ajouter un élément 'petition' avec le contenu de la clé 'text_ocr'
                    div_petition = ET.SubElement(body, "div", attrib={"type": "petition"})
                    head_petition = ET.SubElement(div_petition, "head")
                    label_petition = ET.SubElement(head_petition, "label")
                    label_petition.text = data[i]['text_ocr']

                elif data[i]['comment'] == 'note-head':   
                    # Ajouter un élément 'note-head' avec le contenu de la clé 'text_ocr'
                    note_petition = ET.SubElement(head_petition, "note")
                    note_petition.text = data[i]['text_ocr']
            pass
