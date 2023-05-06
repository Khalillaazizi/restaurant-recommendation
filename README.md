## Application Web Recommandation de restaurants 
Notre application web est une plateforme de Recommandation dees restaurants avec Django. Elle permet aux utilisateurs de rechercher, donner des avis et de lister les restaurants.


## Fonctionnalités

-Parcourir les restaurants par catégories
-Pour chaque restaurant, voir les détails, les avis et les commentaires sur les avis
-Se connecter en tant que membre pour les 2 fonctionnalités supplémentaires suivantes :
-Ajouter des avis sur un restaurant (note en étoiles, note de prix, titre et description de l'avis)
-Aimer un avis
-Ajouter des commentaires à un avis (les réponses sont indentées)
-Ajouter des réponses à un commentaire (les commentaires sont indentés)


## Réalisations techniques

-Utilisation intensive d'AJAX avec Django REST framework
-Liste des restaurants par catégorie
-Aimer un avis
-Ajouter un commentaire
-Ajouter un restaurant
-Ajouter une réponse
-À la réception réussie d'une réponse AJAX, ajouter le nouveau commentaire/réponse au DOM
-Structure de l'arborescence HTML efficace
-Modularisation du code pour une réutilisation aisée


## Explications des (views)
inde : Vue utilisée pour rediriger l'utilisateur de la racine de l'application à la page principale de l'application.

index : Vue principale de l'application où l'utilisateur peut voir la liste des restaurants et effectuer des recherches de restaurants.

addnew : Vue pour ajouter un nouveau restaurant à la base de données.

handleSignup : Vue pour gérer l'inscription d'un nouvel utilisateur.

home : Vue pour afficher la page d'accueil de l'utilisateur connecté.

details : Vue pour afficher les détails d'un restaurant spécifique.

destroy : Vue pour supprimer un restaurant spécifique de la base de données.

add : Vue pour ajouter un nouveau commentaire pour un restaurant spécifique.

reviewed : Vue pour marquer un restaurant comme "revu" pour l'utilisateur connecté.

CommentAdd : Vue pour ajouter un nouveau commentaire pour un restaurant spécifique via l'API.

ReplyAdd : Vue pour ajouter une réponse à un commentaire spécifique via l'API.

LikeAdd : Vue pour ajouter un like à un commentaire spécifique via l'API.

GetRestaurantsByCategory : Vue pour récupérer tous les restaurants dans une catégorie spécifique via l'API.

Le fichier urls.py contient également les chemins pour chacune de ces vues.

## Lancement du projet et Installation
1-Clonez le dépôt GitHub : git clone https://github.com/Khalillaazizi/restaurant-recommendation.git
2-Installer Python, Django (et Anaconda prompt si vous utilisez Windows)
3-Configurez votre environnement python
4-Installez les dépendances requises : pip install -r requirements.txt
5-Appliquez les migrations pour la base de données : python manage.py migrate
6-Lancez le serveur : python manage.py runserver

## Auteur
Khalil LAAZIZI/
Marouane LAMSAOUI/
Oussama Lamkhantar



