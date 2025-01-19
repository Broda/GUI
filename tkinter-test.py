from tkinter import *

window = Tk()
window.title("My First Python GUI")
window.geometry("640x480")

menu = Menu(window)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
window.config(menu=menu)

label = Label(window, text="Hello, World!")
label.grid()

txt = Entry(window, width=10)
txt.grid(column=1, row=0)

def button_Click():
    print(f"Button clicked! {txt.get()}")
    
button = Button(window, text="Click me!", fg="red", command=button_Click)
button.grid(column=2, row=0)

window.mainloop()
