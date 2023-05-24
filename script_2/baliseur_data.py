from create_teiheader import create_teiheader
from grandes_divisions import grandes_divisions
from paragraphes_divisions import paragraphes_divisions
from prises_de_parole import prises_de_parole
from cas_particuliers import cas_particuliers
from annexes import annexes
from generate_id import generate_id 

class BaliseurData:
    def baliseur_data(self):
        # Code de la méthode baliseur_data
        pass

def process_data(baliseur_data_instance):
    # Appel de la méthode baliseur_data de l'instance de BaliseurData
    baliseur_data_instance.baliseur_data()


def baliseur_data(data, body_element, filename, page_number, bp_element ):
    grandes_divisions(data, body_element, filename, page_number, bp_element)
    paragraphes_divisions(data)
    prises_de_parole(data, body_element)
    cas_particuliers(data)
    annexes(data)
    pass
# __________________________________________________________________________________________________________
