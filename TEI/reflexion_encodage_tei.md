# Réflexions encodage TEI - Avril et Mai 2022

## 1- Comment penser l'encodage ? 

### Pourquoi encoder les textes ?

Objectifs de l'encodage : 
- **Structurer les données** 
- **Enrichir sémantiquement les données**
- **Extraire plusieurs aspects des débats**
- **Faciliter la recherche dans le corpus**
- **Offrir de nouveaux modes de visualisation des documents** grâce à l'exploitation possible du texte (texte manipulable/ exploitable par des méthodes computationnelles)
- **Intéropérabilité**

Résultats attendus : 

- **Plateforme** 
 - **de consultation** : obtenir un corpus éditorialisé 
 - **d'exploration** : plusieurs fonctionnalités comme la navigation, recherche plein-texte, affichage facsimilé, sélection de sous-corpus.

**Pour qui ?** --> Domaines des historiens, TAL, sociologie, science politique ; pour les chercheurs et grand public.

### Comment encoder ? Éléments à prendre en compte

L'encodage TEI doit être pensé en fonction de plusieurs critères : 
- 1. les différentes exploitations des textes que l'on souhaite mettre en place
- 2. les particularités de la source
- 3. les projets similaires déjà réalisés
- 4. le processus de balisage automatique / aspects techniques (standard TEI)

Ces critères orientent (1)/ déterminent (2)/ influencent (3)/ contraignent (4) nos choix d'encodage.

#### 1- Exploitations des textes

Qu'est-ce que l'on veut extraire/ manipuler/ analyser ?

- Les **entités nommées** : 
  - Référencement des personnes
  - Référencement des lieux
  - Référencement des institutions

- Les **interventions des députés/ interventions des groupes parlementaires**

- La **structure**

- Les **annexes**

- Les **sujets** : Topic modelling et Word embedding 

- Les **segments liés aux mouvements, partis et idées politiques**

- La **langue** : possibilité d'un encodage linguistique (encodage standoff)

**L'encodage TEI doit s'axer sur ces objectifs d'exploitation.**

#### 2- Particularités de la source

- **Débats oraux retranscrits à l'écrit** : 
  - Genèse : plusieurs étapes avant d'obtenir la publication finale (oral + sténographes + typographes du journal)  
  *--> Quelle(s) étape(s) garder dans notre encodage ? Celui de la publication finale (journal), celui du texte en lui-même, celui de la parole ? --> Solution médiane : journal et texte.*  
  !! Pas de logique d'encodage génétique du texte.

- **Construction particulière du texte écrit** (mise en scène de la séance) :
  - Éléments oraux rapportés
  - Descriptions/ commentaires contextuels
  - Éléments structurels de l'écrit : sommaire + annexes  
  *--> Comment distinguer ces différents aspects dans l'encodage ?*  
  *--> Difficulté pour déterminer la transparence de la retranscription de la séance. Mise en scène fidèle ? Faire des recherches sur l'élaboration du CR.* 
  
- **Mise en page du journal** :
  - Colonnes (passages à la ligne)
  - Changements de pages
  - Particularités typographiques (italique, gras)  
  *--> Faut-il garder la mise en page ? --> Solution médiane : on garde juste les changements de pages pour le sourçage.*

- **Nombre important de débats** :   
  *--> Comment organiser l'ensemble du corpus ?*
  - Création d'un corpus contenant un ensemble de composants

- **Liens entre les débats** :
  - Débats contiennent des références à des séances précédentes   
  *--> Utilisation d'ID pour les relier.*

**L'encodage TEI doit prendre en compte un ensemble de particularités textuels.**  

#### 3- Projets similaires réalisés 
- **Benchmarking** : 
 - Analyse de projets sur l'annotation automatique de grands corpus (TIME US)

 - Analyse de projets similaires sur l'annotation de débats (ParlaClarin et ParlaMint) : analyse des ODD, voir les différents partis pris
 par rapport à cette source.

**Voir les méthodes appliquées / choix effectués et voir ce que l'on pourrait réutiliser et appliquer à nos propres débats.**

#### 4- Contraintes techniques

**4.1- Format/ standard d'encodage**  
Obtenir un encodage conforme et valide.  
Respecter : 
- XML
- TEI

**4.2- Processus de balisage automatique**  
Intention d’utiliser une méthode d’encodage automatique des documents.  

**Comment l'automatisation influence-t-elle les choix d'encodage ?**  

Ce processus de balisage automatique nécessite de :
- **Penser les balises en fonction de ce qui sera possible d'appliquer automatiquement**.

Travail en amont : 
- **Adapter l'encodage en fonction de la capacité de l'OCR** : 
  - On pense les entrées en fonction de ce qui est possible ou non (capacité de l'OCR à prendre en charge tel ou tel aspect).
- **Penser l'encodage en fonction de l'annotation possible dans l'OCR** pour gagner du temps lors de la transformation :
  - OCR offre des entrées utiles pour notre encodage : mise en page du texte déterminée (titre, italique), NER, étiquettes multiples. On peut donc réutiliser ces éléments. 
- **Penser l'annotation dans l'outil d'OCR en fonction de la TEI** :
  - Possible de penser les entrées/ étiquettes de l'OCR en fonction de nos besoins (noms de balise TEI à insérer) pour anticiper au maximum.  

**Choix des balises en fonction de ce qui est reconnu par l'OCR/ capacité de l'OCR et en fonction de ce qui est possible de faire techniquement : cela limite les choix d'encodage.**

**Comment encoder automatiquement ? Choix méthodologiques**  
Plusieurs solutions de transformations possibles en fonction de l'OCR choisi : *--> choix de l'outil d'epita*
- transformation du fichier XML PAGE (OCR eScriptorium) avec une feuille de transformation XSLT
- JSON (epita) à la TEI par XSLT
- JSON (epita) à XML puis à la TEI par XSLT
- **JSON (epita) à TEI par scripts python**   
*--> c cette méthode que l'on appliquera*

- Encodage en plusieurs étapes, scripts python pour l'encodage étape par étape :
 - Texte brut --> encodage structuré --> encodage enrichi

- Garder le texte brut pour laisser la possibilité aux utilisateurs de faire leur propre analyse. Commande pour obtenir le texte brut (enlever les balises) : 
```
sudo apt install jq

jq ‘.[] | .text_ocr’ < [nom du fichier]

JQ
```

## 2- Modélisation de l'encodage TEI : réflexions sur les choix d'encodage - Avril 2022 (v1 et v2)

### Encodage axé sur :

- Prise de parole
- Commentaires contextuels/ descriptions
- Éléments structurels de l'écrit : sommaire, annexes
- Entités nommées (référencements personnes, lieux, institutions).

- Importance de la mise en page *--> abandon de certains aspects pour plusieurs raisons*

**Autres (à mettre de côté) :**
- Actions de post-correction des OCR dans la TEI : coquilles reconnues par TEI Process, balise < corr >, (Eric de la Clergerie).
- Encodage de chaque mot avec un ID et @ref pour lui associer le sujet de l'élément, topic modelling. 

### Organisation du corpus
**Corpus** = regroupement par législature.  
Comment le justifier ?
- Gestion du document complexe quand il y a beaucoup de documents
- Scientifiquement ça se justifie aussi : on travaille par législature
- On est pas à l'abri que les règles qui régissent la sténographie change avec la législature (impact sur l'OCR par exemple les < incident > sont repérés grâce à l'italique, mais s'il n'y a plus d'italique, on ne pourra plus les encoder automatiquement de cette manière)
- Mon stage porte sur le traitement d'une législature (5e legislature de la IIIe république).

Utilisation d'un fichier **TEI Corpus**, où l'on inclut un **ensemble de composants** contenant pour chacun un texte. 

! l'ID des députés (Assemblée nationale) est le même sur l'ensemble des législatures. 

### Problèmes des métadonnées

À définir.
- Métadonnées : en fr ou en fr et anglais ? *--> les deux car certains termes difficiles à traduire en anglais*
- Déterminer les valeurs des attributs (taxonomies à définir) !
- Valeurs des attributs en anglais ? *--> oui*

### Problèmes de la mise en page 

Difficulté de réaliser dans un même encodage l'ensemble de nos objectifs : 
- Difficile d'encoder la mise en page avec les prises de paroles :
  - balises non acceptées dans certains éléments (< lb >) (par ex < incident >, organisation de notre < back >)
  - si on veut faire de la linguistique, impossible de garder les sauts de ligne car un mot peut être séparé en deux
  - idem pour topic modelling, word embedding
  - interrogation sur qu'est-ce qu'on encode : la source, le texte, la prise de parole ? 
  
- Possibilité de réaliser deux encodages : *--> abandon*
  - ODD chaînée possible ? À vérifier
  - Possible de lier les deux lors de la publication sur TeiPublisher ? À vérifier aussi. 

On utilise la source des JO car c'est la publication officielle qui permet de rendre accessible le texte des CR. Pour le projet, nous nous intéressons seulement au texte et non pas à la publication en tant que telle. Cette dernière nous permet de récupérer le texte. Nous axons donc nos objectifs d'encodage sur le texte extrait de sa source.

Interrogation toutefois sur la part que prend le typographe du journal dans la publication du texte : compose et organise le texte en colonnes, selon les règles du journal. Interrogation sur le produit final du travail des sténographes, le journal publie-t-il le rendu final des sténographes ? *--> faire des recherches.*

**Questions encodage mise en page :** *--> non répondues car idée d'encodage abandonné*

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

- < lb /> pas accepté dans l'oraganisation du < back >, pas accepté dans les < relation > < desc /> </ relation >
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

## 3- Exemples d'encodage
**En-tête :**
```
<front>
      <div type="preface">
         <head>COMPTE RENDU IN EXTENSO. — <num>10</num>e SÉANCE</head>
         <head>Séance du <date>mardi 26 novembre</date>.</head>
      </div>              
</front>
```

**Sommaire :**
```
<div type="sommaire">
  <head>SOMMAIRE</head>
  <list>
       <item xml:id="pv">
           Procès verbal : MM. <persName>Paul Dérouiède</persName>, <persName>Georges Laguerre</persName>, <persName>Briens</persName>.
       </item>
               
       <item xml:id="congé">
           Excuses et demandes de congé.
       </item>
  </list>
</div>
```

**Section et prises de parole :**
```
<div corresp="#pv">
  <head>Présidence de M. <persName>Charles Floquet</persName></head>
  <note type="ouverture"><seg>La séance est ouverte à deux heures.</seg></note>
  <note type="aDefinir"><seg>M. <persName>Henri Lavertujon</persName>, l'un des secrétaires, donne lecture du procès-verbal de la séance d'hier.</seg></note>
  <u who="#aDefinir" ana="speaker">
     <seg>M. <persName>Paul Déroulède</persName>. Je demande la parole.</seg>
  </u>
  <u who="#aDefinir" ana="speaker">
     <seg>M. <persName>le président</persName>. Vous avez la parole.</seg>
  </u>
  <u who="#aDefinir" ana="speaker">
     <seg>M. <persName>Paul Déroulède</persName>. Messieurs, j'ai demandé la parole pour faire une rectification au procès-verbal et pour m'expliquer au sujet du rappel à l'ordre qui m'a été infligé.</seg>
     <seg>La plus importante des rectifications concerne le procès-verbal. En effet, au moment où la Chambre s'est prononcée en majorité en faveur de la validation d’un de nos collègues de l'<placeName>Ardèche</placeName>, ni mes amis ni moi n'avons applaudi au succès de telle ou telle candidature représentant telle ou telle  opinion ; ni mes amis ni moi n’avons même applaudi à la défaite de ce que j'appellerai le groupe des invalideurs. <incident><desc>(Bruit à gauche.)</desc></incident></seg>
  </u>
</div>
```

**Annexes : votes de la séance**
```
<back>
 <head>Annexes au procès-verbal de la séance du <date>mardi 26 novembre 1889</date>.</head>
   <listEvent xml:id="vot18891126">
   
   <!-- 1ER ÉVENEMENT -->
     <event xml:id="vot1" type="voting" corresp="#aDefinir"> <!-- corresp référence au sujet des div -->
     
       <!-- SCRUTIN -->
       <head>
         <label>SCRUTIN</label>
         <note>Sur les conclusions du 7e bureau tendant à l'annulation des opérations électorales de la <placeName>1re circonscription de l'arrondissement de Lorient (Morbihan)</placeName>.</note>
       </head>
       <desc>
            <measure type="nbvotants" quantity="506">Nombre des votants <num>506</num></measure>
            <measure type="maj" quantity="254">Majorité absolue <num>254</num></measure>
            <measure type="ayes" quantity="330">Pour l'adoption <num>330</num></measure>
            <measure type="noes" quantity="176">Contre <num>176</num></measure>
       </desc>
       <note type="result">La Chambre des députés a adopté.</note>
       
       <!-- LISTE VOTANTS -->
       <note type="listevotants">
          <listRelation>
             <relation name="votepour" active="#vot1">
                <desc> 
                     Ont voté pour :
                     MM.<persName>Abeille</persName>. <persName>Arène (Emmanuel)</persName>. <persName>Armez</persName>.
                     <persName>Arribat</persName>. <persName>Audifred</persName>. <persName>Aynard (Edouard)</persName>.
                </desc>
             </relation>
             <relation/>
          </listRelation>
      </note>
      
      <!-- NB INITIAL VOTANTS -->
      <note type="nbvotantsinitial">
         Les nombres annoncés en séance avaient été de:
         <desc>
            <measure type="nbvotants" quantity="514">Nombre de votants <num>514</num></measure>
            <measure type="maj" quantity="258">Majorité absolue <num>258</num></measure>
            <measure type="ayes">Pour l'adoption <num>333</num></measure>
            <measure type="noes">Contre <num>181</num></measure>
         </desc>
         Mais, après vérification, ces nombres ont été rectifiés conformément à la liste de scrutin ci-dessus.
      </note>
    </event>
   [...]
</back>                         
```

**Annexes : rectifications votes de la séance précédente**
```
<back>
  <listEvent>
    [...]

    <!-- RECTIFICATIONS DE SÉANCE PRÉCÉDENTE -->
    <event ref="#vot18891125" type="rectifications">
       <head>Rectifications aux scrutins de la séance du <date>25 novembre 1889</date>.</head>
       <desc/>
       <note>M. <persName>Michau</persName> <placeName>(Nord)</placeName>, porté comme s'étant abstenu dans le scrutin sur l'urgence de la proposition de M. <persName>Maxime Lecomte</persName>, déclare avoir voté <quote>« pour »</quote>.</note>
    </event>
  </listEvent> 
</back>
```

## 3- Modélisation de l'encodage TEI : réflexions sur les choix d'encodage - Mai 2022 (v3)

### Problèmes teiHeader

- réfléchir pour la création des identifiants : année session date séance

- Réfléchir au préalable quelle taxonomie pourrait être utile :
 - parlamint : **3 taxonomies : sous-corpus / types d'orateur (président, orateurs ordinaires, orateurs invités) / législatures (organisations possibles d'un parlement)**
 - définir d'autres @ana dans le texte ? *--> au niveau du < text > = indiquer à quel sous-corpus le texte appartient. Exemple : < text ana="#IIIR_5L" >.* 
 - définir d'autres @ana dans le teiHeader ? Dans < TEI > du composant de corpus, dans < person > pour indiquer la période législative pdt laquelle la personne était affiliée à l'organisation spécifiée, dans < org > ?


### Problèmes de la mise en page

- Solution médiane à adopter car indication des changements de pages = essentiel pour le sourçage. Encodage des changements de page mais pas des colonnes ni sauts de ligne.

- Solution permettant de les intégrer dans un < incident > :
```
<floatingText><body><div><pb n="183"/></div></body></floatingText>
```

### Problèmes de l'en-tête

- Suppression du < front > car répétition avec le < teiHeader >. Les informations de l'en-tête du doc doivent être insérées dans le < teiHeader >, possible car toujours construit de la même façon. 

### Problèmes de l'encodage du texte (prises de paroles, commentaires, entités nommées, dates, citations)
**Attention particulière sur les particularités de l'extrait :**
- lecture d'une lettre : ```<quote><seg/></quote>```
- lecture d'un rapport d'une élection contestée : ```<quote><seg/></quote>```
- votes au sein du texte : *--> revenir dessus. Relier ces votes avec les annexes : utiliser @corresp ?*
- ordre du jour : *--> revenir dessus*

**Attention :**
- Certaines parties n'ont pas de titres (les discussions), commence par "l'ordre du jour appelle...". *--> Utiliser l'IA pour traiter ces cas-là.*

**Questionnements :**
*Entités nommées*
- Bien définir ce qu'on inclut dans un < placeName > et < persName > (MM. M. ? rôle/statut annoncé après ? personne mentionnée par son rôle/statut ?). Choix retenus : 
```
<persName>M. Leygues</persName>
```
```
MM. <persName>Paul Déroulède</persName> <persName>Georges Laguerre</persName>
```
```
<persName>M. Reybert, <roleName>rapporteur</roleName></persName>.
```
```
<persName>M. le <roleName>ministre des finances</roleName></persName>
```

*--> dans un 2e temps, possibilité de préciser < forename > < surname >.*

- On garde la mention de la personne qui parle pour faciliter le balisage automatique : remplir le who, voir si on le garde définitivement après ou on l'enlève. *--> à garder.*

- Doute personne anonyme : quand personne anonyme parle, préciser l'anonymat, si c pas entre parenthèse et en italique, on met ça dans un < u >. *--> à intégrer dans la taxonomie des types d'orateurs.*

- < placeName > prenant en compte circonscription ? *--> oui.*

- Encoder les institutions avec orgName.

- ID pour référencer les entités nommées. (à déterminer)

*Guillemets*
- Doute avec les citations : parfois guillemets mais ce n'est pas des citations "j'affirme que j'aurais voté "pour"". *--> pour l'instant baliser avec < quote > et dans un 2e temps il faudra enlever ce balisage grâce à l'anayse des mots/ cas.*

- Parfois citations sans guillemets. *--> Problématique à prendre en compte.*

*Prise de parole/ segmentation*
- numéroter les < div > ? *--> non car cela est complexe à baliser automatiquement et certaines div n'ont pas besoin d'être numérotées (div avant les pb).*

- numéroter les < u > et les < seg > comme dans parlamint ? *--> oui, revoir le nom des @xml:id.*
```
<u who="#pers_ID" xml:id="CR_1889-11-26_u1" ana="#speaker"/>
```
```
<seg xml:id="CR_1889-11-26_u1.1"/>
```

*Date et heure*
- Encoder les dates "samedi" "11 novembre 1880" ? *--> oui et rajouter l'attribut @when.*
- Encoder les heures ? *--> oui avec < time > et @when.*

### Problèmes des annexes
- Pas de < seg > possible dans la solution 1 des annexes. *--> reprise complète de l'encodage, vote non plus pensé comme événement mais inclus dans des divisions.*

## 3- Exemples d'encodage

**Sommaire :**
```
<div type="contents">
            <head>SOMMAIRE</head>
            <list>
               <item xml:id="pv">Procès verbal : MM. <persName ref="#PD_2409">Paul Déroulède</persName>, <persName ref="#pers_ID">Georges Laguerre</persName>, <persName ref="#pers_ID">Briens</persName>, <persName ref="#pers_ID">Bizouard-Bert</persName>, <persName ref="#pers_ID">Vernière</persName>.</item>

               <item xml:id="congé">Excuses et demandes de congé.</item>
		<!-- [...] -->
            </list>
         </div>
```

**Section et prises de parole :**
```
<div type="part" corresp="#pv">
            <!-- le @corresp renvoie au @xml:id de l'< item > du sommaire -->

            <head>Présidence de <persName ref="#pers_ID">M. Charles Floquet</persName></head>

            <note type="opening"><seg>La séance est ouverte à <time when="02:00:00">deux heures</time>.</seg></note>

            <note type="comment">
               <seg><persName ref="#pers_ID">M. Henri Lavertujon, l'un des <roleName ref="#pers_ID">secrétaires</roleName></persName>, donne lecture du procès-verbal de la séance d'hier.</seg>
            </note>

            <!-- @who renvoie à la personne qui parle, @ana renvoie à la taxonomie définie pour la typologie des locuteurs -->
            <u who="#pers_ID" xml:id="CR_1889-11-26_u1" ana="#speaker">
               <seg xml:id="CR_1889-11-26_u1.1"><persName ref="#pers_ID">M. Paul Déroulède</persName>. Je demande la parole.</seg>
            </u>

            <u who="#pers_ID" xml:id="CR_1889-11-26_u2" ana="#speaker">
               <seg xml:id="CR_1889-11-26_u2.1"><persName ref="#pers_ID">M. le <roleName ref="#pers_ID">président</roleName></persName>. Vous avez la parole.</seg>
            </u>

            <u who="#pers_ID" xml:id="CR_1889-11-26_u3" ana="#speaker">
               <seg xml:id="CR_1889-11-26_u3.1"><persName ref="#pers_ID">M. Paul Déroulède</persName>. Messieurs, j'ai demandé la parole pour faire une rectification au procès-verbal et pour m'expliquer au sujet du rappel à l'ordre qui m'a été infligé.</seg>
               <seg xml:id="CR_1889-11-26_u3.2">La plus importante des rectifications concerne le procès-verbal. En effet, au moment où la <orgName ref="#org_ID">Chambre</orgName> s'est prononcée en majorité en faveur de la validation d’un de nos collègues de l'<placeName ref="#lieu_ID">Ardèche</placeName>, ni mes amis ni moi n'avons applaudi au succès de telle ou telle candidature représentant telle ou telle opinion ; ni mes amis ni moi n’avons même applaudi à la défaite de ce que j'appellerai le groupe des invalideurs. <incident><desc>(Bruit à gauche.)</desc></incident></seg>
            </u>
</div>
```
**Votes de la séance au sein du texte** à valider
```
<u who="#pers_ID" xml:id="CR_1889-11-26_u.." ana="#speaker">
	<seg xml:id="CR_1889-11-26_u..1"><persName ref="#pers_ID">M. le <roleName ref="#pers_ID">président</roleName></persName>. Je mets aux voix les conclusions du <num>7e</num> bureau, tendant à l’annulation des opérations électorales dans la <placeName ref="#lieu_ID"><num>1re</num> circonscription de Lorient</placeName>.</seg>
	<seg xml:id="CR_1889-11-26_u..2">Il y a une demande de scrutin signée de MM. <persName ref="#pers_ID">Alfred Naquet</persName>, <persName ref="#pers_ID">Louis de Belleval</persName>, [...] etc.</seg>
	<seg xml:id="CR_1889-11-26_u..3">Le scrutin est ouvert.</seg>
</u>
            
<note type="comment"><seg>(Les votes sont recueillis, et MM. les <roleName ref="#pers_ID">secrétaires</roleName> en font le dépouillement.)</seg></note>
            
<u who="#pers_ID" xml:id="CR_1889-11-26_u..." ana="#speaker">
	<seg xml:id="CR_1889-11-26_u...1"><persName ref="#pers_ID">M. le <roleName ref="#pers_ID">président</roleName></persName>. Voici le résultat du dépouillement du scrutin :</seg>
		<table rows="4" cols="2" corresp="vot18891126_vot1">
                  <row>
                     <cell role="label">Nombre des votants</cell>
                     <cell role="data"><num>514</num></cell>                     
                  </row>
                  <row>
                     <cell role="label">Majorité absolue</cell>
                     <cell role="data"><num>258</num></cell>
                  </row>
                  <row>
                     <cell role="label">Pour l'adoption</cell>
                     <cell role="data"><num>333</num></cell>
                  </row>
                  <row>
                     <cell role="label">Contre</cell>
                     <cell role="data"><num>181</num></cell>
                  </row>
               </table>
	<seg xml:id="CR_1889-11-26_u...6">La <orgName ref="#org_ID">Chambre des députés</orgName> a adopté.</seg>
	<seg xml:id="CR_1889-11-26_u...7"> En conséquence, les opérations électorales de la <placeName ref="#lieu_ID"><num>1re</num> circonscription électorale de Lorient</placeName> sont annulées.</seg>
	<seg>Avis en sera donné à <persName ref="#pers_ID">M. le <roleName ref="#pers_ID">ministre de l'intérieur</roleName></persName>.</seg>
</u>
```

**Ordre du jour** à valider
```
<div type="agenda">
	<head>RÈGLEMENT DE L'ORDRE DU JOUR</head>
            
	<!-- Solution 1 -->
	<u who="#pers_ID" ana="#speaker" xml:id="CR_1889-11-26_u....">
		<seg xml:id="CR_1889-11-26_u....1"><persName ref="#pers_ID">M. le président</persName>. <date when="1889-11-28">Jeudi</date> à <time when="02:00:00">deux heures</time>, séance publique </seg>:
		<seg xml:id="CR_1889-11-26_u....2">Scrutin pour la nomination de deux membres de la <orgName ref="#org_ID">commission supérieure de la caisse nationale des retraites pour la vieillesse</orgName>;</seg> 
		<seg xml:id="CR_1889-11-26_u....3">Scrutin pour la nomination de deux membres de la <orgName ref="#org_ID">commission de surveillance des Caisses d'amortissement et des dépôts et consignations</orgName> ;</seg>
		<seg xml:id="CR_1889-11-26_u....4">Suite de la vérification des pouvoirs :</seg>
		<seg xml:id="CR_1889-11-26_u....5">Discussion des conclusions du rapport du <num>6e</num> bureau sur l'élection de <persName ref="#pers_ID">M. du Mesnildot</persName> ;</seg>
		<!-- [...] -->
		<seg xml:id="CR_1889-11-26_u....14">Il n’y a pas d'observation ?...</seg>
		<seg xml:id="CR_1889-11-26_u....15">L'ordre du jour est ainsi réglé.</seg>
	</u>
            
	<note type="closing" xml:id="CR_1889-11-26_n4"><seg xml:id="CR_1889-11-26_n4.1">(La séance est levée à <time when="06:10:00">six heures dix minutes</time>.)</seg></note>
</div>
```

**Signature**
```
<signed><seg>Le <roleName ref="#pers_ID">Chef du service sténographique</roleName> de la <orgName ref="#org_ID">Chambre des députés</orgName>, <persName ref="#pers_ID">EMILE GROSSELIN</persName>.</seg></signed>
```

**Annexes : votes de la séance**

```
<!-- VOTE 2 -->
            <div xml:id="vot18891126_vot2" type="voting" corresp="#discussion10ebureau">
               <head>
                  <label>SCRUTIN</label>
                  <note><seg>Sur l'amendement de <persName ref="#pers_ID">M. Leygues</persName>, tendant à l'annulation don opérations électorales de la <placeName ref="#lieu_ID"><num>2e</num> circonscription de Montauban (Tarn-et-Garonne)</placeName>. (Résultat du pointage.)</seg></note>
               </head>

               <desc>
                  <measure type="nbvotants" quantity="516">Nombre de votants <num>516</num></measure>
                  <measure type="maj" quantity="259">Majorité absolue <num>259</num></measure>
                  <measure type="ayes" quantity="275">Pour l'adoption <num>275</num></measure>
                  <measure type="noes" quantity="241">Contre <num>241</num></measure>
               </desc>

               <note type="result"><seg>La <orgName ref="#org_ID">Chambre des députés</orgName> a adopté.</seg></note>

               <note type="voterslist">
                  <desc>ONT VOTÉ POUR :</desc>
                  <seg>
                     MM. <persName ref="#pers_ID">Abeille</persName>. <persName ref="#pers_ID">Arène (Emmanuel)</persName>. <persName ref="#pers_ID">Armez</persName>. <persName ref="#pers_ID">Audifred</persName>.</seg>
                  <seg>
                     <persName ref="#pers_ID">Baile ( Martial )</persName>. <persName ref="#pers_ID">Bargy</persName>. <persName ref="#pers_ID">Barodet</persName>. <persName ref="#pers_ID">Barthou</persName>. <persName ref="#pers_ID">Bartissol</persName>. <persName ref="#pers_ID">Batiot (Aristide)</persName>.
                  </seg>
                  
                  <floatingText><body><div><pb n="193"/></div></body></floatingText>
                  
                  <!-- [...] -->
                  
                  <desc>ONT VOTÉ CONTRE :</desc>
                  <seg>
                     MM. <persName ref="#pers_ID">Abrial (Léon)</persName>. <persName ref="#pers_ID">Adam (Achille)</persName>. <persName ref="#pers_ID">Aigle (<roleName ref="#pers_ID">comte</roleName> de l')</persName>. <placeName ref="#lieu_ID">Aïllières (d')</placeName>. <persName ref="#pers_ID">Aimel (Henri)</persName>.
                  </seg>
                  <seg>
                     <persName ref="#pers_ID">Balsan</persName>. <persName ref="#pers_ID">Bar (de)</persName>. <persName ref="#pers_ID">Barascud</persName>. <persName ref="#pers_ID">Barbotin</persName>. <persName ref="#pers_ID">Barrès (Maurice)</persName>. <persName ref="#pers_ID">Baudry-d'Asson (de)</persName>. 
                     <persName ref="#pers_ID">Belval (de)</persName>.
                  </seg>
                  
                  <!-- [...] -->
                  
                  <desc>N'ONT PAS PRIS PART AU VOTE :</desc>
                  <seg>
                     MM. <persName ref="#pers_ID">Arnault</persName>. <persName ref="#pers_ID">Arribat</persName>.
                  </seg>
                  <seg>
                     <persName ref="#pers_ID">Barbe</persName>. <persName ref="#pers_ID">Bastid (Adrien)</persName>. <persName ref="#pers_ID">Baudin</persName>. <persName ref="#pers_ID">Beauquier</persName>. <persName ref="#pers_ID">Berger (Georges)</persName> <placeName ref="#lieu_ID">(Seine)</placeName>.
                  </seg>
                  
                  <!-- [...] -->
                  
                  <desc>ABSENTS PAR CONGÉ :</desc>
                  <seg>
                     MM. <persName ref="#pers_ID">Baïhaut</persName>. <persName ref="#pers_ID">Bourlier</persName>. <persName ref="#pers_ID">Féraud</persName>. <persName ref="#pers_ID">Girodet</persName>. <persName ref="#pers_ID">Gonnet (Gontran)</persName>. <persName ref="#pers_ID">Jullien</persName>.
                  </seg>
               </note>

               <note type="comment"><persName ref="#pers_ID">M. Georges Graux</persName>, absent au moment du vote qui précède, déclare que, s'il avait été présent, il aurait voté « contre » l'annulation de l'élection.</note>
            </div>
         </div>
```

**Annexes : rectifications votes de la séance précédente**

```
<div corresp="#vot18891125" type="rectification">
            <head>Rectifications aux scrutins de la séance du <date>25 novembre 1889</date>.</head>
            <note corresp="#vot18891125_vot1"><seg><persName ref="#pers_ID">M. Michau</persName> <placeName ref="#lieu_ID">(Nord)</placeName>, porté comme s'étant abstenu dans le scrutin sur l'urgence de la proposition de <persName ref="#pers_ID">M. Maxime Lecomte</persName>, déclare avoir voté « pour ».</seg></note>
</div>
```

