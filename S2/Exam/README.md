# Examen TAL L3 S2

## Disclaimer
Le fichier `article_extractor.py` a pour but de tenter de récupérer les articles des sites web de **RFI**, **LeMonde**, et **LeParisien**. Par conséquent, un article de tout autre site que ces trois-ci <u>ne saura pas être scrapé</u>.

Pour le faire, il utilise la librairie **Selenium**, qui, bien que plus lourd et compliqué que **BeautifulSoup**, permet une pleine gestion des pages web dynamiques, cependant, le caractère 'aléatoire' du web-scraping fait qu'il faut tailler son script sur chaque site que l'on veut scraper, chaque site est différent, il est donc impossible de faire un script qui peut scraper n'importe quel article de journal sur n'importe quel site.

J'ai laissé dans le fichier `article_extractor.py` d'autres articles des sites qui sont supportés par le script.

## Description

- Pour les prérequis du devoir, tout peut-être lancé depuis `main.py`.

- Le fichier `models.py` ajoute les classes requises pour le devoir.

- Le fichier `utils.py` contient quelques fonctions utilitaires, ainsi que la classe Stopwatch qui permet de mesurer le temps d'exécution.

- Le fichier `article_tokenizer.py` tokenize le rendu de `article_extractor.py` avec **Spacy** et utilise les classes définies dans `models.py`. Il utilise un système de cache grâce à la librairie **Joblib** pour rendre la vitesse d'exécution un peu moins longue.

- Dans `calc_metrics.py` il y a tous les calculs demandés dans le devoir.

## Réponse aux question du devoir

J'ai pris pour ce devoir [l'article de RFI sur les manifestations en Serbie](https://www.rfi.fr/fr/europe/20250524-crise-politique-en-serbie-des-universitaires-lancent-une-p%C3%A9tition-pour-des-l%C3%A9gislatives-anticip%C3%A9es).

- quelle est la longueur moyenne des phrases de l'article ? (arrondir au dixième)

- quels sont les 5 lemmes de plus de 3 caractères les plus fréquents dans l'article ?

- quels sont les noms propres de l'article ?

```
30.05

['avoir', 'être', 'manifestation', 'nous', 'politique']

['Serbie', 'Aleksander', 'Vučić', 'Serbie', '18:23', 'Novi', 'Sad', 'Miloš', 'Vučević', 'Alexander', 'Vučić', 'Serbie', 'RFI', 'Drazen', 'Maric', 'Subotica', 'faire', 'Vucic', 'Drazen', 'Maric', 'Subotica', 'Aleksandar', 'Vučić', 'Serbes', 'Serbie', 'RFI', '©', 'RFI', 'RFI', 'Internet'] 
```

