| teiHeader du corpus                                       | Exemples         | ParlaClarin                                                                                                                                                                                                                                                                                                                                                                                                                       | Exemples         | ParlaMint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **TEI Guidelines**                                        |                  | Section on the TEI header                                                                                                                                                                                                                                                                                                                                                                                                         |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Exigences générales**                                   |                  | **Caractères** idem. Préciser ces règles dans **< hyphenation >**. Pas de préservation de la mise en page.                                                                                                                                                                                                                                                                                                                        |                  | **Caractères** en UTF-8, traits d'union en fin de ligne sont supprimés (et les mots joints)(cela simplifie le traitement linguistique), le texte contenu dans un élément ne doit ni commencer, ni finir avec un espace, pas de préservation de la mise en page.                                                                                                                                                                                                                                                                                                                                                                           |
|                                                           |                  | **Normalisation** : idem pour @xml:lang, pas d'@xml:id, et recommande que les balises soient anglais ainsi que les valeurs des attributs.                                                                                                                                                                                                                                                                                         |                  | **Normalisation** : pour les codes pays en deux lettres --> norme ISO 3166-1 alpha-2 ; pour les subdivisions de pays --> norme ISO 3166-2 ; codes des langues dans @xml:lang --> BCP 47 (norme ISO_639-1) ; 2 langues --> la langue locale (langue de la transcription) et l'anglais ; date/ heure (@when @from @to) --> norme ISO 8601.                                                                                                                                                                                                                                                                                                  |
|                                                           |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                   |                  | **Noms de fichiers** (structure rigide) : nom du fichier racine corpus se construit comme ceci "ParlaMint-[code du pays ou région]". L'ensemble du corpus doit être stocké dans un répertoire portant le même  nom que celui du fichier                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Structure du corpus**                                   | *cf exemple 1.1* | **< teiCorpus >** idem.                                                                                                                                                                                                                                                                                                                                                                                                           | *cf exemple 1.1* | **< teiCorpus >** comme racine pour chaque **corpus** ParlaMint. **@xmlns** obligatoire pour déterminer l'espace de nom TEI (tous les éléments enfants héritent de cet espace de nom), **@xml:id** obligatoire pour donner l'identifiant de la racine (unique et respecte exigence du W3C), doit être identique au nom du fichier, **@xml:lang** obligatoire pour donner la langue des métadonnées mais aussi principalement des transcriptions.                                                                                                                                                                                          |
|                                                           |                  | **< teiHeader >** idem. Recommandé que les **métadonnées communes** à l'ensemble du corpus soient stockées dans le < teiHeader > du corpus. Intérêt pour les métadonnées particulièrement pertinentes pour les corpus d'actes parlementaires. Pas vraiment de spécification détaillée dans l'ODD.                                                                                                                                 |                  | **< teiHeader >** pour les métadonnées du corpus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                           |                  | **< xi:include >** idem.                                                                                                                                                                                                                                                                                                                                                                                                          |                  | **< xi:include >** permettant de relier le corpus avec les fichiers de composants du corpus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Description bibliographique**                           |                  | **< fileDesc >**                                                                                                                                                                                                                                                                                                                                                                                                                  |                  | **< fileDesc >**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                           | *cf exemple 2.1* | **< titleStmt >** contient mention de titre et personnes/institutions responsables de son contenu intellectuel, < title >, < author > avec un @ref (renvoie vers fiche de la personne) puis < forename > < surname > pour l'auteur du corpus, < editor > (responsabilité secondaire) avec  un @ref < forename > < surname >, < respStmt > idem que ParlaMint, < funder > pour le financeur du projet (sans balise à l'intérieur). | *cf exemple 2.1* | **< titleStmt >** contenant des < title > (titre du corpus en anglais, dans la langue locale, @xml:lang, @type='main' ou 'sub'),  < meeting > spécification de la ou des sessions particulières du parlement contenues dans le corpus (@n, @corresp = organe gouvernemental, @ana = divers pointeurs, texte),  < respStmt > les personnes responsables de la compilation du corpus, et le ou les financeurs du projet contenant < persName > avec @ref pour mettre URI donnant info sur la personne et < resp > < funder > donne info sur les organisations qui ont contribué financièrement à la compilation du corpus avec < orgName >. |
|                                                           | *cf exemple 2.2* | **< editionStmt >** idem.                                                                                                                                                                                                                                                                                                                                                                                                         | *cf exemple 2.2* | **< editionStmt >** contenant < edition > (version du corpus définit au moment du versionning sémantique).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                           | *cf exemple 2.3* | **< extent >** idem, mais pas de @xml:lang.                                                                                                                                                                                                                                                                                                                                                                                       | *cf exemple 2.3* | **< extent >** donne la taille du corpus entier (nb de discours, nb de mots) contient < measure > @unit @quantity @xml:lang, inséré à la toute fin avec un script.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                           | *cf exemple 2.4* | **< publicationStmt >** < authority > pour l'autorité de publication autre qu'un éditeur/ distributeur, puis < avaibility > comprenant < licence > @target et < p >, < distributor > et < date > @when pour  la date de construction du corpus ou la publication.                                                                                                                                                                 | *cf exemple 2.4* | **< publicationStmt >** donne info sur l'éditeur du corpus < publisher > (< orgName > ref >), l'URI < idno >, sous quelle licence il est publié < availability > (< license > < p >),  et sa date < date >.                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                           | *cf exemple 2.5* | **< sourceDesc >** description de la source pour l'ensemble du corpus, idem.                                                                                                                                                                                                                                                                                                                                                      | *cf exemple 2.5* | **< sourceDesc >** pour décrire la source numérique originale du corpus, contient un < bibl > suivi de < title > < idno > < date >.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Description de l'encodage**                             |                  | **< encodingDesc >**                                                                                                                                                                                                                                                                                                                                                                                                              |                  | **< encodingDesc >**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                           |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                   | *cf exemple 3.1* | **< projectDesc >** pour expliquer le projet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                           |                  | **< editorialDecl >** si texte source modifié (élément non pris en charge dans l'encodage TEI),  pouvant contenir < correction >  < normalization > < hyphenation > < quotation > < segmentation > < interpretation >.                                                                                                                                                                                                            | *cf exemple 3.2* | **< editorialDecl >** idem, @xml:lang dans le < p >.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                           | *cf exemple 3.3* | **< appInfo >** puis < application > (@version de l'outil, @ident spécifie l'outil) puis < label > nom de l'outil puis < desc >  quand mise en place d'une procédure automatique pour encoder le texte (par exemple **balisage automatique linguistique**).                                                                                                                                                                       | *cf exemple 3.3* | **< appInfo >** idem.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                           |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                   | *cf exemple 3.4* | **< tagsDecl >** qui permet de donner le compte pour chacune des balises utilisées dans le corps du texte de l'ensemble du corpus suivi d'un < namespace > puis d'un ensemble de < tagUsage > @gi pour nom de la balise @occurs pour l'occurence.                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                           | *cf exemple 3.5* | **< classDecl >** pour définir les vocabulaires à l'aide d'un ensemble de < taxonomy > avec @xml:id (on y  fait référence avec @ana dans le corps du texte), ensemble de  < category > contenant un < catDesc >                                                                                                                                                                                                                   | *cf exemple 3.5* | **< classDecl >** idem (3 vocabulaires définis pour ce projet, taxonomie sous-corpus, legislative, type de rapporteur, ), @xml:id et @xml:lang en plus.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Description des aspects non bibliographiques du texte** |                  | **< profileDesc >**                                                                                                                                                                                                                                                                                                                                                                                                               |                  | **< profileDesc >**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                           | *cf exemple 4.1* | **< settingDesc >** idem.                                                                                                                                                                                                                                                                                                                                                                                                         | *cf exemple 4.1* | **< settingDesc >** (contextualisation) contient un < setting > avec  des < name > @type @key permettant d'indiquer le lieu de la prise de parole, intervalle des dates des transcriptions < date > @from @to aussi.                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                           |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                   | *cf exemple 4.2* | **< textClass >** contenant un < catRef > permettant de donner des info sur la nature/ sujet d’un texte selon des  termes issus d’un système de classification standardisé, @scheme donne le schéma qu'elle utilise, @target donne des pointeurs.                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                           | *cf exemple 4.3* | **< particDesc >** idem pour < listPerson >, presque idem pour < listOrg > et < listRelation > (attributs en moins).                                                                                                                                                                                                                                                                                                              | *cf exemple 4.3* | **< particDesc >** donne infos sur les partis politiques/ autres organisations importantes et sur les orateurs. < listOrg > listes les groupes d'organistion, contient ensemble de < org > (< orgName > < event > < idno > < listEvent >) et < listRelation >  ( < relation > @active @passive @mutual). < listPeron > liste les participants, contient < person > (@xml:id pour référencer ensuite la personne dans la transcription, < persName > < surName >, < sex > @value ayant pour valeur F/M/O/N/U),  et < affiliation > pour dire à quel partis il se rattache, possible d'ajouter < birth > et < death >.                      |
|                                                           | *cf exemple 4.4* | **< langUsage >** idem.                                                                                                                                                                                                                                                                                                                                                                                                           | *cf exemple 4.4* | **< langUsage >** pour définir les langues utilisées dans le corpus (généralement langue locale + anglais) @ident et @xml:lang, possible ajouter @usage pour indiquer le pourcentage  de l'utilisation de la langue au sein du corpus.                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Description des révisions**                             |                  |                                                                                                                                                                                                                                                                                                                                                                                                                                   | *cf exemple 5.1* | **< revisionDesc >** (facultatif), donne les révisions effectuées dans le corpus, contient < change > @when < name > (personne responsable du changement).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |


**Exemple 1.1** : < teiCorpus >
ParlaClarin 
```
<teiCorpus xml:lang="xx" xmlns="http://www.tei-c.org/ns/1.0">
 <teiHeader>
<!-- Common corpus metadata -->
 </teiHeader>
 <TEI xml:id="id.1">
  <teiHeader>
<!-- Document metadata -->
  </teiHeader>
  <text>
   <body>
<!-- Document text -->
   </body>
  </text>
 </TEI>
<!-- More TEI elements here -->
</teiCorpus>
```

ParlaMint
```
<teiCorpus xmlns="http://www.tei-c.org/ns/1.0" xml:id="ParlaMint-FR" xml:lang="fr">
<!-- Common corpus metadata: -->
 <teiHeader>...</teiHeader>
<!-- Reference to the first corpus component: -->
 <xi:include xmlns:xi="http://www.w3.org/2001/XInclude"
 href="2014/ParlaMint-NL_2014-04-16.xml"/>

<!-- Reference to the second corpus component: -->
 <xi:include xmlns:xi="http://www.w3.org/2001/XInclude"
 href="2014/ParlaMint-NL_2014-04-17.xml"/>

<!-- References to more corpus components: -->
 ...

</teiCorpus>
```

**Exemple 2.1** : < titleStmt >
ParlaClarin 
```
<titleStmt>
<title>Exemplar to illustrate Parla-CLARIN encoding</title>
<!--  Persons responsible for creating a corpus, for example:  -->
<!--  author of the corpus  -->
<author ref="http://viaf.org/viaf/305936424">
<forename>Andrej</forename>
<surname>Pančur</surname>
</author>
<!--  editor of the corpus  -->
<editor ref="https://orcid.org/0000-0002-1560-4099 http://viaf.org/viaf/15145066459666591823">
<forename>Tomaž</forename>
<surname>Erjavec</surname>
</editor>
<!--  other responsibilities in building the corpus  -->
<respStmt>
<resp>TEI corpus encoding</resp>
<persName ref="http://viaf.org/viaf/305936424">Andrej Pančur</persName>
<persName ref="https://orcid.org/0000-0002-1560-4099 http://viaf.org/viaf/15145066459666591823">Tomaž Erjavec</persName>
</respStmt>
<funder>CLARIN ERIC</funder>
</titleStmt>
```

ParlaMint 
```
<titleStmt>
 <title type="main">Slovenski parlamentarni korpus ParlaMint-SI [ParlaMint]</title>
 <title type="main" xml:lang="en">Slovenian parliamentary corpus ParlaMint-SI [ParlaMint]</title>
 <title type="sub">Zapisi sej Državnega zbora Republike Slovenije, 7. in 8. mandat (2014 - 2020)</title>
 <title type="sub" xml:lang="en">Minutes of the National Assembly of the Republic of Slovenia, Term 7 and 8 (2014 - 2020)</title>
 <meeting n="7" corresp="#DZ"
  ana="#parla.lower #parla.term #DZ.7">7. mandat</meeting>
 <meeting n="8" corresp="#DZ"
  ana="#parla.lower #parla.term #DZ.8">8. mandat</meeting>
 <respStmt>
  <persName ref="https://orcid.org/0000-0001-6143-6877">Andrej Pančur</persName>
  <persName ref="https://orcid.org/0000-0002-1560-4099">Tomaž Erjavec</persName>
  <resp>Kodiranje ParlaMint TEI XML</resp>
  <resp xml:lang="en">ParlaMint TEI XML corpus encoding</resp>
 </respStmt>
 <funder>
  <orgName>Raziskovalna infrastruktura CLARIN</orgName>
  <orgName xml:lang="en">The CLARIN research infrastructure</orgName>
 </funder>
 <funder>
  <orgName>Slovenska raziskovalna infrastruktura CLARIN.SI</orgName>
  <orgName xml:lang="en">The Slovenian research infrastructure CLARIN.SI</orgName>
 </funder>
</titleStmt>
```

**Exemple 2.2** : < editionStmt >
ParlaClarin et ParlaMint 
```
<editionStmt>
 <edition>2.1</edition>
</editionStmt>
```

**Exemple 2.3** : < extent >
ParlaClarin
```
<extent>
<measure unit="texts" quantity="1">1 text</measure>
<measure unit="utterances" quantity="6">6 utterances</measure>
</extent>
```

ParlaMint 
```
<extent>
 <measure unit="speeches" quantity="75122"
  xml:lang="sl">75.122 govorov</measure>
 <measure unit="speeches" quantity="75122"
  xml:lang="en">75,122 speeches</measure>
 <measure unit="words" quantity="20190034"
  xml:lang="sl">20.190.034 besed</measure>
 <measure unit="words" quantity="20190034"
  xml:lang="en">20,190,034 words</measure>
</extent>
```

**Exemple 2.4** : < publicationStmt >
ParlaClarin
```
<publicationStmt>
<authority>CLARIN ERIC</authority>
<availability>
<licence target="http://creativecommons.org/licenses/by/4.0/"/>
<p>
This work is licensed under the
<ref target="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</ref>
.
</p>
</availability>
<distributor>CLARIN Git repository</distributor>
<!--  date of corpus construction or publication  -->
<date when="2019-09-04">September 4th, 2019</date>
</publicationStmt>
```
ParlaMint 
```
<publicationStmt>
 <publisher>
  <orgName xml:lang="sl">Raziskovalna infrastrukutra CLARIN</orgName>
  <orgName xml:lang="en">CLARIN research infrastructure</orgName>
  <ref target="https://www.clarin.eu/">www.clarin.eu</ref>
 </publisher>
 <idno type="URI" subtype="handle">http://hdl.handle.net/11356/1432</idno>
 <availability status="free">
  <licence>http://creativecommons.org/licenses/by/4.0/</licence>
  <p xml:lang="sl">To delo je ponujeno pod <ref target="http://creativecommons.org/licenses/by/4.0/">Creative Commons Priznanje avtorstva 4.0 mednarodna licenca</ref>.</p>
  <p xml:lang="en">This work is licensed under the <ref target="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</ref>.</p>
 </availability>
 <date when="2021-06-11">11. 6. 2021</date>
</publicationStmt>
```

**Exemple 2.5** : < sourceDesc >
ParlaClarin et ParlaMint 
```
<sourceDesc>
 <bibl>
  <title type="main" xml:lang="sl">Zapisi sej Državnega zbora Republike Slovenije</title>
  <title type="main" xml:lang="en">Minutes of the National Assembly of the Republic of Slovenia</title>
  <idno type="URI">https://www.dz-rs.si</idno>
  <date from="2014-08-01" to="2020-07-16">1.8.2014 - 16.7.2020</date>
 </bibl>
</sourceDesc>
```

**Exemple 3.1** : < projectDesc >
ParlaMint
```
<projectDesc>
 <p xml:lang="sl">Glavni cilji projekta <ref target="https://www.clarin.eu/content/parlamint">ParlaMint</ref> so
   (1) izdelati večjezično množico na enak način kodiranih korpusov
   zapiskov parlamentarnih sej, (2) jezikoslovno označiti te korpuse; (3)
   narediti korpuse dostopne za prevzem in prek konkordančnikov; in (4)
   pripraviti primere uporabe korpusov v politologiji in digitalni
   humanistiki.</p>
 <p xml:lang="en">The <ref target="https://www.clarin.eu/content/parlamint">ParlaMint</ref>
   project aims to (1) create a multilingual set of uniformly encoded
   comparable corpora of parliamentary proceedings (2) process the
   corpora linguistically; (3) make the corpora available for download
   and through concordancers; and (4) build use cases in Political
   Sciences and Digital Humanities based on the corpus data.</p>
</projectDesc>
```

**Exemple 3.2** : < editorialDecl >
ParlaClarin
```
<editorialDecl>
<correction>
<p>No correction of source texts was performed.</p>
</correction>
<normalization>
<p>Only parts relevant to the example document were retained.</p>
</normalization>
<hyphenation>
<p>No end-of-line hyphens were present in the source.</p>
</hyphenation>
<quotation>
<p>Quotation marks have been left in the text and are not explicitly marked up.</p>
</quotation>
<segmentation>
<p>The texts are segmented into utterances (speeches) and segments (corresponding to paragraphs in the source transcription).</p>
</segmentation>
</editorialDecl>
```
ParlaMint
```
<editorialDecl>
 <correction>
  <p xml:lang="en">No correction of source texts was performed.</p>
 </correction>
 <normalization>
  <p xml:lang="en">Text has not been normalised, except for spacing.</p>
 </normalization>
 <hyphenation>
  <p xml:lang="en">No end-of-line hyphens were present in the source.</p>
 </hyphenation>
 <quotation>
  <p xml:lang="en">Quotation marks have been left in the text and are not explicitly marked up.</p>
 </quotation>
 <segmentation>
  <p xml:lang="en">The texts are segmented into utterances (speeches) and segments (corresponding to paragraphs in the source transcription).</p>
 </segmentation>
</editorialDecl>
```

**Exemple 3.3** : < appInfo >
ParlaClarin et ParlaMint
```
<appInfo>
 <application version="1.0"
  ident="reldi-tagger">
  <label>ReLDI morphosyntactic tagger and lemmatiser</label>
  <desc>Part-of-speech tagging and lemmatisation performed with ReLDI Tagger
     trained for Slovene and available from
  <ref target="https://github.com/clarinsi/reldi-tagger">GitHub</ref>.</desc>
 </application>
</appInfo>
```


**Exemple 3.4** : < tagsDecl >
ParlaMint
```
<tagsDecl>
 <namespace name="http://www.tei-c.org/ns/1.0">
  <tagUsage gi="text" occurs="414"/>
  <tagUsage gi="body" occurs="414"/>
  <tagUsage gi="div" occurs="414"/>
  <tagUsage gi="head" occurs="826"/>
  <tagUsage gi="u" occurs="75122"/>
  <tagUsage gi="seg" occurs="280971"/>
  <tagUsage gi="note" occurs="85525"/>
  <tagUsage gi="gap" occurs="7897"/>
  <tagUsage gi="vocal" occurs="1740"/>
  <tagUsage gi="incident" occurs="37"/>
  <tagUsage gi="kinesic" occurs="560"/>
  <tagUsage gi="desc" occurs="10234"/>
 </namespace>
</tagsDecl>
```

**Exemple 3.5** : < classDecl >
PalaClarin
```
<classDecl>
<!--  One or more optional taxonomies, with which we further classify the content and structure of parliamentary debates  -->
<taxonomy>
<desc>Types of speakers</desc>
<category xml:id="chair">
<catDesc>
<term>Chairperson</term>
: chairman of a meeting. See also
<term>The Speaker</term>
: an MP who has been elected by other MPs to act as Chair during debates in the House of Commons.
</catDesc>
</category>
</taxonomy>
<!--  Project-specific classification of the structure of parliamentary periods:  -->
<taxonomy>
<category xml:id="parla.term">
<catDesc>
<term>Legislative period</term>
: term of the parliament between general elections.
</catDesc>
<category xml:id="parla.session">
<catDesc>
<term>Legislative session</term>
: the period of time in which a legislature is convened for purpose of lawmaking, usually being one of two or more smaller divisions of the entire time between two elections. A session is a meeting or series of connected meetings devoted to a single order of business, program, agenda, or announced purpose.
</catDesc>
<category xml:id="parla.meeting">
<catDesc>
<term>Meeting</term>
: Each meeting may be a separate session or part of a group of meetings constituting a session. The session/meeting may take one or more days.
</catDesc>
<category xml:id="parla.sitting">
<catDesc>
<term>Sitting</term>
: sitting day
</catDesc>
</category>
</category>
</category>
</category>
</taxonomy>
</classDecl>
```
ParlaMint
```
<classDecl>...
<taxonomy xml:id="subcorpus">
  <desc xml:lang="sl">
   <term>Podkorpusi</term>
  </desc>
  <desc xml:lang="en">
   <term>Subcorpora</term>
  </desc>
  <category xml:id="reference">
   <catDesc xml:lang="sl">
    <term>Referenca</term>: referenčni podkorpus, do 2019-10-31</catDesc>
   <catDesc xml:lang="en">
    <term>Reference</term>: reference subcorpus, until 2019-10-31</catDesc>
  </category>
  <category xml:id="covid">
   <catDesc xml:lang="sl">
    <term>COVID</term>: COVID podkorpus, od 2019-11-01 dalje</catDesc>
   <catDesc xml:lang="en">
    <term>COVID</term>: COVID subcorpus, from 2019-11-01 onwards</catDesc>
  </category>
 </taxonomy>
</classDecl>
```

**Exemple 4.1** : < settingDesc >
ParlaClarin et ParlaMint
```
<settingDesc>
 <setting>
  <name type="place">Westminster</name>
  <name type="city">London</name>
  <name type="country" key="GB">U.K.</name>
  <date from="2015-01-01" to="2021-03-31"/>
 </setting>
</settingDesc>
```

**Exemple 4.2** : < textClass >
ParlaMint
```
<textClass>
 <catRef scheme="#parla.legislature"
  target="#parla.bi #parla.lower #parla.upper"/>
</textClass>
```
```
#parla.uni : Parlement monocaméral
#parla.bi #parla.lower : Parlement bicaméral, Chambre basse seulement
#parla.bi #parla.upper : Parlement bicaméral, Chambre haute seulement
#parla.bi #parla.lower #parla.upper : Parlement bicaméral, les deux Chambres
```

**Exemple 4.3** : < particDesc >
ParlaClarin et ParlaMint : < listPerson >
```
<listPerson>
 <person xml:id="AccettoMatej">
  <persName>
   <surname>Accetto</surname>
   <forename>Matej</forename>
  </persName>
  <sex value="M">moški</sex>
 </person>
 ...

</listPerson>
```

ParlaClarin : < listOrg >
```
<org xml:id="party.SDZ" role="politicalParty" xml:lang="sl">
<event from="1989-01-11" to="1991-10-13">
<label>existence</label>
</event>
<orgName full="yes" xml:lang="sl">Slovenska demokratična zveza</orgName>
<orgName full="yes">Slovenian Democratic Union</orgName>
<orgName full="init" xml:lang="sl">SDZ</orgName>
<idno type="wikimedia">https://en.wikipedia.org/wiki/Slovenian_Democratic_Union</idno>
</org>
```

ParlaMint : < listOrg >
```
<org ana="#parla.federal #parla.lower"
 role="parliament" xml:id="be_federal_parliament">
 <orgName full="yes" xml:lang="nl">Federaal Parlement van België</orgName>
 <orgName full="yes" xml:lang="en">Belgian Federal Parliament</orgName>
 <event from="1831-02-07">
  <label xml:lang="en">existence</label>
 </event>
 <idno xml:lang="nl" type="wikimedia">https://nl.wikipedia.org/wiki/Federaal_Parlement_van_Belgi%C3%AB</idno>
 <idno xml:lang="en" type="wikimedia">https://en.wikipedia.org/wiki/Belgian_Federal_Parliament</idno>
 <listEvent>
  <head xml:lang="nl">Zittingsperiode</head>
  <head xml:lang="en">Legislative period</head>
  <event to="2007-05-02" from="2003-06-05"
   xml:id="period_51">
   <label xml:lang="nl">Zittingsperiode 51</label>
   <label xml:lang="en">Legislative period 51</label>
  </event>
   ...
 <event from="2019-06-20"
   xml:id="period_55">
   <label xml:lang="nl">Zittingsperiode 55</label>
   <label xml:lang="en">Legislative period 55</label>
  </event>
 </listEvent>
</org>
```

ParlaClarin : < listRelation >
```
<relation name="successor" passive="#pp.SDZ" active="#pp.DS"/>
<relation xml:id="opposition.1" name="opposition" active="#party.SDZ" passive="#DZ"/>
```

ParlaMint : < listRelation >
```
 <relation name="coalition"
  mutual="#MR #OpenVld #N-VA #CD_en_V" from="2014-10-11" to="2018-12-09"
  ana="#period_54"/>
 <relation name="opposition"
  active="#Ecolo #cdH #DéFi #Vuye_Wouters #sp.a #PP #PS #PTB #FDF" passive="#government.BE"
  from="2014-10-11" to="2018-12-09" ana="#period_54"/>
```


**Exemple 4.4** : < langUsage >
ParlaClarin et ParlaMint
```
<langUsage>
 <language ident="sl" xml:lang="sl">slovenski</language>
 <language ident="en" xml:lang="sl">angleški</language>
 <language ident="sl" xml:lang="en">Slovenian</language>
 <language ident="en" xml:lang="en">English</language>
</langUsage>
```

**Exemple 5.1** : < revisionDesc >
ParlaMint
```
<revisionDesc>
 <change when="2021-06-11">
  <name>Tomaž Erjavec</name>: Finalized encoding.</change>
 <change when="2021-05-28">
  <name>Tomaž Erjavec</name>: Built corpus.</change>
</revisionDesc>
```
