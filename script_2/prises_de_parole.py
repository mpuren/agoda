


def prises_de_parole(data, div_content):

    div_sitting = ET.SubElement(body, "div", attrib={"type": "sitting"})
    div_content = ET.SubElement(div_sitting, "div", attrib={"type": "content"})
    u_element = ET.SubElement(div_content, "u")

    for i in range(len(data)):
        
        if "comment" in data[i]:
            
            if data[i]['comment'] == 'u seg':
                
                # Ajouter un élément 'u-seg' avec un élément 'seg' contenant le contenu de la clé 'text_ocr'
                u_seg = ET.SubElement(u_element, "seg")
                u_seg.text = data[i]['text_ocr']

            elif data[i]['comment'] == 'u-beginning seg':
                # Ajouter un élément 'u-beginning seg' avec un élément 'seg' contenant le contenu de la clé 'text_ocr'
                u_element = ET.SubElement(div_content, "u")
                u_beginning_seg = ET.SubElement(u_element, "seg")
                u_beginning_seg.text = data[i]['text_ocr']

            elif data[i]['comment'] == 'u-end seg':
                # Ajouter un élément 'u-end seg' avec un élément 'seg' contenant le contenu de la clé 'text_ocr'
                u_element = ET.SubElement(div_content, "u")
                u_end_seg = ET.SubElement(u_element, "seg")
                u_end_seg.text = data[i]['text_ocr']
        pass
