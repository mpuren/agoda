# Réflexions encodage TEI - Avril 2022

## 1- Comment penser l'encodage ? 

### Pourquoi encoder les textes ?

Objectifs de l'encodage : 
- **Consulter les débats** : plate-forme de consultation et d'exploration des débats parlementaires
- **Exploiter les débats** : rendre le texte manipulable, exploitable par des méthodes computationnelles (la numérisation ne permet pas la manipulation du texte mais elle permet de "nouveaux modes de lecture des sources").

**Pour qui ?** --> Domaines des historiens, TAL, sociologie, science politique ; pour les chercheurs et grand public.

### Comment encoder ? Éléments à prendre en compte

L'encodage TEI doit être pensé en fonction de plusieurs critères : 
- 1. les différentes exploitations des textes que l'on souhaite mettre en place
- 2. les particularités de la source
- 3. les projets similaires déjà réalisés
- 4. le processus de balisage automatique

Ces critères orientent (1)/ déterminent (2)/ influencent (3)/ contraignent (4) nos choix d'encodage.

#### 1- Exploitations des textes

Qu'est-ce que l'on veut extraire/ manipuler/ analyser ?

- Les **entités nommées** : 
  - Référencement des personnes
  - Référencement des lieux

- La **langue** : possibilité d'un encodage linguistique

- Les **sujets** : Topic modelling et Word embedding 

**L'encodage TEI doit s'axer sur ces objectifs de réexploitation.**

#### 2- Particularités de la source

- **Débats oraux retranscrits à l'écrit** : 
  - Source est construite avec plusieurs étapes (oral + sténographes + typographes du journal)  
  *--> Quelle étape garder dans notre encodage ? Celui de la source finale (journal), celui du texte, celui de la parole ? --> Juste le texte.*

- **Construction particulière du texte écrit** (mise en scène de la séance) :
  - Éléments oraux rapportés
  - Descriptions/ commentaires contextuels
  - Éléments structurels de l'écrit : sommaire + annexes  
  *--> Comment distinguer ces différents aspects dans l'encodage ?*  
  *--> Difficulté pour déterminer la transparence de la retranscription de la séance. Mise en scène fidèle ? Faire des recherches sur l'élaboration du CR.* 
  
- **Mise en page du journal** :
  - Colonnes
  - Changements de page
  - Particularités typographiques (italique, gras)
  *--> Faut-il la garder ? --> Non.*

- **Nombre important de débats** : 
  *--> Comment organiser l'ensemble du corpus ?*
  - Création d'un corpus contenant un ensemble de composants

- **Liens entre les débats** :
  - Débats contiennent des références à des séances précédentes 
  *--> Utilisation de d'ID pour les relier.*

**L'encodage TEI doit prendre en compte un ensemble de particularités textuels.** 

#### 3- Projets similaires réalisés 

- Analyse de projets sur l'annotation automatique de grands corpus (TIME US)

- Analyse de projets similaires sur l'annotation de débats (ParlaClarin et ParlaMint) : analyse des ODD, voir les différents partis pris par rapport à cette source.

**Voir les méthodes appliquées/ choix effectués et voir ce que l'on pourrait réutiliser et appliquer à nos propres débats.**

#### 4- Processus de balisage automatique

Intention d’utiliser une méthode d’annotation automatique des documents.  
Plusieurs solutions possibles en fonction de l'OCR choisi : *--> choix de l'outil d'epita*
- transformation du fichier XML PAGE (OCR eScriptorium) avec une feuille de transformation XSLT
- JSON (epita) à la TEI par XSLT
- JSON (epita) à XML puis à la TEI par XSLT
- **JSON (epita) à TEI par scripts python** *--> c cette méthode que l'on appliquera*

Cette méthode nécessite de :
- **Penser l'encodage en fonction de l'OCR** pour gagner du temps lors de la transformation :
  - OCR offre des entrées utiles pour notre encodage : mise en page du texte déterminée (titre, italique), NER. On peut donc réutiliser ces éléments. 
- **Penser l'OCR en fonction de la TEI** :
  - Possible de penser les entrées de l'OCR en fonction de nos besoins (noms de balise TEI à insérer) pour anticiper au maximum.  
- **Toujours adapter en fonction de la capacité de l'OCR** : 
  - On pense les entrées en fonction de ce qui est possible ou non (capacité de l'OCR à prendre en charge tel ou tel aspect).

En plus de penser l'encodage en fonction de la sortie JSON, il faut :
- **Penser les balises en fonction de ce qui sera possible d'appliquer automatiquement**.

**Choix des balises en fonction de ce qui est reconnu par l'OCR et en fonction de ce qui est possible de faire : cela limite les choix d'encodage.**

## 2- Modélisation de l'encodage TEI : réflexions actuelles sur les choix d'encodage 

### Encodage axé sur :

- Prise de parole
- Commentaires contextuels/ descriptions
- Éléments structurels de l'écrit : sommaire, annexes
- Entités nommées (référencements personnes, lieux).

- Importance de la mise en page *--> abandon pour plusieurs raisons*

**Autres (à mettre de côté) :**
- Actions de post-correction des OCR dans la TEI : coquilles reconnues par TEI Process, balise < corr >, (Eric de la Clergerie).
- Encodage de chaque mot avec un ID et @ref pour lui associer le sujet de l'élément, topic modelling. 

### Organisation du corpus
**Corpus** = regroupement par législature.  
Comment le justifier ?
- Gestion du document complexe quand il y a beaucoup de documents
- Scientifiquement ça se justifie aussi : on travaille par legislature, et l'ID des députés (Assemblée nationale) est oragnisé par legislature
- On est pas à l'abri que les règles qui régissent la sténographie change avec la législature (impact sur l'OCR par exemple les < incident > sont repérés grâce à l'italique, mais s'il n'y a plus d'italique, on ne pourra plus les encoder automatiquement de cette manière)
- Mon stage porte sur le traitement d'une législature (5e legislature de la IIIe république).

Utilisation d'un fichier **TEI Corpus**, où l'on inclut un **ensemble de composants** contenant pour chacun un texte. 

### Problèmes des métadonnées :

À définir.
- Métadonnées : en fr ou en fr et anglais ?
- Déterminer les valeurs des attributs (taxonomies à définir) !
- Valeurs des attributs en anglais ?

### Problèmes de la mise en page : 

Difficulté de réaliser dans un même encodage l'ensemble de nos objectifs : 
- Difficile d'encoder la mise en page avec les prises de paroles :
  - balises non acceptées dans certains éléments (< lb >) (par ex < incident >, < back >)
  - si on veut faire de la linguistique, impossible de garder les sauts de ligne car un mot peut être séparé en deux
  - idem pour topic modelling, word embedding
  - interrogation sur qu'est-ce qu'on encode : la source, le texte, la prise de parole ? 
  
- Possibilité de réaliser deux encodages : *--> abandon*
  - ODD chaînée possible ? À vérifier
  - Possible de lier les deux lors de la publication sur TeiPublisher ? À vérifier aussi. 

On utilise la source des JO car c'est la source qui permet de rendre accessible le texte des CR. Pour le projet, nous nous intéressons seulement au texte et non pas à la source journalistique en tant que telle. Cette dernière nous permet de récupérer le texte. Nous axons donc nos objectifs d'encodage sur le texte extrait de sa source.

Interrogation toutefois sur la part que prend le typographe du journal dans la publication du texte : compose et organise le texte en colonnes, selon les règles du journal. Interrogation sur le produit final du travail des sténographes, le journal publie-t-il le rendu final des sténographes ? *--> faire des recherches.*

**Questions encodage :** *--> non répondues car idée d'encodage abandonné*

```
<body> ... </body>
```
 
- réfléchir aux placements des < lb >
- pas de < lb > possible dans < incident >
- comment gérer l'italique ?
- Parfois changement de colonne dans un < u >
- Prévoir des balises pour les coquilles du journal ?
- Numéroter les colonnes ? Numéroter les pages ? (quelle numérotation effectuer ? garder celle présente sur les pages ?)
- Pourquoi < seg > et pas < p > (si encodage de la source du journal et encodage mise en page)
- Coquilles dans le journal : le préciser ? *--> non car pas d'édition du facsimilé*


```
<back> ... </back>
```

- < lb /> pas accepté
- Annexes : comment représenter leur mise en page ? ------ à reproduire ? les paragraphes ?


### Problèmes de l'en-tête

```
<front> ... </front>
```

- < front > balisage à confirmer.

- Phrase tout en haut : "Journal officiel du 27 novembre 1889 CHAMBRE DES DÉPUTÉS — SÉANCE DU 26 NOVEMBRE 1889 Session extraordinaire de 1889 ?" : qu'est-ce qu'on en fait ? *--> à enlever car ça va à l'encontre de notre objectif, MAIS garder le début "Journal officiel du 27 novembre 1889", à mettre dans le < teiHeader >.* 

- Composition du < front > : 
  - Mettre tout le haut dans teiHeader du composant.
  - À partir de "Compte rendu" mettre dans < front > et < head >. 
  - Dans le teiHeader du corpus possible de mettre : titre globale "Journal officiel de la République française. Débats parlementaires. Chambre des députés : compte rendu in-extenso" (cf titre de Gallica).
  

### Problèmes de l'encodage du texte (prises de paroles, commentaires, entités nommées, dates, citations)

```
<body> ... </body> et <back> ... </back>
```
- Parfois dans un même paragraphe 2 personnes parlent, créer 2 < u > ? Exemple : "voix au centre" : comment traiter ce cas ? Créer un < u > ? plusieurs fois prise de paroles par des personnes anonymes. *--> attribut @trans='overlap' (coupe la parole), dans le teiHeader créer un < personGrp > (cf Transcription of speechs - Utterances, à lire)*.

- *--> < u who="" > et garder le < persName > ensuite pour remplir la valeur de l'attribut.*

- Est-ce qu'on marque la distinction entre les paroles "dites" et les commentaires ? *--> Oui. Possible de les repérer grâce à la virgule. S'il y a le nom suivi d'un point alors c'est une prise de parole < u >, mais si c'est une virgule alors c'est un commentaire et donc on met < note > et pas un < u >.*

- Encoder les dates ? *--> À voir, < date > peut-être.*

- Lettre lue à l'oral, citations, comment les représenter ? *--> < quote >, dès qu'il y a des guillemets.*

- Lecture d'un rapport, résultat des élections, comment l'encoder ? *--> dans < u >.*

- Lieu à mettre dans des < placeName > ? *--> oui.*


- Mettre les noms dans les < persName > ? *--> Oui. Pas de < roleName >, que dans des < persName >.*
  - "M. le ministre" mettre dans un < persName > ou rôle ou autre ? *--> oui.*
  - Quand rôle juste avant le nom l'inclure dans un < persName > ? *--> oui tout mettre dans le persName.*
  
- Difficulté pour déterminer les @toWhom *--> ne pas en faire.*

