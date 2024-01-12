#Topic*  Module And Pip
import tkinter as tk
m= tk.Tk()
m.title("Divjot")
button = tk.Button(m, text='Destroy', height=2, width=25, command=m.destroy)
button.pack()
m.mainloop()