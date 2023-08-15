# FastAPI Beanie CRUD Application

Ceci est une application de démonstration construite avec FastAPI et Beanie, un ORM asynchrone pour MongoDB. L'application offre des opérations CRUD (Create, Read, Update, Delete) pour gérer des tâches (todos) d'utilisateurs.

## Prérequis

- Python 3.11+
- MongoDB

## Installation

1. Cloner ce dépôt : git clone git@github.com:LeDoyen14/ToDo-App.git
2. Accéder au répertoire de l'application : cd backend
3. Installer les dépendances : pip install -r requirements.txt

## Utilisation

1. Exécuter l'application : uvicorn app.main:app --reload

2. Accéder à l'API dans un navigateur ou via un outil comme [httpie](https://httpie.io/).

## Endpoints

- `GET /` : Récupérer toutes les tâches de l'utilisateur connecté.
- `POST /create` : Créer une nouvelle tâche.
- `GET /{todo_id}` : Récupérer une tâche spécifique par son ID.
- `PUT /{todo_id}` : Mettre à jour une tâche existante par son ID.
- `DELETE /{todo_id}` : Supprimer une tâche existante par son ID.

## Modèles

L'application utilise les modèles suivants :

- `User` : Modèle représentant un utilisateur.
- `Todo` : Modèle représentant une tâche.

## Schémas

Les schémas utilisés pour la validation des données sont les suivants :

- `TodoCreate` : Schéma pour créer une nouvelle tâche.
- `TodoUpdate` : Schéma pour mettre à jour une tâche existante.
- `TodoOut` : Schéma pour la sortie de données d'une tâche.

## Services

Les services offerts par l'application sont regroupés dans le dossier `services`.

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à proposer une demande d'extraction.

## Licence

Ce projet est sous licence MIT. 
