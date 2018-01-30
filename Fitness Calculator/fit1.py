from Tkinter import *
import tkMessageBox

class fit:
    def age(self):
        self.age=age
    def weight(self):
        self.weight=weight
    def height(self):
        self.height=height
    def bplow(self):
        if(self.bplow<=90):
            print("bp is low")
        else:
            print("Normal")
    def bphigh(self):
        if(self.bphigh>120):
            print("bp high")
        else:
            print("Normal")
    def pulserate(self):
        if(self.pulserate<60):
            print("Low")
        elif(self.pulserate>60 and self.pulserate<100):
            print("normal")
        else:
            print("High")
    def rbccount(self):
        if(self.rbccount<475000):
            print("Low")
        elif(self.rbccount>475000 and self.rbccount<610000):
            print("Normal")
        else:
            print("High")
    def wbccount(self):
        if(self.wbccount<4000):
            print("Low")
        elif(self.wbccount>4000 and self.wbccount<10000):
            print("Normal")
        else:
            print("High")
    def platelets(self):
        if(self.platelets<150000):
            print("Low")
        elif(self.platelets>150000 and self.platelets<450000):
            print("Normal")
        else:
            print("High")
        
        def hb(self):
            if(self.hb<12):
                print("Low")
            elif(self.hb>12 and self.hb<16):
                print("Normal")
            else:
                print("High")
        def uricacid(self):
            if(self.uricacid<4):
                print("Low")
            elif(self.uricacid>4 and self.uricacid<7):
                print("Normal")
            else:
                print("High")
        def cholestrol(self):
            if(self.cholestrol<40):
                print("Low")
            elif(self.cholestrol>40 and self.cholestrol<50):
                print("Normal")
            else:
                print("High")
        def __init__(self,top):
            
             
          """Constructor method"""
          top.title('Calulator') 
          top.geometry()
          self.e = Entry(top)
          self.e.grid(row=0,column=0,columnspan=6,pady=3)
          self.e.focus_set() #Sets focus on the input text area
    
  

#Generating Entrys
Entry(top,text="Name:",width=10,command=lambda:self.equals()).grid(row=4, column=4,columnspan=2)
Entry(top,text="age",width=3,command=lambda:self.action()).grid(row=1, column=4,columnspan=2)
Entry(top,text="weight",width=3,command=lambda:self.action()).grid(row=1, column=5)
Entry(top,text="height",width=3,command=lambda:self.height()).grid(row=4, column=3)
Entry(top,text="bplow",width=3,command=lambda:self.bplow()).grid(row=2, column=3)
Entry(top,text="bphigh",width=3,command=lambda:self.bphigh()).grid(row=3, column=3)
Entry(top,text="pulserate",width=3,command=lambda:self.pulserate()).grid(row=1, column=3) 
Entry(top,text="rbccount",width=3,command=lambda:self.rbccount()).grid(row=4, column=2)
Entry(top,text="wbccount",width=3,command=lambda:self.wbccount()).grid(row=1, column=0)
Entry(top,text="platelets",width=3,command=lambda:self.platelets()).grid(row=1, column=1)
Entry(top,text="hb",width=3,command=lambda:self.hb()).grid(row=1, column=2)
Entry(top,text="uricacid",width=3,command=lambda:self.action(4)).grid(row=2, column=0)
Entry(top,text="cholestrol",width=3,command=lambda:self.action(5)).grid(row=2, column=0)

Button(top,text="Generate Report",width=3,command=lambda:self.action(1)).grid(row=3, column=0)
top = Tk()
obj=fit(root) #object instantiated
root.mainloop()
