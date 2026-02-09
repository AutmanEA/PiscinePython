#!/bin/bash

echo "[ -- GENERATEUR DE FICHIER PYTHON POUR LA PISCINE -- ]"

while [ -z $dossier ]
	echo "Entrer le nom du dossier :"
	read dossier
do

mkdir -p $dossier

while [ -z $fichier ]
	echo "Entrer le nom du fichier :"
	read fichier
do

touch $dossier/$fichier

cat << EOF > $dossier/$fichier
def main():
    """
    Docstring for main
    """
    pass


if __name__ == "__main__":
    main()
EOF
