#!/usr/bin/python3
# Austin McCowan
# 2/10/2020

'''gui program for/based on game_library'''

import pickle
import data_reboot as dr
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox


# Constants
TITLE_FONT = ("Times New Roman", 24)
BUTTON_FONT = ("Arial", 15)
TEXT_LIST = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
             't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

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
            
            # If file fails to load, raise error
            raise Exception("Data failed to save")
        
        
class Screen(tk.Frame):
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        screens[Screen.current].tkraise()
        
class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        # Title
        self.lbl_title = tk.Label(self, text= "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan=3, sticky = "news")
        
        # Add button
        self.btn_add = tk.Button(self, text = "Add", font = BUTTON_FONT, command = self.go_add)
        self.btn_add.grid(row = 1, column = 1, sticky='news')
        
        # Edit Button
        self.btn_edit = tk.Button(self, text = "Edit", font = BUTTON_FONT, command = self.go_edit)
        self.btn_edit.grid(row = 2, column = 1, sticky='news')
        
        # Search Button
        self.btn_search = tk.Button(self, text = "Search", font = BUTTON_FONT, command = self.go_search)
        self.btn_search.grid(row = 3, column = 1, sticky='news')
        
        # Remove Button
        self.btn_remove = tk.Button(self, text = "Remove", font = BUTTON_FONT, command = self.go_remove)
        self.btn_remove.grid(row = 4, column = 1, sticky='news')
        
        # Save Button
        self.btn_save = tk.Button(self, text = "Save", font = BUTTON_FONT, command = content.save)
        self.btn_save.grid(row = 5, column = 1, sticky='news')                
        
        # Grid column configures    
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
    # --Screen transition functions--
    # to go to the add menu
    def go_add(self):
        Screen.current = 2
        screens[Screen.current].clear()
        Screen.switch_frame()
        
        for i in range(len(content.games)):
            if (i+1) not in content.games.keys():
                screens[2].edit_key = i+1
                break
            else:
                screens[2].edit_key = len(content.games)+1
    
    # to open the edit pop up
    def go_edit(self):
        pop_up = tk.Tk()
        pop_up.title("Edit")
        
        frm_edit = EditSelect(pop_up)
        frm_edit.grid(row=0, column=0, sticky='news')
        pop_up.grid_columnconfigure(0, weight=1)
    
    # to go to search menu    
    def go_search(self):     
        Screen.current = 1
        Screen.switch_frame()
    
    # to open up the remove popup
    def go_remove(self):
        pop_up_remove = tk.Tk()
        pop_up_remove.title("Remove")
        
        frm_remove = Remove(pop_up_remove)
        frm_remove.grid(row=0, column=0, sticky='news')
        pop_up_remove.grid_columnconfigure(0, weight=1)
    
    # To save edits made to the library
    def go_save(self):
        pass
    
class SearchFilters(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        
        # Widgets, check buttons
        self.lbl_print_filers = tk.Label(self, text="Print Filters")
        self.lbl_print_filers.grid(row=0, column=0, columnspan=3)
        
        # Checkbutton genre
        self.genre_filter = tk.BooleanVar()
        self.genre_filter.set(True)
        self.chk_genre = tk.Checkbutton(self, text="Genre", variable = self.genre_filter)
        self.chk_genre.grid(row=1, column=0)
        
        # Checkbutton title
        self.title_filter = tk.BooleanVar()
        self.title_filter.set(True)            
        self.chk_title = tk.Checkbutton(self, text="Title", variable = self.title_filter)
        self.chk_title.grid(row=2, column=0)
        
        # Checkbutton developer
        self.developer_filter = tk.BooleanVar()
        self.developer_filter.set(True)        
        self.chk_developer = tk.Checkbutton(self, text="Developer", variable = self.developer_filter)
        self.chk_developer.grid(row=3, column=0)
        
        # Checkbutton publisher
        self.publisher_filter = tk.BooleanVar()
        self.publisher_filter.set(True)        
        self.chk_publisher = tk.Checkbutton(self, text="Publisher", variable = self.publisher_filter)
        self.chk_publisher.grid(row=4, column=0) 
        
        # Checkbutton system
        self.system_filter = tk.BooleanVar()
        self.system_filter.set(True)        
        self.chk_system = tk.Checkbutton(self, text="System", variable = self.system_filter)
        self.chk_system.grid(row=1, column=1) 
        
        # Checkbutton release date
        self.release_filter = tk.BooleanVar()
        self.release_filter.set(True)        
        self.chk_release = tk.Checkbutton(self, text= "Release Date", variable = self.release_filter)
        self.chk_release.grid(row=2, column=1) 
        
        # Checkbutton rating
        self.rating_filter = tk.BooleanVar()
        self.rating_filter.set(True)        
        self.chk_rating = tk.Checkbutton(self, text="Rating", variable = self.rating_filter)
        self.chk_rating.grid(row=3, column=1) 
        
        # Checkbutton mode
        self.mode_filter = tk.BooleanVar()
        self.mode_filter.set(True)        
        self.chk_mode = tk.Checkbutton(self, text="Game Mode", variable = self.mode_filter)
        self.chk_mode.grid(row=4, column=1) 
        
        # Checkbutton price
        self.price_filter = tk.BooleanVar()
        self.price_filter.set(True)        
        self.chk_price = tk.Checkbutton(self, text="Price", variable = self.price_filter)
        self.chk_price.grid(row=1, column=2) 
        
        # Checkbutton beat it
        self.beat_filter = tk.BooleanVar()
        self.beat_filter.set(True)        
        self.chk_beat = tk.Checkbutton(self, text="Beat it?", variable = self.beat_filter)
        self.chk_beat.grid(row=2, column=2) 
        
        # Checkbutton purchase
        self.purchase_filter = tk.BooleanVar()
        self.purchase_filter.set(True)        
        self.chk_purchase = tk.Checkbutton(self, text="Purchase Date", variable = self.purchase_filter)
        self.chk_purchase.grid(row=3, column=2)
        
        self.notes_filter = tk.BooleanVar()
        self.notes_filter.set(True)
        self.chk_notes = tk.Checkbutton(self, text="Notes", variable=self.notes_filter)
        self.chk_notes.grid(row=4, column=2)
        
        # grid column configures
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
               
class Search(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        # Widgets
        self.lbl_title = tk.Label(self, text="Search")
        self.lbl_title.grid(row=0, column=0, columnspan=6)
        
        self.lbl_search_by = tk.Label(self, text="Search By:")
        self.lbl_search_by.grid(row=1, column=0, columnspan=3, sticky='news')
        
        self.lbl_search_for = tk.Label(self, text="Search For:")
        self.lbl_search_for.grid(row=3, column=0, columnspan=3, sticky='news')
        
        # Drop down menu
        self.category_list = ["None", "genre","title", "developer", "publisher", "system", "release date", "rating", "single/multi/either", "price", "beat it", "purchase date"]
        self.tkvar_search = tk.StringVar(self)
        self.tkvar_search.set(self.category_list[0])
        
        self.dbx_search_by = tk.OptionMenu(self, self.tkvar_search, *self.category_list)
        self.dbx_search_by.grid(row=2, column=0, columnspan=3, sticky='news')
        
        # More widgets
        self.ent_search_for = tk.Entry(self)
        self.ent_search_for.grid(row=4, column=0, columnspan=3, sticky='news')
        
        self.frm_search_filters = SearchFilters(self)
        self.frm_search_filters.grid(row=1, column=3, rowspan=4, columnspan=3)
        
        self.scr_text = ScrolledText(self, height=8, width=40)
        self.scr_text.grid(row=5, column=0, columnspan=6, sticky='news')
            
        self.btn_back = tk.Button(self, font = BUTTON_FONT, text="Back", command = self.go_mainmenu)
        self.btn_back.grid(row=6, column=0, columnspan=2, sticky='news')
        
        self.btn_clear = tk.Button(self, font = BUTTON_FONT, text="Clear", command = self.clear)
        self.btn_clear.grid(row=6, column=2, columnspan=2, sticky='news')
        
        self.btn_submit = tk.Button(self, font = BUTTON_FONT, text="Submit", command = self.search_with_param)
        self.btn_submit.grid(row=6, column=4, columnspan=2, sticky='news')
        
        # Grid column configure
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        
        self.search_update()
        
    def search_with_param(self):
        # grabs the values currently selected in the 'search by' drop down and typed in the 'search for' entry.
        search_for = self.ent_search_for.get()
        search_cat = self.tkvar_search.get()
        
        # Make sure search category is not 'None'
        if search_cat != self.category_list[0]:   
            self.scr_text.delete(0.0, "end")
            
            # Searches through every entry in games
            for key in content.games.keys():
                
                ''' Since category_list is in the same order as the categories in games, do self.category_list.index(search_cat)-1
                 to return the index of whatever category is being searched. The minus 1 is to account for the placeholder text "None".
                'list.index(value)' is basically: Loop through length of the list until value = list[i], then return i.'''
                if search_for.lower() in content.games[key][self.category_list.index(search_cat)-1].lower():
                    entry = content.games[key]
                    self.filter_print(entry)
                    
        # If there is no search category selected (or rather 'None'), just run search_update
        else:
            self.search_update()
            
            
    def search_update(self):
        self.scr_text.delete(0.0, "end")
        for key in content.games.keys():
            entry = content.games[key]
            self.filter_print(entry)
    
    def clear(self):
        self.frm_search_filters.genre_filter.set(False)
        self.frm_search_filters.title_filter.set(False)
        self.frm_search_filters.developer_filter.set(False)
        self.frm_search_filters.publisher_filter.set(False)
        self.frm_search_filters.system_filter.set(False)
        self.frm_search_filters.release_filter.set(False)
        self.frm_search_filters.rating_filter.set(False)
        self.frm_search_filters.mode_filter.set(False)
        self.frm_search_filters.price_filter.set(False)
        self.frm_search_filters.beat_filter.set(False)
        self.frm_search_filters.purchase_filter.set(False)
        self.frm_search_filters.notes_filter.set(False)
        self.scr_text.delete(0.0, "end")
        
    # Functions    
    def go_mainmenu(self):
        Screen.current = 0
        Screen.switch_frame()   
    
    def filter_print(self, entry):
        # Used to detect text in an entry
        empty = True
        
        if self.frm_search_filters.genre_filter.get() == True:
            msg = entry[0] + "\n"
            self.scr_text.insert("insert", msg)
            
            # If any text is present, a separating line can be used
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[0]:            
                    empty = False
            
        if self.frm_search_filters.title_filter.get() == True:
            msg = entry[1] + "\n"
            self.scr_text.insert("insert", msg)           
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[1]:            
                    empty = False
                    
        if self.frm_search_filters.developer_filter.get() == True:
            msg = entry[2] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[2]:            
                    empty = False            
        
        if self.frm_search_filters.publisher_filter.get() == True:
            msg = entry[3] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[3]:            
                    empty = False            
        
        if self.frm_search_filters.system_filter.get() == True:
            msg = entry[4] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[4]:            
                    empty = False            
        
        if self.frm_search_filters.release_filter.get() == True:
            msg = entry[5] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[5]:            
                    empty = False            
        
        if self.frm_search_filters.rating_filter.get() == True:
            msg = entry[6] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[6]:            
                    empty = False            
            
        if self.frm_search_filters.mode_filter.get() == True:
            msg = entry[7] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[7]:            
                    empty = False            
        
        if self.frm_search_filters.price_filter.get() == True:
            msg = entry[8] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[8]:            
                    empty = False            
        
        if self.frm_search_filters.beat_filter.get() == True:
            msg = entry[9] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[9]:            
                    empty = False            
        
        if self.frm_search_filters.purchase_filter.get() == True:
            msg = entry[10] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[10]:            
                    empty = False            
        
        if self.frm_search_filters.notes_filter.get() == True:
            msg = entry[11] + "\n"
            self.scr_text.insert("insert", msg)
            
            for i in range(len(TEXT_LIST)):
                if TEXT_LIST[i] in entry[11]:            
                    empty = False            
                    
        # If the entry in search contains anything, place a separating line to distinguish where one entry ends and one starts
        if empty == False:
            msg = "---------------------------------------------\n"
            self.scr_text.insert("insert", msg)
    
class EditSelect(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        self.parent = parent
        
        self.lbl_title = tk.Label(self, text="Which game would you like to edit?")
        self.lbl_title.grid(row=0, column=0, columnspan=2)
        
        self.titles_to_edit = ["select a title..."]
        for key in content.games.keys():
            self.titles_to_edit.append(content.games[key][1])
            
        self.tkvar_titles_to_edit = tk.StringVar(self)
        self.tkvar_titles_to_edit.set(self.titles_to_edit[0])
        
        self.dbx_titles_to_edit = tk.OptionMenu(self, self.tkvar_titles_to_edit, *self.titles_to_edit)
        self.dbx_titles_to_edit.grid(row=1, column=0, columnspan=2, sticky='news')
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT, command = self.go_mainmenu)
        self.btn_cancel.grid(row=2, column=0, sticky='news')
        
        self.btn_okay = tk.Button(self, text="OK", font=BUTTON_FONT, command = self.go_editor)
        self.btn_okay.grid(row=2, column=1, sticky='news')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
    # For the cancel button    
    def go_mainmenu(self):
        Screen.current = 0
        Screen.switch_frame()
        
        self.parent.destroy()
    
    # For the okay button
    def go_editor(self):        
        if self.tkvar_titles_to_edit.get() == self.titles_to_edit[0]:
            pass
        else:
            for i in range(len(self.titles_to_edit)):
                if self.tkvar_titles_to_edit.get() == self.titles_to_edit[i]:
                    screens[2].edit_key = i
                    break
                
            Screen.current = 2
            screens[2].load_to_edit()
            Screen.switch_frame()            
            self.parent.destroy()

class Remove(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master=parent)
        self.parent = parent
        
        self.lbl_title = tk.Label(self, text="Which game would you like to remove?")
        self.lbl_title.grid(row=0, column=0, columnspan=2)
             
        self.titles = ["Please Choose a game..."]
        for key in content.games.keys():
            self.titles.append(content.games[key][1])
            
        self.tkvar_remove = tk.StringVar(self)
        self.tkvar_remove.set(self.titles[0])
        
        self.dbx_titles_to_remove = tk.OptionMenu(self, self.tkvar_remove, *self.titles)
        self.dbx_titles_to_remove.grid(row=1, column=0, columnspan=2, sticky='news')
        
        self.btn_cancel = tk.Button(self, text="Cancel", font=BUTTON_FONT, command=self.go_mainmenu)
        self.btn_cancel.grid(row=2, column=0, sticky='news')
        
        self.btn_remove = tk.Button(self, text="Remove", font=BUTTON_FONT, command=self.remove_game)
        self.btn_remove.grid(row=2, column=1, sticky='news')
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
    
    # For the cancel button
    def go_mainmenu(self):
        Screen.current = 0
        Screen.switch_frame()
        
        self.parent.destroy()
        
    def remove_game(self):
        temp_dictionary = content.games
        game_to_remove = self.tkvar_remove.get()
        index_of_remove = None
            
        for key in content.games.keys():
            if game_to_remove == content.games[key][1]:
                index_of_remove = key
        
        try:
            for key in range(1, len(content.games)+1):
                if key >= index_of_remove and key != len(content.games):
                    content.games[key] = content.games[key+1]
                if key == len(content.games):
                    content.games.pop(key)
        except:
            # Failsafe
            content.games = temp_dictionary
            content.games.pop(index_of_remove)        
            
        self.go_mainmenu()
        
        
class PopMessage(tk.Frame):
    def __init__(self, parent, msg='generic'):
        tk.Frame.__init__(self, master=parent)
        self.parent = parent
        
        self.lbl_continue = tk.Label(self, text=msg)
        self.lbl_continue.grid(row=0, column=0, sticky='news')
        
        self.btn_ok = tk.Button(self, text='OK', command=self.parent.destroy)
        self.btn_ok.grid(row=1, column=0, sticky='news')
    
class Editor(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.edit_key = 0
        
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
        
        self.mode_options = ["Single", "Multi", "Either"]
        self.tkvar_mode = tk.StringVar(self)
        self.tkvar_mode.set(self.mode_options[0])
        
        self.dbx_mode = tk.OptionMenu(self, self.tkvar_mode, *self.mode_options)
        self.dbx_mode.grid(row=3, column=4, columnspan=2, sticky='news')
        
        self.lbl_price = tk.Label(self, text="Price")
        self.lbl_price.grid(row=4, column=0)
        
        self.ent_price = tk.Entry(self)
        self.ent_price.grid(row=4, column=1, columnspan=2, sticky='news')
        
        self.boolean_beat_it = tk.BooleanVar()
        self.boolean_beat_it.set(False)
        self.chk_beat = tk.Checkbutton(self, variable=self.boolean_beat_it, text="Beat it?")
        self.chk_beat.grid(row=4, column=3, columnspan=3, sticky='news')
        
        self.lbl_purchase = tk.Label(self, text="Purchase")
        self.lbl_purchase.grid(row=5, column=0)
        
        self.ent_purchase = tk.Entry(self)
        self.ent_purchase.grid(row=5, column=1, columnspan=2, sticky='news')
        
        self.lbl_notes = tk.Label(self, text="Notes:")
        self.lbl_notes.grid(row=6, column=0)
        
        self.scr_notes = ScrolledText(self, height=8, width=40)
        self.scr_notes.grid(row=7, column=0, columnspan=6, sticky='news')
        
        self.btn_cancel = tk.Button(self, text="Cancel", command=self.go_mainmenu)
        self.btn_cancel.grid(row=8, column=0, columnspan=2, sticky='news')
        
        self.btn_clear = tk.Button(self, text="Clear", command=self.clear)
        self.btn_clear.grid(row=8, column=2, columnspan=2, sticky='news')
        
        self.btn_submit = tk.Button(self, text="Submit", command=self.submit_edit)
        self.btn_submit.grid(row=8, column=4, columnspan=2, sticky='news')
        
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
    
    def go_mainmenu(self):
        Screen.current = 0
        Screen.switch_frame()
        self.clear()
    
    # This function occurs when EditSelect is used. It LOADs the contents of the selected game inTO EDITor
    def load_to_edit(self):
        entry = content.games[self.edit_key]
        
        self.ent_genre.delete(0, "end")
        self.ent_genre.insert(0, entry[0])
        
        self.ent_title.delete(0, "end")
        self.ent_title.insert(0, entry[1])
        
        self.ent_developer.delete(0, "end")
        self.ent_developer.insert(0, entry[2])
        
        self.ent_publisher.delete(0, "end")
        self.ent_publisher.insert(0, entry[3])
        
        self.ent_system.delete(0, "end")
        self.ent_system.insert(0, entry[4])
        
        self.ent_release.delete(0, "end")
        self.ent_release.insert(0, entry[5])
        
        self.ent_rating.delete(0, "end")
        self.ent_rating.insert(0, entry[6])
        
        # Insert drop down menu stuff
        for i in range(len(self.mode_options)):
            if entry[7].lower() == self.mode_options[i].lower():
                self.tkvar_mode.set(self.mode_options[i])
                self.dbx_mode.config(textvariable = self.tkvar_mode)
                break
        
        self.ent_price.delete(0, "end")
        self.ent_price.insert(0, entry[8])
        
        # Enable/disable the check button
        if entry[9].lower() == "yes":
            self.chk_beat.select()
        else:
            self.chk_beat.deselect()
        
        self.ent_purchase.delete(0, "end")
        self.ent_purchase.insert(0, entry[10])
        
        self.scr_notes.delete(0.0, "end")
        self.scr_notes.insert(0.0, entry[11])
        
    def submit_edit(self):
        entry = []
        entry.append(self.ent_genre.get())
        entry.append(self.ent_title.get())
        entry.append(self.ent_developer.get())
        entry.append(self.ent_publisher.get())
        entry.append(self.ent_system.get())
        entry.append(self.ent_release.get())
        entry.append(self.ent_rating.get())
        entry.append(self.tkvar_mode.get())
        entry.append(self.ent_price.get())
        if self.boolean_beat_it.get() == True:
            entry.append("yes")
        else:
            entry.append("no")
        entry.append(self.ent_purchase.get())
        entry.append(self.scr_notes.get(0.0, "end"))
        
        content.games[self.edit_key] = entry
        
        popup = tk.Tk()
        popup.title("title")
        msg = "Entry Saved"
        frm_error = PopMessage(popup, msg)
        frm_error.grid(row=0, column=0)
        
        #messagebox.showinfo(message="Entry saved")
        Screen.current = 0
        Screen.switch_frame()
        self.clear()

    def clear(self):
        self.ent_genre.delete(0, "end")
        self.ent_title.delete(0, "end")      
        self.ent_developer.delete(0, "end")
        self.ent_publisher.delete(0, "end")        
        self.ent_system.delete(0, "end")
        self.ent_release.delete(0, "end")
        self.ent_rating.delete(0, "end")      
        self.ent_price.delete(0, "end")
        self.ent_purchase.delete(0, "end")
        self.scr_notes.delete(0.0, "end")
        self.chk_beat.deselect()
        
# Functions/global functions


## Main
if __name__ == "__main__":
    content = Library()
    root = tk.Tk()
    root.title("Game Library")
    root.geometry("500x500")

    # Editor() can be seen as Add()
    screens = [MainMenu(), Search(), Editor()]
    
    screens[0].grid(row=0, column=0, sticky='news')
    screens[1].grid(row=0, column=0, sticky='news')
    screens[2].grid(row=0, column=0, sticky='news')
    
    root.grid_columnconfigure(0, weight=1)
    screens[0].tkraise()
    root.mainloop()