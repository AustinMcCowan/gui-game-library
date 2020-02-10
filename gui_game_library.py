#!/usr/bin/python3
# Austin McCowan
# 2/10/2020

'''gui program for/based on game_library'''

import pickle
import data_reboot as dr

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