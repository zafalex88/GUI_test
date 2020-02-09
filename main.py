import tkinter as tk

#creating the window
root = tk.Tk(className='square root', useTk=1)
canvas1 = tk.Canvas(root, width= 500, height=400)
canvas1.pack()

#creating labels
label1 = tk.Label(root, text="Calculate The Square Root")
label1.config(font=('verdana', 18))
canvas1.create_window(250, 40, window=label1)

label2 = tk.Label(root, text='Enter any number: ')
label2.config(font=('verdana', 12))
canvas1.create_window(250, 120, window=label2)

#creating the entry box
entry = tk.Entry(root)
canvas1.create_window(250, 150, window=entry)

#square root function with labels
def getSquareRoot():
    x1 = entry.get()
    
    label1 = tk.Label(root, text='The square root of ' + x1 + ' is:')
    label1.config(font=('verdana', 8, 'bold'))
    canvas1.create_window(250, 240, window=label1)
    
    label2 = tk.Label(root, text= float(x1)**0.5)
    label2.config(font=('verdana', 9, 'bold'))
    canvas1.create_window(250, 260, window=label2)

#creating a button and adding the function    
button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
button1.config(bg='red', fg='white', font=('verdana', 9, 'bold'))
canvas1.create_window(250, 200, window=button1)

root.mainloop()