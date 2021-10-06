# Deploiement

Projet DE #3 - API de données & Modele prédiction
Prérequis:
  - Python3
  - Fastapi

Commenncer par installer les dépendances qui se trouvent à la racine:
pip install -r requirements.txt

Puis entraîner le modele de prédiction sur le fichier csv. Le script enregistre dans le dossier /api/data le résultat du modele
(RandomForestClassifier).

# API

Après avoir entraîner le modele, vous pouvez retrouvez l'API dans le dossier api ainsi que c'est fichiers attribué (Dockerfile, ...)
lancer l'api avec la commande: uvicorn main:api --reload

Vous retrouverez l'api accessible à l'adresse localhost:8000/docs


# Tests

Les tests permettent de traiter uniquement l'état d'authentification, si un utilisateur est authentifié.
Placez vous dans le dossier tests afin d'accéder aux fichier tests attribués.

Vous trouverez aussi le fichier docker-compose.yml, il s'agit du fichier qui va permettre de lancer tous nos services ensemble.
