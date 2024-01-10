import tkinter as tk
m = tk.Tk()
m.title("Hello World")
button = tk.Button(m, text='Stop', height=25, width=25, command=print("hello"))
button.pack()
m.mainloop()