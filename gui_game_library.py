#!/usr/bin/python3
# Austin McCowan
# 2/10/2020

'''gui program for/based on game_library'''

import pickle
import data_reboot as dr
import tkinter as tk
from tkinter import scrolledtext

# Constants
TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)

# Classes
class Library(object):
    def __init__(self):
        
        # Try and open the pickle file and grab contents
        try: 
            datafile = open("game_lib.pickle", "rb")
            self.games = pickle.load(datafile)
            
        # If unable to grab content, run the function inside of data_reboot.py. Then try loading content again.    
        except:            
            dr.fix_it()
            print("Data failed to load; Grabbing original content")
            datafile = open("game_lib.pickle", "rb")
            self.games = pickle.load(datafile)
        
        # Close datafile    
        datafile.close()
        
class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(text= "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, sticky = "news")
        
        
# Functions/global functions


## Main
if __name__ == "__main__":
    content = Library()
    root = tk.Tk()
    root.title("Game Library")
    root.geometry("500x500")
    main_menu = MainMenu()
    main_menu.grid(row = 0, column = 0)
    
    root.mainloop()