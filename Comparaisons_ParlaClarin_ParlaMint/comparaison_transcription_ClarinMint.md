| Transcription du texte        | Exemples        | ParlaClarin                                                                                                                                                                        | Exemples       | ParlaMint                                                                    |
|-------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------|
| **Guidelines TEI**                |                 |   Transcriptions of Speech, Names, Dates, People, and Places, Default Text Structure, Elements Available in All TEI Documents, Simple Analytic Mechanisms                                                                                                                                                          |                |Transcriptions of Speech, Names, Dates, People, and Places, Default Text Structure, Elements Available in All TEI Documents, Simple Analytic Mechanisms                                                                              |
| **Divisions**                     |                 | < text >                                                                                                                                                                           |                | < text >                                                                     |
|                               | *cf exemple 1.1*  | < front > avec une < div > contenant des < head > et < docDate > pour l'en-tête du doc                                                                                             |                |                                                                              |
|                               |                 | < body >                                                                                                                                                                           |                | < body >                                                                     |
|                               | *cf exemple 1.2*  | < listEvent > contenant les métadonnées des votes                                                                                                                                  |                |                                                                              |
|                               |                 | au moins 1 < div >                                                                                                                                                                 | *cf exemple 1.3* | au moins 1 < div >, @xml:id="id div" @n="numéro div" @type="debateSection"   |
|                               |                 | < head >, < note > @type                                                                                                                                                           |                | < pb >, < head >, < note > @type                                             |
| **Énoncés**                       | *cf exemple 1.4*  | < u >                                                                                                                                                                              | *cf exemple 1.4* | < u >                                                                        |
|                               |                 | @who renvoie vers < person >, @ana renvoie vers type de locuteur                                                                                                                   |                | @who renvoie vers < person >, @ana renvoie vers type de locuteur, @xml:id    |
|                               |                 | < seg > pour paragraphes                                                                                                                                                           |                | < seg > pour paragraphes, @xml:id                                            |
| **Commentaires du transcripteur** |*cf exemple 1.5*                 | < note > @type                                                                                                                                                                     |*cf exemple 1.5*                 | < note > @type                                                               |
|                               |                 | < incident >, puis < desc > @xml:lang                                                                                                                                              |                | < incident > @type, puis < desc > @xml:lang                                  |
|                               |                 | < vocal > @who, puis < desc > @xml:lang                                                                                                                                            |                | < vocal > @type, puis < desc > @xml:lang                                     |
|                               |                 | < kinesic > @who, puis < desc > @xml:lang                                                                                                                                          |                | < kinesic > @type, puis < desc > @xml:lang                                   |
| **Lacunes**                       | *cf exemple 1.6*  | < gap > puis < desc > @reason (inaudible, editorial) @xml:lang si editorial                                                                                                        | *cf exemple 1.6* | < gap > puis < desc > @reason  (inaudible, editorial) @xml:lang si editorial |
| **Interruptions de la parole**    |                 |                                                                                                                                                                                    | *cf exemple 1.7* | < note > ou < vocal > @type puis < desc >                                    |
|                               | *cf exemple 1.8*  | < u > @next @prev                                                                                                                                                                  | *cf exemple 1.8* | < u > @next @prev                                                            |
| **Adresses, questions, réponses** | *cf exemple 1.9*  | < u > @toWho (personne à laquelle s'adresse le discours) @who, @ana taxonomie définie dans l'en-tête portant sur les types d'énoncés, @xml:id (id de la question ou de la réponse) |                |                                                                              |
| **Résultats des votes**           | *cf exemple 1.10*  | < note > avec < measure > @xml:id, @corresp (#ayes #noes définis dans < taxonomy > dans l'en-tête), @quantity                                                                         | *cf exemple 1.9* | < note > @type                                                               |
|                               | *cf exemple 1.11* | < listEvent > juste après < body > contenant les métadonnées des votes : divisées en < event > < desc > < measure >                                                                |                |                                                                              |




**Exemple 1.1** : ParlaClarin
```
<front>
    <div type="preface">
    <!--  text before speeches started  -->
        <head>THE PARLIAMENT OF THE REPUBLIC OF SLOVENIA</head>
        <head>Continuation of the second session</head>
        <docDate when="2011-01-30">30th January 2011</docDate>
    </div>
</front>
```

**Exemple 1.2** : ParlaClarin
```
<body>
	<listEvent>
		[...]
	</listEvent>
	<div>
		[...]
	</div>
</body>
```

**Exemple 1.3** : ParlaMint
```
<div xml:id="ParlaMint-FR_2017-07-03-O1001_d1_2" n="2" type="debateSection">
	[...]
</div>
```

**Exemple 1.4** : ParlaClarin
```
<note type="speaker">MILAN KUČAN:</note>
<u who="#KučanMilan" ana="#chair">
	<seg>We will now vote on the Third Amendment.</seg>
	<seg>How are you going to vote?</seg>
</u>
```

**Exemple 1.4** : ParlaMint
```
<note type="debate">TITRE_TEXTE_DISCUSSION</note>
<u who="#PA332747" xml:id="ParlaMint-FR_2017-07-03-O1001_u3" ana="#speaker">
	<seg xml:id="ParlaMint-FR_2017-07-03-O1001_u3.1">Monsieur le Président de la République, vous avez la parole.</seg>
</u>
```
**Exemple 1.5** : ParlaClarin
```
<note type="speaker">The president, Dr. Milan Brglez:</note>
<note type="time">The sesssion began at 10 o'clock.</note>

<vocal who="#opposition">
	<desc xml:lang="en">shouting</desc>
</vocal>

<incident>
	<desc xml:lang="en">army storms the parliament</desc>
</incident>

<kinesic who="#governmet">
	<desc xml:lang="en">clapping</desc>
</kinesic>
```
**Exemple 1.5** : ParlaMint
```
<note type="speaker">The president, Dr. Milan Brglez:</note>
<note type="time">The sesssion began at 10 o'clock.</note>

<vocal type="interruption">
	<desc>sounds from the chamber</desc>
</vocal>

<kinesic type="signal">
	<desc>signal for end of debate</desc>
</kinesic>

<incident type="action">
	<desc>minute of silence</desc>
</incident>
```

**Exemple 1.6** : ParlaClarin et ParlaMint
```
<gap reason="inaudible">
	<desc>Microphone off</desc>
</gap>

<gap reason="editorial">
	<desc xml:lang="en">Table omitted</desc>
</gap>
```
 
**Exemple 1.7** : ParlaMint
```
<u who="#BorisJohnson" ana="#regular">
	<seg>I propose a no-deal Brexit. 
	<vocal type="interruption">
 		<desc>Jeremy Corbyn: Traitor!</desc>
	</vocal> Because England does not want any dealings with the European Union.</seg>
</u>
```

**Exemple 1.8** : ParlaClarin et ParlaMint
```
<u who="#BorisJohnson" xml:id="GB001.8.3" 
next="#GB001.8.5">I propose a no-deal Brexit.</u>
<u who="#JeremyCorbyn" xml:id="GB001.8.4">Traitor!</u>
<u who="#BorisJohnson" xml:id="GB001.8.5"
 prev="#GB001.8.3">Because England does not want any dealings with the European Union.</u>
```

 **Exemple 1.9** : ParlaClarin
```
<u xml:id="q_1" who="#kappa" toWhom="#eta" ana="#question">
	<seg>I would like to ask the Mr. Eta about ...</seg>
</u>
<u xml:id="a_1" who="#eta" toWhom="#kappa" ana="#answer">
	<seg>Mr. Kappa, BNAT was the only umbrella professional body for ...</seg>
</u>
```
 
 **Exemple 1.10** : ParlaClarin
```
<note type="summary">(Question carried by
	<measure xml:id="quantity_1" corresp="#ayes" quantity="72">72</measure> to
	<measure xml:id="quantity_2" corresp="#noes" quantity="56">56</measure>
 votes)</note>
```
 **Exemple 1.10** : ParlaMint
```
<note type="vote-ayes">84 voted for the adoption of the measure.</note>
<note type="vote-noes">2 voted against the adoption of the measure.</note>
```

 **Exemple 1.11** : ParlaClarin
```
<listEvent>
	<event type="voting" xml:id="vot1" ana="#approved" corresp="true">
		<desc>
			<measure type="quorum" xml:id="vot1-quo1" ana="#majority" quantity="80"/>
			<measure type="count" xml:id="vot1-cnt2" ana="#ayes" corresp="#quantity_1" quantity="72"/>
			<measure type="count" xml:id="vot1-cnt3" ana="#noes" corresp="#quantity_2" quantity="34"/>
		</desc>
	</event>
	<event type="recount" xml:id="rct1" ana="#approved" corresp="true">
		<desc>
			<measure type="count" xml:id="vot-cnt1" ana="#ayes" corresp="#quantity_3" quantity="76"/>
		</desc>
	</event>
	<listRelation>
		<relation name="recount" active="#rct1"passive="#vot1"/>
	</listRelation>
</listEvent>
```
