import json, os
from script_balisage_formel import add_seg, add_signed
from script_balisage_semantique import add_utterance, add_comment, add_incident, add_quote
from script_nettoyage import nettoyage_saut_ligne

# Chemin vers les fichiers JSON
path_to_json = '/home/fanny/Documents/AGODA/Docs de travail AGODA Github/Transformations/json_data/'


compteur = 1


# Fonction principale
def main(x,compteur):
  """
  Expliquer fonction
  :return:
  """


  # appeler les fichier contenant les définitions classées par thématiques
  add_quote(x)
  add_incident(x)
  add_seg(x)
  add_comment(x)
  add_utterance(x)
  add_signed(x)
  nettoyage_saut_ligne(x)

  # écrire dans un fichier pour chacune des séances
  # nommer chaque fichier d'une certaine façon

  # Écriture du contenu de data dans les JSON - étape pas obligatoire
  with open('essai' + str(compteur) + '.json', 'w') as f:
    json.dump(x, f)

  return




# Boucle permettant de lire chaque fichier JSON dont le nom finit par ".json" contenu dans un dossier dont le chemin est donné
for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  with open(path_to_json + file_name) as json_file:
    data = json.load(json_file)

    # Application de la fonction main
    main(data, compteur)
    compteur +=1

    # Création fichier .xml en mode écriture
    for i in range(len(data)):
      if "comment" in data[i]:
        if "body" in data[i]["comment"]:
          name = json_file
          output_xml = open(str(file_name)+".xml", mode="w")
      # Boucle permettant d'écrire dans le fichier .xml tous les text_ocr de data
      if "text_ocr" in data[i]:
        if len(data[i]["text_ocr"]) > 0:
          output_xml.write(data[i]['text_ocr'])


output_xml.close()