# Chaîne de traitement

## Extraire les textes des images
La stratégie consiste à combiner deux solutions :
- Ré-océriser les textes les plus fautifs et les post-corriger
- Corriger les textes déjà océrisés les moins fautifs 
L'idée est de pouvoir avancer sur l'annotation en TEI même si tout le corpus n'est pas corrigé.

### Créer une IA capable de diviser le corpus en textes peu fautifs / textes très fautifs

Evaluer le taux d'erreur entre Gallica, OCR Tesseract, Abby et eScriptorium
- Produire ground truth (en cours)
- Entraîner modèle avec eScriptorium (en cours)
- Océriser avec Abby le numéro concerné (à récupérer)

Stratégie de réocérisation :
- Tout réocériser avec Tesseract ou eScriptorium
- Mesurer le taux d'erreur par page et non par numéro
- Décider d'un niveau où la réocérisation est nécessaire (certaines pages en ont besoin plus que d'autres)
- Créer SVM
- Réocériser avec Abby Reader

**Etapes**

*Evaluer le taux d'erreur entre Gallica, OCR Tesseract, Abby et eScriptorium*
1. Produire ground truth (en cours)
2. Entraîner modèle avec eScriptorium (en cours)
3. Océriser avec Abby le numéro concerné (à récupérer)
4. Mesurer le taux d'erreur par page et non par numéro (car le résultat différe pas mal en fonction entre les pages)

*Stratégie de réocérisation*
4. Décider d'un niveau où la réocérisation est nécessaire (quel est le pourcentage d'erreur trop élevé ?)
5. Faut-il tout réocériser avec Tesseract ou eScriptorium ? A décider en fonction des résultats de l'évaluation de l'accuracy de l'OCR de Gallica.
6. Créer IA (SVM )
7. Prétraitement de l'image (cf. ci-dessous "Améliorer les images d'origine")
7. Réocériser avec Abby Reader

### Améliorer les images d'origine
- Eliminer la courbure de la page. Une idée intéressante consiste à réaliser un traitement OCR séquentiel de chaque tronçon de baseline, chacun redressé indépendamment puis reconnu. La ligne de texte étant ensuite « recomposée » (facile, puisque tout appartient à la même baseline à la base). C’est librement inspiré de ce qui est décrit ici : [https://arxiv.org/pdf/2102.08742.pdf](https://arxiv.org/pdf/2102.08742.pdf)

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

Il faut peut-être travailler avec les embeddings et récupérer les embeddings qui sont des embeddings du topic (à éclaircir..)
