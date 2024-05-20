import tkinter
import time
import sys
import os
from datetime import date

def data():
    data_show = date.today()
    txt5.config(text=data_show)


def timing():
    time_cur = time.strftime("%I : %M : %S")
    txt3.config(text=time_cur)
    txt3.after(200, timing)

def restart():
    res = sys.executable
    os.execl(res, res, *sys.argv)

win = tkinter.Tk()
WID = (win.winfo_screenwidth() // 2) - 300
HEI = (win.winfo_screenheight() // 2) - 150
win.geometry(f"600x300+{WID}+{HEI}")
win.title("Дата и время")
win.resizable(False, False)


txt1 = tkinter.Label(win, text="Дата и время", font=("Arial Bold", 32))
txt1.pack()

txt2 = tkinter.Label(win, text="(12-часовой)", font=("Arial Bold", 12))
txt2.place(x=260, y=50)

txt3 = tkinter.Label(win, font=("Arial Bold", 60), background="green")
txt3.place(x=100, y=117)
timing()

txt4 = tkinter.Label(win, text="hors" + " "*13+"minuts"+ " "*10+ "seconds",  font=("Arial Bold", 18))
txt4.place(x=125, y=227)

txt5 = tkinter.Label(win, font=("Arial Bold", 18))
txt5.place(x=250, y=77)
data()

btn_res = tkinter.Button(text="Перезагрузить", command=restart)
btn_res.place(x=450, y=270)


btn_exit = tkinter.Button(win, text="Выйти", command=sys.exit)
btn_exit.place(x=550,y=270)





win.mainloop()
