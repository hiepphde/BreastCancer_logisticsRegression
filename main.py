# -*- coding: utf-8 -*-
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import cv2
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import pickle
import sklearn

#Loadmodel
filename = 'E:/Study/NoronNhanTao/MODEL/LoR_BreastCancer.sav'
model = pickle.load(open(filename, 'rb'))

#Predict
def pred():
    pc1 = cbb1.get("1.0", "end-1c")
    pc1 = float(pc1)
    pc2 = cbb2.get("1.0", "end-1c")
    pc2 = float(pc2)
    pc3 = cbb3.get("1.0", "end-1c")
    pc3 = float(pc3)
    pc4 = cbb4.get("1.0", "end-1c")
    pc4 = float(pc4)
    pc5 = cbb5.get("1.0", "end-1c")
    pc5 = float(pc5)
    print(pc1 + pc2 + pc3 + pc4 + pc5)
    x = np.array([[pc1, pc2, pc3, pc4, pc5]])
    pred_main = model.predict(x)
    pred_main = [1 if y >= 0.5 else 0 for y in pred_main]
    pred_main = pred_main[0]
    kq=""
    if pred_main == 0:
        kq="Lành tính"
    else:
        kq="Ác tính"
    lbl_pred.configure(text=kq)



window = tk.Tk()
window.title('NHÓM 14')
greeting = tk.Label(text="Tools", font=('calibri', 20, 'bold'))
window.geometry("400x450")
greeting.pack()

style = Style()
style.configure('TButton', font=('calibri', 10, 'bold'), borderwidth='4')
style.map('TButton', foreground=[('active', '!disabled', 'blue')], background=[('active', 'black')])

lbl = Label(window)
lbl.pack(padx=15, pady=15)

###
lbl1 = ttk.Label(window, text="PC_1:")
lbl1.place(x=50, y=70)

cbb1 = Text(window, height=0.1, width=10)
cbb1.place(x=100, y=70)

###
lbl2 = ttk.Label(window, text="PC_2:")
lbl2.place(x=50, y=100)

cbb2 = Text(window, height=0.1, width=10)
cbb2.place(x=100, y=100)

###
lbl3 = ttk.Label(window, text="PC_3:")
lbl3.place(x=50, y=130)

cbb3 = Text(window, height=0.1, width=10)
cbb3.place(x=100, y=130)

###
lbl4 = ttk.Label(window, text="PC_4:")
lbl4.place(x=50, y=160)

cbb4 = Text(window, height=0.1, width=10)
cbb4.place(x=100, y=160)

###
lbl5 = ttk.Label(window, text="PC_5:")
lbl5.place(x=50, y=190)

cbb5 = Text(window, height=0.1, width=10)
cbb5.place(x=100, y=190)

frm_pred = Frame(window)
frm_pred.pack(side=BOTTOM)
lbl2 = Label(frm_pred, text='Predict is: ',font=('Arial', 13))
lbl2.pack(side=LEFT, padx=10, pady=10)
lbl_pred = Label(frm_pred,font=('Arial', 13))
lbl_pred.pack(padx=10, pady=10)


frm = Frame(window)
frm.pack(side=BOTTOM, padx=15, pady=15)
btn = Button(frm, text="Predict", command=pred())
btn.pack(side=tk.LEFT,padx=10, pady=10)
btn2 = Button(frm, text="Thoát", command=lambda: exit())
btn2.pack(padx=10, pady=10)



window.mainloop()