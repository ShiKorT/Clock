import tkinter
import time
import sys
import os

def timing():
    time_cur = time.strftime("%H : %M : %S")
    txt2.config(text=time_cur)
    txt2.after(200, timing)
def restart():
    res = sys.executable
    os.execl(res, res, *sys.argv)

win = tkinter.Tk()
WID = (win.winfo_screenwidth() // 2) - 300
HEI = (win.winfo_screenheight() // 2) - 150
win.geometry(f"600x300+{WID}+{HEI}")
win.title("Часы")
win.resizable(False, False)


txt1 = tkinter.Label(win, text="Часы", font=("Arial Bold", 32))
txt1.pack()

txt2 = tkinter.Label(win, font=("Arial Bold", 60), background="green")
txt2.place(x=100,y=80)
timing()

txt3 = tkinter.Label(win, text="hors" + " "*13+"minuts"+ " "*10+ "seconds",  font=("Arial Bold", 18))
txt3.place(x=125,y=200)

btn_res = tkinter.Button(text="Перезагрузить", command=restart)
btn_res.place(x=450,y=270)


btn_exit = tkinter.Button(win, text="Выйти", command=sys.exit)
btn_exit.place(x=550,y=270)





win.mainloop()
