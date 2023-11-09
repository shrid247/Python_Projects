#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
from tkinter.ttk import Notebook,Frame
from tkinter import filedialog,Menu


# In[24]:


def clicked():
    window.destroy()
def file_open():
    file = filedialog.askopenfile(filetypes = [("Text files","*.txt"),("all","*.*")])
    if file is not None:
        file_path=file.name
        try:
            with open(file_path,'r') as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print('The file was not found.')
        except Exception as e:
            print(f"An error occurred: {e}")
#def new_tab():
    #tab = Frame(tab_control)
    #tab_control.add(tab, text  ='New tab')
    #label = Label(tab1,text = 'New tab content')
    #label.pack()
    #tab_control.select(tab)
def new_window_():
    new_window =Tk()
    new_window.title('Notepad')
    new_window.geometry('400x400')

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        content = text.get(1.0, END)
        with open(file_path, 'w') as f:
            f.write(content)

def save_file_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        content = text.get(1.0, END)
        with open(file_path, 'w') as f:
            f.write(content)    
def undo():
    text.edit_undo()
def copy():
    text.clipboard_clear()
    text.clipboard_append(text.append(SEL_FIRST,SEL_LAST))
def paste():
    text.insert(INSERT,text.clipboard_get())
def cut():
    text.clipboard_clear()
    text.clipboard_append(text.append(SEL_FIRST,SEL_LAST))
    text.delete(SEL_FIRST,SEL_LAST)
def dele():
    text.delete(SEL_FIRST,SEL_LAST)


# In[26]:


window = Tk()
window.title('Notepad')
window.geometry('400x400')

tab_control = Notebook(window)
tab1 = Frame(tab_control)

tab_control.add(tab1, text='untitled')
label1 = Label(tab1, text='hi')
label1.place(x=0, y=0)

tab_control.pack(expand=1, fill='both')







menu = Menu(window)
item1 = Menu(menu,tearoff=0)
item1.add_command(label = 'New tab')
item1.add_command(label = 'New window',command = new_window_)
item1.add_command(label='Open', command = file_open)
item1.add_command(label = 'Save',command  = save_file)
item1.add_command(label = 'Save as',command = save_file_as)
item1.add_separator()
item1.add_command(label = 'Close tab')
item1.add_command(label = 'CLose window', command = clicked)
item1.add_command(label = 'Exit', command = clicked)
item2 = Menu(menu, tearoff=0)
item2.add_command(label='Undo',command = undo)
item2.add_command(label='Cut',command = cut)
item2.add_command(label = 'Copy', command = copy)
item2.add_command(label = 'Paste', command = paste)
item2.add_command(label = 'Delete', command = dele)
item2.add_separator()
item2.add_command(label = 'Find')
item2.add_command(label = 'Find next')
item2.add_command(label = 'Find previous')
item2.add_command(label = 'Replace')
item2.add_command(label = 'Go to')
item2.add_separator()
item2.add_command(label = 'Select all')
item2.add_command(label = 'Time/Date')

menu.add_cascade(label='File',menu = item1)
menu.add_cascade(label='Edit',menu = item2)
zoom_menu = Menu(menu, tearoff=0)
zoom_menu.add_command(label="Zoom In")
zoom_menu.add_command(label="Zoom Out")
item3 = Menu(menu,tearoff=0)
item3.add_cascade(label = 'Zoom', menu = zoom_menu)
item3.add_command(label='Status bar')
item3.add_command(label='Word wrap')
menu.add_cascade(label = 'View',menu = item3)




text = Text(window)
text.pack(fill = 'both',expand = True)

window.config(menu = menu)
window.mainloop()


# In[ ]:




