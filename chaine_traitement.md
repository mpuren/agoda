# Chaîne de traitement

## Extraire les textes de simages
La stratégie consiste à combiner deux solutions :
- Ré-océriser les textes les plus fautifs et les post-corriger
- corriger les textes déjà océrisés les moins fautifs 
L'idée est de pouvoir avancer sur l'annotation en TEI même si tout le corpus n'est pas corrigé.
### Créer une IA capable de diviser le corpus en textes peu fautifs / textes très fautifs
- Produire une vérité de terrain pour permettre de mieux évaluer le taux d'erreur
- Méthode d'évaluation du taux d'erreur et annotation pour produire les données d'entraînement
- Créer une IA (SVM ?)
- 
### Réocériser les textes les plus fautifs
- Améliorer les images (éliminer la courbure de la page). Une idée intéressante consiste à réaliser un traitement OCR séquentiel de chaque tronçon de baseline, chacun redressé indépendamment puis reconnu. La ligne de texte étant ensuite « recomposée » (facile, puisque tout appartient à la même baseline à la base). C’est librement inspiré de ce qui est décrit ici : [https://arxiv.org/pdf/2102.08742.pdf](https://arxiv.org/pdf/2102.08742.pdf)
- Créer un modèle avec eScriptorium
### Post-corriger les textes
Plusieurs approches :
- Utiliser un dictionnaire : pyspellchecker (créer un dictionnaire adapaté) ou solution d'Edwin)
- Utiliser une solution endogène (cf. script d'Eric en perl qui permet de conserver la trace de la correction via une balise TEI <corr>)
Bibliographie à utiliser :
Nguyen, Thi-Tuyet-Hai, Adam Jatowt, MIickael Coustaty, et Antoine Doucet. 2021. « Survey of Post-OCR Processing Approaches ». _ACM Computing Surveys_ 1, 1 (March 2020) (mars): 36. [https://doi.org/10.5281/zenodo.4640070](https://doi.org/10.5281/zenodo.4640070).
Rigaud, Christophe, Antoine Doucet, Mickaël Coustaty, et Jean-Philippe Moreux. 2019. « ICDAR 2019 Competition on Post-OCR Text Correction ». In _15th International Conference on Document Analysis and Recognition_, 1588‑93. Sydney, Australia. [https://hal.archives-ouvertes.fr/hal-02304334](https://hal.archives-ouvertes.fr/hal-02304334).

## Annoter automatiquement les textes en TEI
- Créer un schéma XML approprié et un ODD documenté
- Utiliser les scripts Python développés dans le cadre d'eScriptorium (cf. gitlab)
- TEI process (développé par Eric) (cf. gitlab). Permet notamment

## Reconnaissance des entités nommées
- Chaîne de traitement FRMG pour le français 
- Modèle de langue pour le français : CamemBERT (à privilégier car plus à jour)

## Topic Modeling
Eric proposait de réaliser également le topic modeling sur les bigrammes.

Quelle est la granularité thématique désirée ?
- Thématique : plus générique ? (International, économie...)
- Thématique plus précise ? (Par exemple : le canal de Panama...)

Identifier les grandes thématiques et mettre les documents dans chaque catégorie et entraîner un classifieur multiclasse. Le classifieur peut s'appuyer sur tout le contenu du texte.
L'idée est d'associer à chaque fragment à son topic et entrainer plusieurs classifieur qui vont associer un degré de probabilité avec un nouveau texte.
 
On pourrait annoter chaque débat avec un thème large et ajouter une thématique plus précise, par exemple au niveau des titres.

On peut envisager d'aller plus loin en annotant les mots appartenant à un topic en utilisant le mécanisme des id (<w xml-id="345">Tonkin</w>) en utilisant un <span>. On pourrait ainsi avoir plusieurs topics sur un paragraphe. Une liste d'étiquette serait affichée et tu mets en évidence les mots après avoir cliqué sur l'étiquette.

Il faut peut-être travailler avec les embeddings et récupérer les embeddings qui sont des embeddings du topic.
