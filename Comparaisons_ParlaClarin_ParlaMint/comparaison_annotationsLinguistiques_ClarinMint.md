| Annotations linguistiques | Exemples       | ParlaClarin                                                                                                                                                   | Exemples       | ParlaMint                                                                                                     |
|---------------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|---------------------------------------------------------------------------------------------------------------|
| **TEI Guidelines**            |                | Simple Analytic Mechanisms                                                                                                                                    |                | Simple Analytic Mechanisms                                                                                    |
|                           |                | Corpus annoté linguistiquement est séparé de sa version de base, mais l'annotation est inclue dans le corps du texte (pas de pointeurs vers le texte de base) |                | Corpus annoté linguistiquement est séparé de sa version de base, annotation est inclue dans le corps du texte |
| **Annotation de base**        | *cf exemple 2.1* | Phrases balisées avec < s >                                                                                                                                   | *cf exemple 2.1* | Phrases balisées avec < s >                                                                                   |
|                           |                | Mots avec < w >, forme de base d'un mot avec @lemma, tags analytiques/ balises partie du discours avec @msd                                                   |                | Mots avec < w >, forme de base d'un mot avec @lemma, tags analytiques/ balises partie du discours avec @msd   |
|                           |                | Symboles de ponctuation avec < pc >, pas d'attribut @lemma                                                                                                    |                | Symboles de ponctuation avec < pc >, pas d'attribut @lemma                                                    |
|                           |                | Blancs linguistiquement significatifs avec @join (no, right, left et both)                                                                                    |                | Blancs linguistiquement significatifs avec @join (no, right, left et both)                                    |
| **Autre méthode**             | *cf exemple 2.2* | Mots avec < w >, forme de base d'un mot avec @lemma, @ana sa valeur es un pointeur (pas très bien compris)                                                    | *cf exemple 2.2* | Mots avec < w >, forme de base d'un mot avec @lemma, @ana sa valeur es un pointeur (pas très bien compris)    |
| **Normalisation des mots**    | *cf exemple 2.3* |                                                                                                                                                               | *cf exemple 2.3* |                                                                                                               |
| **Annotation segmentaire**    | *cf exemple 2.4* |                                                                                                                                                               |                |                                                                                                               |
| **Entités nommées**           |                |                                                                                                                                                               | *cf exemple 2.5* | PER (personne)/ LOC (localisation)/ ORG (organisation)/ MISC (divers), spécifiées dans une taxonomie du header |

**Exemple 2.1** : ParlaClarin et ParlaMint
```
<s>
	<w msd="UPosTag=DET|Case=Gen|Gender=Neut|Number=Sing|PronType=Dem" lemma="ta">Tega</w>
	<w msd="UPosTag=PRON|PronType=Prs|Reflex=Yes|Variant=Short" lemma="se">se</w>
	<w msd="UPosTag=PART" lemma="sploh">sploh</w>
	<w msd="UPosTag=AUX|Mood=Ind|Number=Sing|Person=1|Polarity=Neg|Tense=Pres|VerbForm=Fin" lemma="biti">nisem</w>
	<w msd="UPosTag=VERB|Aspect=Perf|Gender=Masc|Number=Sing|VerbForm=Part" lemma="zavesti" join="right">zavedel</w>
 	<pc msd="UPosTag=PUNCT">.</pc>
</s>
```

**Exemple 2.2** : ParlaClarin et ParlaMint


**Exemple 2.3** : ParlaClarin
```
<w>abyste
	<w norm="aby" lemma="aby"/>
	<w norm="byste" lemma="být"/>
</w>
```
ou
```
<w norm="najlepši" lemma="lep">
	<w>nar</w>
	<w>lepši</w>
</w>
```
**Exemple 2.3** : ParlaMint
```
<w>abyste
	<w norm="aby" lemma="aby" msd="UPosTag=SCONJ"/>
	<w norm="byste" lemma="být" msd="UPosTag=AUX|Mood=Cnd|Number=Plur|Person=2|VerbForm=Fin"/>
</w>
```
ou
```
<w norm="najlepši" lemma="lep">
	<w>nar</w>
	<w>lepši</w>
</w>
```


**Exemple 2.4** : ParlaClarin
```
<s>
	<name type="person">
		<w>John</w>
		<w>Malkovič</w>
	</name>
	<w>went</w>
	<w>to</w>
	<name type="location">
		<w>New</w>
		<w>York</w>
	</name>
	<pc>.</pc>
</s>
```

**Exemple 2.5** : ParlaMint
```
<w lemma="and" msd="UPosTag=CCONJ">and</w>
<name type="ORG">
	<w lemma="Westminster" msd="UPosTag=PROPN|Number=Sing">Westminster</w>
	<w join="right" lemma="Hall" msd="UPosTag=PROPN|Number=Sing">Hall</w>
</name>
<w lemma="," msd="UPosTag=PUNCT">,</w>
```
