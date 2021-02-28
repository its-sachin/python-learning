import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Tabs')

nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1, text = 'One')
nb.add(page2, text = 'Two')
# nb.grid(row = 0, column = 0)
nb.pack(expand = True, fill = 'both')

lable1 = ttk.Label(page1, text = "This is lable 1")
lable1.grid(row = 0, column = 0)


lable2 = ttk.Label(page2, text = "This is lable 2")
lable2.grid(row = 0, column = 0)


win.mainloop()