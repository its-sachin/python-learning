import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
from tkinter import messagebox as m_box

win = tk.Tk()
win.title('GUI')

# Create labels

# ttk.Label(win, text= 'Enter your name: ').pack()    ------------> Displays at the centre

text_editor = tk.Text(win)
text_editor.config(wrap = 'word', relief = tk.FLAT)
text_editor.pack(fill = tk.BOTH, expand = True)

name_label = ttk.Label(win, text= 'Enter your name: ')
name_label.grid(row= 0, column= 0, sticky = tk.W, padx = 40, pady = 0) 

email_label = ttk.Label(win, text= 'Enter your age: ')
email_label.grid(row= 1, column= 0, sticky = tk.W)

age_label = ttk.Label(win, text= 'Enter your email: ')
age_label.grid(row= 2, column= 0, sticky = tk.W)

gender_label = ttk.Label(win, text= 'Select your gender: ')
gender_label.grid(row= 3, column= 0, sticky = tk.W)


# Create entry boxes

name_vr = tk.StringVar()
name_box = ttk.Entry(win, width = 20, textvariable = name_vr)
name_box.grid(row = 0, column = 1)
name_box.focus()

age_vr = tk.StringVar()
age_box = ttk.Entry(win, width = 20, textvariable = age_vr)
age_box.grid(row = 1, column = 1)

email_vr = tk.StringVar()
email_box = ttk.Entry(win, width = 20, textvariable = email_vr)
email_box.grid(row = 2, column = 1)



# Create Como box

gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=16, textvariable = gender_var, state = 'readonly')
gender_combobox['values'] = ('Male','Female','Other')
gender_combobox.grid(row=3,column=1)
gender_combobox.current(0)

# Radio Button

usertype =tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text ='Student', value = 'Student', variable = usertype)
radiobtn1.grid(row = 4, column = 0)

radiobtn2 = ttk.Radiobutton(win, text ='Teacher', value = 'Teacher', variable = usertype)
radiobtn2.grid(row = 4, column = 1)

# Check Button

checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text = 'Check if you want to subscribe', variable = checkbtn_var )
checkbtn.grid(row = 5, columnspan = 3)
# /Create Button

# def action1():
#     username = name_vr.get()
#     userage = age_vr.get()
#     useremail = email_vr.get()
#     print(f'{username} is {userage} years old , and has emailid = {useremail}')

#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     if checkbtn_var.get() == 0:
#         subscribed = 'NO'
#     else: subscribed = 'Yes'

#     print(user_gender, user_type, subscribed)

#     with open('file.txt','a') as f:


#     name_box.delete(0,tk.END)
#     age_box.delete(0,tk.END)
#     email_box.delete(0,tk.END)
#     name_label.configure(foreground = 'Blue')

#     submit_button.configure(foreground = 'Blue')

# Write in csv

# def action2():
#     username = name_vr.get()
#     userage = age_vr.get()
#     useremail = email_vr.get()
#     print(f'{username} is {userage} years old , and has emailid = {useremail}')

#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     if checkbtn_var.get() == 0:
#         subscribed = 'NO'
#     else: subscribed = 'Yes'

#     with open('file.csv', 'a', newline= '') as f:
#         dict_writer = DictWriter(f,fieldnames = {'User Name','User Age', 'User Email','User Gender', 'User Type', 'Subscribed'} )
#         if os.start('file.csv').st_size == 0:
#             dict_writer.writeheader()
#         dict_writer.writerow({
#             'User Name' : username,
#             'User Age' : userage,
#             'User Email' : useremail,
#             'User Gender' : user_gender,
#             'User Type' : user_type,
#             'subscribed' : subscribed
#         })

#     name_box.delete(0,tk.END)
#     age_box.delete(0,tk.END)
#     email_box.delete(0,tk.END)
#     name_label.configure(foreground = 'Blue')

def action3():
    name = name_vr.get()
    age = age_vr.get()
    email = email_vr.get()
    gender = gender_var.get()
    utype = usertype.get()

    if name == "" or age == "" or email == "":
        m_box.showerror('Error', 'Please fill all the required entries.')
    else:
        try:
            age = int(age)
        except ValueError:
            m_box.showerror('Title', 'Only integers allowed in age.')
        else:
            print(f'{name} : {age} : {email} : {gender}')



submit_button = ttk.Button(win, text = 'Submit', command = action3)
submit_button.grid(row=6,column=0)

win.mainloop()

def sort():
    try:
        x_read = text_editor1a.get(1.0 , tk.END)
        l1 = x_read.splitlines()

        l = [float(i) for i in l1]
        l.sort()
        print(l)
        for i in l:
            text_editor2a.delete(1.0,tk.END)
            text_editor2a.insert(tk.END,f'{i} \n')
    except:
        mbox = messagebox.showerror('Warning', 'Input not valid')