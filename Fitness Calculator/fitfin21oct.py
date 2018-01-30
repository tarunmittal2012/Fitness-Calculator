from Tkinter import *
import Tkinter
import tkMessageBox
top = Tk()
#top.configure(background='green')

L0 = Label(top, text="Fitness Calculator",
           fg="purple",
           font="Times").grid(row=0,column=1)

L1=Label(top,text="Name",
           fg="red",
           font="Times").grid(row=1,column=0)
E1= Entry(top,bd=5)
E1.grid(row=1,column=1)

L2=Label(top,text="age ",
         fg="red",
         font="Times").grid(row=2,column=0)
E2= Entry(top,bd=5)
E2.grid(row=2,column=1)
l3=Label(top,text="weight",fg="red",font="Times").grid(row=3,column=0)
E3= Entry(top,bd=5)
E3.grid(row=3,column=1)
l4=Label(top,text="height",fg="red",font="Times").grid(row=4,column=0)
E4=Entry(top,bd=5)
E4.grid(row=4,column=1)

l5=Label(top,text="bplow",fg="red",font="Times").grid(row=5,column=0)
E5=Entry(top,bd=5)
E5.grid(row=5,column=1)



def abc():
    if((str(E1.get())=="")):
        tkMessageBox.showinfo("!!ERROR!!", "INVALID INPUT")
    else:
        bplow()
def bplow():
    bplow1=str(E4.get())
    if (bplow1<='90'):
        print("Low")
    else:
        print("Normal")
    E15.insert(bplow1)
    E15.grid(row=1,column=1)
        

L6=Label(top,text="bphigh",
         fg="red",
         font="Times").grid(row=6,column=0)
E6 = Entry(top,bd=5)
E6.grid(row=6,column=1)
def bphigh():
    bphigh1=str(E6.get())
    if(bphigh1>120):
        prstr("High")
    else:
        print("Normal")
    E15.insert(bphigh1)
    E15.grid(row=2,column=1)
    



L7=Label(top,text="Pulserate",
         fg="red",
         font="Times").grid(row=7,column=0)
E7= Entry(top,bd=5)
E7.grid(row=7,column=1)

def pulserate():
    pulserate1=str(E7.get())
    if(pulserate1<'60'):
        print ("Low")
    elif (pulserate>'60' and pulserate<'100'):
        print("Normal")
    else:
        print("High")
    E16.insert(pulserate1)
    E16.grid(row=3,column=1)
    


L8=Label(top,text="RBCcount",
           fg="red",
           font="Times").grid(row=8,column=0)
E8 = Entry(top,bd=5)
E8.grid(row=8,column=1)

def rbccount():
    rbccount1=str(E8.get())
    if(rbccount1<'475000'):
        print("Low")
    elif(rbccount1>'475000' and rbccount1<'610000'):
        print("Normal")
    else:
        print("High")
    E17.insert(rbccount1)
    E17.grid(row=4,column=1)

    

L9=Label(top,text="WBCcount",
         fg="red",
         font="Times").grid(row=9,column=0)
E9= Entry(top,bd=5)
E9.grid(row=9,column=1)

def wbccount():
    wbccount1=int(E9.get())
    if(wbccount1<4000):
        print("Low")
    elif(wbccount1>4000 and wbccount1<10000):
        print("Normal")
    else:
        print("High")
    E18.insert(wbccount1)
    E18.grid(row=5,column=1)


L10=Label(top,text="Platelets",
         fg="red",
         font="Times").grid(row=10,column=0)
E10 = Entry(top,bd=5)
E10.grid(row=10,column=1)

def platelets():
    platelets1=int(E10.get())
    if(platelets1<150000):
        print("Low")
    elif (platelets1>150000 and platelets1<450000):
        print("Normal")
    else:
        print("High")
    E19.insert(platelets1)
    E19.grid(row=6,column=1)


L11=Label(top,text="HB",
         fg="red",
         font="Times").grid(row=11,column=0)
E11 = Entry(top,bd=5)
E11.grid(row=11,column=1)

def hb(self):
    hb1=int(E11.get())
    if(hb1<12):
        print("Low")
    elif(hb1>12 and hb1<16):
        print("Normal")
    else:
        print("High")
    E20.insert(hb1)
    E20.grid(row=7,column=1)

L12=Label(top,text="URIC ACID",
           fg="red",
           font="Times").grid(row=12,column=0)
E12 = Entry(top,bd=5)
E12.grid(row=12,column=1)
def uricacid1():
    uricacid1=int(E12.get())
    if(uricacid1<4):
        print("Low")
    elif(uricacid1>4 and uricacid1<7):
        print("Normal")
    else:
        print("High")
    E21.insert(uricacid1)
    E21.grid(row=8,column=1)

L13=Label(top,text="CHOLESTROL",
         fg="red",
         font="Times").grid(row=13,column=0)
E13 = Entry(top,bd=5)
E13.grid(row=13,column=1)
def cholestrol(self):
    cholestrol1=int(E13.get())
    if(cholestrol1<40):
        print("Low")
    elif(cholestrol1>40 and cholestrol1<50):
        print("Normal")
    else:
         print("High")
    E22.insert(cholestrol1)
    E22.grid(row=9,column=1)


def result():

    top=Tk()
    for m in range(2,11):
        for n in range(2):
            o=Label(text='',relief=GROOVE)
            o.grid(row=m,column=n,sticky=NSEW)
  

    L16=Label(top,text="BMI(Body Mass Index):",fg="red")
    L16.grid(row=2,column=0)
    E14=Entry(top,bd=5)
    E14.grid(row=2,column=1)

    L17=Label(top,text="BP(HIGH/MEDIUM/LOW):",fg="red")
    L17.grid(row=3,column=0)
    E15=Entry(top,bd=5)
    E15.grid(row=3,column=1)


    L18=Label(top,text="Pulse Rate(HIGH/MEDIUM/LOW):",fg="red")
    L18.grid(row=4,column=0)
    E16=Entry(top,bd=5)
    E16.grid(row=4,column=1)

    L19=Label(top,text="RBC Count(HIGH/MEDIUM/LOW):",fg="red")
    L19.grid(row=5,column=0)
    E17=Entry(top,bd=5)
    E17.grid(row=5,column=1)

    L20=Label(top,text="WBC Count(HIGH/MEDIUM/LOW):",fg="red")
    L20.grid(row=6,column=0)
    E18=Entry(top,bd=5)
    E18.grid(row=6,column=1)

    L21=Label(top,text="Platelets(HIGH/MEDIUM/LOW):",fg="red")
    L21.grid(row=7,column=0)
    E19=Entry(top,bd=5)
    E19.grid(row=7,column=1)

    L22=Label(top,text="HB(HIGH/MEDIUM/LOW):",fg="red")
    L22.grid(row=8,column=0)
    E20=Entry(top,bd=5)
    E20.grid(row=8,column=1)

    L23=Label(top,text="Uric Acid(HIGH/MEDIUM/LOW):",fg="red")
    L23.grid(row=9,column=0)
    E21=Entry(top,bd=5)
    E21.grid(row=9,column=1)

    L24=Label(top,text="Cholestrol(HIGH/MEDIUM/LOW):",fg="red")
    L24.grid(row=10,column=0)
    E22=Entry(top,bd=5)
    E22.grid(row=10,column=1)
    


B1=Button(top, text='Generate Report',command=result,bg="sky blue")
B1.grid(row=13,column=2)

"""------------------TO RESET ALL ENTRIES---------------"""
def clear_textbox():
    E1.delete(0,END)
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
D1=Label(top,text="Tarun Mittal")
D1.grid(row=19,column=1)
D2=Label(top,text="Himanshu Goyal")
D2.grid(row=19,column=2)




top.mainloop()



