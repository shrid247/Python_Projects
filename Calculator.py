#!/usr/bin/env python
# coding: utf-8

# In[45]:


from tkinter import *


# In[62]:


def on_click(arg):
    entry.insert(END,arg)
def result():
    result = entry.get()
    entry.delete(0,END)
    ans = eval(result)
    entry.insert(0,ans)
    
def clear():
    entry.delete(0,END)
    


# In[71]:


window = Tk()
window.title('Calculator')
window.geometry('280x250')

entry = Entry(window, width =30,borderwidth = 5)
entry.place(x=50,y=0)

btn1 = Button(window, text = '1',width =5,activebackground = 'grey',command = lambda:on_click(1))
btn1.place(x=0,y=150)
btn2= Button(window, text = '2',width=5,activebackground = 'grey',command = lambda:on_click(2))
btn2.place(x=50,y=150)
btn3= Button(window, text = '3',width=5,activebackground = 'grey',command = lambda:on_click(3))
btn3.place(x=100,y=150)
btn_plus=Button(window,text = '+',width = 5,activebackground = 'grey',command = lambda:on_click('+'))
btn_plus.place(x=150,y=150)
btn4= Button(window, text = '4',width=5,activebackground = 'grey',command = lambda:on_click(4))
btn4.place(x=0,y=120)
btn5=Button(window, text = '5',width = 5,activebackground = 'grey',command = lambda:on_click(5))
btn5.place(x=50,y=120)
btn6=Button(window, text  ='6',width = 5,activebackground = 'grey',command = lambda:on_click(6))
btn6.place(x=100,y=120)
btn_minus=Button(window, text = '-',width = 5,activebackground  ='grey',command = lambda:on_click('-'))
btn_minus.place(x=150,y=120)
btn7=Button(window, text  ='7',width = 5,activebackground = 'grey',command = lambda:on_click(7))
btn7.place(x=0,y=90)
btn8=Button(window, text  ='8',width = 5,activebackground = 'grey',command = lambda:on_click(8))
btn8.place(x=50,y=90)
btn9=Button(window, text  ='9',width = 5,activebackground = 'grey',command = lambda:on_click(9))
btn9.place(x=100,y=90)
btn_multiply=Button(window, text = '*',width = 5,activebackground = 'grey',command = lambda:on_click('*'))
btn_multiply.place(x=150,y=90)
btn0=Button(window, text  ='0',width = 5,activebackground = 'grey',command = lambda:on_click(0))
btn0.place(x=0,y=180)
btn_point=Button(window, text  ='.',width = 5,activebackground = 'grey',command = lambda:on_click('.'))
btn_point.place(x=50,y=180)
btn_divi=Button(window, text = '/',width  = 5,activebackground = 'grey',command = lambda:on_click('/'))
btn_divi.place(x=100,y=180)
btn_equal=Button(window, text = '=',width = 5, activebackground = 'grey',command = result)
btn_equal.place(x=150,y=180)
btn_clear=Button(window, text = 'AC',width = 5, activebackground = 'grey',command = clear)
btn_clear.place(x = 0,y= 60)





window.mainloop()


# In[ ]:




