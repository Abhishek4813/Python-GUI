
from tkinter import *
root=Tk()
result=0
num1=num2=0
string='Null'
def callback():
    global result,num1,num2,string
    if gate.get()!=3:
         num1=int(entry1.get())
         num2=int(entry2.get())
    if gate.get()==1:
            result=num1 & num2
            string='AND'
    if gate.get()==2:
            result=num1|num2
            string='OR'
    if gate.get()==4:
            string='XOR'
            result=num1^num2
    if gate.get()==3:
        num1=int(entry1.get())
        entry2.insert(0,"Null")
        result=~num1
        string="NOT"
    entry3.insert(0,result)
    entry1.delete(0,END)
    entry2.delete(0,END)
def explain():
    entry3.delete(0,END)
    global num1,num2,result
    main=Tk()
    frameA=Frame(main)
    frameB=Frame(main)
    frameA.grid(row=0,column=0,pady=100,padx=350)
    frameB.grid(row=0,column=1,pady=100)
    label=Label(frameA,text="Number 1 :",font=("Areal",24,'bold'))
    label.grid(row=0,column=0,pady=100)
    entry=Entry(frameA,font=("Areal",24,'bold'),width=10,bg='#e9e9e9',fg='#696969')
    entry.insert(0,num1)
    entry.grid(row=0,column=1)
    label=Label(frameB,text="Binary :",font=("Areal",24,'bold'))
    label.grid(row=0,column=3,pady=100)
    entry=Entry(frameB,font=("Areal",24,'bold'),width=10,bg='#e9e9e9',fg='#696969')
    if num1>=0:
        entry.insert(0,bin(num1).lstrip("0b"))
    else:
        entry.insert(0,"-"+bin(num1).lstrip("-0b"))
    entry.grid(row=0,column=4)
    label=Label(frameA,text="Number 2 :",font=("Areal",24,'bold'))
    label.grid(row=1,column=0)
    entry=Entry(frameA,font=("Areal",24,'bold'),width=10,bg='#e9e9e9',fg='#696969')
    entry.insert(0,num2)
    entry.grid(row=1,column=1)
    label=Label(frameB,text="Binary :",font=("Areal",24,'bold'))
    label.grid(row=1,column=3)
    entry=Entry(frameB,font=("Areal",24,'bold'),width=10,bg='#e9e9e9',fg='#696969')
    if num2>=0:
        entry.insert(0,bin(num2).lstrip("0b"))
    else:
        entry.insert(0,"-"+bin(num2).lstrip("-0b"))
    entry.grid(row=1,column=4)
    label=Label(main,text=string,font=("Areal",24,'bold'))
    label.grid(row=2,column=0)
    entry=Entry(main,font=("Areal",24,'bold'),bg='#e9e9e9',fg='#696969')
    if result>=0:
        entry.insert(0,bin(result).lstrip("0b"))
    else:
        entry.insert(0,"-"+bin(result).lstrip("-0b"))
    entry.grid(row=2,column=1)
    label=Label(main,text="Decimal Result",font=("Areal",24,'bold'))
    label.grid(row=3,column=0,pady=100)
    entry=Entry(main,font=("Areal",24,'bold'),bg='#e9e9e9',fg='#696969')
    entry.insert(0,result)
    entry.grid(row=3,column=1)
frame1=Frame()
frame2=Frame()
frame3=Frame()
frame4=Frame()
frame1.grid(row=0,column=0,pady=100,padx=350)
frame2.grid(row=0,column=1,pady=100)
frame3.grid(row=1,column=0,columnspan=2)
frame4.grid(row=4,column=0,columnspan=2)
label=Label(frame1,text="Number 1 :",font=("Areal",24,'bold'))
label.grid(row=0,column=0)
entry1=Entry(frame1,font=("Areal",24,'bold'),width=5,bg='#e9e9e9',fg='#696969')
entry1.grid(row=0,column=1)
label=Label(frame2,text="Number 2 :",font=("Areal",24,'bold'))
label.grid(row=0,column=2)
entry2=Entry(frame2,font=("Areal",24,'bold'),width=5,bg='#e9e9e9',fg='#696969')
entry2.grid(row=0,column=3)
gate=IntVar()
and_gate=Radiobutton(frame3,text="AND",var=gate,value=1,font=("Areal",24,'bold'))
and_gate.grid(row=1,column=0,padx=150)
or_gate=Radiobutton(frame3,text=" OR",var=gate,value=2,font=("Areal",24,'bold'))
or_gate.grid(row=1,column=1)
not_gate=Radiobutton(frame3,text="NOT",var=gate,value=3,font=("Areal",24,'bold'))
not_gate.grid(row=2,column=0,pady=25)
xor_gate=Radiobutton(frame3,text="XOR",var=gate,value=4,font=("Areal",24,'bold'))
xor_gate.grid(row=2,column=1)
button1=Button(text="Result",font=("Areal",15,'bold'),command=callback,width=24)
button1.grid(row=3,column=0,pady=75)
button2=Button(text="Explanation",command=explain,font=("Areal",15,'bold'),width=24)
button2.grid(row=3,column=1)
label=Label(frame4,text='Result',font=("Areal",24,'bold'))
label.grid(row=4,column=0,padx=200)
entry3=Entry(frame4,font=("Areal",24,'bold'),bg='#e9e9e9',fg='#696969')
entry3.grid(row=4,column=1)
mainloop()
