# Deploiement

Projet DE #3 - API de données & Modele prédiction
Prérequis:
  - Python3
  - Fastapi

Le but du projet est de développer et déployer une API qui pourra prédire la probabilité de churn d'une entreprise.

Commenncer par installer les dépendances qui se trouvent à la racine:
pip install -r requirements.txt

Un script pour entraîner le modele de prédiction sur le fichier csv. Le script enregistre dans le dossier /api/data le résultat du modele
(RandomForestClassifier).

Lancer le script (depuis la racine) avec la commande: python3 train.py

# API

Après avoir entraîner le modele, vous pouvez retrouvez l'API dans le dossier api/ ainsi que c'est fichiers attribué (Dockerfile, ...)
déplacer vous dans le répertoire et lancer l'api avec la commande: uvicorn main:api --reload

Vous retrouverez l'api accessible à l'adresse localhost:8000/docs


# Tests

Les tests permettent de traiter uniquement l'état d'authentification, si un utilisateur est authentifié.
Placez vous dans le dossier tests afin d'accéder aux fichier tests attribués.
Lancer la commande: docker-compose up --build
Cette commande permet de lancer les conteneurs de tests en même temps que l'API. Alors vous devriez obtenir une réponse serveur de ceci:
![image](https://user-images.githubusercontent.com/49723939/137333738-4cece0af-e57e-4927-9d04-85edb927617a.png)

On pourra améliorer le code en ajoutant différents endpoints, persister les données avec des volumes, stocker nos images dans DockerHub...
