import tkinter as tk

class Vue:
    def __init__(self):
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        
        self.button_calculer = tk.Button(self.window, text="Calculer", command=self.calculer_expression)
        self.button_calculer.pack()
        
        self.text_resultat = tk.Text(self.window, height=1)
        self.text_resultat.pack()


        self.root = tk.Tk()
        self.root.title("Éditeur d'Expressions")

        self.label_x = tk.Label(self.root, text="X :")
        self.label_x.grid(row=0, column=0)

        self.entre_x = tk.Entry(self.root)
        self.entre_x.grid(row=0, column=1)

        self.label_y = tk.Label(self.root, text="Y :")
        self.label_y.grid(row=1, column=0)

        self.entre_y = tk.Entry(self.root)
        self.entre_y.grid(row=1, column=1)

        self.label_operateur = tk.Label(self.root, text="Opérateur :")
        self.label_operateur.grid(row=2, column=0)

        self.entre_operateur = tk.Entry(self.root)
        self.entre_operateur.grid(row=2, column=1)

        self.bouton_dessiner_cercle = tk.Button(self.root, text="Dessiner Cercle", command=self.dessiner_cercle)
        self.bouton_dessiner_cercle.grid(row=3, column=0)

        self.bouton_dessiner_carre = tk.Button(self.root, text="Dessiner Carré", command=self.dessiner_carre)
        self.bouton_dessiner_carre.grid(row=3, column=1)

        self.bouton_dessiner_triangle = tk.Button(self.root, text="Dessiner Triangle", command=self.dessiner_triangle)
        self.bouton_dessiner_triangle.grid(row=4, column=0)

        self.label_nom = tk.Label(self.root, text="Nom :")
        self.label_nom.grid(row=5, column=0)

        self.entre_nom = tk.Entry(self.root)
        self.entre_nom.grid(row=5, column=1)

        self.label_valeur = tk.Label(self.root, text="Valeur :")
        self.label_valeur.grid(row=6, column=0)

        self.entre_valeur = tk.Entry(self.root)
        self.entre_valeur.grid(row=6, column=1)

        self.bouton_definir_operande_gauche = tk.Button(self.root, text="Définir Opérande Gauche")
        self.bouton_definir_operande_gauche.grid(row=7, column=0)

        self.bouton_definir_operande_droit = tk.Button(self.root, text="Définir Opérande Droit")
        self.bouton_definir_operande_droit.grid(row=7, column=1)

        self.bouton_calculer_expression = tk.Button(self.root, text="Calculer Expression")
        self.bouton_calculer_expression.grid(row=8, column=0)

    def obtenir_valeur_entree_x(self):
        return self.entre_x.get()

    def obtenir_valeur_entree_y(self):
        return self.entre_y.get()

    def obtenir_valeur_operateur(self):
        return self.entre_operateur.get()

    def obtenir_valeur_entree_nom(self):
        return self.entre_nom.get()

    def obtenir_valeur_entree_valeur(self):
        return self.entre_valeur.get()

    def ajouter_evenement_dessiner_cercle(self, fonction):
        self.dessiner_cercle = fonction

    def ajouter_evenement_dessiner_carre(self, fonction):
        self.dessiner_carre = fonction

    def ajouter_evenement_dessiner_triangle(self, fonction):
        self.dessiner_triangle = fonction

    def ajouter_evenement_definir_operande_gauche(self, fonction):
        self.definir_operande_gauche = fonction

    def ajouter_evenement_definir_operande_droit(self, fonction):
        self.definir_operande_droit = fonction

    def ajouter_evenement_calculer_expression(self, fonction):
        self.calculer_expression = fonction

    def definir_controleur(self, controleur):
        self.controleur = controleur
            
    def dessiner_cercle(self):
        x = self.obtenir_valeur_entree_x()
        y = self.obtenir_valeur_entree_y()
        operateur = self.obtenir_valeur_operateur()
        self.controleur.dessiner_cercle(x, y, operateur)

    def dessiner_carre(self):
        x = self.obtenir_valeur_entree_x()
        y = self.obtenir_valeur_entree_y()
        nom = self.obtenir_valeur_entree_nom()
        valeur = self.obtenir_valeur_entree_valeur()
        self.controleur.dessiner_carre(x, y, nom, valeur)

    def dessiner_triangle(self):
        x = self.obtenir_valeur_entree_x()
        y = self.obtenir_valeur_entree_y()
        valeur = self.obtenir_valeur_entree_valeur()
        self.controleur.dessiner_triangle(x, y, valeur)

    def definir_operande_gauche(self):
        x = self.obtenir_valeur_entree_x()
        y = self.obtenir_valeur_entree_y()
        self.controleur.definir_operande_gauche(x, y)

    def definir_operande_droit(self):
        x = self.obtenir_valeur_entree_x()
        y = self.obtenir_valeur_entree_y()
        self.controleur.definir_operande_droit(x, y)

    def calculer_expression(self):
        self.controleur.calculer_expression()
        
    def afficher_resultat(self, resultat):
        self.text_resultat.delete("1.0", tk.END)
        self.text_resultat.insert(tk.END, "Résultat : " + str(resultat))

    def afficher_message(self, message):
        self.text_resultat.delete("1.0", tk.END)
        self.text_resultat.insert(tk.END, "Message : " + message)
        
    def run(self):
        self.window.mainloop()