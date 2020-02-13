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
        self.btn_add.grid(row = 1, column = 1, sticky='news')
        
        self.btn_edit = tk.Button(self, text = "Edit", font = BUTTON_FONT)
        self.btn_edit.grid(row = 2, column = 1, sticky='news')
        
        self.btn_search = tk.Button(self, text = "Search", font = BUTTON_FONT)
        self.btn_search.grid(row = 3, column = 1, sticky='news')
        
        self.btn_remove = tk.Button(self, text = "Remove", font = BUTTON_FONT)
        self.btn_remove.grid(row = 4, column = 1, sticky='news')
        
        self.btn_save = tk.Button(self, text = "Save", font = BUTTON_FONT)
        self.btn_save.grid(row = 5, column = 1, sticky='news')        
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
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
        self.lbl_title.grid(row=0, column=0, columnspan=6)
        
        self.lbl_search_by = tk.Label(self, text="Search By:")
        self.lbl_search_by.grid(row=1, column=0, columnspan=3, sticky='news')
        
        self.lbl_search_for = tk.Label(self, text="Search For:")
        self.lbl_search_for.grid(row=3, column=0, columnspan=3, sticky='news')
        
        category_list = ["genre","title", "developer", "publisher", "system", "release date", "rating", "single/multi/either", "price", "beat it", "purchase date"]
        self.tkvar_search = tk.StringVar(self)
        self.tkvar_search.set(category_list[0])
        
        self.dbx_search_by = tk.OptionMenu(self, self.tkvar_search, *category_list)
        self.dbx_search_by.grid(row=2, column=0, columnspan=3, sticky='news')
        
        self.ent_search_for = tk.Entry(self)
        self.ent_search_for.grid(row=4, column=0, columnspan=3, sticky='news')
        
        self.frm_search_filters = SearchFilters(self)
        self.frm_search_filters.grid(row=1, column=3, rowspan=4, columnspan=3)
        
        self.scr_text = ScrolledText(self, height=8, width=40)
        self.scr_text.grid(row=5, column=0, columnspan=6)
            
        self.btn_back = tk.Button(self, font = BUTTON_FONT, text="Back")
        self.btn_back.grid(row=6, column=0, columnspan=2, sticky='news')
        
        self.btn_clear = tk.Button(self, font = BUTTON_FONT, text="Clear")
        self.btn_clear.grid(row=6, column=2, columnspan=2, sticky='news')
        
        self.btn_clear = tk.Button(self, font = BUTTON_FONT, text="Submit")
        self.btn_clear.grid(row=6, column=4, columnspan=2, sticky='news')
        
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        
class Edit(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self, text="Which game would you like to edit?")
        self.lbl_title.grid(row=0, column=0, columnspan=2)
        
        titles_to_edit = ["placeholder I", "placeholder II"]
        self.tkvar_titles_to_edit = tk.StringVar(self)
        self.tkvar_titles_to_edit.set(titles_to_edit[0])
        
        self.dbx_titles_to_edit = tk.OptionMenu(self, self.tkvar_titles_to_edit, *titles_to_edit)
        self.dbx_titles_to_edit.grid(row=1, column=0, columnspan=2, sticky='news')
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT)
        self.btn_cancel.grid(row=2, column=0)
        
        self.btn_okay = tk.Button(self, text="OK", font=BUTTON_FONT)
        self.btn_okay.grid(row=2, column=1)
        
        

class Remove(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_title = tk.Label(self, text="Which game would you like to remove?")
        self.lbl_title.grid(row=0, column=0, columnspan=2)
        
        titles = ["placeholder I", "placeholder II"]
        self.tkvar_remove = tk.StringVar(self)
        self.tkvar_remove.set(titles[0])
        
        self.dbx_titles_to_remove = tk.OptionMenu(self, self.tkvar_remove, *titles)
        self.dbx_titles_to_remove.grid(row=1, column=0, columnspan=2, sticky='news')
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT)
        self.btn_cancel.grid(row=2, column=0)
        
        self.btn_remove = tk.Button(self, text="Remove", font=BUTTON_FONT)
        self.btn_remove.grid(row=2, column=1)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

class SaveMessage(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.lbl_saved = tk.Label(self, text="File saved", font=TITLE_FONT)
        self.lbl_saved.grid(row=0,column=0, sticky='news')
        
        self.btn_okay = tk.Button(self, text="OK", font=BUTTON_FONT)
        self.btn_okay.grid(row=0, column=0)
    
class Editor(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        
        self.lbl_genre = tk.Label(self, text="Genre")
        self.lbl_genre.grid(row=0, column=0)
        
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row=0, column=1, columnspan=2, sticky='news')
        
        self.lbl_title = tk.Label(self, text="Title")
        self.lbl_title.grid(row=0, column=3)
        
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row=0, column=4, columnspan=2, sticky='news')
        
        self.lbl_developer = tk.Label(self, text="Developer")
        self.lbl_developer.grid(row=1, column=0)
        
        self.ent_developer = tk.Entry(self)
        self.ent_developer.grid(row=1, column=1, columnspan=2, sticky='news')
        
        self.lbl_publisher = tk.Label(self, text="Publisher")
        self.lbl_publisher.grid(row=1, column=3)
        
        self.ent_publisher = tk.Entry(self)
        self.ent_publisher.grid(row=1, column=4, columnspan=2, sticky='news')
        
        self.lbl_system = tk.Label(self, text="System")
        self.lbl_system.grid(row=2, column=0)
        
        self.ent_system = tk.Entry(self)
        self.ent_system.grid(row=2, column=1, columnspan=2, sticky='news')
        
        self.lbl_release = tk.Label(self, text="Release")
        self.lbl_release.grid(row=2, column=3)
        
        self.ent_release = tk.Entry(self)
        self.ent_release.grid(row=2, column=4, columnspan=2, sticky='news')
        
        self.lbl_rating = tk.Label(self, text="Rating")
        self.lbl_rating.grid(row=3, column=0)
        
        self.ent_rating = tk.Entry(self)
        self.ent_rating.grid(row=3, column=1, columnspan=2, sticky='news')
        
        self.lbl_mode = tk.Label(self, text="Game mode")
        self.lbl_mode.grid(row=3, column=3)
        
        mode_options = ["Single", "Multi", "Either"]
        self.tkvar_mode = tk.StringVar(self)
        self.tkvar_mode.set(mode_options[0])
        
        self.dbx_mode = tk.OptionMenu(self, self.tkvar_mode, *mode_options)
        self.dbx_mode.grid(row=3, column=4, columnspan=2, sticky='news')
        
        self.lbl_price = tk.Label(self, text="Price")
        self.lbl_price.grid(row=4, column=0)
        
        self.ent_price = tk.Entry(self)
        self.ent_price.grid(row=4, column=1, columnspan=2, sticky='news')
        
        self.chk_beat = tk.Checkbutton(self, text="Beat it?")
        self.chk_beat.grid(row=4, column=3, columnspan=3, sticky='news')
        
        self.lbl_purchase = tk.Label(self, text="Purchase")
        self.lbl_purchase.grid(row=5, column=0)
        
        self.ent_purchase = tk.Entry(self)
        self.ent_purchase.grid(row=5, column=1, columnspan=2, sticky='news')
        
        self.lbl_notes = tk.Label(self, text="Notes:")
        self.lbl_notes.grid(row=6, column=0)
        
        self.scr_notes = ScrolledText(self, height=8, width=40)
        self.scr_notes.grid(row=7, column=0, columnspan=6, sticky='news')
        
        self.btn_cancel = tk.Button(self, text="Cancel")
        self.btn_cancel.grid(row=8, column=0, columnspan=2)
        
        self.btn_clear = tk.Button(self, text="Clear")
        self.btn_clear.grid(row=8, column=2, columnspan=2)
        
        self.btn_submit = tk.Button(self, text="Submit")
        self.btn_submit.grid(row=8, column=4, columnspan=2)
        
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)  
        
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
    
    save_menu = SaveMessage()
    save_menu.grid(row=0, column=0, sticky='news')
    
    editor_menu = Editor()
    editor_menu.grid(row=0, column=0, sticky='news')
    
    root.grid_columnconfigure(0, weight=1)
    search_menu.tkraise()
    root.mainloop()