from tkinter import *
from tkinter import ttk
#import sauvegarderentry

fenetreform=Tk()
fenetreform.title("Customer form")
    
frame=ttk.Frame(fenetreform)

Nameentry=StringVar()
Emailentry=StringVar()
Phonenumberentry=StringVar()



Name_label=ttk.Label(frame,text="Name",foreground="red",relief="raised")
Name_entry=ttk.Entry(frame,width=40,textvariable=Nameentry)

Email_label=ttk.Label(frame,text="Email",foreground="red",relief="raised")
Email_Entry=ttk.Entry(frame,width=40,textvariable=Emailentry)

Phonenumber_label=ttk.Label(frame,text="Phone Number",foreground="red",relief="raised")
Phonenumber_entry=ttk.Entry(frame,width=40,textvariable=Phonenumberentry)


save_button=ttk.Button(frame,text="sauvegarder parametres")#command=sauvegarderentry)




frame.grid()
Name_label.grid(column=1,row=1)
Phonenumber_label.grid(column=1,row=2)
Email_label.grid(column=1,row=3)
#######################################

Name_entry.grid(column=2,row=1)
Phonenumber_entry.grid(column=2,row=2)
Email_Entry.grid(column=2,row=3)


save_button.grid(column=3,row=4,ipadx=20)


for child in frame.winfo_children():child.grid_configure(padx=5,pady=5)
fenetreform.mainloop()
