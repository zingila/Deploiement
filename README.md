# Deploiement

Projet DE #3 - Base de données & API de données
Prérequis:
  - Mongodb
  - Python3
  - Flask

Commande d'installation de la base de donnée mongodb:
$ sudo apt update
$ python -m pip install pymongo

$ sudo apt install mongodb
$ sudo systemctl status mongodb
$ sudo service mongodb start

Commande pour peupler la base de donnée:
$ mongoimport --type csv -d projet -c transfert --headerline --drop top250-00-19.csv

Puis vérifier que sur mongo la base de donnée est prête:
$ mongo
> use projet
> db.transfert.find()

On en profite pour créer un utilisateur depuis mongo:
db.createUser(
  {
    user: "myUserAdmin",
    pwd:  "abc123",
    roles: [ { role: "userAdmin", db: "projet" }]
  }
)

Ensuite il reste plus qu'à lancer notre fichier app qui contient indirectement les liaisons entre flask et docker:
$ python3 app.py
