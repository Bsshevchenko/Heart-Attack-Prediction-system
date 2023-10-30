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


