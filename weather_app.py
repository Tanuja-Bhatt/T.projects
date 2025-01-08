from tkinter import *
from tkinter import ttk
import requests

def get_data():
    state = state_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+state+"&appid=4e63f574c12cc0a85699c92c491b737d").json()
    w_label1.config(text = data["weather"][0]["main"])
    wb_label1.config(text = data["weather"][0]["description"])
    wc_label1.config(text = str(int(data["main"]["temp"]-273.15)))
    wd_label1.config(text = data["main"]["pressure"])


win = Tk()
win.title("T Projects")
win.config(bg = "brown")
win.geometry("500x570")

name_label = Label(win,text = "WEATHER APP",font = ("Baskerville Old Face",40,"bold"))
name_label.place(x = 25, y = 50, height = 50, width = 450)

state_name = StringVar()
list_states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text = "WEATHER APP",values = list_states,font = ("Baskerville Old Face",25,"bold"),textvariable = state_name)
com.place(x = 25, y = 120, height = 50, width = 450)

w_label = Label(win,text = "Weather climate",font = ("Arial",10,"bold"))
w_label.place(x = 25, y = 260, height = 50, width = 140)

w_label1 = Label(win,text = "",font = ("Arial",10,"bold"))
w_label1.place(x = 250, y = 260, height = 50, width = 210)

wb_label = Label(win,text = "Weather Description",font = ("Arial",10,"bold"))
wb_label.place(x = 25, y = 330, height = 50, width = 140)

wb_label1 = Label(win,text = "",font = ("Arial",10,"bold"))
wb_label1.place(x = 250, y = 330, height = 50, width = 210)

wc_label = Label(win,text = "Temperature",font = ("Arial",10,"bold"))
wc_label.place(x = 25, y = 400, height = 50, width = 140)

wc_label1 = Label(win,text = "",font = ("Arial",10,"bold"))
wc_label1.place(x = 250, y = 400, height = 50, width = 210)

wd_label = Label(win,text = "Pressure",font = ("Arial",10,"bold"))
wd_label.place(x = 25, y = 470, height = 50, width = 140)

wd_label1 = Label(win,text = "",font = ("Arial",10,"bold"))
wd_label1.place(x = 250, y = 470, height = 50, width = 210)

display = Button(win,text = "Submit", font = ("Baskerville Old Face",25,"bold"),command = get_data)
display.place(x = 200, y = 190, height = 50, width = 100)

win.mainloop()
