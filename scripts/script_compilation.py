from script_balisage_formel import add_seg, add_signed, add_page_number
from script_balisage_semantique import add_utterance, add_comment, add_incident, add_quote
from script_balisage_logique import add_structure, add_division, add_structural_comment, add_item, add_title, add_table


# Fonction principale de compilation
def compilation(x, zwt, inc):
  """
  Appel des fonctions permettant d'ajouter les balises sur le texte contenu dans la variable x
  """


  # Appeler les définitions classées par thématiques dans un ordre bien précis
  #1
  add_quote(x)

  #2
  add_incident(x)

  #3
  add_seg(x)

  #4
  add_utterance(x)
  add_comment(x)

  #5
  add_signed(x)

  #6
  add_table(x)
  add_structural_comment(x)

  #add_item(x)
  #add_title(x)
  #add_division(x)
  add_page_number(x,zwt, inc)
  #add_structure(x)

  return

