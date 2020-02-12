#!/usr/bin/python3
# Austin McCowan
# 2/10/2020

'''gui program for/based on game_library'''

import pickle
import data_reboot as dr
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

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
        
    # updates the information in game_lib.pickle with the current information in the program (games)
    def save(self):
        try:
            datafile = open("game_lib.pickle", "wb")
            pickle.dump(self.games, datafile)
            datafile.close()
            
        except:
            
            raise Exception("Data failed to save")
        
class MainMenu(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self, text= "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan=3, sticky = "news")
        
        self.btn_add = tk.Button(self, text = "Add", font = BUTTON_FONT)
        self.btn_add.grid(row = 1, column = 1)
        
        self.btn_edit = tk.Button(self, text = "Edit", font = BUTTON_FONT)
        self.btn_edit.grid(row = 2, column = 1)
        
        self.btn_search = tk.Button(self, text = "Search", font = BUTTON_FONT)
        self.btn_search.grid(row = 3, column = 1)
        
        self.btn_remove = tk.Button(self, text = "Remove", font = BUTTON_FONT)
        self.btn_remove.grid(row = 4, column = 1)
        
        self.btn_save = tk.Button(self, text = "Save", font = BUTTON_FONT)
        self.btn_save.grid(row = 5, column = 1)        
        
class SearchFilters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        self.lbl_print_filers = tk.Label(self, text="Print Filters")
        self.lbl_print_filers.grid(row=0, column=0, columnspan=3)
        
        self.chk_genre = tk.Checkbutton(self, text="Genre")
        self.chk_genre.grid(row=1, column=0)
            
        self.chk_title = tk.Checkbutton(self, text="Title")
        self.chk_title.grid(row=2, column=0)
        
        self.chk_developer = tk.Checkbutton(self, text="Developer")
        self.chk_developer.grid(row=3, column=0)
        
        self.chk_publisher = tk.Checkbutton(self, text="Publisher")
        self.chk_publisher.grid(row=4, column=0) 
        
        self.chk_system = tk.Checkbutton(self, text="System")
        self.chk_system.grid(row=1, column=1) 
        
        self.chk_release = tk.Checkbutton(self, text= "Release Date")
        self.chk_release.grid(row=2, column=1) 
        
        self.chk_rating = tk.Checkbutton(self, text="Rating")
        self.chk_rating.grid(row=3, column=1) 
        
        self.chk_mode = tk.Checkbutton(self, text="Game Mode")
        self.chk_mode.grid(row=4, column=1) 
        
        self.chk_price = tk.Checkbutton(self, text="Price")
        self.chk_price.grid(row=1, column=2) 
        
        self.chk_beat = tk.Checkbutton(self, text="Beat it?")
        self.chk_beat.grid(row=2, column=2) 
        
        self.chk_purchase = tk.Checkbutton(self, text="Purchase Date")
        self.chk_purchase.grid(row=3, column=2)     
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
               
class Search(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self, text="Search")
        self.lbl_title.grid(row=0, column=2, columnspan=2)
        
        self.lbl_search_by = tk.Label(self, text="Search By:")
        self.lbl_search_by.grid(row=1, column=0, columnspan=3)
        
        self.lbl_search_for = tk.Label(self, text="Search For:")
        self.lbl_search_for.grid(row=3, column=0, columnspan=3)
        
        self.drp_search_by = tk.Entry(self)
        self.drp_search_by.grid(row=2, column=0, columnspan=3)
        
        self.ent_search_for = tk.Entry(self)
        self.ent_search_for.grid(row=4, column=0, columnspan=3)
        
        self.search_filters = SearchFilters(self)
        self.search_filters.grid(row=1, column=3, rowspan=4, columnspan=3)
        
        self.scrolled_text = ScrolledText(self, height=8, width=40)
        self.scrolled_text.grid(row=5, column=0, columnspan=6)
            
        self.btn_back = tk.Button(self, font = BUTTON_FONT, text="Back")
        self.btn_back.grid(row=6, column=0, columnspan=2)
        
        self.btn_clear = tk.Button(self, font = BUTTON_FONT, text="Clear")
        self.btn_clear.grid(row=6, column=2, columnspan=2)
        
        self.btn_clear = tk.Button(self, font = BUTTON_FONT, text="Submit")
        self.btn_clear.grid(row=6, column=4, columnspan=2)        
        
class Edit(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self, text="Which game would you like to edit?")
        self.lbl_title.grid(row=0, column=0, columnspan=2)
        
        self.drp_titles = tk.Entry(self)
        self.drp_titles.grid(row=1, column=0, columnspan=2)
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT)
        self.btn_cancel.grid(row=2, column=0)
        
        self.btn_okay = tk.Button(self, text="OK", font=BUTTON_FONT)
        self.btn_okay.grid(row=2, column=1)

class Remove(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self, text="Which game would you like to remove?")
        self.lbl_title.grid(row=0, column=0, columnspan=2)
        
        self.drp_titles = tk.Entry(self)
        self.drp_titles.grid(row=1, column=0, columnspan=2)
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT)
        self.btn_cancel.grid(row=2, column=0)
        
        self.btn_remove = tk.Button(self, text="Remove", font=BUTTON_FONT)
        self.btn_remove.grid(row=2, column=1)

class Save_Message(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_saved = tk.Label(self, text="File saved", font=TITLE_FONT)
        self.btn_okay = tk.Button(self, text="OK", font=BUTTON_FONT)
    
class Editor(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        
        
# Functions/global functions


## Main
if __name__ == "__main__":
    content = Library()
    root = tk.Tk()
    root.title("Game Library")
    root.geometry("500x500")
    main_menu = MainMenu()
    main_menu.grid(row=0, column=0, sticky ='news')
    
    search_menu = Search()
    search_menu.grid(row=0, column=0, sticky='news')
    
    edit_menu = Edit()
    edit_menu.grid(row=0, column=0, sticky='news')
    
    remove_menu = Remove()
    remove_menu.grid(row=0, column=0, sticky='news')
    
    root.grid_columnconfigure(0, weight=1)
    search_menu.tkraise()
    root.mainloop()