import re, os


def clean_xml(path_to_xml):
  for file_name in sorted([file for file in os.listdir(path_to_xml) if file.endswith('.xml')]):
    with open(os.path.join(path_to_xml, file_name)) as xml_file:
      xml = xml_file.read()
      xml = re.sub("(?<!-)\n", " ", xml)
      #souci si le mot divisé sur 2 lignes est réellement composé (grand-père par ex)
      xml = re.sub("-\n", "", xml)
      xml_file.close()

      xml_cleaned = open(str(os.path.join(path_to_xml, file_name)), mode="w")
      xml_cleaned.write(xml)
  return xml

def delete(data):
  """

  :return:
  """
  for i in range(len(data)):
    if "comment" in data[i]:
      if re.search(r"useless", data[i]["comment"]):
        data[i]['text_ocr'] = "".join("")
      else:
        pass
  return data