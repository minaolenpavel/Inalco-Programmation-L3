# TP №2 : Gestion de fichiers, formats csv et json

## Exercice 1 : Manipulation de fichiers textuels

### 1 

Si on considère qu'un mot est une suite de caractères séparée par un espace, alors le texte fait 46928 mots de long.

### 2 

Selon NLTK, le texte contient 54512 tokens.

### 3 

Le texte contient 8414 tokens uniques.

## Exercice 2 : Fichiers CSV

### 1 

### 2 

#### 1

C'est un fichier CSV avec un point-virgule (;) piur séparateur. Il recense toutes les communes de France, dans l'ordre des colonnes il contient pour chacune d'entre elles, le code INSEE de la commune, le nom de la commune, le code postal, le libellé d'acheminement, et il semblerait que la 5 ème colonne désigne le nom d'un village auquel la commune est rattachée. Ex : Vaux est un village rattaché à la commune d'Auxerre.

~~~
89024;AUXERRE;89000;AUXERRE;
89024;AUXERRE;89290;AUXERRE;VAUX
~~~

#### 2
13036 est le code postal d'Eyragues

#### 3

Marseille apparait 27 fois. Parce qu'il y a des villages qui sont rattachés à la commune de Marseille.

### 3 

#### 1 

C'est un fichier CSV.

#### 2

Etant né en 2003, le prénom le plus attribué cette année (sans considéraion de la mention "prénom rare") était Léa pour les filles (8961 entrées) et Lucas (8287 entrées) pour les garçons. Pour 2022 c'est Jade pour les filles (3420) et Gabriel pour les garçons (4889).

#### 3

#### 4 

Le prénim PAUL a été le plus donnée dans le 03 en 2021. 976 fois cette année là.

## Exercice 3 : Fichiers JSON

### 1

Les données sur les sénateurs sont organisées en liste d'objets. C'est une liste qui contient des objets avec des propriétés qui donnent des informations comme le matricule, le nom, ou la circonscription de chaque sénateur dans la liste.

### 2 

On retrouve : 

- Le matricule
- Le titre selon le sexe 
- Le nom/prénom d'usage
- L'état
- La date de naissance/décès
- Le groupe politique 
- La commission permanente 
- Le type d'appartenance au groupe politique 
- La circonscription 
- La fonction au bureau du Sénat
- La catégorie socio-professionnelle 
- La description de la profession

### 3 

Il y a 348 sénateurs actifs dans le jeu de données.

### 4 

L'âge moyen parmi les sénateurs actifs présents dans le jeu de données est 61 ans.