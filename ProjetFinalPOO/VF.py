import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import sqlite3
from datetime import datetime
from PIL import Image, ImageTk


class Application(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Gestion de Flotte")
        self.config(bg="black")
        self.iconbitmap("b.ico")
        self.geometry("600x480")
        self.resizable(0, 0)
        # Base de données SQLite
        self.conn = sqlite3.connect("gestion_flotte.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Utilisateurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom_utilisateur TEXT NOT NULL,
                mot_de_passe TEXT NOT NULL
            )
        ''')

        # Création de la table Véhicules si elle n'existe pas
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Vehicules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                immatriculation INTEGER NOT NULL,
                marque TEXT NOT NULL,
                modele TEXT NOT NULL,
                annee INTEGER NOT NULL,
                date_entree TEXT,
                heure_entree TEXT,
                heure_sortie TEXT,
                chauffeur_id INTEGER NOT NULL,
                destination TEXT,
                proprietaire_id INTEGER,
                FOREIGN KEY (proprietaire_id) REFERENCES Utilisateurs(id)
            )
        ''')
        self.is_authenticated = False
        self.connexion()

    def connexion(self):
        self.initialiser_fenetre()

        self.nom_utilisateur_var = tk.StringVar()
        self.mot_de_passe_var = tk.StringVar()

        side_img_data = Image.open("side-img.jpeg")
        email_icon_data = Image.open("email-icon.png")
        mot_de_passe_icon_data = Image.open("password-icon.png")

        self.side_img = ImageTk.PhotoImage(side_img_data.resize((300, 480)))
        self.email_icon = ImageTk.PhotoImage(email_icon_data.resize((20, 20)))
        self.mot_de_passe_icon = ImageTk.PhotoImage(mot_de_passe_icon_data.resize((17, 17)))

        tk.Label(self, text="", image=self.side_img).pack(expand=True, side="left")

        frame = tk.Frame(self, width=300, height=480)
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        tk.Label(frame, text="BIENVENUE", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(
            anchor="w", pady=(50, 5), padx=(25, 40))
        tk.Label(frame, text="Connectez-vous à votre compte:", fg="#7E7E7E", anchor="w", justify="left",
                 font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 40))

        tk.Label(frame, text=f"  Nom d'utilisateur:", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
                 image=self.email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 40))
        tk.Entry(frame, width=225, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88", textvariable=self.nom_utilisateur_var,
                 fg="#000000").pack(anchor="w", padx=(25, 40))

        tk.Label(frame, text="  Mot de passe:", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
                 image=self.mot_de_passe_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 40))
        tk.Entry(frame, width=225, bg="#EEEEEE", relief="solid", highlightthickness=1, textvariable=self.mot_de_passe_var,
                 highlightbackground="#601E88", fg="#000000", show="*").pack(anchor="w", padx=(25, 40))

        tk.Button(frame, text="Connexion", bg="#601E88", activebackground="#E44982", font=("Arial Bold", 12),
                  fg="#ffffff", width=225, command=self.connexion2).pack(anchor="w", pady=(40, 0), padx=(25, 40))
        tk.Button(frame, text="Inscription", bg="#EEEEEE", activebackground="#EEEEEE", font=("Arial Bold", 9),
                  fg="#601E88", width=225, command=self.inscription, compound="left").pack(anchor="w",
                                                                                                  pady=(20, 0),
                 
                                                                                                  padx=(25, 40))

    def inscription(self):
        self.initialiser_fenetre()

        self.new_nom_utilisateur_var = tk.StringVar()
        self.new_mot_de_passe_var = tk.StringVar()
        side_img_data = Image.open("side-img.jpeg")
        email_icon_data = Image.open("email-icon.png")
        mot_de_passe_icon_data = Image.open("password-icon.png")

        self.side_img = ImageTk.PhotoImage(side_img_data.resize((300, 480)))
        self.email_icon = ImageTk.PhotoImage(email_icon_data.resize((20, 20)))
        self.mot_de_passe_icon = ImageTk.PhotoImage(mot_de_passe_icon_data.resize((17, 17)))
        tk.Label(app, text="", image=self.side_img).pack(expand=True, side="left")

        frame = tk.Frame(app, width=300, height=480)
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        tk.Label(frame, text="INSCRIPTION", fg="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(
            anchor="w", pady=(50, 5), padx=(25, 40))
        tk.Label(frame, text="BIENVENUE:", fg="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(
            anchor="w", padx=(25, 40))
        tk.Label(frame, text="  Nouveau utilisateur:", fg="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 14), image=self.email_icon, compound="left").pack(anchor="w", pady=(38, 0),
                                                                                  padx=(25, 40))
        tk.Entry(frame, width=225, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                 fg="#000000",textvariable=self.new_nom_utilisateur_var).pack(anchor="w", padx=(25, 40))

        tk.Label(frame, text="  Nouveau Mot de passe:", fg="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 14), image=self.mot_de_passe_icon, compound="left").pack(anchor="w", pady=(21, 0),
                                                                                     padx=(25, 40))
        tk.Entry(frame, width=225, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                 fg="#000000", show="*",textvariable=self.new_mot_de_passe_var).pack(anchor="w", padx=(25, 40))

        tk.Button(frame, text="INSCRIPTION", command=self.inscription2, bg="#601E88", activebackground="#E44982", font=("Arial Bold", 12),
                  fg="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 40))
        tk.Button(frame, text="RETOUR",command=self.connexion, bg="#EEEEEE", activebackground="#EEEEEE", font=("Arial Bold", 9), fg="#601E88",
                  width=225,compound="left").pack(anchor="w", pady=(20, 0), padx=(25, 40))

    def gestion_flotte(self):
        self.initialiser_fenetre()
        side_img_data = Image.open("side-img.jpeg")
        self.side_img = ImageTk.PhotoImage(side_img_data.resize((300, 480)))
        tk.Label(app, text="", image=self.side_img).pack(expand=True, side="left")
        frame = tk.Frame(app, width=300, height=480)
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")
        
        tk.Button(frame, text="Ajouter Véhicule", command=self.ajouter_vehicule, bg="#601E88", activebackground="#E44982", font=("Arial Bold", 12),
                  fg="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 40))
        
        tk.Button(frame, text="Modifier Véhicule", command=self.modifer_vehicule, bg="#601E88", activebackground="#E44982", font=("Arial Bold", 12),
                  fg="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 40))
        
        tk.Button(frame, text="Supprimer Véhicule", command=self.supprimer_vehicule, bg="#601E88", activebackground="#E44982", font=("Arial Bold", 12),
                  fg="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 40))
        
        tk.Button(frame, text="Afficher la liste des véhicules", command=self.afficher_vehicule, bg="#601E88", activebackground="#E44982", font=("Arial Bold", 12),
                  fg="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 40))

        tk.Button(frame, text="Déconnexion", command=self.deconnexion, bg="#601E88", activebackground="#E44982", font=("Arial Bold", 12),
                  fg="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 40))

    def ajouter_vehicule(self):
        self.initialiser_fenetre()

        canvas = tk.Canvas(self, bg="white", width=300, height=480)
        canvas.pack(side="left", fill="both", expand=True)


        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        self.marque_var = tk.StringVar()
        self.model_var = tk.StringVar()
        self.annee_var = tk.StringVar()
        self.matri_var = tk.StringVar()
        self.date_entree_var = tk.StringVar()
        self.heure_entree_var = tk.StringVar()
        self.heure_sortie_var = tk.StringVar()
        self.chauffeur_id_var = tk.StringVar()
        self.destination_var = tk.StringVar()

        side_img_data = Image.open("sideimg.jpg")
        self.side_img = ImageTk.PhotoImage(side_img_data.resize((300, 900)))
        tk.Label(frame, text="", image=self.side_img).pack(expand=True, side="left")

        tk.Label(frame, text="Marque du véhicule: ", fg="#601E88", anchor="w", justify="left",
                font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                fg="#000000", textvariable=self.marque_var).pack(anchor="w", padx=(25, 40))

        tk.Label(frame, text="Modèle du véhicule: ", fg="#601E88", anchor="w", justify="left",
                font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                fg="#000000", textvariable=self.model_var).pack(anchor="w", padx=(25, 40))
            
                    
        tk.Label(frame, text="Année du modèle du véhicule: ", fg="#601E88", anchor="w", justify="left",
                    font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 40))
        tk.Label(frame, text="(Format: YYYY)", fg="#7E7E7E", anchor="w", justify="left", font=("Arial", 10)).pack(
            anchor="w", padx=(25, 40))

        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                    fg="#000000",textvariable=self.annee_var).pack(anchor="w", padx=(25, 40))
            
        tk.Label(frame, text="Numéro D'immatriculation: ", fg="#601E88", anchor="w", justify="left",
                    font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0),
                                                                                        padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                    fg="#000000",textvariable=self.matri_var).pack(anchor="w", padx=(25, 40))
            
        tk.Label(frame, text="Date de mise en circulation: ", fg="#601E88", anchor="w", justify="left",
                    font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0),padx=(25, 40))

        tk.Label(frame, text="(Format: YYYY-MM-DD)", fg="#7E7E7E", anchor="w", justify="left", font=("Arial", 10)).pack(
            anchor="w", padx=(25, 40))

        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                    fg="#000000",textvariable=self.date_entree_var).pack(anchor="w", padx=(25, 40))

        tk.Label(frame, text="Heure d'entrée: ", fg="#601E88", anchor="w", justify="left",
                    font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0),padx=(25, 40))
        tk.Label(frame, text="(Format: HH:MM)", fg="#7E7E7E", anchor="w", justify="left", font=("Arial", 10)).pack(
            anchor="w", padx=(25, 40))

        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                    fg="#000000",textvariable=self.heure_entree_var).pack(anchor="w", padx=(25, 40))
            
        tk.Label(frame, text="Heure de sortie: ", fg="#601E88", anchor="w", justify="left",
                    font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 40))
        tk.Label(frame, text="(Format: HH:MM)", fg="#7E7E7E", anchor="w", justify="left", font=("Arial", 10)).pack(
            anchor="w", padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                    fg="#000000",textvariable=self.heure_sortie_var).pack(anchor="w", padx=(25, 40))
            
        tk.Label(frame, text="ID du chauffeur: ", fg="#601E88", anchor="w", justify="left",
                    font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0),
                                                                                        padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                    fg="#000000",textvariable=self.chauffeur_id_var).pack(anchor="w", padx=(25, 40))
            
        tk.Label(frame, text="Destination: ", fg="#601E88", anchor="w", justify="left",
                    font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0),
                                                                                        padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                    fg="#000000",textvariable=self.destination_var).pack(anchor="w", padx=(25, 40))
    
        tk.Button(frame, text="Ajouter Véhicule", command=self.ajouter_vehicule_2, bg="#601E88", activebackground="#E44982",
          font=("Arial Bold", 12), fg="#ffffff", width=225, compound="center", image=self.mot_de_passe_icon).pack(anchor="w", pady=(40, 0), padx=(25, 40))

        tk.Button(frame, text="Retour", command=self.gestion_flotte, bg="#601E88", activebackground="#E44982",
          font=("Arial Bold", 12), fg="#ffffff", width=225, compound="center", image=self.mot_de_passe_icon).pack(anchor="w", pady=(40, 0), padx=(25, 40))


        frame.update_idletasks()  
        canvas.config(scrollregion=canvas.bbox("all")) 

        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    def ajouter_vehicule_2(self):
        marque = self.marque_var.get()
        modele= self.model_var.get()
        annee  = self.annee_var.get()
        matri = self.matri_var.get()
        date_entree = self.date_entree_var.get()
        heure_entree = self.heure_entree_var.get()
        heure_sortie = self.heure_sortie_var.get()
        chauffeur_id = self.chauffeur_id_var.get()
        destination = self.destination_var.get()
        if not marque or not  modele or not annee  or not matri:
             messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
             return
        try:
             annee  = int(annee )
        except ValueError:
             messagebox.showerror("Erreur", "L'année doit être un nombre entier.")
             return

        try:
             matri = int(matri)
        except ValueError:
             messagebox.showerror("Erreur", "L'immatricule doit être un nombre entier.")
             return

        try:
             date_entree = str(datetime.strptime(date_entree, "%Y-%m-%d").date())
             heure_entree = str(datetime.strptime(heure_entree, "%H:%M").time())
             heure_sortie = str(datetime.strptime(heure_sortie, "%H:%M").time())
        except ValueError:
             messagebox.showerror("Erreur", "Format de date/heure invalide.")
             return

        self.cursor.execute('''
                INSERT INTO Vehicules (immatriculation , marque, modele, annee , date_entree, heure_entree,heure_sortie, chauffeur_id, destination, proprietaire_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (matri , marque, modele, annee , date_entree, heure_entree,heure_sortie, chauffeur_id, destination, self.current_user_id))
        self.conn.commit()
        messagebox.showinfo("Succès", "Véhicule ajouté avec succès!")

    def modifer_vehicule(self):
        vehicle_id = simpledialog.askinteger("Modification", "Entrez l'ID du véhicule à modifier:")

        if vehicle_id is None:
            return  
        self.cursor.execute('''
             SELECT id, marque, modele, annee 
             FROM Vehicules
             WHERE proprietaire_id = ? AND id = ?
         ''', (self.current_user_id, vehicle_id))

        selected_vehicle = self.cursor.fetchone()

        if not selected_vehicle:
            messagebox.showerror("Erreur", f"Aucun véhicule trouvé avec l'ID {vehicle_id}.")
            return
        else:
            self.modifer_2(vehicle_id)

    def modifer_2(self,vehicle_id):
        self.initialiser_fenetre()

        canvas = tk.Canvas(self, bg="white", width=300, height=480)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        self.heure_entree_var = tk.StringVar()
        self.heure_sortie_var = tk.StringVar()
        self.chauffeur_id_var = tk.StringVar()
        self.destination_var = tk.StringVar()

        side_img_data = Image.open("side-img.jpeg")
        self.side_img = ImageTk.PhotoImage(side_img_data.resize((300, 480)))
        tk.Label(frame, text="", image=self.side_img).pack(expand=True, side="left")

        tk.Label(frame, text="Heure d'entrée: ", fg="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0),padx=(25, 40))
        tk.Label(frame, text="(Format: HH:MM)", fg="#7E7E7E", anchor="w", justify="left", font=("Arial", 10)).pack(
            anchor="w", padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                 fg="#000000", textvariable=self.heure_entree_var).pack(anchor="w", padx=(25, 40))

        tk.Label(frame, text="Heure de sortie: ", fg="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0),padx=(25, 40))
        tk.Label(frame, text="(Format: HH:MM)", fg="#7E7E7E", anchor="w", justify="left", font=("Arial", 10)).pack(anchor="w", padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                 fg="#000000", textvariable=self.heure_sortie_var).pack(anchor="w", padx=(25, 40))

        tk.Label(frame, text="ID du chauffeur: ", fg="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0),
                                               padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                 fg="#000000", textvariable=self.chauffeur_id_var).pack(anchor="w", padx=(25, 40))

        tk.Label(frame, text="Destination: ", fg="#601E88", anchor="w", justify="left",
                 font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0),
                                               padx=(25, 40))
        tk.Entry(frame, width=40, bg="#EEEEEE", relief="solid", highlightthickness=1, highlightbackground="#601E88",
                 fg="#000000", textvariable=self.destination_var).pack(anchor="w", padx=(25, 40))

        tk.Button(frame, text="Modifier", command=lambda: self.modifer_3(vehicle_id), bg="#601E88", activebackground="#E44982",
                  font=("Arial Bold", 12), fg="#ffffff", width=225, compound="center", image=self.mot_de_passe_icon).pack(
            anchor="w", pady=(40, 0), padx=(25, 40))

        tk.Button(frame, text="Retour", command=self.gestion_flotte, bg="#601E88",
                  activebackground="#E44982",
                  font=("Arial Bold", 12), fg="#ffffff", width=225, compound="center", image=self.mot_de_passe_icon).pack(
            anchor="w", pady=(40, 0), padx=(25, 40))

        frame.update_idletasks()  
        canvas.config(scrollregion=canvas.bbox("all"))  

        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"))

    def modifer_3(self,vehicle_id):

        new_heure_entree = self.heure_entree_var.get()
        new_heure_sortie = self.heure_sortie_var.get()
        new_chauffeur_id = self.chauffeur_id_var.get()
        new_destination = self.destination_var.get()

        try:
            new_heure_entree = str(datetime.strptime(new_heure_entree,"%H:%M").time()) if new_heure_entree else None
            new_heure_sortie = str(datetime.strptime(new_heure_sortie, "%H:%M").time()) if new_heure_sortie else None
            new_chauffeur_id = int(new_chauffeur_id) if new_chauffeur_id else None

            self.cursor.execute('''
                 UPDATE Vehicules
                 SET heure_entree = ?, heure_sortie = ?, chauffeur_id = ?, destination = ?
                 WHERE proprietaire_id = ? AND id = ?
             ''', (new_heure_entree,new_heure_sortie, new_chauffeur_id, new_destination, self.current_user_id, vehicle_id))

            self.conn.commit()
            messagebox.showinfo("Succès", f"Informations du véhicule ID {vehicle_id} modifiées avec succès!")
        except ValueError:
            messagebox.showerror("Erreur", "Format de date/heure invalide.")

    def connexion2(self):
        nom_utilisateur = self.nom_utilisateur_var.get()
        mot_de_passe = self.mot_de_passe_var.get()
        if not nom_utilisateur or not mot_de_passe:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return
        self.cursor.execute('''
             SELECT id FROM Utilisateurs
             WHERE nom_utilisateur = ? AND mot_de_passe = ?
         ''', (nom_utilisateur, mot_de_passe))

        user_id = self.cursor.fetchone()
        if user_id:
            self.is_authenticated = True
            self.current_user_id = user_id[0]
            self.gestion_flotte()
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect.")

    def afficher_vehicule(self):
        vehicles_window = tk.Toplevel(self)
        vehicles_window.title("Liste des véhicules")
        vehicles_window.iconbitmap("b.ico")


        tree = ttk.Treeview(vehicles_window,
                            columns=("id", "matri", "marque", "Model", "annee ", "Entry Date", "Entry Time", "Exit Time",
                                     "ID Chauffeur", "Destination"),
                            show="headings", height=10)
        tree.heading("id", text="ID")
        tree.heading("matri", text="Matricule")
        tree.heading("marque", text="Marque")
        tree.heading("Model", text="Modèle")
        tree.heading("annee ", text="Année")
        tree.heading("Entry Date", text="Date de mise en circulation")
        tree.heading("Entry Time", text="Heure d'entrée")
        tree.heading("Exit Time", text="Heure de sortie")
        tree.heading("ID Chauffeur", text="ID Chauffeur")
        tree.heading("Destination", text="Destination")


        for col in tree["columns"]:
            tree.column(col, width=100, anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(vehicles_window, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)


        self.cursor.execute('''
            SELECT id, immatriculation , marque, modele, annee , date_entree, heure_entree, heure_sortie, chauffeur_id, destination
            FROM Vehicules
            WHERE proprietaire_id = ?
        ''', (self.current_user_id,))

        vehicles = self.cursor.fetchall()

        for i, vehicle in enumerate(vehicles, start=1):
            tree.insert("", "end", values=vehicle, tags=("evenrow" if i % 2 == 0 else "oddrow"))


        tree.tag_configure("evenrow", background="#f0f0f0")
        tree.tag_configure("oddrow", background="#ffffff")

        tree.pack(fill="both", expand=True)

        if not vehicles:
            messagebox.showinfo("Liste des véhicules", "Aucun véhicule trouvé.")


        tree.bind("<ButtonRelease-1>", lambda event: self.on_vehicle_select(event, tree))

    def inscription2(self):
        new_nom_utilisateur = self.new_nom_utilisateur_var.get()
        new_mot_de_passe = self.new_mot_de_passe_var.get()

        # Vérifier si l'utilisateur existe déjà
        self.cursor.execute('''
            SELECT * FROM Utilisateurs
            WHERE nom_utilisateur = ? AND mot_de_passe = ?
        ''', (new_nom_utilisateur, new_mot_de_passe))

        existing_user = self.cursor.fetchone()

        if existing_user:
            messagebox.showerror("Erreur",
                                 "Utilisateur déjà existant avec le même nom d'utilisateur et le même mot de passe.")
        else:

            self.cursor.execute('''
                INSERT INTO Utilisateurs (nom_utilisateur, mot_de_passe)
                VALUES (?, ?)
            ''', (new_nom_utilisateur, new_mot_de_passe))

            self.conn.commit()
            messagebox.showinfo("Succès", "Inscription réussie! Vous pouvez maintenant vous connecter.")
            self.connexion()

    def deconnexion(self):
        self.connexion()

    def initialiser_fenetre(self):
        for widget in self.winfo_children():
            widget.destroy()

    def supprimer_vehicule(self):
        supprimer_vehicule_window = tk.Toplevel(self)
        supprimer_vehicule_window.title("Supprimer Véhicule")

        ttk.Label(supprimer_vehicule_window, text="ID du véhicule à supprimer:").grid(row=0, column=0, sticky=tk.W,
                                                                                  pady=(0, 5))
        vehicle_id_entry = ttk.Entry(supprimer_vehicule_window)
        vehicle_id_entry.grid(row=0, column=1, pady=(0, 5))

        ttk.Button(supprimer_vehicule_window, text="Supprimer",
                   command=lambda: self.confirmer_suppression(vehicle_id_entry.get())).grid(row=1, column=0, columnspan=2,
                                                                                     pady=(10, 0))

    def confirmer_suppression(self, vehicle_id):
        try:
            vehicle_id = int(vehicle_id)
        except ValueError:
            messagebox.showerror("Erreur", "L'ID du véhicule doit être un nombre entier.")
            return

        # Vérifier si le véhicule avec l'ID donné existe
        self.cursor.execute('SELECT id FROM Vehicules WHERE id = ?', (vehicle_id,))
        vehicle_existant = self.cursor.fetchone()

        if vehicle_existant:
            # Confirmer la suppression
            confirmer_suppression = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce véhicule?")
            if confirmer_suppression:
                # Supprimer le véhicule de la base de données
                self.cursor.execute('DELETE FROM Vehicules WHERE id = ?', (vehicle_id,))
                self.conn.commit()
                messagebox.showinfo("Succès", "Véhicule supprimé avec succès!")
        else:
            messagebox.showerror("Erreur", "Aucun véhicule trouvé avec cet ID.")


if __name__ == "__main__":
    app = Application()
    app.mainloop()

