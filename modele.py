from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def evaluer(self):
        pass

class Constante(Expression):
    def __init__(self, valeur):
        self.valeur = valeur
        
    def evaluer(self):
        return self.valeur

class Variable(Expression):
    def __init__(self, nom, valeur):
        self.nom = nom
        self.valeur = valeur
        
    def evaluer(self):
        return self.valeur

class Terme(Expression):
    def __init__(self, operateur, operande_gauche, operande_droit):
        self.operateur = operateur
        self.operande_gauche = operande_gauche
        self.operande_droit = operande_droit
        
    def evaluer(self):
        if self.operateur == "+":
            return self.operande_gauche.evaluer() + self.operande_droit.evaluer()
        elif self.operateur == "-":
            return self.operande_gauche.evaluer() - self.operande_droit.evaluer()
        elif self.operateur == "*":
            return self.operande_gauche.evaluer() * self.operande_droit.evaluer()
        elif self.operateur == "/":
            return self.operande_gauche.evaluer() / self.operande_droit.evaluer()
    

    