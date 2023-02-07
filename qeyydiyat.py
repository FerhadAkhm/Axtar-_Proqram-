def qeyd():
    import tkinter as t
    from PIL import ImageTk, Image
    win = t.Tk()
    win.title("Danni tapma programi")
    win.geometry("700x400")
    win.config(bg="Light Green")
    win.resizable(width="False", height="False")
    v = t.IntVar()

    # resize
    my_pic1 = Image.open("face.png")
    resized1 = my_pic1.resize((20,20), Image.ANTIALIAS)
    new_pic1 = ImageTk.PhotoImage(resized1)

    my_pic2 = Image.open("insta.png")
    resized2 = my_pic2.resize((20,20), Image.ANTIALIAS)
    new_pic2 = ImageTk.PhotoImage(resized2)

    my_pic3 = Image.open("tel.png")
    resized3 = my_pic3.resize((20,20), Image.ANTIALIAS)
    new_pic3 = ImageTk.PhotoImage(resized3)

    my_pic4 = Image.open("login.png")
    resized4 = my_pic4.resize((100,100), Image.ANTIALIAS)
    new_pic4 = ImageTk.PhotoImage(resized4)

    # widgets
    ad = t.Entry(win,width=30, bg= "Grey")
    yazi = t.Label(win,text="Ad       :",bg="Light Green",font="bold 15")
    sad = t.Entry(win,width=30, bg="Gray")
    oglan = t.Radiobutton(win,text = "Kisi",bg="Grey",variable=v,value = 1)
    qiz = t.Radiobutton(win,text = "Qadin",bg="Grey",variable=v,value = 0)
    yas_deyisen = t.Scale(win,from_=0, to=120,bg= "Grey",length=180,orient= 'horizontal')
    yazi1 = t.Label(win,text="S. Adı  :",bg="Light Green", font="bold 15")
    yazi2 = t.Label(win,text="Yaşı    :",bg="Light Green", font="bold 15")
    yazi3 = t.Label(win,text="Cinsi    :",bg="Light Green", font="bold 15")
    frame1= t.Frame(win,width= 250,height= 400,bg = "#407088")
    a = t.Button(frame1,text="Təstiq Et!",fg="Light Green",bg="Black",font="bold 13 italic")
    b = t.Button(frame1,image= new_pic4, borderwidth=0,width=100,height=100,bg="#407088",activebackground="#407088")
    yazi4 = t.Label(frame1, text="Şəkil Yüklə!",fg="Orange" ,bg="#407088", font="bold 15")
    yazi5 = t.Label(frame1, text="Link daxil edin!!",fg="Red" ,bg="#407088", font="bold 10")
    sekil1 = t.Label(frame1, image=new_pic1, width=15,height=15,bg="#407088")
    sekil2 = t.Label(frame1, image=new_pic2, width=20,height=15,bg="#407088")
    sekil3 = t.Label(frame1, image=new_pic3, width=15,height=15,bg="#407088")
    face_ac = t.Entry(frame1,width=30, bg="Gray")
    insta_ac = t.Entry(frame1,width=30, bg="Gray")
    tel =t.Entry(frame1,width=30, bg="Gray", borderwidth= 0)
    c = t.Button(frame1,text="Yenidən Yaz!",fg="Light Green",bg="Black",font="bold 13 italic")

    # placements
    a.place(x = 140, y = 350)
    ad.place(x = 90, y = 80)
    yazi.place(x = 10, y= 73)
    sad.place(x = 90, y = 120)
    yazi1.place(x = 10, y = 113)
    yazi2.place(x = 10, y = 160)
    yazi3.place(x = 10, y = 200)
    yazi4.place(x = 67,y = 120)
    oglan.place(x = 90, y = 205)
    qiz.place(x = 136, y = 205)
    yas_deyisen.place(x=90,y=150)
    b.place(x = 70, y= 20)
    frame1.place(x = 450, y = 0)
    sekil1.place(x = 15, y = 180)
    sekil2.place(x=15,y = 210)
    sekil3.place(x=15,y= 240)
    face_ac.place(x = 40, y = 180)
    insta_ac.place(x = 40, y = 210)
    tel.place(x = 40, y = 240)
    yazi5.place(x= 130, y = 260)
    c.place(x=10,y = 350)
    win.mainloop()