

def paragraphes_divisions(data):

    for i in range(len(data)):
        
        if "comment" in data[i]:

            if data[i]['comment'] == 'seg':
                # Ajouter un élément 'seg' avec le contenu de la clé 'text_ocr'
                global seg
                seg = ET.SubElement(body, "seg")
                seg.text = data[i]['text_ocr']


            elif data[i]['comment'] == 'seg-beginning':
                # Ajouter un élément 'seg-beginning' avec le contenu de la clé 'text_ocr'
                seg_beginning = ET.SubElement(seg, "seg")
                seg_beginning.text = data[i]['text_ocr']


            elif data[i]['comment'] == 'seg-end':
                # Ajouter un élément 'seg-end' avec le contenu de la clé 'text_ocr'
                seg = ET.SubElement(body, "seg")
                seg_end = ET.SubElement(seg, "seg")
                seg_end.text = data[i]['text_ocr']


            elif data[i]['comment'] == 'comment seg':
                # Ajouter un élément 'comment seg' avec le contenu de la clé 'text_ocr'
                note = ET.SubElement(body, "note", attrib={"type": "comment"})
                comment_seg = ET.SubElement(note, "seg")
                comment_seg.text = data[i]['text_ocr']

            elif data[i]['comment'] == 'comment-beginning seg':
                # Ajouter un élément 'comment-beginning seg' avec le contenu de la clé 'text_ocr'
                note = ET.SubElement(body, "note", attrib={"type": "comment"})
                comment_beginning_seg = ET.SubElement(note, "seg")
                comment_beginning_seg.text = data[i]['text_ocr']


            elif data[i]['comment'] == 'comment-end seg':
                # Ajouter un élément 'comment-end seg' avec le contenu de la clé 'text_ocr'
                note = ET.SubElement(body, "note", attrib={"type": "comment"})
                comment_end_seg = ET.SubElement(note, "seg")
                comment_end_seg.text = data[i]['text_ocr']

            elif data[i]['comment'] == 'note seg':
                # Ajouter un élément 'note seg' avec le contenu de la clé 'text_ocr'
                note_seg = ET.SubElement(note, "seg")
                note_seg.text = data[i]['text_ocr']   
        pass

 
 
    # Éléments spécifiques à la première page________________________________________________________________________________
