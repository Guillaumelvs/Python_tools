"""
Created on Mon Feb 28 11:45:52 2022

@author: Guillaumelvs

"""

import tkinter as tk
import re


my_window = tk.Tk()
my_window.title("Remise au bon format du chemin")
my_window['bg'] = "#191E1A"

dim_canvas = tk.Canvas(my_window, width=900, height=60, bg='black') 
dim_canvas.grid()




dim_canvas.create_text(5, 17, anchor='w', text="Chemin :", fill="white")


path_to_change = tk.StringVar()
path_to_change.set("...\path\ to .../path/")
height_entry = tk.Entry(dim_canvas, textvariable=path_to_change, width=140, bg="#B2C3B9")
height_entry.grid()
height_entry.place(relx=1, rely=0.2, anchor='e')

def good_path():
    goodPath = path_to_change.get()
    goodPath = re.sub(re.compile(r'\\'), '/', goodPath)
    path_to_change.set(goodPath)

B = tk.Button(my_window,text ="Afficher le chemin au bon format", command=good_path)


B.grid()
B.place(relx=0.5, rely=0.7, anchor='e')

my_window.mainloop()