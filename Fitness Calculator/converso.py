from Tkinter import *
import Tkinter
import tkMessageBox
top = Tk()
top.configure(background='green')

L0 = Label(top, text="NUMBER CONVERSION CALCULATOR",
           fg="red",
           font="Times").grid(row=0,column=1)
"""--------------------BINARY TO OTHERS-------------------"""
LB = Label(top,text="Binary To Others",
           fg="red",
           font="Times").grid(row=1,column=1)
"""--------------------BINARY TO DECIMAL-------------------"""
L2=Label(top,text="Binary To Decimal  ",
         fg="red",
         font="Times").grid(row=2,column=0)
E2 = Entry(top,bd=5)
E2.grid(row=2,column=1)
E22=Entry(top,bd=5)
E22.grid(row=2,column=3)

def abc():
    if((str(E2.get())=="")):
        tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        binary_to_decimal()
def binary_to_decimal():
    binary=str(E2.get())
    btd = int(binary, 2)
    E22.insert(0,btd)
    
B2=Tkinter.Button(top,relief=RAISED,text="Convert Binary to Decimal",fg='green',command=abc)
B2.grid(row=2,column=2)
"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------BINARY TO OCTAL-------------------"""
L3=Label(top,text="Binary To Octal  ",
         fg="red",
         font="Times").grid(row=3,column=0)
E3 = Entry(top,bd=5)
E3.grid(row=3,column=1)
E33=Entry(top,bd=5)
E33.grid(row=3,column=3)

def binary_to_octal():
    binary=str(E3.get())
    bto= int(binary, 2)
    bto=oct(bto)
    str(bto)
    bto=bto[1:]
    E33.insert(0,bto)

B3=Tkinter.Button(top,relief=RAISED,text="Convert Binary To Octal",fg='green',command=binary_to_octal)
B3.grid(row=3,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------BINARY TO HEXADECIMAL-------------------"""
L4=Label(top,text="Binary To Hexadecimal  ",
         fg="red",
         font="Times").grid(row=5,column=0)
E4 = Entry(top,bd=5)
E4.grid(row=5,column=1)
E44=Entry(top,bd=5)
E44.grid(row=5,column=3)

def binary_to_hexadecimal():
    binary=str(E4.get())
    bth = int(binary, 2)
    bth=hex(bth)
    str(bth)
    bth=bth[2:]
    bth=bth.upper()
    E44.insert(0,bth)

B4=Tkinter.Button(top,relief=RAISED,text="Convert Binary To Hexadecimal",fg='green',command=binary_to_hexadecimal)
B4.grid(row=5,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------BINARY TO OTHERS COMPLETE---------------"""

"""-------------------------------------------------------------------------------------------------------------------------------------------------"""



"""--------------------DECIMAL TO OTHERS-------------------"""
LD = Label(top,text="Decimal To Others",
           fg="red",
           font="Times").grid(row=6,column=1)
"""--------------------DECIMAL TO BINARY-------------------"""
L5=Label(top,text="Decimal To Binary   ",
         fg="red",
         font="Times").grid(row=7,column=0)
E5 = Entry(top,bd=5)
E5.grid(row=7,column=1)
E55=Entry(top,bd=5)
E55.grid(row=7,column=3)

def decimal_to_binary():
    decimal=str(E5.get())
    dtb = int(decimal)
    dtb=bin(dtb)
    str(dtb)
    dtb=dtb[2:]
    E55.insert(0,dtb)
B5=Tkinter.Button(top,relief=RAISED,text="Convert Binary to Decimal",fg='green',command=decimal_to_binary)
B5.grid(row=7,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------DECIMAL TO OCTAL-------------------"""
L6=Label(top,text="Decimal To Octal  ",
         fg="red",
         font="Times").grid(row=8,column=0)
E6 = Entry(top,bd=5)
E6.grid(row=8,column=1)
E66=Entry(top,bd=5)
E66.grid(row=8,column=3)

def decimal_to_octal():
    decimal=str(E6.get())
    dto=int(decimal)
    dto=oct(dto)
    str(dto)
    dto=dto[1:]
    E66.insert(0,dto)


B6=Tkinter.Button(top,relief=RAISED,text="Convert Decimal To Octal",fg='green',command=decimal_to_octal)
B6.grid(row=8,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------DECIMAL TO HEXADECIMAL-------------------"""
L7=Label(top,text="Decimal To Hexadecimal  ",
         fg="red",
         font="Times").grid(row=9,column=0)
E7 = Entry(top,bd=5)
E7.grid(row=9,column=1)
E77=Entry(top,bd=5)
E77.grid(row=9,column=3)

def decimal_to_hexadecimal():
    decimal=str(E7.get())
    dth = int(decimal)
    dth=hex(dth)
    str(dth)
    dth=dth[2:]
    dth=dth.upper()
    E77.insert(0,dth)

B7=Tkinter.Button(top,relief=RAISED,text="Convert Decimal To Hexadecimal",fg='green',command=decimal_to_hexadecimal)
B7.grid(row=9,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------DECIMAL TO OTHERS COMPLETE---------------"""
"""-------------------------------------------------------------------------------------------------------------------------------------------------"""



"""--------------------OCTAL TO OTHERS-------------------"""
LO = Label(top,text="Octal To Others ",
           fg="red",
           font="Times").grid(row=10,column=1)
"""--------------------OCTAL TO BINARY-------------------"""
L8=Label(top,text="Octal To Binary   ",
         fg="red",
         font="Times").grid(row=11,column=0)
E8 = Entry(top,bd=5)
E8.grid(row=11,column=1)
E88=Entry(top,bd=5)
E88.grid(row=11,column=3)

def octal_to_binary():
    octal=str(E8.get())
    otb = str(int(octal,8))
    otb=int(otb)
    otb=bin(otb)
    otb=otb[2:]
    E88.insert(0,otb)
B8=Tkinter.Button(top,relief=RAISED,text="Convert Octal To Binary",fg='green',command=octal_to_binary)
B8.grid(row=11,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------OCTAL TO DECIMAL-------------------"""
L9=Label(top,text="Octal To Decimal  ",
         fg="red",
         font="Times").grid(row=12,column=0)
E9 = Entry(top,bd=5)
E9.grid(row=12,column=1)
E99=Entry(top,bd=5)
E99.grid(row=12,column=3)

def octal_to_decimal():
    octal=str(E9.get())
    otd= str(int(octal,8))
    E99.insert(0,otd)

B9=Tkinter.Button(top,relief=RAISED,text="Convert Octal To Decimal",fg='green',command=octal_to_decimal)
B9.grid(row=12,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------OCTAL TO HEXADECIMAL-------------------"""
L10=Label(top,text="Octal To Hexadecimal  ",
         fg="red",
         font="Times").grid(row=13,column=0)
E10= Entry(top,bd=5)
E10.grid(row=13,column=1)
E101=Entry(top,bd=5)
E101.grid(row=13,column=3)

def octal_to_hexadecimal():
    octal=str(E10.get())
    oth = str(int(octal,8))
    oth=int(oth)
    oth=hex(oth)
    oth=oth[2:]
    oth=oth.upper()
    E101.insert(0,oth)

B10=Tkinter.Button(top,relief=RAISED,text="Convert Octal To Hexadecimal",fg='green',command=octal_to_hexadecimal)
B10.grid(row=13,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------OCTAL TO OTHERS COMPLETE---------------"""




"""-------------------------------------------------------------------------------------------------------------------------------------------------"""



"""--------------------HEXADECIMAL TO OTHERS-------------------"""
LH = Label(top,text="Hexadecimal To Others ",
           fg="red",
           font="Times").grid(row=14,column=1)
"""--------------------HEXADECIMAL TO BINARY-------------------"""
L11=Label(top,text="Hexadecimal To Binary   ",
         fg="red",
         font="Times").grid(row=15,column=0)
E11= Entry(top,bd=5)
E11.grid(row=15,column=1)
E111=Entry(top,bd=5)
E111.grid(row=15,column=3)

def hexadecimal_to_binary():
    hexadecimal=str(E11.get())
    htb = int(hexadecimal,16);
    htb=bin(htb)
    htb=htb[2:]
    E111.insert(0,htb)
    
B11=Tkinter.Button(top,relief=RAISED,text="Convert Hexadecimal to Binary",fg='green',command=hexadecimal_to_binary)
B11.grid(row=15,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------HEXADECIMAL TO DECIMAL-------------------"""
L12=Label(top,text="Hexadecimal To Decimal  ",
         fg="red",
         font="Times").grid(row=16,column=0)
E12= Entry(top,bd=5)
E12.grid(row=16,column=1)
E121=Entry(top,bd=5)
E121.grid(row=16,column=3)

def hexadecimal_to_decimal():
    hexadecimal=str(E12.get())
    htd=int(hexadecimal,16)
    E121.insert(0,htd)
    
B12=Tkinter.Button(top,relief=RAISED,text="Convert Hexadecimal To Decimal",fg='green',command=hexadecimal_to_decimal)
B12.grid(row=16,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------------HEXADECIMAL TO OCTAL-------------------"""
L13=Label(top,text="Hexadecimal To Octal  ",
         fg="red",
         font="Times").grid(row=17,column=0)
E13= Entry(top,bd=5)
E13.grid(row=17,column=1)
E131=Entry(top,bd=5)
E131.grid(row=17,column=3)

def hexadecimal_to_octal():
    hexadecimal=str(E13.get())
    hto =int(hexadecimal,16)
    hto=oct(hto)
    hto=hto[1:]
    E131.insert(0,hto)
B13=Tkinter.Button(top,relief=RAISED,text="Convert Hexadecimal To Octal",fg='green',command=hexadecimal_to_octal)
B13.grid(row=17,column=2)

"""-------------------XXXXXXXXXXXXXXXX-------------------"""

"""--------------OCTAL TO OTHERS COMPLETE---------------"""

"""------------------TO RESET ALL ENTRIES---------------"""
def clear_textbox():
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    E5.delete(0, END)
    E6.delete(0, END)
    E7.delete(0, END)
    E8.delete(0, END)
    E9.delete(0, END)
    E10.delete(0, END)
    E11.delete(0, END)
    E12.delete(0, END)
    E13.delete(0, END)
    #OUTPUT ENTIRES CLEAR
    E22.delete(0, END)
    E33.delete(0, END)
    E44.delete(0, END)
    E55.delete(0, END)
    E66.delete(0, END)
    E77.delete(0, END)
    E88.delete(0, END)
    E99.delete(0, END)
    E101.delete(0, END)
    E111.delete(0, END)
    E121.delete(0, END)
    E131.delete(0, END)

B14=Button(top, text='RESET ALL ENTRIES',command=clear_textbox)
B14.grid(row=20,column=0)
"""-------------TO RESET ALL ENTRIES ENDED---------------"""

def close_window (): 
    top.destroy()
B15=Button (top,text = "EXIT",command=close_window)
B15.grid(row=20,column=3)
D=Label(top,text="Developed By:-")
D.grid(row=19,column=0)
D1=Label(top,text="Shubham Pandey")
D1.grid(row=19,column=1)
D2=Label(top,text="Akhil Pathania")
D2.grid(row=19,column=2)
D3=Label(top,text="Seval Patel")
D3.grid(row=19,column=3)



top.mainloop()



