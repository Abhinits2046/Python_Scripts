# -*- coding: utf-8 -*-
"""
Created on Thu May  28 13:43:03 2018

@author: Abhinits2046
"""
from tkinter import *
import math

class calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.operate = ""
        self.result = False
    ##Number Entry
    def numberEntry(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        if self.input_value == ".":
            self.current = firstnum+secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result= False
        self.current = float(self.current)
        if self.check_sum == True:
            self.validfunction()
        else:
            self.total = float(txtDisplay.get())

    def validfunction(self):
        if self.operate == "add":
            self.total += self.current
        if self.operate == "sub":
            self.operate -= self.current
        if self.operate == "*":
            self.operate *= self.current
        if self.operate == "/":
            self.operate /= self.current
            self.input_value = True
            self.check_sum = False
            self.display(self.total)

    def operation(self, operation):
        self.current = float(self.current)
        if self.check_sum:
            self.validfunction()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.operate = operate
        self.result = False

    def clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_clear(self):
        self.clear_Entry()
        self.total = 0

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def sign(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def square(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    # def add(self):
    #     self.result= False
    #     self.current = math.add(float(tex))


added_value = calc()
root = Tk()
root.title("Basic Calculator")
root.resizable(width = False , height = False)
calc = Frame(root)
calc.grid()

txtDisplay = Entry(calc, font=('arial', 20 , 'bold'), bg = "black", fg='white',bd = 20, width = 18 , justify = RIGHT)
txtDisplay.grid(row = 0, column =0, columnspan = 4, pady =1)
txtDisplay.insert(0, "0")

###################################  Buttons Code  #####################
########### First Column1 Buttons (CE,7,4,1,0) #####################
buttonCE = Button(calc, pady=1, bd=2, fg= "white", font=('arial' ,20, 'bold'),width= 4, height = 1,
                 text = "CE", bg="dimgray", command = added_value.all_clear).grid(row=1,column= 0)

button7 = Button(calc, pady=1, bd=2, fg= "white", font=('arial' ,20, 'bold'),width= 4, height = 1,
                 text = "7", bg="black").grid(row=2,column= 0)

button4 = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "4", bg="black").grid(row=3, column= 0)

button1 = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "1", bg="black").grid(row=4, column= 0)

button0 = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "0", bg="black").grid(row=5, column= 0)

########### First Column2 Buttons (C,8,5,2,.) #####################

buttonC = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "C", bg="dimgray", command = added_value.clear_Entry).grid(row=1, column= 1)

button8 = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "8", bg="black").grid(row=2, column= 1)

button5 = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "5", bg="black").grid(row=3, column= 1)

button2 = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "2", bg="black").grid(row=4, column= 1)

buttonDot = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= ".", bg="black").grid(row=5, column= 1)

########### First Column3 Buttons (√,9,6,3,±) #####################
buttonSqrt = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "√", bg="dimgray", command = added_value.square).grid(row=1, column= 2)

button9 = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "9", bg="black").grid(row=2, column= 2)

button6 = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "6", bg="black").grid(row=3, column= 2)

button3 = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "3", bg="black").grid(row=4, column= 2)

buttonSignchange = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "±", bg="black").grid(row=5, column= 2)


########### First Column4 Buttons (+,-,*,/,=) #####################
buttonAdd = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "+", bg="dimgray").grid(row=1, column= 3)

buttonSub = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "-", bg="dimgray").grid(row=2, column= 3)

buttonMulti = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "*", bg="dimgray").grid(row=3, column= 3)

buttonDevid = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "/", bg="dimgray").grid(row=4, column= 3)

buttonEqual = Button(calc,pady=1, bd=2, fg="white" ,font=('arial', 20, 'bold'), width = 4, height = 1,
                 text= "=", bg="dimgray").grid(row=5, column= 3)
root.mainloop()




