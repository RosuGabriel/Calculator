from tkinter import *

root = Tk()
root.geometry('285x431')
root.resizable(False,False)
root.title('calculator')
root.configure(background='#B8E2F2')
#root.iconbitmap(r'calculator.ico') # path to the icon

# Create an entry widget
e = Entry(root, font = ('Aerial', 15))
e.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 10)

result = 0 
ex = ''

def button_click(number):
    global ex
    if number == 'clear':
        global result
        result = 0
        e.delete(0, END)
        ex = ''
    elif number != '.' or number not in e.get():  
        if ex == '':
           actual = e.get()
           e.delete(0, END)
           e.insert(0, actual + str(number))
           result=float(actual + str(number))
        else:   
            actual = e.get()
            e.delete(0, END)
            e.insert(0, actual + str(number))
        
def eq_button():  
    global result
    global ex
    
    if ex == '':
        print(result)
        e.delete(0, END)    
    if ex == 'ad':
        result = float(result)
        result += float(e.get())
        print(result)
        e.delete(0, END)
    if ex == 'scad':
        result = float(result)
        result= result-float(e.get())
        print(result)
        e.delete(0,END)
    if ex == 'mul':
        result = float(result)
        result = result * float(e.get())
        print(result)
        e.delete(0,END)
    if ex == 'div':
        result = float(result)
        result=result / float(e.get())
        print(result)
        e.delete(0,END)
    elif ex == 'pr':
        result = result * float(e.get())
        if result - int(result) == 7.105427357601002e-15:
            result = int(result)*1.0
        elif result - int(result) == 0.9999999999999929:
            result = int(result)*1.0+1
        print(result)
    if result == 0:
        result = 0
    elif result.is_integer():
        result = int(result)
    
    e.delete(0, END)
    e.insert(0, result)
    ex = ''
    
def addition_button():
    global result
    global ex

    if ex == '':
        print(result)
        e.delete(0, END)    
    if ex == 'ad':
        result = float(result)
        result += float(e.get())
        print(result)
        e.delete(0, END)
    if ex == 'scad':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result - float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'mul':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result * float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'div':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0,END)
        else:
            result = result / float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'pr':
        result = result * float(e.get())
        if result - int(result) == 7.105427357601002e-15:
            result = int(result) * 1.0
        elif result - int(result) == 0.9999999999999929:
            result = int(result) * 1.0 + 1
        print(result)   
        
    ex = 'ad'
   
def sub_button():
    global result
    global ex
    
    if ex == '':
        print(result)
        e.delete(0, END)    
    if ex == 'ad':
        result = float(result)
        result += float(e.get())
        print(result)
        e.delete(0, END)
    if ex == 'scad':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result - float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'mul':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result * float(e.get())
            print(result)
            e.delete(0, END) 
    if ex == 'div':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result / float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'pr':
        result = result * float(e.get())
        if result - int(result) == 7.105427357601002e-15:
            result = int(result) * 1.0
        elif result - int(result) == 0.9999999999999929:
            result = int(result) * 1.0 + 1
        print(result)      
        
    ex='scad'
    
def mul_button():
    global result
    global ex
    
    if ex == '':
        print(result)
        e.delete(0, END)    
    if ex == 'ad':
        result = float(result)
        result += float(e.get())
        print(result)
        e.delete(0, END)
    if ex == 'scad':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result - float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'mul':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result * float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'div':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result / float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'pr':
        result = result * float(e.get())
        if result - int(result) == 7.105427357601002e-15:
            result = int(result) * 1.0
        elif result - int(result) == 0.9999999999999929:
            result = int(result) * 1.0 + 1
        print(result)     
    
    ex = 'mul'
    
def impartire():
    global result
    global ex
    
    if ex == '':
        print(result)
        e.delete(0, END)    
    if ex == 'ad':
        result = float(result)
        result += float(e.get())
        print(result)
        e.delete(0, END)
    if ex == 'scad':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result-float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'mul':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result= result * float(e.get())
            print(result)
            e.delete(0, END)
        
    if ex == 'div':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result / float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'pr':
         result = result * float(e.get())
         if result-int(result) == 7.105427357601002e-15:
             result = int(result) * 1.0
         elif result - int(result) == 0.9999999999999929:
             result = int(result) * 1.0 + 1
         print(result)          
    
    ex = 'div'
    
def procent():
    global result
    global ex
     
    if ex == '':
        print(result)
        e.delete(0, END)    
    if ex == 'ad':
        result = float(result)
        result += float(e.get())
        print(result)
        e.delete(0, END)
    if ex == 'scad':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result-float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'mul':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0, END)
        else:
            result = result * float(e.get())
            print(result)
            e.delete(0, END)
    if ex == 'div':
        result = float(result)
        if result == 0:
            result = float(e.get())
            e.delete(0,END)
        else:
            result = result / float(e.get())
            print(result)
            e.delete(0, END)

    result = float(result)
    result = result/100
    print(result)
    e.delete(0, END)
    ex='pr'

btnclear = Button(root, text='C', padx=39, pady=20, command= lambda: button_click('clear'), bg='#FC8955')
buton1 = Button(root, text='1',padx=40, pady=20, command= lambda: button_click(1), bg='#B8E2F2')
buton2 = Button(root, text='2',padx=40, pady=20, command= lambda: button_click(2), bg='#B8E2F2')
buton3 = Button(root, text='3',padx=40, pady=20, command= lambda: button_click(3), bg='#B8E2F2')
buton4 = Button(root, text='4',padx=40, pady=20, command= lambda: button_click(4), bg='#B8E2F2')
buton5 = Button(root, text='5',padx=40, pady=20, command= lambda: button_click(5), bg='#B8E2F2')
buton6 = Button(root, text='6',padx=40, pady=20, command= lambda: button_click(6), bg='#B8E2F2')
buton7 = Button(root, text='7',padx=40, pady=20, command= lambda: button_click(7), bg='#B8E2F2')
buton8 = Button(root, text='8',padx=40, pady=20, command= lambda: button_click(8), bg='#B8E2F2')
buton9 = Button(root, text='9',padx=40, pady=20, command= lambda: button_click(9), bg='#B8E2F2')
buton0 = Button(root, text='0',padx=40, pady=20, command= lambda: button_click(0), bg='#B8E2F2')
buton_pct = Button(root, text='. ',padx=40, pady=20, command= lambda: button_click('.'), bg='#B8E2F2')
button_add = Button(root, text='+',padx=39, pady=20, command= addition_button, bg='#89CFF0')
buton_pr = Button(root, text='%', padx=38, pady=20, command= procent, bg='#B8E2F2')
egal = Button(root, text='=',padx=39, pady=20, command= eq_button, bg='#FC8955')
buton_minus = Button(root, text=' -',padx=39, pady=20, command= sub_button, bg='#89CFF0')
buton_mul = Button(root, text='x',padx=40, pady=20, command= mul_button, bg='#89CFF0')
buton_div = Button(root, text=' /',padx=39, pady=20, command= impartire, bg='#89CFF0')

btnclear.grid(row=6,columnspan=1, column=2)
buton0.grid(row=5, column=0)
buton1.grid(row=4, column=0)
buton2.grid(row=4, column=1)
buton3.grid(row=4, column=2)
buton4.grid(row=3, column=0)
buton5.grid(row=3, column=1)
buton6.grid(row=3, column=2)
buton7.grid(row=2, column=0)
buton8.grid(row=2, column=1)
buton9.grid(row=2, column=2)

button_add.grid(row=6, column=1)
egal.grid(row=7, column=2)
buton_minus.grid(row=6, column=0)
buton_mul.grid(row=7, column=1)
buton_div.grid(row=7,column=0)
buton_pr.grid(row=5, column=2)
buton_pct.grid(row=5, column=1)

root.mainloop()