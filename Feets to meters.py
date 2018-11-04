from tkinter import *
from tkinter import ttk


def calculate():
    try:
        r=float(feet.get())*0.305
        result_label["text"]=r
        result_label["background"]="yellow"
    except:
        print("Valeur Non Valide")
    
        

win=Tk()
win_label=ttk.Label(text="Win",background="yellow",foreground="red")
win_label.grid()
win.title("Feet to Meter")
win.rowconfigure(1,weight=1)
win.columnconfigure(1,weight=1)
win.columnconfigure(2,weight=1)
win.columnconfigure(3,weight=1)
win.rowconfigure(2,weight=1)
win.rowconfigure(3,weight=1)


frame=ttk.Frame(win)


feet=StringVar()
                               


feet_entry=ttk.Entry(win,textvariable=feet)
equalto_label=ttk.Label(win,text="is equal to")
result_label=ttk.Label(win)
meters_label=ttk.Label(win,text="meters")
Feets_label=ttk.Label(win,text="Feets",background='blue',foreground='yellow')
quit_button=ttk.Button(win,text="EXIT",command=win.destroy)
Calculate_button=ttk.Button(win,text="Calculate",command=calculate)

                               

equalto_label.grid(column=1,row=3,padx=30)
Calculate_button.grid(column=3,row=4,ipady=10)
quit_button.grid(column=1,row=4,ipady=10)
frame.grid(padx=30,pady=30)
feet_entry.grid(column=2,row=2)
result_label.grid(column=2,row=3,padx=30)
meters_label.grid(column=3,row=3)
Feets_label.grid(column=4,row=2)



############################
frame2=ttk.Frame(win)



feet=StringVar()
                               

frame2_label=ttk.Label(text="frame2",background="yellow",foreground="red")
feet_entry=ttk.Entry(frame2,textvariable=feet)
equalto_label=ttk.Label(frame2,text="is equal to")
result_label=ttk.Label(frame2)
meters_label=ttk.Label(frame2,text="meters")
Feets_label=ttk.Label(frame2,text="Feets",background='blue',foreground='yellow')
quit_button=ttk.Button(frame2,text="EXIT",command=win.destroy)
Calculate_button=ttk.Button(frame2,text="Calculate",command=calculate)

                               
frame2_label.grid(padx=30,pady=30)
equalto_label.grid(column=1,row=3,padx=30)
Calculate_button.grid(column=3,row=4,ipady=10)
quit_button.grid(column=1,row=4,ipady=10)
frame2.grid(padx=30,pady=30,column=2)
feet_entry.grid(column=2,row=2)
result_label.grid(column=2,row=3,padx=30)
meters_label.grid(column=3,row=3)
Feets_label.grid(column=4,row=2)
##############################


frame3=ttk.Frame(win)


feet=StringVar()
                               

frame3_label=ttk.Label(text="frame3",background="yellow",foreground="red")
feet_entry=ttk.Entry(frame3,textvariable=feet)
equalto_label=ttk.Label(frame3,text="is equal to")
result_label=ttk.Label(frame3)
meters_label=ttk.Label(frame3,text="meters")
Feets_label=ttk.Label(frame3,text="Feets",background='blue',foreground='yellow')
quit_button=ttk.Button(frame3,text="EXIT",command=win.destroy)
Calculate_button=ttk.Button(frame3,text="Calculate",command=calculate)

                               
frame3_label.grid(padx=30,pady=30)
equalto_label.grid(column=1,row=3,padx=30)
Calculate_button.grid(column=3,row=4,ipady=10)
quit_button.grid(column=1,row=4,ipady=10)
frame3.grid(padx=30,pady=30,column=2)
feet_entry.grid(column=2,row=2)
result_label.grid(column=2,row=3,padx=30)
meters_label.grid(column=3,row=3)
Feets_label.grid(column=4,row=2)






















































win.mainloop()

