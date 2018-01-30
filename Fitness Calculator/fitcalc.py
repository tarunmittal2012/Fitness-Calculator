import sys
from Tkinter import *
import tkMessageBox
top=Tk()
top.geometry('600x600+400+300')


top.title('Fitness')
for k in range(2,4):
    for l in range(4):
        m=Label(text='',relief=GROOVE)
        m.grid(row=k,column=l,sticky=NSEW)
for i in range(5,16):
    for j in range(2):
        l=Label(text='',relief=RIDGE)
        l.grid(row=i,column=j,sticky=NSEW)
name=StringVar()
age=IntVar()
weight=IntVar()
height=IntVar()
bplow=IntVar()
bphigh=IntVar()
pulserate=IntVar()
rbccount=IntVar()
wbccount=IntVar()
platelets=IntVar()
hb=IntVar()
uricacid=IntVar()
cholestrol=IntVar()
var=IntVar()
var1=IntVar()

l1=Label(top,text="WELCOME IN FITNESS WORLD",bg="grey",fg="red")
l1.grid(row=1,column=0)
L2=Label(top,text="Name:")

L2.grid(row=2,column=0)
E1=Entry(top,bd=5,textvariable=name)
E1.grid(row=2, column=1)

L3=Label(top,text="AGE:")
L3.grid(row=2, column=2)
E2=Entry(top,bd=5,textvariable=age)
E2.grid(row=2, column=3)

L4=Label(top,text="Gender")
L4.grid(row=3,column=0)
easy=Radiobutton(top,text="Male",value=1)
easy.grid(row=3,column=1)
moderate=Radiobutton(top,text="Female",value=2)
moderate.grid(row=3,column=2)



L5=Label(top,text="Weight:")
L5.grid(row=5,column=0)
E3=Entry(top,bd=5,textvariable=weight)
E3.grid(row=5,column=1)

L6=Label(top,text="Height:")
L6.grid(row=6,column=0)
E4=Entry(top,bd=5,textvariable=height)
E4.grid(row=6,column=1)

L7=Label(top,text="BP Low:")
L7.grid(row=7,column=0)
E5=Entry(top,bd=5,textvariable=bplow)
E5.grid(row=7,column=1)

L8=Label(top,text="BP High:")
L8.grid(row=8,column=0)
E6=Entry(top,bd=5,textvariable=bphigh)
E6.grid(row=8,column=1)

L9=Label(top,text="Pulse Rate:")
L9.grid(row=9,column=0)
E7=Entry(top,bd=5,textvariable=pulserate)
E7.grid(row=9,column=1)

L10=Label(top,text="RBC Count:")
L10.grid(row=10,column=0)
E8=Entry(top,bd=5,textvariable=rbccount)
E8.grid(row=10,column=1)

L11=Label(top,text="WBC \n Count:")
L11.grid(row=11,column=0)
E9=Entry(top,bd=5,textvariable=wbccount)
E9.grid(row=11,column=1)

L12=Label(top,text="Platelets:")
L12.grid(row=12,column=0)
E10=Entry(top,bd=5,textvariable=platelets)
E10.grid(row=12,column=1)

L13=Label(top,text="HB:")
L13.grid(row=13,column=0)
E11=Entry(top,bd=5,textvariable=hb)
E11.grid(row=13,column=1)

L14=Label(top,text="Uric Acid:")
L14.grid(row=14,column=0)
E12=Entry(top,bd=5,textvariable=uricacid)
E12.grid(row=14,column=1)

L15=Label(top,text="Cholestrol:")
L15.grid(row=15,column=0)
E13=Entry(top,bd=5,textvariable=cholestrol)
E13.grid(row=15,column=1)



def hellocallback():
    res=name.get()
    show=Label(top,text=("HELLO",res))
    show.grid(row=16,column=0)
A=Button(top,text="Generate Report",command=hellocallback(),height=2,width=15,bg="sky blue")
A.grid(row=15,column=2)
top.mainloop()
import sys
from Tkinter import *
import tkMessageBox
top=Tk()
top.geometry('500x500+400+300')
top.title("Report")
for m in range(2,11):
    for n in range(2):
        o=Label(text='',relief=GROOVE)
        o.grid(row=m,column=n,sticky=NSEW)
bmi=StringVar()
bp=StringVar()
pr=StringVar()
rc=StringVar()
wc=StringVar()
ps=StringVar()
hb1=StringVar()
ua=StringVar()
cl=StringVar()

var2=IntVar()
var3=IntVar()

L16=Label(top,text="BMI(Body Mass Index):")
L16.grid(row=2,column=0)
E14=Entry(top,bd=5,textvariable=bmi)
E14.grid(row=2,column=1)

L17=Label(top,text="BP(HIGH/MEDIUM/LOW):")
L17.grid(row=3,column=0)
E15=Entry(top,bd=5,textvariable=bp)
E15.grid(row=3,column=1)


L18=Label(top,text="Pulse Rate(HIGH/MEDIUM/LOW):")
L18.grid(row=4,column=0)
E16=Entry(top,bd=5,textvariable=pr)
E16.grid(row=4,column=1)

L19=Label(top,text="RBC Count(HIGH/MEDIUM/LOW):")
L19.grid(row=5,column=0)
E17=Entry(top,bd=5,textvariable=rc)
E17.grid(row=5,column=1)

L20=Label(top,text="WBC Count(HIGH/MEDIUM/LOW):")
L20.grid(row=6,column=0)
E18=Entry(top,bd=5,textvariable=wc)
E18.grid(row=6,column=1)

L21=Label(top,text="Platelets(HIGH/MEDIUM/LOW):")
L21.grid(row=7,column=0)
E19=Entry(top,bd=5,textvariable=ps)
E19.grid(row=7,column=1)

L22=Label(top,text="HB(HIGH/MEDIUM/LOW):")
L22.grid(row=8,column=0)
E20=Entry(top,bd=5,textvariable=hb1)
E20.grid(row=8,column=1)

L23=Label(top,text="Uric Acid(HIGH/MEDIUM/LOW):")
L23.grid(row=9,column=0)
E21=Entry(top,bd=5,textvariable=ua)
E21.grid(row=9,column=1)

L24=Label(top,text="Cholestrol(HIGH/MEDIUM/LOW):")
L24.grid(row=10,column=0)
E22=Entry(top,bd=5,textvariable=cl)
E22.grid(row=10,column=1)

def hellocallback1():
    res=name.get()
    show=Label(top,text=("Your Report is",res))
    show.grid(row=11,column=0)
A=Button(top,text="Report is:",command=hellocallback1,height=2,width=15,bg="orange")
A.grid(row=11,column=2)
top.mainloop()

