from vue import Vue
from modele import Expression, Constante, Variable, Terme
from controleur import Controleur

vue = Vue()
controleur = Controleur(vue)

def dessiner_cercle():
    x = vue.obtenir_valeur_entree_x()
    y = vue.obtenir_valeur_entree_y()
    operateur = vue.obtenir_valeur_operateur()
    controleur.dessiner_cercle(x, y, operateur)

def dessiner_carre():
    x = vue.obtenir_valeur_entree_x()
    y = vue.obtenir_valeur_entree_y()
    nom = vue.obtenir_valeur_entree_nom()
    valeur = vue.obtenir_valeur_entree_valeur()
    controleur.dessiner_carre(x, y, nom, valeur)

def dessiner_triangle():
    x = vue.obtenir_valeur_entree_x()
    y = vue.obtenir_valeur_entree_y()
    valeur = vue.obtenir_valeur_entree_valeur()
    controleur.dessiner_triangle(x, y, valeur)

def definir_operande_gauche():
    x = vue.obtenir_valeur_entree_x()
    y = vue.obtenir_valeur_entree_y()
    controleur.definir_operande_gauche(x, y)

def definir_operande_droit():
    x = vue.obtenir_valeur_entree_x()
    y = vue.obtenir_valeur_entree_y()
    controleur.definir_operande_droit(x, y)

def calculer_expression():
    controleur.calculer_expression()

vue.ajouter_evenement_dessiner_cercle(dessiner_cercle)
vue.ajouter_evenement_dessiner_carre(dessiner_carre)
vue.ajouter_evenement_dessiner_triangle(dessiner_triangle)
vue.ajouter_evenement_definir_operande_gauche(definir_operande_gauche)
vue.ajouter_evenement_definir_operande_droit(definir_operande_droit)
vue.ajouter_evenement_calculer_expression(calculer_expression)

vue.run()