# Plan v2 ODD 

<hr/>

# 1. Introduction (Pierre Marie)
## 1.1 Contextualisation  

## 1.2 Objectifs scientifiques

## 1.3 Choix de transcription 
### 1.3.1 Éléments transcrits
### 1.3.2 Éléments non transcrits

<hr/>

# 2. Organisation générale (Fanny)
## 2.1 Structure du corpus

## 2.2 Structure des composants

## 2.3 Nommage des fichiers

<hr/>

# 3. Prérequis généraux (Pierre Marie Fanny)
## 3.1 Caractères

## 3.2 Valeurs standards
 
## 3.3 Langues

## 3.4 Taxonomies

<hr/>

# 4. Métadonnées (Pierre Marie Fanny)
## 4.1 Métadonnées bibliographiques (fileDesc)
### 4.1.1 Mention de titres (titleStmt)
### 4.1.2 Mention d'édition (editionStmt)
### 4.1.3 Étendue (extent)
### 4.1.4 Mention de publication (publicationStmt)
### 4.1.5 Description de la source (sourceDesc)

## 4.2  Métadonnées de l'encodage (encodingDesc - revisionDesc)
### 4.2.1 Description de l'encodage (encodingDesc)
#### 4.2.1 Description du projet (projectDesc)
#### 4.2.2 Déclaration des pratiques éditoriales (editorialDecl)
#### 4.2.3 Déclaration des balises (tagsDecl)
#### 4.2.4 Déclaration des classifications (classDecl)
### 4.2.2 Description des révisions (revisionDesc)

## 4.3 Métadonnées non bibliographiques (profileDesc - standOff)
### 4.3.1 Index des participants (particDesc)
#### 4.3.1.1 Description des orateurs
#### 4.3.1.2 Description des organisations
### 4.3.2 Index des lieux (settingDesc - standOff))
#### 4.3.2.1 Description du lieu de la séance
#### 4.3.2.2 Description des lieux mentionnés 
### 4.3.3 Utilisation des langues (langUsage)

<hr/>

# 5. Balisage physique (Fanny)
## 5.1 Balisage formel et typographique
### 5.1.1 Éléments pris en compte
### 5.1.2 Éléments non pris en compte

## 5.2 Balisage logique
### 5.2.1 Corps du texte
#### 5.2.1.1 Sommaire
#### 5.2.1.2 Divisions 
#### 5.2.1.3 Titres
#### 5.2.1.4 Résultats des votes
#### 5.2.1.5 Signature
### 5.2.2 Annexes
#### 5.2.2.1 Titre
#### 5.2.2.2 Scrutin
#### 5.2.2.3 Rectification

<hr/>


# 6. Balisage sémantique (Fanny)
## 6.1 Discours
### 6.1.1 Énoncés
### 6.1.2 Commentaires du transcripteur
### 6.1.3 Citations

## 6.2 Entités nommées
### 6.2.1 Personnes
### 6.2.2 Lieux
### 6.2.3  Institutions
### 6.2.4 Éléments temporels et éléments quantifiables

<hr/>

## 7. Bibliographie (Pierre Marie)

<hr/>

# Plan détaillé v2 ODD 

<hr/>

# 1. Introduction (Pierre Marie)
## 1.1 Contextualisation + explication de la source   
(notamment préciser comment le texte est produit, particularités de la source)

## 1.2 Objectifs scientifiques  

- exploiter les données : qu'est-ce que l'on veut extraire/ manipuler/ analyser.
- Importance de la structure et sens du texte = physique, logique, sémantique --> pris en compte dans le balisage.

## 1.3 Choix de transcription 

### 1.3.1 Éléments transcrits
	
- prises de paroles, commentaires, annexes
- ponctuation respectée
- orthographe non corrigée (faute OCR, faute d'orthographe)
 
### 1.3.2 Éléments non transcrits
	
- bandeau non reproduit
- traits non reproduits
- pied de page concernant l'impression non reproduit

<hr/>

# 2. Organisation générale (Fanny)
## 2.1 Structure du corpus
- teiCorpus : comment il est formé (structure globale)

## 2.2 Structure des composants
- composants : comment ils sont formés (structure globale)

```
<text>
```
- En-tête non prise en compte dans le corps du texte, mais intégrée dans les métadonnées.

- Corps du texte
```
<body>
```
- Annexes
```
<back>
```

## 2.3 Nommage des fichiers
Fichier du teiCorpus : FR_3R_5L  

Fichier du composant : FR_3R_5L_1889-11-26  


<hr/>

# 3. Prérequis généraux (Pierre Marie Fanny)
## 3.1 Caractères

## 3.2 Valeurs standards
(Éléments temporels)

## 3.3 Langues

## 3.4 Taxonomies
- du sous-corpus : correspon aux @ana présent dans < text > : "FR_3R_5L_" + la date de la séance. 
```
<text ana="#FR_3R_5L_1889-11-26">
```
- des types d'orateur (@ana dans les < u >) : (orateur) "speaker", (personne anonyme) "unknown", (rapporteur) "rapporteur/ recorder", (président) "chair"
- des votes (@type des < measure >) : (nombre des votants) "nbvoters", (majorité absolue) "majority", (pour) "ayes", (contre) "noes"
- des items (@xml:id ou @type des < div >) : à déterminer à partir du contenu des < item >
- les @type des < note > : à déterminer à partir d'une analyse des notes
- référence des personnes (@xml:id, @who dans les < u >, @ref dans les < persName > et < roleName >) : id de data BnF
- référence des lieux (@xml:id, @ref dans les < placeName >) : geonames
- référence des institutons/ partis politiques (@xml:id, @ref dans les < orgName >) : id data BnF.

- les @type des < div > des annexes : voting/ rectification ? 

<hr/>

# 4. Métadonnées (Pierre Marie Fanny)
## 4.1 Métadonnées bibliographiques (fileDesc)
### 4.1.1 Mention de titres (titleStmt)
### 4.1.2 Mention d'édition (editionStmt)
### 4.1.3 Étendue (extent)
### 4.1.4 Mention de publication (publicationStmt)
### 4.1.5 Description de la source (sourceDesc)

## 4.2  Métadonnées de l'encodage (encodingDesc - revisionDesc)
### 4.2.1 Description de l'encodage (encodingDesc)
#### 4.2.1 Description du pojet (projectDesc)
#### 4.2.2 Déclaration des pratiques éditoriales (editorialDecl)
#### 4.2.3 Déclaration des balises (tagsDecl)
#### 4.2.4 Déclaration des classifications (classDecl)
###4.2.2 Description des révisions (revisionDesc)

## 4.3 Métadonnées non bibliographiques (profileDesc - standOff)
### 4.3.1 Index des participants (particDesc)
#### 4.3.1.1 Description des orateurs
#### 4.3.1.2 Description des organisations
### 4.3.2 Index des lieux (settingDesc - standOff))
#### 4.3.2.1 Description du lieu de la séance
#### 4.3.2.2 Description des lieux mentionnés 
### 4.3.3 Utilisation des langues (langUsage)


<hr/>

# 5. Balisage physique (Fanny)
(traits éditoriaux : forme et typographie pour source imprimée + structure)

## 5.1 Balisage formel et typographique
 
### 5.1.1 Éléments pris en compte
**Balisage formel : mise en page**  
- changements de pages reproduits, mais pas l'emplacement du chiffre de la page
```
<floatingText><body><div><pb n="175"/></div></body></floatingText>
```

- paragraphes reproduits (numérotation)
```
<seg xml:id="CR_1889-11-26_u1.1">
```
### 5.1.2 Éléments non pris en compte
**Balisage formel : mise en page**  
- changements de lignes pas reproduits
- changements de colonnes pas reproduits
- alinéas non reproduits
- emplacement du texte centré, à droite, à gauche non reproduit

**Balisage typographique : typographie**  
- Graisses non reproduites
- Petites capitales non reproduites

## 5.2 Balisage logique

### 5.2.1 Corps du texte
#### 5.2.1.1 Sommaire
```
<div type="contents">
	<head>SOMMAIRE</head>
	<list>
		<item xml:id="pv">Procès verbal : MM. <persName ref="#PD_2409">Paul Déroulède</persName>, <persName ref="#pers_ID">Georges Laguerre</persName>, <persName ref="#pers_ID">Briens</persName>, <persName ref="#pers_ID">Bizouard-Bert</persName>, <persName ref="#pers_ID">Vernière</persName>.</item>
		<!-- [...] -->
	</list>
</div>
```
#### 5.2.1.2 Divisions 
```
<div type="part" corresp="#pv">
	<!-- [...] -->
</div>
```

#### 5.2.1.3 Titres
```
<head>Présidence de <persName ref="#pers_ID">M. Charles Floquet</persName></head>
```


#### 5.2.1.4 Résultats des votes
```
<u who="#pers_ID" xml:id="CR_1889-11-26_u..." ana="#chair">
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

#### 5.2.1.5 Signature
```
<signed><seg>Le Chef du service sténographique de la Chambre des députés, EMILE GROSSELIN.</seg></signed>
```

### 5.2.2 Annexes
#### 5.2.2.1 Titre
```
<head>Annexes au procès-verbal de la séance du <date when="1889-11-26">mardi 26 novembre 1889</date>.</head>
```

#### 5.2.2.2 Scrutin
*Division*
```
<div xml:id="CR_1889-11-26_vot">
<!-- [...] -->
</div>
```

```
<div xml:id="CR_1889-11-26_vot1" type="voting" corresp="#discussion7ebureau">
<!-- [...] -->
</div>
```

*En-tête*
```
<head>
	<label>SCRUTIN</label>
	<note><seg>Sur les conclusions du <num>7e</num> bureau tendant à l'annulation des opérations électorales de la <placeName ref="#lieu_ID"><num>1re</num> circonscription de l'arrondissement de Lorient (Morbihan)</placeName>.</seg></note>
</head>
```

*Détail du scrutin*
```
<desc>
	<measure type="nbvoters" quantity="506">Nombre des votants <num>506</num></measure>
	<measure type="majority" quantity="254">Majorité absolue <num>254</num></measure>
	<measure type="ayes" quantity="330">Pour l'adoption <num>330</num></measure>
	<measure type="noes" quantity="176">Contre <num>176</num></measure>
</desc>
```

*Liste des votants*

```<note type="voterslist">
	<desc>Ont voté pour :</desc>
		<seg>MM.<persName ref="#pers_ID">Abeille</persName>. <persName ref="#pers_ID">Arène (Emmanuel)</persName>. <persName ref="#pers_ID">Armez</persName>. <persName ref="#pers_ID">Arribat</persName>. <persName ref="#pers_ID">Audifred</persName>. <persName ref="#pers_ID">Aynard (Edouard)</persName>.</seg>
		<!-- [...] -->
	
	<desc>Ont voté contre :</desc>
	<!-- [...] -->
                  
	<desc>N'ont pas pris part au vote :</desc>
	<!-- [...] -->
                  
	<desc>Absents par congés : </desc>
	<!-- [...] -->
</note>
```

*Cas particulier : scrutin corrigé*
```
<note type="numbersannounced">
	<seg>Les nombres annoncés en séance avaient été de:</seg>
	<desc>
		<measure type="nbvoters" quantity="514">Nombre de votants<num>514</num></measure>
		<measure type="majority" quantity="258">Majorité absolue <num>258</num></measure>
		<measure type="ayes">Pour l'adoption <num>333</num></measure>
		<measure type="noes">Contre <num>181</num></measure>
	</desc>
	<seg>Mais, après vérification, ces nombres ont été rectifiés conformément à la liste de scrutin ci-dessus.</seg>
</note>
```


#### 5.2.2.3 Rectification 
*Division*
*Titre*
*Notes*
```
<div corresp="#CR_1889-11-25_vot" type="rectification">
	<head>Rectifications aux scrutins de la séance du <date>25 novembre 1889</date>.</head>
	<note corresp="#CR_1889-11-25_vot1"><seg><persName ref="#pers_ID">M. Michau</persName> <placeName ref="#lieu_ID">(Nord)</placeName>, porté comme s'étant abstenu dans le scrutin sur l'urgence de la proposition de <persName ref="#pers_ID">M. Maxime Lecomte</persName>, déclare avoir voté « pour ».</seg></note>
	<!-- [...] -->
</div>
```

<hr/>


# 6. Balisage sémantique (Fanny)

## 6.1 Discours

### 6.1.1 Énoncés
```
<u who="#pers_ID" xml:id="CR_1889-11-26_u1" ana="#speaker">
	<seg xml:id="CR_1889-11-26_u1.1"><persName ref="#pers_ID">M. Paul Déroulède</persName>. Je demande la parole.</seg>
</u>
```
	
### 6.1.2 Commentaires du transcripteur

- Commentaires sur l'organisation de la séance
```
<note type="opening"><seg>La séance est ouverte à <time when="02:00:00">deux heures</time>.</seg></note>
```
--> le @type permet de distinguer les types de commentaire.

- Commentaires sur l'atmosphère de la séance
```
<incident><desc>(Bruit à gauche.)</desc></incident>
```
	
### 6.1.3 Citations
```
<quote>« Oui, nous les validerons tous ! »</quote>
```

## 6.2 Entités nommées   

mini intro : def de ce qu'est une entité nommée. 
	
### 6.2.1 Personnes
	
- Nom
```
<persName ref="#pers_ID">M. Leygues</persName>
MM. <persName ref="#pers_ID">Paul Déroulède</persName> <persName ref="#pers_ID">Georges Laguerre</persName>
```

- Rôle
```
<persName ref="#pers_ID">M. Reybert, <roleName ref="#pers_ID">rapporteur</roleName></persName>
<persName ref="#pers_ID">M. le <roleName ref="#pers_ID">ministre des finances</roleName></persName>
```
	
### 6.2.2 Lieux
```
<placeName ref="#lieu_ID">Département de la Corrèze, arrondissement de Tulle, 1re circonscription</placeName>
```

### 6.2.3  Institutions
```
la <orgName ref="#org_ID">Chambre des députés</orgName>
```
	
### 6.2.4 Éléments temporels et éléments quantifiables
- les dates
```
<date when="1880-11-11">11 novembre 1880</date>
```

- les heures
```
<time when="02:00:00">deux heures</time>
```

- les chiffres
```
<num>12,189</num>
```

<hr/>

## 7. Bibliographie (Pierre Marie)
