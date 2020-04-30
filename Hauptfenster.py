from tkinter import *
import tkinter.messagebox 
Fenster = Tk()
def help():
    tkinter.messagebox.showinfo('Befehle:','Hallo,hallo,wie geht es dir?, wie geht es dir, gut, help')
def Help():
    tkinter.messagebox.showinfo('About', 'Coder: André Siepmann, Version: 0.0.0')
def Bye():
    Fenster.quit()
menu = Menu(Fenster)
Fenster.config(menu=menu)
dateimenu= Menu(Fenster)
menu.add_cascade(label="Datei", menu=dateimenu)
dateimenu.add_command(label="EXIT", command=Bye)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=Help)
helpmenu.add_command(label="Commandos", command=help)
Textfeld_Oben = Label()
Textfeld_Oben.pack()
Eingabe_Oben = Entry()
Eingabe_Oben.pack()
Textfeld_Oben.config(text="Für hilfe bei den Commandos type help")
def Lese():
    if Eingabe_Oben.get() == 'Hallo':
        Textfeld_Oben.config(text="Hallo")
    elif Eingabe_Oben.get() == 'hallo':
        Textfeld_Oben.config(text="Hallo")
    elif Eingabe_Oben.get() == 'wie geht es dir?':
        Textfeld_Oben.config(text="Mir geht es gut und dir?")
    elif Eingabe_Oben.get() == 'wie geht es dir':
        Textfeld_Oben.config(text="Mir geht es gut und dir?")
    elif Eingabe_Oben.get() == 'gut':
        Textfeld_Oben.config(text="Das freut mich!")
    elif Eingabe_Oben.get() == 'help':
        Textfeld_Oben.config(text=" Commandos:Hallo,hallo,wie geht es dir?, wie geht es dir, gut, help")
    else:
        Textfeld_Oben.config(text="I don't know what to say")

Lesen = Button(text="Ich Lese und Antworte", command=Lese)
Lesen.pack()

mainloop()
