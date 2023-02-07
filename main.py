import tkinter as k
from qeyydiyat import *
from axtaris import *
win1 = k.Tk()
win1.config(bg="#d2d16f")
win1.geometry("700x400")
win1.resizable(width="False",height="False")

def kecid():
    win1.destroy()
    qeyd()
def kecid1():
    win1.destroy()
    axtar()

soz1 = k.Label(text="Qeydiyyatdan Keç!",bg = "#d2d16f",font="7")
soz1.place(x=105,y = 115)
soz2 = k.Label(text="Axtarış Et!",bg = "#d2d16f",font="7")
soz2.place(x=473,y=115)
kn1 = k.Button(text="Qeyd Ol!",borderwidth=1,font= "10", bg= "Pink",command= kecid)
kn1.place(x= 145,y= 150)
kn2 = k.Button(text="Axtarış!",borderwidth=1,font="10", bg= "Pink",command= kecid1)
kn2.place(x=480 , y=150 )
win1.mainloop()
