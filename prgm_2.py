from tkinter import*
window=Tk(className='MyApp',baseName='DemoApp')
window.geometry('400x500+150+200')
window.configure(bg='pink')
disply=Entry(window,font=('Arial',20),bg='black',fg='green',width=30)
disply.grid(row=0,column=0,columnspan=4)
def click(value):
    disply.insert(END,value)
def clear():
    disply.delete(0,END)
def delete():
    text=disply.get()
    disply.delete(0,END)
    disply.insert(0,text[:-1])
def equal():
    expression = disply.get()
    if "+" in expression:
            a, b = expression.split("+")
            result = float(a) + float(b)
    elif "-" in expression:
            a, b = expression.split("-")
            result = float(a) - float(b)

    elif "*" in expression:
            a, b = expression.split("*")
            result = float(a) * float(b)

    elif "/" in expression:
            a, b = expression.split("/")
            result = float(a) / float(b)

    elif "%" in expression:
            a, b = expression.split("%")
            result = float(a) % float(b)

    disply.delete(0, END)
    disply.insert(0, str(result))


Button(window,text='C',command=clear,width=16,height=2).grid(row=1,column=0)
Button(window,text='DEL',command=delete,width=16,height=2).grid(row=1,column=1,columnspan=3)

Button(window,text='/',width=8,height=3,command=lambda:click('/')).grid(row=2,column=0)
Button(window,text='*',width=8,height=3,command=lambda:click('*')).grid(row=2,column=1)
Button(window,text='7',width=8,height=3,command=lambda:click('7')).grid(row=2,column=2)
Button(window,text='8',width=8,height=3,command=lambda:click('8')).grid(row=2,column=3)

Button(window,text='9',width=8,height=3,command=lambda:click('9')).grid(row=3,column=0)
Button(window,text='-',width=8,height=3,command=lambda:click('-')).grid(row=3,column=1)
Button(window,text='4',width=8,height=3,command=lambda:click('4')).grid(row=3,column=2)
Button(window,text='5',width=8,height=3,command=lambda:click('5')).grid(row=3,column=3)

Button(window,text='6',width=8,height=3,command=lambda:click('6')).grid(row=4,column=0)
Button(window,text='+',width=8,height=3,command=lambda:click('+')).grid(row=4,column=1)
Button(window,text='1',width=8,height=3,command=lambda:click('1')).grid(row=4,column=2)
Button(window,text='2',width=8,height=3,command=lambda:click('2')).grid(row=4,column=3)

Button(window,text='3',width=8,height=3,command=lambda:click('3')).grid(row=5,column=0)
Button(window,text='.',width=8,height=3,command=lambda:click('.')).grid(row=5,column=1)
Button(window,text='0',width=8,height=3,command=lambda:click('0')).grid(row=5,column=2)
Button(window,text='%',width=8,height=3,command=lambda:click('%')).grid(row=5,column=3)

Button(window,text='=',command=equal,width=16,height=2).grid(row=6,column=0,columnspan=1)

window.mainloop()