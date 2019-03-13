from time import *
from tkinter import *
a=Tk()
a.title("Calculator")
def ddd():
    t1.delete(0,END)
def ccc():
    t1.delete(0)
def bb1():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "1")
def bb2():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "2")
def bb3():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "3")
def bb4():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "4")
def bb5():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "5")
def bb6():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "6")
def bb7():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "7")
def bb8():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "8")
def bb9():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "9")
def bb14():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, "0")
def bb10():
    signn = 1
    cc1(signn)
    t1.delete(0, END)
    t1.insert(END, "+")
def bb11():
    signn = 11
    cc1(signn)
    t1.delete(0, END)
    t1.insert(END, "-")
def bb12():
    signn = 111
    cc1(signn)
    t1.delete(0, END)
    t1.insert(END, "*")
def bb13():
    signn = 1111
    cc1(signn)
    t1.delete(0, END)
    t1.insert(END, "/")
def bb15():
    ff2 = t1.get()
    if f1 == 1:
        rrr = float(ff) + float(ff2)
    elif f2 == 1:
        rrr = float(ff) - float(ff2)
    elif f3 == 1:
        rrr = float(ff) * float(ff2)
    elif f4 == 1:
        rrr = float(ff) / float(ff2)
    else:
        rrr = 0
    t1.delete(0, END)
    t1.insert(END, rrr)
def bb16():
    if t1.get()=="+" or t1.get()=="-" or t1.get()=="*" or t1.get()=="/" :
        t1.delete(0, END)
    t1.insert(END, ".")
# def qq():
#     mmm = messagebox.askyesno(title="Quit",message="Are you sure you want to quit")
#     if(mmm==1):
#         a.destroy()
# def hh():
#
# mm1=Menu()
# mm2=Menu()
# mm2.add_command(label="History",command=hh)
# mm2.add_command(label="Quit",command=qq)
# mm1.add_cascade(label="File",menu=mm2)
# a.config(menu=mm1)
t1=Entry(textvariable=a,relief=RIDGE,bd=5,justify=RIGHT)
t1.place(x=1,y=1)
b1=Button(text="1",height=1,width=5,command=bb1)
b1.place(x=1,y=90)
b2=Button(text="2",height=1,width=5,command=bb2)
b2.place(x=50,y=90)
b3=Button(text="3",height=1,width=5,command=bb3)
b3.place(x=100,y=90)
b4=Button(text="4",height=1,width=5,command=bb4)
b4.place(x=1,y=60)
b5=Button(text="5",height=1,width=5,command=bb5)
b5.place(x=50,y=60)
b6=Button(text="6",height=1,width=5,command=bb6)
b6.place(x=100,y=60)
b7=Button(text="7",height=1,width=5,command=bb7)
b7.place(x=1,y=30)
b8=Button(text="8",height=1,width=5,command=bb8)
b8.place(x=50,y=30)
b9=Button(text="9",height=1,width=5,command=bb9)
b9.place(x=100,y=30)
b10=Button(text="+",height=1,width=5,command=bb10)
b10.place(x=150,y=30)
b11=Button(text="-",height=1,width=5,command=bb11)
b11.place(x=150,y=60)
b12=Button(text="*",height=1,width=5,command=bb12)
b12.place(x=150,y=90)
b13=Button(text="/",height=1,width=5,command=bb13)
b13.place(x=150,y=120)
b14=Button(text="0",height=1,width=5,command=bb14)
b14.place(x=50,y=120)
b15=Button(text="=",height=1,width=5,command=bb15)
b15.place(x=100,y=120)
b16=Button(text=".",height=1,width=5,command=bb16)
b16.place(x=1,y=120)
b17=Button(text="Clear",height=1,width=27,command=ddd)
b17.place(x=1,y=150)
b18=Button(text="Delete",height=1,width=27,command=ccc)
b18.place(x=1,y=180)

def cc1(signn):
    global ff,f1,f2,f3,f4
    ff=t1.get()
    if signn==1:
        f1=1;f2=0;f3=0;f4=0
    elif signn==11:
        f1=0;f2=1;f3=0;f4=0
    elif signn==111:
        f1=0;f2=0;f3=1;f4=0
    elif signn==1111:
        f1=0;f2=0;f3=0;f4=1
    else:
        f1=0;f2=0;f3=0;f4=0
a.mainloop()

