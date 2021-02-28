import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Menubar')

mainmenu = tk.Menu(win)

def func():
    print('Function is called')

file_menu = tk.Menu(mainmenu, tearoff = 0)
file_menu.add_command(label = 'NewFile', command = func)
file_menu.add_command(label = 'NewWindow', command = func)
file_menu.add_separator()
file_menu.add_command(label = 'OpenFile', command = func)
file_menu.add_command(label = 'OpenFolder', command = func)

open_recent_menu = tk.Menu(file_menu,tearoff = 0)
open_recent_menu.add_command(label = 'Recent Closed Editor', command = func)
open_recent_menu.add_command(label = 'Clear Recent Closed Editor', command = func)
file_menu.add_cascade(label = 'Open Recent Menu', menu = open_recent_menu)

mainmenu.add_cascade(label = 'File',menu = file_menu)


edit_menu = tk.Menu(mainmenu, tearoff = 0)
edit_menu.add_command(label = 'Undo', command = func)
edit_menu.add_command(label = 'Redo', command = func)
edit_menu.add_separator()
edit_menu.add_command(label = 'Cut', command = func)
edit_menu.add_command(label = 'Copy', command = func)
mainmenu.add_cascade(label = 'Edit',menu = edit_menu)

canvas = tk.Canvas(win,width = 500, height = 500)
canvas.grid(row = 0,column = 0)
photo = tk.PhotoImage(file = '4.png')
canvas.create_image(0,0, image = photo)

win.config(menu=mainmenu)

win.mainloop()