from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def sauvegarderConfigsAdmin():
    global candidats
    global fenetreAdmin
    a=listecandidatsentry.get()
    candidats=a.split(",")
    fenetreAdmin.destroy()
    
    
def afficherfenetreAdmin():
    global fenetreAdmin
    fenetreAdmin=Toplevel(fenetre)
    
    
    
    
    fenetreAdmin.title("Configuration de L election")
    
    frame=ttk.Frame(fenetreAdmin)
    listecandidatsentry=StringVar()
    
    candidats_label=ttk.Label(frame,text="Veuillez inserer les noms des candidats(separes par des ',')",background="grey")
    nbrelecteur_label=ttk.Label(frame,text="Nombre des electeurs",background="grey")
    candidats_entry=ttk.Entry(frame,width=40,textvariable=listecandidatsentry)
    nbrelecteur_entry=ttk.Entry(frame,width=40,textvariable=nbElecteurs)
    save_button=ttk.Button(frame,text="sauvegarder parametres",command=sauvegarderConfigsAdmin)


    
    frame.grid()
    nbrelecteur_label.grid(column=2,row=3)
    candidats_label.grid(column=2,row=2,padx=20)
    candidats_entry.grid(column=3,row=2,pady=10)
    nbrelecteur_entry.grid(column=3,row=3,pady=10)
    save_button.grid(column=3,sticky=(S,E),ipadx=20)


    for child in frame.winfo_children():child.grid_configure(padx=5,pady=5)
    fenetreAdmin.mainloop()




def afficherfenetreelection():
    fen3=Toplevel(fenetre)
    

    




























    

def login():
    if (passw.get())in motsdePasse and idf.get() =="electeur":
        if len(candidats)>0:
            fenetre.withdraw()
            afficherFenetreElection()
                
    elif passw.get()=="admin" and idf.get()=="admin":
        fenetre.withdraw()
        afficherfenetreAdmin()
    else:
        messagebox.showinfo("Error", "Mauvais	paramètres de connexion")
        
    
fenetre=Tk()
fenetre.title("Connexion")
listecandidatsentry=StringVar()
fenetreElection=None
choixcandidat=StringVar()

fenetreAdmin= None
valeurCandidats = StringVar()
idf=StringVar()
passw=StringVar()
candidats=[]
motsdePasse=[]
nbElecteurs=IntVar()

frame=ttk.Frame(fenetre)
intro_label=ttk.Label(frame,text="Veuillez inserer votre identifiant et le mot de passe",background="grey")
idf_label=ttk.Label(frame,text="Identifiant:",background="grey")
passw_label=ttk.Label(frame,text="Mot de Passe:",background="grey")
idf_entry=ttk.Entry(frame,width=40,textvariable=idf)
passw_entry=ttk.Entry(frame,width=40,textvariable=passw)
connect_button=ttk.Button(frame,text="me connecter",command=login)



frame.grid()
intro_label.grid()
idf_label.grid(column=2,row=2)
passw_label.grid(column=2,row=3,padx=20)
idf_entry.grid(column=3,row=2,pady=10)
passw_entry.grid(column=3,row=3,pady=10)
connect_button.grid(column=3,sticky=(S,E),ipadx=20)

for child in frame.winfo_children():child.grid_configure(padx=5,pady=5)
#it creates spaces on the frame boarders

fenetre.mainloop()
