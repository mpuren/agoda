# Plan v2 ODD 

<hr/>

# 1. Introduction (Pierre Marie)
## 1.1 Contextualisation  
Pierre et Marie
## 1.2 Objectifs scientifiques
Pierre
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
## 3.3 Taxonomies
Marie ?

<hr/>

# 4. Métadonnées (Marie)
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
### 4.3.1 Index des participants (standOff)
#### 4.3.1.1 Description des orateurs
#### 4.3.1.2 Description des organisations
### 4.3.2 Index des lieux (settingDesc - standOff)
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

Fonctionnement de la chambre
- chambre haute versus basse
- session extraordinaire et ordinaire

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

## 3.3 Taxonomies
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

# 4. Métadonnées (Marie)
La TEI permet d'ajouter de nombreuses métadonnées aux fichiers TEI. Ces métadonnées sont enregistrées dans l'élément <teiHeader> qui apparaît à deux niveaux :
- dans le <teiCorpus>
- dans chacun des documents TEI composant le corpus.
Les métadonnées enregistrées dans le <teiCorpus> concernent l'ensemble des 
documents, tandis que celles enregistrés dans les fichiers TEI individuels sont 
spécifiques à chaque numéro du Journal Officiel, c'est-à-dire à chaque séance.

Les métadonnées contenues dans ces <teiHeader> peuvent donc différer ; par ailleurs, le <teiHeader> dans le <teiCorpus> comportent également des éléments supplémentaires. 
 
## 4.1 Métadonnées bibliographiques (fileDesc)
L'élément <fileDesc> contient les métadonnées bibliographiques décrivant le fichier électronique. Il contient également l'élément <sourceDesc> permettant d'enregistrer les informations décrivant la source dont le fichier TEI est dérivé. Nous utilisons <sourceDesc> pour encoder les données bibliographiques décrivant la source numérisée, ici le Journal officiel de la République française. Débats parlementaires. Chambre des députés : compte rendu in-extenso, au niveau du périoddique (dans l'élément <teiCorpus>) et au niveau du numéro (dans l'élément <TEI>).

### 4.1.1 Mention de titres (titleStmt)

Quatre éléments sont contenus dans <titleStmt> : <title>, <meeting>, <respStmt> et <funder> apparaissent dans cet ordre. L'usage des deux premiers éléments diffère au niveau du corpus et du document, tandis que <respStmt> et <funder> sont utilisés de manière similaire. 

#### 4.1.1.1 Utilisation de l'élément <title>

Au niveau du corpus et du document, on distingue le titre principal et le sous-titre grâce à l'attribut @type. U attribut @xml-lang permet de fournir ces titres en français et en anglais.

Dans <teiCorpus> :
- le titre principal est le suivant : "Corpus des débats parlementaires français de la Troisième République" ;
- le sous-titre est composé du texte "Comptes-rendus des débats en séance publique de la Chambre des députés" suivi de la législature et des dates de début et fin de cette dernière.

            <title type="main" xml:lang="fr">Corpus des débats parlementaires français de la
               Troisième République</title>
            <title type="main" xml:lang="en">Corpus of French Parliamentary Debates of the Third
               Republic</title>
            <title type="sub" xml:lang="fr">Comptes-rendus des débats en séance publique de la
               Chambre des députés, 5e législature (1889-1893)</title>
            <title type="sub" xml:lang="en">Proceedings of the debates in plenary sitting of the
               Chamber of Deputies,5th legislature (1889-1893)</title>

Au niveau du document TEI individuel:
- le titre principal est "Journal officiel de la République française. Débats parlementaires" ;
- le sous-titre est "Chambre des députés : compte rendu in-extenso".

            <title type="main" xml:lang="fr">Journal officiel de la République française. Débats
               parlementaires</title>
            <title type="main" xml:lang="en">Official Journal of the French Republic. Parliamentary
               debates</title>
            <title type="sub" xml:lang="fr">Chambre des députés : compte rendu in-extenso</title>
            <title type="sub" xml:lang="en">Chamber of Deputies: verbatim report</title>

#### 4.1.1.2 Utilisation de l'élément <meeting>

L'élément <meeting> renseigne le titre d'une réunion ou d'une conférence. Un attribut @ana associe systématiquement les éléments appropriés provenant de la taxonomie décrite dans (ajouter lien vers la section).

Dans <teiCorpus>, l'élément <meeting> renseigne le numéro de la législature. La valeur de l'attribut @n correspond au numéro de législature suivi du type de chambre ("lower" pour la Chambre des députés vs. "higher" pour le Sénat).

<meeting n="5-lower" ana="#parla.lower #parla.term">5e législature</meeting>

Dans les documents TEI composant le corpus, l'élément <meeting> est utilisé trois fois :
- Un premier élément enregistre s'il s'agit d'une session ordinaire ou d'une session extraordinaire. La valeur de l'attribut @n est définie de la façon suivante : la lettre correspond au type de session (O pour ordinaire et E pour extraordinaire) ; le numéro correspond à la place de la session dans la législature.
- Le deuxième élément indique le numéro de la législature. La valeur de l'attribut @n a pour valeur le numéro de la législature suivi de la lettre L pour "législature".
- Le troisième élément enregistre le numéro de la séance. L'attribut @n permet d'enregistrer le numéro de la séance.

            <meeting n="E1" ana="#parla.lower #parla.session">Session
               extraordinaire de 1889</meeting>
            <meeting n="5L" ana="#parla.lower #parla.legislature">5e
               législature</meeting>
            <meeting n="10" ana="#parla.lower #parla.sitting">10e
               séance</meeting>

#### 4.1.1.3 Utilisation de <respStmt> et <funder>

<respStmt> enregistre les noms de personnes ayant participé à la production du document électronique et à leur responsabilité respective.

            <respStmt>
               <persName>
                  <forename>Fanny</forename>
                  <surname>Lebreton</surname>
                  <ptr type="id-hal" target="fanny-lebreton"/>
               </persName>
               <resp xml:lang="fr">Transformation du JSON en XML-TEI et ajout automatique des
                  balises TEI par des scripts Python</resp>
               <resp xml:lang="en">Transformation from JSON to XML-TEI and automatic addition of TEI
                  tags by Python scripts</resp>
            </respStmt>
            <respStmt>
               <persName>
                  <forename>Marie</forename>
                  <surname>Puren</surname>
                  <ptr type="id-hal" target="marie-puren"/>
                  <ptr type="orcid" target="0000-0001-5452-3913"/>
               </persName>
               <resp xml:lang="fr">TEI Header</resp>
               <resp xml:lang="en">TEI Header</resp>
            </respStmt>

La source du financement du projet est indiqué dans l'élément <funder>.

### 4.1.2 Mention d'édition (editionStmt) [fait]
L'élément <editionStmt> renseigne le numéro de l'édition électronique.

### 4.1.3 Étendue (extent)
L'élément <extent> donne des informations sur la taille du corpus. On y trouve trois types de mesures :
- le nombre d'interventions (une intervention correspondant à une chaîne de caractères contenus dans un élément <u>),
- le nombre de mots,
- le nombre de pages (uniquement dans les documents TEI individuels).

         <extent>
            <measure unit="pages" quantity="19" xml:lang="fr">19 pages</measure>
            <measure unit="pages" quantity="19" xml:lang="en">19 pages</measure>
            <measure unit="utterances" quantity="75122" xml:lang="sl">75.122 énoncés</measure>
            <measure unit="utterances" quantity="75122" xml:lang="en">75,122 utterances</measure>
            <measure unit="words" quantity="20190034" xml:lang="sl">20.190.034 mots</measure>
            <measure unit="words" quantity="20190034" xml:lang="en">20,190,034 words</measure>
         </extent>

Ces chiffres sont fournis pour chaque document TEI. Dans <teiCorpus>, il s'agit du nombre total d'interventions et de mots dans le corpus.   

### 4.1.4 Mention de publication (publicationStmt)
Le contenu de cet élément est semblable au niveau du corpus et du document. Il est utilisé pour donner des informations sur la publication du document électronique. 

Nous utilisons de la façon suivante quatre des éléments qui peuvent être contenus dans le <publicationStmt>:
- L'élément <publisher> contient le nom du projet responsable de la publication du document, à savoir AGODA.
- L'élément <authority> enregistre le nom de 'organisme en charge de la publication du fichier, ici BnF Datalab
- Le document électronique est distribué sous une licence CC-BY comme indiqué dans l'élément <availability>
- Dans l'élément <date>, on trouve la date de production du document électronique.

### 4.1.5 Description de la source (sourceDesc)
Les informations bibliographiques décrivant la source numérisée dont dérive le fichier électronique sont contenues dans <sourceDesc>. Nous utilisons l'élément <biblFull> afin d'en donner une description bibliographique structurée. Les informations contenues dans l'élément <biblFull> sont similaires au niveau du corpus et au niveau du document, excepté le texte dans l'élément <date>. Nous indiquons en effet les dates extrêmes de la législature dans le <teiCorpus>, tandis qu'on trouve la date de publication du compte-rendu de la séance dans le Journal Officiel.

         <sourceDesc>
            <biblFull>
               <titleStmt>
                  <title>Journal officiel de la République française. Débats parlementaires. Chambre
                     des députés : compte rendu in-extenso</title>
               </titleStmt>
               <publicationStmt>
                  <publisher xml:lang="fr">Pas d'information disponible</publisher>
                  <publisher xml:lang="en">No information available</publisher>
                  <pubPlace>
                     <location>
                        <country key="FR"/>
                        <settlement type="city">Paris</settlement>
                     </location>
                  </pubPlace>
                  <date when="1889-11-27">27 novembre 1889</date>
                  <distributor facs="https://gallica.bnf.fr/ark:/12148/bpt6k477552f/f1">Source
                     gallica.bnf.fr / Bibliothèque nationale de France</distributor>
                  <availability>
                     <licence xml:lang="fr"
                        target="https://gallica.bnf.fr/edit/und/conditions-dutilisation-des-contenus-de-gallica">
                        <p>Les contenus accessibles sur le site Gallica sont pour la plupart des
                           reproductions numériques d'œuvres tombées dans le domaine public
                           provenant des collections de la BnF.</p>
                        <p>Ces contenus sont considérés, en vertu du code des relations entre le
                           public et l’administration, comme étant des informations publiques et
                           leur réutilisation s'inscrit dans le cadre des dispositions prévues aux
                           articles L. 321-1 à L. 327-1 de ce code.</p>
                     </licence>
                  </availability>
               </publicationStmt>
               <seriesStmt>
                  <title>Journal Officiel de la République française</title>
                  <biblScope unit="series">Débats parlementaires</biblScope>
                  <biblScope unit="volume">Chambre des députés</biblScope>
                  <idno type="ISSN">1270-5942</idno>
               </seriesStmt>
            </biblFull>
         </sourceDesc>

## 4.2  Métadonnées de l'encodage (encodingDesc)
Cet élément donne des informations sur les principes éditoriaux et de transcription utilisés. 

### 4.2.1 Elements communs à <teiCorpus> et aux documents individuels

#### 4.2.1.1 Description du projet
Dans <projectDesc>, nous décrivons le contexte de production des fichiers XML-TEI, et de la constitution du corpus.

#### 4.2.1.2 Déclaration des balises (tagsDecl)
Dans l'élément <tagsDecl>, nous donnons des informations sur la fréquence d'apparition d'éléments particuliers. Cette liste d'éléments respecte celle utilisée par le projet ParlaMint et pourra être utilisée pour valider l'intégrité et une meilleure intéropérabilité des fichiers TEI en cas d'échange des données.

            <namespace name="http://www.tei-c.org/ns/1.0">
               <tagUsage gi="body" occurs="1"/>
               <tagUsage gi="desc" occurs="188"/>
               <tagUsage gi="div" occurs="3"/>
               <tagUsage gi="head" occurs="3"/>
               <tagUsage gi="incident" occurs="18"/>
               <tagUsage gi="note" occurs="3"/>
               <tagUsage gi="seg" occurs="595"/>
               <tagUsage gi="u" occurs="256"/>
            </namespace>

### 4.2.2 Elements supplémentaires utilisés dans <teiCorpus>

#### 4.2.2.1 Déclaration des pratiques éditoriales (editorialDecl)

#### 4.2.2.2 Informations sur les application utilisées pour traiter les documents dans <appInfo>
Nous utilisons l'élément <appInfo> pour donner des informations sur les logiciels et les langages utilisés pour traiter les documents numérisés.

         <appInfo>
            <application ident="outil-soduco" version="1">
               <label>Outil Soduco</label>
               <desc>Application utiliser pour océriser les textes</desc>
            </application>
         </appInfo>
         <appInfo>
            <application ident="python" version="3.10.4">
               <label>Python</label>
               <desc>Language utilisé pour baliser automatiquement le document en XML-TEI</desc>
            </application>
         </appInfo>

#### 4.2.2.3 Déclaration des classifications dans <classDecl>
Dans <teiCorpus>, l'élément <classDecl> contient les taxonomies utilisées. Nous utilisons deux taxonomies réduites, provenant des taxonomies utilisées par le projet ParlaMint. Nous utilisons une taxonomie pour la législature et une autre pour les types d'orateurs. L'exemple ci-dessous présente un extrait de la taxonomie des types d'orateur (ici, pour un orateur non identifié).

               <category xml:id="unknown">
                  <catDesc xml:lang="fr"><term>Orateur inconnu</term>: orateur non
                     identifié</catDesc>
                  <catDesc xml:lang="en"><term>Unknown speaker</term>: unidentified
                     speaker</catDesc>
               </category>

## 4.3 Métadonnées non bibliographiques (profileDesc)

### 4.3.1 Elements communs à <teiCorpus> et aux documents individuels

#### 4.3.1.1 Utilisation des langues<langUsage>

#### 4.3.1.2 Description du lieu de la séance<settingDesc>

### 4.3.2 Elements supplémentaires utilisés dans <teiCorpus>

#### 4.3.2.1 <textClass>

#### 4.3.2.2 Index des participants <particDesc>

standoff

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
