from modele import Expression, Constante, Variable, Terme

class Controleur:
    def __init__(self, model):
            self.model = model
    

    def dessiner_cercle(self, x, y, operateur):
        self.expression = Terme(operateur, Constante(x), Constante(y))
        self.vue.afficher_resultat("cercle dessiné avec succés")     


    def dessiner_carre(self, x, y, nom, valeur):
        self.expression = Terme("carre", Constante(x), Constante(y))
        self.expression.operande_gauche.ajouter_variable(Variable(nom, valeur))
        self.vue.afficher_resultat("Carré dessiné avec succès.")


    def dessiner_triangle(self, x, y, valeur):
        self.expression = Terme("triangle", Constante(x), Constante(y))
        self.expression.operande_droit.ajouter_terme(Terme(Constante(valeur)))
        self.vue.afficher_resultat("Triangle dessiné avec succès.")

    def definir_operande_gauche(self, x, y):
        if self.expression is not None:
            self.expression.operande_gauche = Terme(self.expression.operateur, Constante(x), Constante(y))
            self.vue.afficher_resultat("Opérande gauche défini avec succès.")


    def definir_operande_droit(self, x, y):
        if self.expression is not None:
            self.expression.operande_droit = Terme(self.expression.operateur, Constante(x), Constante(y))
            self.vue.afficher_resultat("Opérande droit défini avec succès.")


          

    def effectuer_calcul(self, nombre1, nombre2,operateur):
        return self.model.effectuer_calcul(nombre1, nombre2,operateur)