# Résolution de labyrinthe

### Sommaire

1. Description du projet
2. Description technique
3. Prise en main

## 1. Description du projet

Le but du projet est de réaliser un programme permettant à un agent de trouver la sortie d'un labyrinthe.

Afin de se faire, nous allons créer un agent qui pourra se déplacer dans le labyrinthe selon une liste de mouvements générée aléatoirement.

Cet agent fera parti d'une liste dans laquelle il sera confronté aux autres agents grâce à la distance le séparant de la sortie.

Cet agent aura une chance définie d'être sélectionné ou modifié pour faire parti d'une nouvelle génération afin d'essayer de trouver la sortie du même labyrinthe.

## 2. Description technique

Afin de parcourir le labyrinthe, nous dotons notre agent d'un algorithme de génétique, lui permettant d'apprendre pas-à-pas à se déplacer dans le labyrinthe.

Un déplacement se caractérise avec notre agent par son mouvement d'une case à la suivante (en fonction de la direction choisie).

Notre agent se différencie des autres et apprend par l'évolution de son génome, représenté dans notre cas par la liste des mouvements que notre agent doit effectuer afin de trouver la sortie.

L'évolution du génome est aléatoire et peut donc avoir lieu ou non lors du passage d'un génération à la suivante. Si elle a lieu, elle peut se caractériser de 3 manières différentes : Ajout d'un déplacement à la liste du génome, suppression d'un déplacement de la liste du génome, modification d'un déplacement existant.

Notre population est composée d'une liste d'agents, tous triés en fonction du calcul de leur taux de réussite. Ce taux, aussi appelé "fitness" est représenté par la distance absolue (ignorant les obstacles) séparant notre agent de la sortie du labyrinthe.

Lors de chaque "itération", nous créons une nouvelle génération. Pour se faire, nous prennons l'Alpha de la génération précédente (à savoir l'agent ayant eu le meilleur score de "fitness") afin de l'ajouter à la nouvelle génération, puis nous faisons appel à une roue biaisée afin de populer le reste de notre génération.

## 3. Prise en main

Afin de lancer le projet, il est nécessaire d'installer Python avec une version supérieur ou égale à la `3.10.1`.
Aucune installation de librairie quelconque n'est nécessaire au bon fonctionnement du projet.

Il existe trois labyrinthes dans le dossier mazes, la sélection du labyrinthe se fait dans le fichier main, il suiffit de remplacer le numéro du labyrinthe par un autre numéro valide (1,2 ou 3).
Une fois le labyrinthe choisi il suffit de lancer le fichier main avec votre commande python favorite ;).