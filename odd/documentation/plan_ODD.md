# Plan ODD 

<hr/>

# 1. Introduction (Pierre Marie) - À rédiger
## 1.1 Contextualisation (Pierre et Marie) (à rédiger)
- Pierre
  - Mise en place de la 3ème République
  - Lois constitutionnelles
  - Système bicaméral et pouvoir des 2 chambres (Chambre haute vs Chambre basse)
  - Mode d'élection de la Chambre des députés
  - Durée du mandat et législature
  - Rôle de la Chambre des Députés

- Marie
  - Fonctionnement de la Chambre des députés : Fonctionnement des sesssions + Fonctionnement des séances + Prises de parole

- Marie et/ou Pierre
  - Rédaction des comptes-rendus
  
## 1.2 Objectifs scientifiques (Pierre) (à rédiger)
- exploiter les données : qu'est-ce que l'on veut extraire/ manipuler/ analyser.
- Importance de la structure et sens du texte = physique, logique, sémantique --> pris en compte dans le balisage.

## 1.3 Choix de transcription (Pierre et Marie) (à rédiger)
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
## 2.2 Structure des composants
## 2.3 Nommage des fichiers

<hr/>

# 3. Prérequis généraux (Pierre Marie Fanny) - À compléter
## 3.1 Caractères (Fanny) (à compléter)
## 3.2 Valeurs standards (Fanny)
## 3.3 Taxonomies (Marie) (à rédiger)
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

# 4. Métadonnées (Marie) - À compléter
## 4.1 Métadonnées bibliographiques (fileDesc)
### 4.1.1 Mention de titres (titleStmt)
### 4.1.2 Mention d'édition (editionStmt)
### 4.1.3 Taille du corpus (extent)
### 4.1.4 Mention de publication (publicationStmt)
### 4.1.5 Description de la source (sourceDesc)

## 4.2  Métadonnées de l'encodage (encodingDesc)
### 4.2.1 Elements communs à teiCorpus et aux documents individuels
### 4.2.2 Elements supplémentaires utilisés dans teiCorpus

## 4.3 Métadonnées non bibliographiques (profileDesc) (à rédiger)
### 4.3.1 Elements communs à <teiCorpus> et aux documents individuels
#### 4.3.1.1 Utilisation des langues<langUsage>
#### 4.3.1.2 Description du lieu de la séance<settingDesc>
### 4.3.2 Elements supplémentaires utilisés dans <teiCorpus>
#### 4.3.2.1 <textClass>
#### 4.3.2.2 Index des participants <particDesc>

<hr/>

# 5. Balisage physique (Fanny)
## 5.1 Balisage formel
## 5.2 Balisage logique
### 5.2.1 Éléments structurels du sommaire
### 5.2.2 Éléments structurels du corps du texte
### 5.2.3 Éléments structurels des parties complémentaires

<hr/>


# 6. Balisage sémantique (Fanny)
## 6.1 Éléments du discours
### 6.1.1 Énoncés
### 6.1.2 Commentaires des sténographes
### 6.1.3 Citations

## 6.2 Entités nommées
### 6.2.1 Personnes
### 6.2.2 Lieux
### 6.2.3  Organisations
### 6.2.4 Éléments temporels et éléments quantifiables

<hr/>

## 7. Bibliographie (Pierre Marie) - À rédiger

<hr/>

**À prendre en compte :**
- Si changement dans le plan, modifier tous les renvois présents dans la rédaction (cf. partie ...).
- Si changement dans la taxonomie des orateurs, reporter le changement dans la partie 1.6.1.1 Énoncés.
- Lorsque les valeurs de l'@xml:id du sommaire seront créées, ajouter une note à leur sujet en partie 1.5.2.1 Éléments structurels du sommaire.

