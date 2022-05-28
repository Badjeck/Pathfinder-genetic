# Résolution de labyrinthe

### Sommaire

1. Description du projet
2. Description technique
3. Prise en main

## 1. Description du projet

Le but du projet est de réaliser un programme permettant à un agent de traverser des labyrinthes en utilisant un minimum de coup possible afin d'arriver à la sortie.
Afin de se faire, nous allons créer un agent qui pourra se déplacer dans le labyrinthe selon une liste de mouvements prédéfinis.
Cette agent fera parti d'une liste dans laquelle il sera confronté aux autres agents grâce à la distance le séparant de la sortie.

## 2. Description technique

Afin de parcourir le labyrinthe, nous dotons notre agent d'un algorithme de génétique, lui permettant d'apprendre pas-à-pas à se déplacer dans le labyrinthe.

Notre agent se différencie des autres et apprend par l'évolution de son génome, représenté dans notre cas par la liste des mouvements que notre agent doit effectuer afin de trouver la sortie.

Notre population est composée d'une liste d'agents, tous triés en fonction du calcul de leur taux de réussite. Ce taux, aussi appelé "fitness" est représenté par la distance absolue (ignorant les obstacles) séparant notre agent de la sortie du labyrinthe.

## 3. Prise en main

Afin de lancer le projet, il est nécessaire d'installer Python `3.10.1`.
Aucune installation de librairie quelconque n'est nécessaire au bon fonctionnement du projet.