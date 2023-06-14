from bs4 import BeautifulSoup
import requests 
import pandas as pd
import tkinter as tk
from tkinter import ttk

url = 'https://www.premierleague.com/tables'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

equipo = soup.find_all('span', class_='long')
puntos = soup.find_all('td', class_='points')

equipos = list()
puntosEquipos = list()

for i in equipo:
    equipos.append(i)

for i in puntos:
    puntosEquipos.append(i)

datos_equipos = []
for equipo, punto in zip(equipos, puntosEquipos):
    nombre_equipo = equipo.text.strip()
    punto_equipo = punto.text.strip()
    datos_equipos.append({'Equipo': nombre_equipo, 'Puntos': punto_equipo})

root = tk.Tk()
root.title("Premier League: Temporada Actual")

table = ttk.Treeview(root)
table["columns"] = ("Equipo", "Puntos")
table.column("#0", width=0, stretch=tk.NO)
table.column("Equipo", anchor=tk.CENTER, width=500)
table.column("Puntos", anchor=tk.CENTER, width=200)

table.heading("#0", text="")
table.heading("Equipo", text="Equipo")
table.heading("Puntos", text="Puntos")

for dato in datos_equipos:
    table.insert("", tk.END, text="", values=(dato['Equipo'], dato['Puntos']))

table.pack()

root.mainloop()
