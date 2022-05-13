# Guide annotations OCR

## Entités nommées

| **NER**         | **Étiquettes annotation OCR**     | *Exemples*                                                                                            |
|-----------------|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| **personne**    | persName (anciennement PER)       | ```<persName>M. Leygues</persName>```                                                                 |
|                 |                                   | ```MM. <persName>Paul Déroulède</persName> <persName>Georges Laguerre</persName>```                   |
|                 |                                   | ```<persName>Voix au centre</persName>. Ce n'est pas une rectification.```                            |
| **rôle**        | roleName (anciennement ACT)       | ```<persName>M. Henri Lavertujon, l'un des <roleName>secrétaires</roleName></persName>```             |
|                 |                                   | ```<persName>M. Reybert, <roleName>rapporteur</roleName></persName>.```                               |
|                 |                                   | ```<persName>M. le <roleName>ministre des finances</roleName></persName>```                           |
| **lieu**        | placeName (anciennement LOC)      | ```<placeName>Département de la Corrèze, arrondissement de Tulle, 1re circonscription</placeName>.``` |
| **institution** | orgName (transformation de TITRE) | ```la <orgName>Chambre des députés</orgName>```                                                       |

## Structure du texte

https://docs.google.com/spreadsheets/d/1AyXBBcTLiMK7k0AB32O1PB5vG0TyTCh2gbSHY2Qmck8/edit?usp=sharing
