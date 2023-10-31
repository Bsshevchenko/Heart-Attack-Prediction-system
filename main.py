from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import ttk
import os
import matplotlib

matplotlib.use('TkAgg') #Установка бэкенда TkAgg - это бэкенд, который использует Tkinter, интерфейс Python для графической библиотеки Tk, в качестве основного графического движка. 

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# FigureCanvasTkAgg - класс предоставляет функциональность для отображения графиков и фигур matplotlib в окне Tkinter. 
# После импортирования этой строки кода вы можете использовать класс FigureCanvasTkAgg для создания экземпляра холста, который может быть встроен в окно Tkinter и показан в приложении пользовательского интерфейса на основе Tkinter.

from matplotlib.figure import Figure

# класс Figure - создает экземпляр объекта Figure, который представляет собой пустую фигуру. 
# Затем вы можете добавлять графики, оси, надписи и другие элементы на эту фигуру, чтобы создать и настроить ваш график.

import numpy as np
import matplotlib.pyplot as plt



#####      Создание основы приложения    ######

background = '#f0ddd5' #фон
framebg = '#62a7ff' #элементы,блоки
framefg = '#fefbfb' #текст

root = Tk() #Создание экземпляра класса Tk, который представляет главное окно приложения.
root.title('Heart Attack Prediction System') #Установка заголовка окна на "Heart Attack Prediction System".
root.geometry("1450x730+60+80") # Установка размеров окна в пикселях и его положения на экране. Значение "1450x730" определяет ширину и высоту окна, а "60+80" указывает смещение по горизонтали и вертикали относительно левого верхнего угла экрана.
root.resizable(False, False) # Запрет изменения размеров окна пользователем. Оба аргумента установлены на False, что означает, что пользователь не сможет изменить ширину или высоту окна.
root.config(bg=background) #Установка фонового цвета окна на значение переменной background. Это позволяет настроить внешний вид окна с помощью заданной цветовой палитры.

#################################

#Icon 1
image_icon = PhotoImage(file="Heart Attack Prediction System\Images\icon.png")
root.iconphoto(False, image_icon) #Установка иконки приложения

################################## Header 

logo = PhotoImage(file='Heart Attack Prediction System\Images\header.png') #
myimage = Label(image=logo, bg=background) #Создается виджет в качестве своего содержимого использует изображение logo, bd - фон
myimage.place(x=0, y=0) #координаты размещения виджета

#Frame 
Heading_entry = Frame(root, width=800, height=190, bg='#df2d4b') #Виджет контейнер, для группировки и организации других виджетов
Heading_entry.place(x=600, y=20)

# Label widget for text
Label(Heading_entry, text='Registration No', font='arial 13', bg='#df2d4b', fg=framefg).place(x=30, y=0)
Label(Heading_entry, text='Date', font='arial 13', bg='#df2d4b', fg=framefg).place(x=430, y=0)
Label(Heading_entry, text='Patient Name', font='arial 13', bg='#df2d4b', fg=framefg).place(x=30, y=90)
Label(Heading_entry, text='Birth Year', font='arial 13', bg='#df2d4b', fg=framefg).place(x=430, y=90)

#Label widget for photo
Entry_image = PhotoImage(file = 'Heart Attack Prediction System\Images\Rounded Rectangle 1.png')
Entry_image2 = PhotoImage(file = 'Heart Attack Prediction System\Images\Rounded Rectangle 2.png')

Label(Heading_entry, image=Entry_image, bg='#df2d4b').place(x=20, y=30)
Label(Heading_entry, image=Entry_image, bg='#df2d4b').place(x=430, y=30)

Label(Heading_entry, image=Entry_image2, bg='#df2d4b').place(x=20, y=120)
Label(Heading_entry, image=Entry_image2, bg='#df2d4b').place(x=430, y=120)

#Entry widget for input
Registration = IntVar() 
reg_entry = Entry(Heading_entry, textvariable=Registration, width=30, font='arial 15', bg='#0e5363', fg='white', bd=0) #Виджет "Entry" используется для получения текстового ввода от пользователя. В данном коде заданы следующие параметры для виджета "reg_entry":
reg_entry.place(x=30, y=45)

Date = StringVar()
today = date.today()
d1 = today.strftime('%d/%m/%Y')
date_entry = Entry(Heading_entry, textvariable=Date, width=15, font='arial 15', bg='#0e5363', fg='white', bd=0)
date_entry.place(x=500, y=45)
Date.set(d1)

Name = StringVar() 
name_entry = Entry(Heading_entry, textvariable=Name, width=20, font='arial 20', bg='#ededed', fg='#222222', bd=0) 
name_entry.place(x=30, y=130)

DOB = IntVar()
dob_entry = Entry(Heading_entry, textvariable=DOB, width=20, font='arial 20', bg='#ededed', fg='#222222', bd=0) 
dob_entry.place(x=450, y=130)

################################## Body

Detail_entry = Frame(root, width=490, height=260, bg='#dbe0e3')
Detail_entry.place(x=30, y=450)

#Radio button
Label(Detail_entry, text='sex:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=10)
Label(Detail_entry, text='fbs:', font='arial 13', bg=framebg, fg=framefg).place(x=180, y=10)
Label(Detail_entry, text='exang:', font='arial 13', bg=framebg, fg=framefg).place(x=335, y=10)

def selection1():
    if gen.get() == 1:
        Gender = 1
        return(Gender)
        print(Gender)
    elif gen.get() == 0:
        Gender = 0
        return(Gender)
        print(Gender)
    else:
        print(Gender)
        
def selection2():
    if fbs.get() == 1:
        Fbs = 1
        return(Fbs)
        print(Fbs)
    elif fbs.get() == 0:
        Fbs = 0
        return(Fbs)
        print(Fbs)
    else:
        print(Fbs)
        
def selection3():
    if exang.get() == 1:
        Exang = 1
        return(Exang)
        print(Exang)
    elif exang.get() == 0:
        Exang = 0
        return(Exang)
        print(Exang)
    else:
        print(Exang)
    

gen = IntVar()
R1 = Radiobutton(Detail_entry, text='male', variable=gen, value=1, command=selection1)
R2 = Radiobutton(Detail_entry, text='female', variable=gen, value=2, command=selection1)
R1.place(x=43, y=10)
R2.place(x=93, y=10)

fbs = IntVar()
R3 = Radiobutton(Detail_entry, text='True', variable=fbs, value=1, command=selection2)
R4 = Radiobutton(Detail_entry, text='False', variable=fbs, value=2, command=selection2)
R3.place(x=213, y=10)
R4.place(x=263, y=10)

exang = IntVar()
R5 = Radiobutton(Detail_entry, text='Yes', variable=exang, value=1, command=selection3)
R6 = Radiobutton(Detail_entry, text='No', variable=exang, value=2, command=selection3)
R5.place(x=387, y=10)
R6.place(x=430, y=10)

#Combobox - выпадающий список

Label(Detail_entry, text='cp:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=50)
Label(Detail_entry, text='restecg:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=90)
Label(Detail_entry, text='slope:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=130)
Label(Detail_entry, text='ca:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=170)
Label(Detail_entry, text='thal:', font='arial 13', bg=framebg, fg=framefg).place(x=10, y=210)


def selection4():
    input = cp_combobox.get()
    if input == '0 = typical angina':
        return(0)
    elif input == '1 = atypical angina':
        return(1)
    elif input == '2 = non-angina pain':
        return(2)
    elif input == '3 = asymptomatic':
        return(3)
    else:
        print(Exang)

def selection5():
    input = slope_combobox.get()
    if input == '0 = upsloping':
        return(0)
    elif input == '1 = flat':
        return(1)
    elif input == '2 = downsloping':
        return(2)
    else:
        print(Exang)
      

cp_combobox = Combobox(Detail_entry, values=['0 = typical angina', '1 = atypical angina', '2 = non-angina pain', '3 = asymptomatic'], font='arial 12', state = 'r', width=14).place(x=53, y=50)
restecg_combobox = Combobox(Detail_entry, values=['0', '1', '2'], font='arial 12', state = 'r', width=11).place(x=80, y=90)
slope_combobox = Combobox(Detail_entry, values=['0 = upsloping', '1 = flat', '2 = downsloping'], font='arial 12', state = 'r', width=12).place(x=70, y=130)
ca_combobox = Combobox(Detail_entry, values=['0', '1', '2', '3', '4'], font='arial 12', state = 'r', width=14).place(x=52, y=170)
thal_combobox = Combobox(Detail_entry, values=['0', '1', '2', '3'], font='arial 12', state = 'r', width=14).place(x=52, y=210)

####### Data Entry box

Label(Detail_entry, text='Smoking:', font='arial 13', width= 7, bg='#dbe0e3', fg='black').place(x=240, y=50)
Label(Detail_entry, text='trestbps:', font='arial 13', width= 7, bg=framebg, fg=framefg).place(x=240, y=90)
Label(Detail_entry, text='chol:', font='arial 13', width= 7, bg=framebg, fg=framefg).place(x=240, y=130)
Label(Detail_entry, text='thalach:', font='arial 13', width= 7, bg=framebg, fg=framefg).place(x=240, y=170)
Label(Detail_entry, text='oldpeak:', font='arial 13', width= 7, bg=framebg, fg=framefg).place(x=240, y=210)

trestbps = StringVar()
chol = StringVar()
thalach = StringVar()
oldpeak = StringVar()

trestbps_entry = Entry(Detail_entry, textvariable=trestbps, width=10, font='arial 15', bg='#ededed', fg='#222222', bd=0).place(x=320, y=90)
chol_entry = Entry(Detail_entry, textvariable=chol, width=10, font='arial 15', bg='#ededed', fg='#222222', bd=0).place(x=320, y=130)
thalach_entry = Entry(Detail_entry, textvariable=thalach, width=10, font='arial 15', bg='#ededed', fg='#222222', bd=0).place(x=320, y=170)
oldpeak_entry = Entry(Detail_entry, textvariable=oldpeak, width=10, font='arial 15', bg='#ededed', fg='#222222', bd=0).place(x=320, y=210)

################ smoking and non smoking button

button_mode=True
choice='smoking'

def changemode():
    global button_mode
    global choice
    
    if button_mode:
        choice = 'non_smoking'
        mode.config(image=non_smoking_icon, activebackground='#dbe0e3')
        button_mode = False
    else:
        choice = 'smoking'
        mode.config(image=smoking_icon, activebackground='#dbe0e3')
        button_mode = True
    
    print(choice)
              

smoking_icon = PhotoImage(file='Heart Attack Prediction System\Images\smoker.png')
non_smoking_icon = PhotoImage(file='Heart Attack Prediction System\Images\smoker-non.png')
mode = Button(root, image=smoking_icon, bg='#dbe0e3', bd=0, cursor='hand2', command=changemode, activebackground='#dbe0e3')
mode.place(x=350, y=495)

############# logOut button

logout_icon = PhotoImage(file='Heart Attack Prediction System\Images\logout.png')
logout_button = Button(root, image=logout_icon, bg='#df2d4b', cursor='hand2', bd=0, activebackground='#df2d4b')
logout_button.place(x=1390, y=60)











root.mainloop() #Запуск приложения
