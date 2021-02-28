import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()
win.title('Label Frame')


label_frame = ttk.LabelFrame(win, text = 'Enter your details below: ')
label_frame.grid(row = 0, column = 0, padx = 40, pady = 40)

labels = ['Name: ','Age: ', 'Class: ', 'Countary: ','State: ','City: ']

entry_box = {
    'Name' : tk.StringVar(),
    'Age' : tk.StringVar(),
    'Class' : tk.StringVar(),
    'Countary' : tk.StringVar(),
    'State' : tk.StringVar(),
    'City' : tk.StringVar() 
}

for i in range(len(labels)):
    cur_label = 'label' + str(i)
    cur_label =  ttk.Label(label_frame, text= labels[i])
    cur_label.grid(row= i, column= 0, sticky = tk.W, padx = 4, pady = 0)

k = 0
for i in entry_box:
    cur_box = 'entry' + i
    cur_box = ttk.Entry(label_frame, width = 20, textvariable = entry_box[i])
    cur_box.grid(row = k, column = 1)
    cur_box.focus()
    k += 1

for child in label_frame.winfo_children():
    child.grid(padx = 4, pady = 4)

win.mainloop()