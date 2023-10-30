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

#Header 

logo = PhotoImage(file='Heart Attack Prediction System\Images\header.png') #
myimage = Label(image=logo, bg=background) #Создается виджет в качестве своего содержимого использует изображение logo, bd - фон
myimage.place(x=0, y=0) #координаты размещения виджета

#frame 3
Heading_entry = Frame(root, width=800, height=190, bg='#df2d4b') #Виджет контейнер, для группировки и организации других виджетов
Heading_entry.place(x=600, y=20)

Label(Heading_entry, text='Registration No', font='arial 13', bg='#df2d4b', fg=framefg).place(x=30, y=0)
Label(Heading_entry, text='Date', font='arial 13', bg='#df2d4b', fg=framefg).place(x=430, y=0)
Label(Heading_entry, text='Patient Name', font='arial 13', bg='#df2d4b', fg=framefg).place(x=30, y=90)
Label(Heading_entry, text='Birth Year', font='arial 13', bg='#df2d4b', fg=framefg).place(x=430, y=90)

Entry_image = PhotoImage(file = 'Heart Attack Prediction System\Images\Rounded Rectangle 1.png')
Entry_image2 = PhotoImage(file = 'Heart Attack Prediction System\Images\Rounded Rectangle 2.png')

Label(Heading_entry, image=Entry_image, bg='#df2d4b').place(x=20, y=30)
Label(Heading_entry, image=Entry_image, bg='#df2d4b').place(x=430, y=30)

Label(Heading_entry, image=Entry_image2, bg='#df2d4b').place(x=20, y=120)
Label(Heading_entry, image=Entry_image2, bg='#df2d4b').place(x=430, y=120)

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





root.mainloop() #Запуск приложения
