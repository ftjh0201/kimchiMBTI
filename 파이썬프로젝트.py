import tkinter
window=tkinter.Tk()
window.title("")
window.geometry("320x200+100+100")
window.resizable(False, False)
frame1 = tkinter.Frame(window, relief="solid", bd=2)
frame2 = tkinter.Frame(window, relief="solid", bd=2)
frame1.pack(side=e)
frame2.pack()



#생성(Label)
a = tkinter.Label(frame1, text="프레임1_A")
b = tkinter.Label(frame1, text="프레임1_B")
c = tkinter.Label(frame2, text="프레임2_C")
d = tkinter.Label(frame2, text="프레임2_D")
a.pack()
b.pack()
c.grid(row=0, column=0)
d.grid(row=0, column=1)
#반영(window)


window.mainloop()