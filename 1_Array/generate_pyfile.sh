#!/bin/bash

echo "[ -- GENERATEUR DE FICHIER PYTHON POUR LA PISCINE -- ]"
echo "Entrer le nom du dossier :"
read dossier
mkdir -p $dossier
echo "Entrer le nom du fichier :"
read fichier
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
