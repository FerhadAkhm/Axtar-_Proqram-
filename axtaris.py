def axtar():
    import tkinter as l
    win2 = l.Tk()
    win2.resizable(width=False,height=False)
    win2.config(bg="Purple")
    win2.geometry("400x400")
    duy = l.Button(text="Axtar",fg="Purple",bg="grey",font="bold 13")
    yaz = l.Label(win2, text="Ad       :", bg="Purple", font="bold 13")
    yaz1 = l.Label(win2, text="S. Adı  :", bg="Purple", font="bold 13")
    giris1 = l.Entry(bg="Pink")
    giris2 = l.Entry(bg="Pink")
    yaz.place(x = 10, y= 96)
    yaz1.place(x=10,y=196)
    giris1.place(x =100 , y = 100)
    giris2.place(x = 100, y = 200)
    duy.place(x=320, y= 340)

    win2.mainloop()