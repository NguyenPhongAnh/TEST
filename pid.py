from tkinter import*
import serial
import numpy as np
import math
from math import *
import time
def action():
    top.destroy()
    window.deiconify()


ser = serial.Serial('Com4', 9600)
window = Tk()
top=Toplevel()  # màn hình hiện thị đầu tiên
top.title("GIAO DIỆN ĐẦU") #tên
top.geometry('787x573') #kích  thước
MC=PhotoImage(file="abia.png") # hình
Label(top,image=MC).grid() # vị trí
Button(top,text="     START     ",font='Times 20 bold', bg='#00b300',fg='white',command=lambda:action()).place(x=300,y=500) # nút nhấn

window.withdraw()


def bangDH():
    theta1 = int(textBox7.get("1.0", "end-1c"))
    theta2 = int(textBox5.get("1.0", "end-1c"))
    theta3 = int(textBox6.get("1.0", "end-1c"))

    print("theta1", theta1)
    print("theta2", theta2)
    print("theta3", theta3)

    L1 = 105.2
    L2 = 83
    L3 = 83
    c1 = math.cos(math.radians(theta1))
    s1 = math.sin(math.radians(theta1))
    c2 = math.cos(math.radians(theta2))
    s2 = math.sin(math.radians(theta2))
    c23 = math.cos(math.radians(theta2 + theta3))
    s23 = math.sin(math.radians(theta2 + theta3))
    PX = c1 * ((L3 * c23) + (L2 * c2))
    PY = s1 * ((L3 * c23) + (L2 * c2))
    PZ = ( L3 * s23) + (L2 * s2 ) + L1
    PX = round(PX, 2)
    PY = round(PY, 2)
    PZ = round(PZ, 2)
    print(PX, PY, PZ)
    Px_FK.delete(0, END)
    Py_FK.delete(0, END)
    Pz_FK.delete(0, END)
    Px_FK.insert(0,PX)
    Py_FK.insert(0,PY)
    Pz_FK.insert(0,PZ)


def donghocthuan():
    L1 = 105.2
    L2 = 83
    L3 = 83

    theta1 = int(textBox7.get("1.0", "end-1c"))
    theta2 = int(textBox5.get("1.0", "end-1c"))
    theta3 = int(textBox6.get("1.0", "end-1c"))
    print(theta1)

    bangDH()
    if ((int(theta1) < 10) and (int(theta1) >= 0)):
        theta1 = '000' + str(theta1)
    elif((int(theta1) >= 10) and (int(theta1) < 100)):
        theta1 = '00' + str(theta1)
    elif ((int(theta1) >= 100)):
        theta1 = '0' + str(theta1)
    else:
        if((int(theta1) > -10)):
            theta1 = abs((theta1))
            theta1 = str('-')+str('00')+str(theta1)
        elif (((int(theta1) <= -10) and (int(theta1) >-100))):
            theta1 = abs((theta1))
            theta1 = str('-') + str('0') + str(theta1)
    print("theta1: ",theta1)
    ########### THETA 2 #########################################################################
    # theta2 bắt đầu từ 0 đến 180 độ tương ứng xung từ 0 đến 800
    if ((int(theta2) < 10) and (int(theta2) >= 0)):
        theta2 = '000' + str(theta2)
    elif ((int(theta2) >= 10) and (int(theta2) < 100)):
        theta2 = '00' + str(theta2)
    elif ((int(theta2) >= 100)):
        theta2 = '0' + str(theta2)
    else:
        if ((int(theta2) > -10)):
            theta2 = abs((theta2))
            theta2 = str('-') + str('00') + str(theta2)
        elif ((int(theta2) <= -10 and (int(theta2) > -100))):
            theta2 = abs((theta2))
            theta2 = str('-') + str('0') + str(theta2)
    print("theta2: ", theta2)
    ########### THETA 3 #########################################################################
    # theta1 bắt đầu từ -90 đến 90 độ tương ứng xung từ 400 đến 1200 nên 800 ở giữa

    if ((int(theta3) < 10) and (int(theta3) >= 0)):
        theta3 = '000' + str(theta3)
    elif ((int(theta3) >= 10) and (int(theta3) < 100)):
        theta3 = '00' + str(theta3)
    elif ((int(theta3) >= 100)):
        theta3 = '0' + str(theta3)
    else:
        if ((int(theta3) > -10)):
            theta3 = abs((theta3))
            theta3 = str('-') + str('00') + str(theta3)
        elif ((int(theta3) <= -10 and (int(theta3) >-100))):
            theta3 = abs((theta3))
            theta3 = str('-') + str('0') + str(theta3)
    print("theta3: ", theta3)

    string = str(theta1) + str(theta2) + str(theta3)  + '0' + '\n'  # cộng tất cả gửi qa arduino, đht để số 0, đhn để số 1
    # string = str(d1) + str(theta2) + str(theta3) + str(tocdo_thuan) + '0' + '\n'
    print("da gui: ", string)
    ser.write(string.encode())
    data_nhan = ser.readline()  # đọc tín hiệu từ arduino
    print("datanhanstp3: ", data_nhan)
    print("//////////////////////////////////")


def donghocnghich():
    L1 = 105.2
    L2 = 83
    L3 = 83

    PX = float(textBox1.get("1.0", "end-1c"))
    PY = float(textBox2.get("1.0", "end-1c"))
    PZ = float(textBox3.get("1.0", "end-1c"))

    r = -math.sqrt(math.pow(PX,2) + math.pow(PY,2))
    theta1 = math.atan2(PY, PX)

    a = ((L1 - PZ) * (L1 - PZ) - L2 * L2 - L3 * L3 + r * r) / (2 * L2 * L3)
    if (a > 1):
        a = round(a,0)

    theta3 = math.acos(a)

    theta2 = math.atan2(L2 + L3 * math.cos(theta3), L3 * math.sin(theta3)) + math.atan2(r, PZ -L1 );
    theta2 = math.degrees(theta2)
    theta1 = math.degrees(theta1)
    theta3 = math.degrees(theta3)
    theta1 = int(theta1)
    theta2 = int(theta2)
    theta3 = int(theta3)
    theta1 = round(theta1, 0)
    theta2 = round(theta2, 0)
    theta3 = round(theta3, 0)
    The1_IK.delete(0, END)
    The2_IK.delete(0, END)
    The3_IK.delete(0, END)
    The1_IK.insert(0, theta1)
    The2_IK.insert(0, theta2)
    The3_IK.insert(0, theta3)
    ########theta1####################################
    if ((int(theta1) < 10) and (int(theta1) >= 0)):
        theta1 = '000' + str(theta1)
    elif((int(theta1) >= 10) and (int(theta1) < 100)):
        theta1 = '00' + str(theta1)
    elif ((int(theta1) >= 100)):
        theta1 = '0' + str(theta1)
    else:
        if((int(theta1) > -10)):
            theta1 = abs((theta1))
            theta1 = str('-')+str('00')+str(theta1)
        elif ((int(theta1) <= -10 and (int(theta1) >-100))):
            theta1 = abs((theta1))
            theta1 = str('-') + str('0') + str(theta1)
    print("theta1: ",theta1)
    ########### THETA 2 #########################################################################
    # theta2 bắt đầu từ 0 đến 180 độ tương ứng xung từ 0 đến 800
    if ((int(theta2) < 10) and (int(theta2) >= 0)):
        theta2 = '000' + str(theta2)
    elif ((int(theta2) >= 10) and (int(theta2) < 100)):
        theta2 = '00' + str(theta2)
    elif ((int(theta2) >= 100)):
        theta2 = '0' + str(theta2)
    else:
        if ((int(theta2) > -10)):
            theta2 = abs((theta2))
            theta2 = str('-') + str('00') + str(theta2)
        elif ((int(theta2) <= -10 and (int(theta2) > -100))):
            theta2 = abs((theta2))
            theta2 = str('-') + str('0') + str(theta2)
    print("theta2: ", theta2)
    ########### THETA 3 #########################################################################
    # theta1 bắt đầu từ -90 đến 90 độ tương ứng xung từ 400 đến 1200 nên 800 ở giữa

    if ((int(theta3) < 10) and (int(theta3) >= 0)):
        theta3 = '000' + str(theta3)
    elif ((int(theta3) >= 10) and (int(theta3) < 100)):
        theta3 = '00' + str(theta3)
    elif ((int(theta3) >= 100)):
        theta3 = '0' + str(theta3)
    else:
        if ((int(theta3) > -10)):
            theta3 = abs((theta3))
            theta3 = str('-') + str('00') + str(theta3)
        elif ((int(theta3) <= -10 and (int(theta3) >-100))):
            theta3 = abs((theta3))
            theta3 = str('-') + str('0') + str(theta3)
    print("theta3: ", theta3)

    string = str(theta1) + str(theta2) + str(theta3)  + '0' + '\n'  # cộng tất cả gửi qa arduino, đht để số 0, đhn để số 1
    # string = str(d1) + str(theta2) + str(theta3) + str(tocdo_thuan) + '0' + '\n'
    print("da gui: ", string)
    ser.write(string.encode())
    data_nhan = ser.readline()  # đọc tín hiệu từ arduino
    print("datanhanstp3: ", data_nhan)
    print("//////////////////////////////////")
def home():
    string = str('dddddddddddddddd')
    ser.write(string.encode())
    print("datanhanstp3: ", string)
def ATOB():
    string = "000000600050" + "007000700100" + "007000000200" + "007000700100" + "000000700100" + "000000000200" + "000000700100" + "000000000000" + "dddddddddddd"
    ser.write(string.encode())

def BTOC():
    string = "000000600050" + "000000700100" + "000000000200" + "000000700100" + "013000700100" + "013000000200" + "013000700100" + "000000000000" + "dddddddddddd"
    ser.write(string.encode())

def CTOA():
    string = "000000600050" + "013000700100" + "013000000202" + "013000700100" + "007000700100" + "007000000200" + "007000700100" + "000000000000"+ "dddddddddddd"
    ser.write(string.encode())
#####GIAO DIỆN
window.title("Power System")
window.geometry('1500x200')
window.geometry("1400x800")  # thiet lap cua cua so win
window.resizable(False, False)
window.configure(bg = 'white')
my_canvas = Canvas(window, width= 50, height=50, bg='light blue')
my_canvas.pack(fill= BOTH, expand= True)
my_canvas.create_line(700, 200, 700, 450, fill='black', width=3)
btn1 = Button(window, text="SEND FK", font =("Times",20,"bold"), command=donghocthuan, fg="black", bg="green").place(x=200, y=550)
## GIAO DIỆN ĐỘNG THUẬN
textBox7 = Text(window, height=1, width=7, font=("Helvetica", 20)) ###Theta1
textBox7.pack()
textBox7.place(x=200, y=300)
textBox5 = Text(window, height=1, width=7, font=("Helvetica", 20)) ###Theta2
textBox5.pack()
textBox5.place(x=200, y=370)
textBox6 = Text(window, height=1, width=7, font=("Helvetica", 20)) ###Theta3
textBox6.pack()
textBox6.place(x=200, y=440)


##PX PY PZ của động thuận
Label(window,text='     Px     ',font='Times 20 bold',fg='red').place(x=400,y=300)
Label(window,text='     Py     ',font='Times 20 bold',fg='green').place(x=400,y=370)
Label(window,text='     Pz     ',font='Times 20 bold',fg='blue').place(x=400,y=440)

Px_FK = Entry(window,width=7,font='Times 20 bold')
Px_FK.place(x=550,y=300)
Py_FK = Entry(window,width=7,font='Times 20 bold')
Py_FK.place(x=550,y=370)
Pz_FK = Entry(window,width=7,font='Times 20 bold')
Pz_FK.place(x=550,y=440)
lable_text_2 = Label(window, text = "FORWARD KINEMATIC", font ="Times 20 bold", bg = 'light blue',fg = 'red').place(x = 130,y = 200)
lable_text_3 = Label(window, text = "Theta 2", font ="Times 20 bold", bg = 'light blue',fg = 'black').place(x = 70,y = 370)
lable_text_4 = Label(window, text = "Theta 1", font ="Times 20 bold", bg = 'light blue',fg = 'black').place(x = 70,y = 300)
lable_text_5 = Label(window, text = "Theta 3", font ="Times 20 bold", bg = 'light blue',fg = 'black').place(x = 70,y = 440)

lable_text_8 = Label(window, text = "CONTROL INTERFACE", font ="Times 40 bold", bg = 'light blue',fg = 'red').place(x = 400,y = 10)

    #################################### DONG HOC NGHICH ##################################################
lable_text_7 = Label(window, text = "INVERSE KINEMATIC", font ="Times 20 bold", bg = 'light blue',fg = 'red').place(x = 900,y = 200)
btn2 = Button(window, text="SEND IK ", font =("Times",20,"bold"), command=donghocnghich, fg="black", bg="green").place(x=200, y=620)

textBox1 = Text(window, height=1, width=7, font=("Helvetica", 20)) ###PX
textBox1.pack()
textBox1.place(x=980, y=300)
textBox2 = Text(window, height=1, width=7, font=("Helvetica", 20))###PY
textBox2.pack()
textBox2.place(x=980, y=370)
textBox3 = Text(window, height=1, width=7, font=("Helvetica", 20))###PZ
textBox3.pack()
textBox3.place(x=980, y=440)
lable_text_9 = Label(window, text = "Theta 2", font ="Times 20 bold", bg = 'light blue',fg = 'black').place(x = 1100,y = 370)
lable_text_10 = Label(window, text = "Theta 1", font ="Times 20 bold", bg = 'light blue',fg = 'black').place(x = 1100,y = 300)
lable_text_11 = Label(window, text = "Theta 3", font ="Times 20 bold", bg = 'light blue',fg = 'black').place(x = 1100,y = 440)
The1_IK = Entry(window,width=7,font='Times 20 bold')
The1_IK.place(x=1200,y=300)
The2_IK = Entry(window,width=7,font='Times 20 bold')
The2_IK.place(x=1200,y=370)
The3_IK = Entry(window,width=7,font='Times 20 bold')
The3_IK.place(x=1200,y=440)

##PX PY PZ của động nghịch
Label(window,text='     Px     ',font='Times 20 bold',fg='red').place(x=830,y=300)
Label(window,text='     Py     ',font='Times 20 bold',fg='green').place(x=830,y=370)
Label(window,text='     Pz     ',font='Times 20 bold',fg='blue').place(x=830,y=440)

#################################### HOME ##################################################
btn_home = Button(window, text="  HOME   ", font =("Times",20,"bold"), command=home, fg="black", bg="red").place(x=200, y=690)

#################################### NUT HUT VAT ###########################
btn_AB = Button(window, text="GRIP A TO B", font =("Times",20,"bold"), command=ATOB, fg="black", bg="red").place(x=1050, y=550)
btn_BC = Button(window, text="GRIP B TO C", font =("Times",20,"bold"), command=BTOC, fg="black", bg="red").place(x=1050, y=620)
btn_CA = Button(window, text="GRIP C TO A", font =("Times",20,"bold"), command=CTOA, fg="black", bg="red").place(x=1050, y=690)
window.mainloop()