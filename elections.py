from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb #J'utilise le module messagebox en faisant mb.<commande>(...) grace au "as"
from random import *

#NOTICE IMPORTANTE:
#Je n'utilise pas forcément tout le temps ttk. vu que je ne suis pas habitué a l'écrire :)

def sauvegarderConfigsAdmins():
    global candidats
    global AdminWin
    Candidats = candi_VAR.get()      #recuperation des canddidats
    candidats = Candidats.split(",") #transformation des noms en liste
    AdminWin.destroy()
    win.deiconify()
    nbrele = nbrElecteurs.get()
    #A partir de la j'ai créé une boucle pour generer les codes et je fais en sorte d'eliminer les codes en double
    #meme si la probabilite de leur apparition est tes faible et ensuite je les affiche
    for i in range(int(nbrele)):
        password = str(randint(100,999999))
        if password not in motsDePasse:
            motsDePasse.append(password)
    mdp = " ".join(motsDePasse)
    mb.showinfo("Vos paramètres ont été sauveguardés","Voici la liste des mots de passe valide : \n"+mdp)

def afficherFenetreAdmin():
    #Creation interface admin
    global AdminWin
    AdminWin = Toplevel(win)
    AdminWin.title("Config")
    
    #Widgets interface
    TxtLabel = Label(AdminWin , text="Veuillez inserer les noms des candidats (séparés par des ',')")
    ElecteursLabel = Label(AdminWin , text="Nombre d'élécteurs")
    CandidatsEntry = Entry(AdminWin , textvariable=candi_VAR)
    nbrElecteursSpinBox = Spinbox(AdminWin , from_=0 , to=500 , textvariable=nbrElecteurs)
    saveButton = Button(AdminWin , text="sauvegarder paramètres" , command=sauvegarderConfigsAdmins)
    
    #Affichage Widgets
    TxtLabel.grid(column=0 , row=0)
    ElecteursLabel.grid(column=0 , row=1)
    CandidatsEntry.grid(column=1 , row=0)
    nbrElecteursSpinBox.grid(column=1 , row=1)
    saveButton.grid(column=1 , row=2)
    
def afficherFenetreElection():
    """
    Explications: Pour cree cette interface on va d'abord creer le texte en haut puis les boutons puis le bouton de validation dans ce meme
    ordre dut a la faccon dont python lit le code (ligne par ligne) et utiliser grid sans arguments additionels (on peut utiliser la methode pack)
    pour que l'arrangement se fasse tout seul.
    Donc le texte sera cree en premier puis la boucle va creer tout les radio buttons necessaires et finalement le bouton de validation pour que
    l'ordre recherché soit respecté.

    NOTE_IMPORTANTE: On peut faire une boucle while (a la place de la boucle for) pour se simplifier la tache de creation et d'affichage
    et de cette maniere on pourrait gérer l'affichage en ligne et en colonne du grid mais avec for c'est plus rapide. (Tout depend de la maniere
    avec laquelle vous etes le plus a l'aise). 
    """
    #Creation de l'interface pour l'electeur
    global ElectionWin
    ElectionWin = Toplevel(win)
    ElectionWin.title("Election")
    textLabel1 = Label(ElectionWin , text="Veuillez choisir un candidat pour lequel voter:")
    ValidationButton = Button(ElectionWin , text="Valider Vote" , command=voter)
    textLabel1.grid()

    #Radio Buttons pr le choix du candidat
    for i in candidats:
        can_n = Radiobutton(ElectionWin , text=i , variable=choixCandidat , value=i)
        can_n.grid()
    #affichage boutton validation
    ValidationButton.grid()

def voter():
    global ElectionWin
    ElectionWin.destroy()
    win.deiconify()
    mb.showinfo("Vote comptbilisé !","Merci d'avoir voté pour: "+str(choixCandidat.get())+"\n Votre vote a été enregistré !")


def login():
    Password_Var = passEntry.get()
    Id_VAR = idEntry.get()
    if Password_Var == "admin" and Id_VAR == "admin": #POur enter en tant qu'admin
        win.withdraw()
        afficherFenetreAdmin()
    elif Id_VAR == "electeur" and Password_Var in motsDePasse and len(candidats) > 0: #Pr enter en tant qu'electeur
        win.withdraw()
        afficherFenetreElection()
    elif len(candidats) == 0: #Cas 0 candidats
        mb.showerror("Pas de candidats")
    else: #Cas mauvaise connection
        mb.showerror("Mauvais paramètres de connexion")

#prog principal
win = Tk()

#vars pr win election
ElectionWin = None
choixCandidat = StringVar()  #le choix de l'electeur est stocke ici

#vars admin win
AdminWin = None
candidats = []            #Liste des candidats
motsDePasse = []          #Liste des mots de passe
nbrElecteurs = IntVar()   #Variable pour connaitre le nbr d'electeurs
candi_VAR = StringVar()   #variable pour trouver les candidats

#interface de connexion
win.title("Connexion")

frame = ttk.Frame(win)
textLabel = ttk.Label(frame , text="Veuillez inserer votre identifiant et le mot de passe" ,relief=RAISED)
idLabel = ttk.Label(frame , text="Identifiant:")
passLabel = ttk.Label(frame , text="Mot de Passe:")
idEntry = ttk.Entry(frame)
passEntry = ttk.Entry(frame)
ButtonCo = ttk.Button(frame , text="me conneter" , command=login)

textLabel.grid(column=0 , row=0 , columnspan=2)
idLabel.grid(column=1 , row=1 , sticky = (E))
passLabel.grid(column=1 , row=2 ,  sticky = (E))
idEntry.grid(column=2 , row=1)
passEntry.grid(column=2 , row=2)
ButtonCo.grid(column=2 , row=3 , sticky = (E))

frame.grid()

for child in frame.winfo_children():
    child.grid_configure(padx=5 , pady=5)

win.mainloop()

