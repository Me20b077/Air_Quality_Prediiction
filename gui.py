import tkinter as tk
from tkinter import filedialog
from tkinter import *
import numpy
import numpy as np

import tensorflow
# from tensorflow.keras.models import load_model
import joblib


aqi_model =   joblib.load('my_random_forest.joblib')  

top = tk.Tk()
top.geometry('800x600')
top.title('AQI Calculator')
top.configure(background='#CDCDCD')

Label(top,background='#CDCDCD',font=('arial',15,'bold'),text='PM2.5').pack(side='top')
f1 = IntVar()
e1 = Entry(top,textvariable=f1)
e1.pack(side='top')

Label(top,background='#CDCDCD',font=('arial',15,'bold'),text='NO').pack(side='top')
f2 = IntVar()
e2 = Entry(top,textvariable=f2)
e2.pack(side='top')

Label(top,background='#CDCDCD',font=('arial',15,'bold'),text='NO2').pack(side='top')
f3 = IntVar()
e3 = Entry(top,textvariable=f3)
e3.pack(side='top')


Label(top,background='#CDCDCD',font=('arial',15,'bold'),text='NH3').pack(side='top')
f4 = IntVar()
e4 = Entry(top,textvariable=f4)
e4.pack(side='top')


Label(top,background='#CDCDCD',font=('arial',15,'bold'),text='CO').pack(side='top')
f5 = IntVar()
e5 = Entry(top,textvariable=f5)

e5.pack(side='top')


Label(top,background='#CDCDCD',font=('arial',15,'bold'),text='SO2').pack(side='top')
f6 = IntVar()
e6 = Entry(top,textvariable=f6)
e6.pack(side='top')



Label(top,background='#CDCDCD',font=('arial',15,'bold'),text='O3').pack(side='top')
f7 = IntVar()
e7 = Entry(top,textvariable=f7)
e7.pack(side='top')


Label(top,background='#CDCDCD',font=('arial',15,'bold'),text='Benzene').pack(side='top')
f8 = IntVar()
e8 = Entry(top,textvariable=f8)
e8.pack(side='top')

label1 = Label(top,text = '',font=('arial',15,'bold'))
label1.place(relx=0.5,rely=0.7)

label2 = Label(top,text = '',font=('arial',15,'bold'))
label2.place(relx=0.5,rely=0.8)

means = [65.65,17.68,28.12,21.91,2.29,14.49,34,2.93]
stds = [62.4,22.28,24,22.46,6.99,17.7,21.19,14.82]

def detect_aqi():
    global aqi
    d1 = f1.get()
    d2 = f2.get()
    d3 = f3.get()
    d4 = f4.get()
    d5 = f5.get()
    d6 = f6.get()
    d7 = f7.get()
    d8 = f8.get()
    x = [[d1,d2,d3,d4,d5,d6,d7,d8]]

    for i in range(8):
        x[0][i] = (x[0][i]-means[i])/stds[i]
    x=np.array(x)
    aqi = round(aqi_model.predict(x)[0],2)
    label1.config(text = 'AQI value is '+str(aqi))
    aqi_level = 'Normal'
    if aqi<13:
        aqi_level = 'Very Good'
    elif aqi<51:
        aqi_level = 'Good'
    elif aqi<101:
        aqi_level = 'Satisfactory'
    elif aqi<201:
        aqi_level = 'Moderate'
    elif aqi<301:
        aqi_level = 'Poor'
    elif aqi<401:
        aqi_level = 'Very Poor'
    else:
        aqi_level = 'Severe'
    
    label2.config(text = 'Condition : '+ aqi_level)
    
    print(aqi)
    print(aqi_level)
    return aqi

detect = Button(top,text = 'Calculate AQI',command=detect_aqi,padx=10,pady=5)
detect.place(relx=0.75,rely=0.25)
top.mainloop()