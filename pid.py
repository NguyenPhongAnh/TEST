import time
from tkinter import *
import tkinter
import serial
import numpy as np
import math
from math import *
##test github

board = serial.Serial('COM5',9600)
time.sleep(1)


open_window = Tk()
open_window.title("Giao diện ON-OFF")
open_window.geometry("400x300")

def home():
    string = str('h')
    board.write(string.encode())
    data_nhan = board.readline()
    print("data nhan: ", data_nhan)
    goc_1 = 0
def quit():
    control_window.destroy()
def goc():
    lbl_1.configure(text = "Động cơ góc " + txt_goc.get())
    goc_1 = txt_goc.get()
    string = str(goc_1) +'\n'
    chuoi = string.encode()
    print("da gui: ",chuoi)
    board.write(chuoi)  
    data_nhan = board.readline()
    print("data nhan: ", data_nhan)
def chuyen_window():
    global control_window
    global txt_goc
    global lbl_1
    control_window = Tk()
    control_window.title("Giao diện ON-OFF")
    control_window.geometry("400x300")
    open_window.destroy()
    btn_home = Button(control_window,text = "HOME", command=home)
    btn_home.place(x=100,y=100,width=50,height=50)
    btn_quit = Button(control_window,text = "QUIT",command=quit)
    btn_quit.place(x=10,y=100,width=50,height=50)
    lbl_1 = Label(control_window, text= "Control Window")
    lbl_1.pack()
    lbl_2 = Label(control_window,text = "Nhập góc")
    lbl_2.place(x=50,y=50)
    txt_goc = Entry(control_window,width=20)
    txt_goc.place(x=160,y=50)
    btn_goc = Button(control_window, text = "Góc",command=goc)
    btn_goc.place(x=260,y=50)



lbl = Label(open_window, text= "Open Window")
lbl.place (x=10,y=0)
btn_open = Button(open_window, text = "Chuyển cửa sổ", command = chuyen_window)
btn_open.place(x=10,y=50,width=100,height=100)

open_window.mainloop()
control_window.mainloop()
