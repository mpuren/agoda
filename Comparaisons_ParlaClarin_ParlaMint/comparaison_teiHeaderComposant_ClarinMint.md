| **teiHeader du composant** (métadonnées spécifiques au texte en question) | **Exemples**  | **ParlaClarin**                                                                                                                                                                                                                                                                                                         | **teiHeader du composant** (métadonnées spécifiques au texte en question) | **Exemples**  | **ParlaClarin**                                                                                                                                                                                                                                                                                                         | **Exemples**  | **ParlaMint**                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Exigences générales**                                                   |               | Il est recommandé que les métadonnées communes à l'ensemble du corpus soient stockées dans l'en-tête TEI du corpus, tandis que les métadonnées spécifiques au texte se trouvent dans l'en-tête TEI du texte du corpus. Relate que les métadonnées pertinentes pour les débats, sinon il faut se référer aux guidelines. |               | La plupart des métadonnées contiennent du texte libre, ces données doivent être données en langue anglaise, pour aider les chercheurs d'autres pays à les comprendre, et il est recommandé de les donner aussi dans la langue locale dans laquelle la transcriptions parlementaires est écrite, pour qu'un chercheur local puisse les utiliser dans sa langue maternelle |
| **Description bibliographique**                                           |               | **< fileDesc >**                                                                                                                                                                                                                                                                                                        |               | **< fileDesc >**                                                                                                                                                                                                                                                                                                                                                         |
|                                                                           | *Exemple 1.1* | **< titleStmt >**  contient :  **< title >**  titre du composant (extension du titre racine du corpus) +  **< meeting >**  spécification de la session particulière                                                                                                                                                     | *Exemple 1.1* | **< titleStmt >** contient (idem que corpus) : **< title >** titre du composant (extension du titre racine du corpus) + **< meeting >** spécification de la session particulière + **< respStmt >** personnes responsable + **< funder >** financeurs du projet                                                                                                          |
|                                                                           |               |                                                                                                                                                                                                                                                                                                                         | *Exemple 1.2* | **< editionStmt >** contient (idem que corpus) : **< edition >**                                                                                                                                                                                                                                                                                                         |
|                                                                           |               |                                                                                                                                                                                                                                                                                                                         | *Exemple 1.3* | **< extent >** contient (idem que corpus) : **< measure >** pour le nombre de discours et de mots                                                                                                                                                                                                                                                                        |
|                                                                           | *Exemple 1.4* | **< publicationStmt >**  contient (idem que corpus) :  **< authority >** +  **< availability >**  licence + **< distributor >** + **< date >**  date de publication                                                                                                                                                     | *Exemple 1.4* | **< publicationStmt >** contient (idem que corpus) : **< publisher >** éditeur du corpus + **< idno >** l'identifiant du fichier + **< availability >** licence + **< date >** date de publication                                                                                                                                                                       |
|                                                                           | *Exemple 1.5* | **< sourceDesc >**  contient (presque idem que corpus) :  **< bibl >**  avec  **< title >**  propre au composant +  **< idno >**  que si la transcription est disponible sur le web                                                                                                                                     | *Exemple 1.5* | **< sourceDesc >** contient (presque idem que corpus) : **< bibl >** avec **< title >** propre au composant + **< idno >** que si la transcription est disponible sur le web + **< date >** propre au composant                                                                                                                                                          |
| **Description de l'encodage**                                             |               | **< encodingDesc >** : absence                                                                                                                                                                                                                                                                                          |               | **< encodingDesc >** (élément en moins pour le composant)                                                                                                                                                                                                                                                                                                                |
|                                                                           |               |                                                                                                                                                                                                                                                                                                                         | *Exemple 2.1* | **< projectDesc >** contient : **< p >**                                                                                                                                                                                                                                                                                                                                 |
|                                                                           |               |                                                                                                                                                                                                                                                                                                                         | *Exemple 2.2* | **< tagsDecl >** contient : le compte de toutes les balises utilisées de la partie données **< namespace >** + **< tagUsage >**                                                                                                                                                                                                                                          |
| **Description des aspects non bibliographiques du texte**                 | *Exemple 3.1* | **< profileDesc >**                                                                                                                                                                                                                                                                                                     | *Exemple 3.1* | **< profileDesc >** (élément en moins pour le composant)                                                                                                                                                                                                                                                                                                                 |
|                                                                           |               | **< settingDesc >**  contient :  **< setting >**  avec  **< name >**  et  **< date >** (moment de la séance)                                                                                                                                                                                                            |               | **< settingDesc >** contient (presque idem que corpus) : **< setting >** avec **< name >** et **< date >**(lieu et moment de la séance)                                                                                                                                                                                                                                  |
| **Révision**                                                              |               |                                                                                                                                                                                                                                                                                                                         | *Exemple 4.1* | **< revisionDesc >** : documente les révisions effectuées, série d'éléments **< change >** + @when donne la date de la modification + **< name >** + description texte libre de la modification                                                                                                                                                                          |










**Exemple 1.1** : < titleStmt >
ParlaClarin
```
<titleStmt>
<!--  There are no rules on how these titles should be written  -->
<title>The parliament of the Republic of Slovenia</title>
<title>Continuation of the second session</title>
<title>30th January 2011</title>
<meeting n="2" corresp="#DZ" ana="#parla.meeting"/>
</titleStmt>
```
ParlaMint
```
<titleStmt>
<title type="main" xml:lang="fr">Corpus parlementaire français ParlaMint-FR, session ordinaire [ParlaMint]</title>
<title type="main" xml:lang="en">French parliamentary corpus ParlaMint-FR, ordinary session [ParlaMint]</title>
<title type="sub" xml:lang="fr">Comptes-rendus des débats en séance publique de l'Assemblée Nationale, séance : 1, 03/07/2017</title>
<title type="sub" xml:lang="en">Proceedings of the debates in plenary sitting of the Assemblée Nationale, sitting: 1, 03/07/2017</title>
<meeting n="O1" corresp="#PO717460" ana="#parla.lower #parla.session #PO717460">session ordinaire</meeting>
<meeting n="1" corresp="#PO717460" ana="#parla.lower #parla.sitting #PO717460">1. séance</meeting>
<respStmt>
<persName>Sascha Diwersy</persName>
<persName>Giancarlo Luxardo</persName>
<resp xml:lang="en">ParlaMint TEI XML corpus encoding</resp>
</respStmt>
<funder>
<orgName xml:lang="en">The CLARIN research infrastructure</orgName>
</funder>
</titleStmt>
```

**Exemple 1.2** : < editionStmt >
ParlaMint
```
<editionStmt>
<edition>2.1</edition>
</editionStmt>
```

**Exemple 1.3** : < extent >
ParlaMint
```
<extent>
<measure unit="speeches" quantity="38" xml:lang="en">38 speeches</measure>
<measure unit="speeches" quantity="38" xml:lang="fr">38 interventions</measure>
<measure unit="words" quantity="26108" xml:lang="en">26,108 words</measure>
<measure unit="words" quantity="26108" xml:lang="fr">26 108 mots</measure>
</extent>
```

**Exemple 1.4** : < publicationStmt >
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
<date when="2019-07-24">24. 7. 2019</date>
</publicationStmt>
```
ParlaMint
```
<publicationStmt>
<publisher xml:lang="en">CLARIN research infrastructure</publisher>
<idno subtype="handle" type="URI">http://hdl.handle.net/11356/1432</idno>
<availability status="free">
<licence>http://creativecommons.org/licenses/by/4.0/</licence>
<p xml:lang="en">This work is licensed under the terms of the Creative Commons Attribution 4.0 International License</p>
</availability>
<date when="2021-06-08">June 8, 2021</date>
</publicationStmt>
```

**Exemple 1.5** : < sourceDesc >
ParlaClarin 
```
<bibl>
<title>Continuation of the second session</title>
<idno type="URI">https://www.dz-rs.si/wps/portal/Home/deloDZ/seje/evidenca?mandat=III&type=sz&uid=6A9C9127BB26C19AC12569E600561164</idno>
<date when="2001-01-30">30. 1. 2001</date>
</bibl>
```
ParlaMint
```
<bibl>
<title type="main" xml:lang="fr">Travaux parlementaires (Assemblée nationale)</title>
<title type="sub" xml:lang="fr">Débats en séance publique - Comptes rendus au format XML</title>
<idno type="URI">http://data.assemblee-nationale.fr/travaux-parlementaires/debats</idno>
</bibl>
```

**Exemple 2.1** : < projectDesc >
ParlaMint
```
<projectDesc>
<p xml:lang="fr">
<ref target="https://www.clarin.eu/content/parlamint">ParlaMint</ref>
</p>
<p xml:lang="en">
<ref target="https://www.clarin.eu/content/parlamint">ParlaMint</ref>
is a project that aims to (1) create a multilingual set of comparable corpora of parliamentary proceedings uniformly encoded according to the
<ref target="https://github.com/clarin-eric/parla-clarin">Parla-CLARIN recommendations</ref>
and covering the COVID-19 pandemic from November 2019 as well as the earlier period from 2015 to serve as a reference corpus; (2) process the corpora linguistically to add Universal Dependencies syntactic structures and Named Entity annotation; (3) make the corpora available through concordancers and Parlameter; and (4) build use cases in Political Sciences and Digital Humanities based on the corpus data.
</p>
</projectDesc>
```

**Exemple 2.2** : < tagsDecl >
ParlaMint
```
<tagsDecl>
<namespace name="http://www.tei-c.org/ns/1.0">
<tagUsage gi="body" occurs="1"/>
<tagUsage gi="desc" occurs="31"/>
<tagUsage gi="div" occurs="5"/>
<tagUsage gi="head" occurs="5"/>
<tagUsage gi="incident" occurs="5"/>
<tagUsage gi="kinesic" occurs="24"/>
<tagUsage gi="note" occurs="5"/>
<tagUsage gi="seg" occurs="363"/>
<tagUsage gi="u" occurs="38"/>
<tagUsage gi="vocal" occurs="2"/>
<tagUsage gi="w" occurs="27612"/>
</namespace>
</tagsDecl>
```

**Exemple 3.1** : < profileDesc >
ParlaMint
```
<profileDesc>
<settingDesc>
<setting>
<name type="city">Paris</name>
<name type="country" key="FR">France</name>
<date when="2017-07-03">03/07/2017</date>
</setting>
</settingDesc>
</profileDesc>
```

**Exemple 4.1** : < profileDesc >
ParlaMint
```
<revisionDesc>
<change when="2021-02-01">
<name>Giancarlo Luxardo</name>
: Initial version.
</change>
</revisionDesc>
```
