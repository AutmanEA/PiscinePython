# Plonger dans Python

## Tuto installation d'environnement virtuel

### Pourquoi faire ?
Avoir un environnement virtuel permet d'avoir toutes les librairies d'un projet au même endroit, ce qui permet d'avoir toutes les informations d'un simple coup d'oeil de "quoi installer" pour que ça marche sur un autre poste, ainsi qu'être sûr que tout soit utile.

### Prerequis

Python 3 (^3.5) et pip.

### Créer et activer l'environnement

Utiliser la commande ```python -m venv <path>``` pour générer l'environnement.

```sh
cd ~/your_workspace_path #if needed
python -m venv directory_name
```
Puis, activer l'environnement pour pouvoir l'utiliser avec ```source```.

```sh
source ./directory_name/bin/activate
```

Pour retourner sur un projet et travailler dessus plus tard, ignorez juste l'étape de création.

### Désactiver l'environnement

Une fois l'utilisation de l'environnement terminé (À la fin d'un days de piscine par exemple), utiliser la commande dans votre workspace pour désactiver l'environnement virtuel.

```sh
cd ~/your_workspace_path #if needed
deactivate
```

### Installer et importer des librairies

Une fois que l'environnement virtuel est créé: installer, mettre à jour et importer des paquets est similaire à une utilisation classique de python et de son installateur de paquet pip.

Par exemple, avec le paquet pytest
```sh
pip install pytest
```
et dans le fichier.py
```py
import pytest
```

Si un fichier requirement est présent, installer tous les packages est possible avec la commande:
```sh
pip install -r requirement.txt
```

### Générer un requirement.txt

A chaque fin de projet ou pour sauvegarder une liste de paquet afin d'installer rapidement tous les paquets, il est possible avec ```pip freeze``` de générer la liste des lib installées dans notre environnement.

Utiliser une redirection pour créer un fichier:
```sh
pip freeze > requirement.txt
```

## Notes générales sur python

### Commandes de base

#### Lancer un 'programme' python

```sh
python mon_programme.py
```
#### Structure d'un programme python

##### le main

```python
def main():
    """
    Docstring for main
    """
    pass


if __name__ == "__main__":
    main()
```

##### file generator

to generate python files :
```bash
chmod +x generate_pyfile.sh
./generate_pyfile.sh
```
and then follow instructions (french only), first enter folder name, second enter file name.
