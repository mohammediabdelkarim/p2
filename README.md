Scrapper extract.py

Projet P2 - Books Online -

Description du script

Ce script est un scraper conçu pour le site https://books.toscrape.com

Il parcours chaque catégorie de livre sur le site afin de :

    créer un répertoire dédiée à la catégorie correspondante : "nom_de_catégorie"
    créer un fichier "nom_de_catégorie.csv" contenant les informations suivantes :
        product_page_url
        universal_ product_code (upc)
        title
        price_including_tax
        price_excluding_tax
        number_available
        product_description
        category
        review_rating
        image_url
  

Environnement d'utilisation :

    Python==3.8.11
    requests==2.31.0
    bs4==0.0.1

Utilisation

Les fichier suivants doivent être copier dans le même répertoire :

    extract.py
    requirements.txt

Pour lancer le programme de scrapping il est nécessaire de créer un environnement virtuel et d'y installer les librairies nécessaires à l'aide des commandes suivantes :

    python3 -m venv venv
    python3 -m pip install -r requirements.txt

Activer env virtuel
    
    sous mac/linux : source venv/bin/activate
    sous windows   : env\Scripts\activate.bat

Une fois l'environnement configurer, lancer le programme :

    python3 -m extract.py
