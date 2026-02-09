#!/bin/bash

echo "[ -- GENERATEUR DE FICHIER PYTHON POUR LA PISCINE -- ]"

while [ -z $dossier ]
do
	echo "Entrer le nom du dossier :"
	read dossier
done

mkdir -p $dossier

while [ -z $fichier ]
do
	echo "Entrer le nom du fichier :"
	read fichier
done

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
