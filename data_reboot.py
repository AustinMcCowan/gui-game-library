#!/usr/bin/python3
# Austin McCowan
# 1/28/2020

''' Reboots the data incase it becomes broken and thus unusable '''

import pickle

backup_content = {1: ['RPG', 'Nier:Automata', 'PlatinumGames', 'Square Enix', 'PS4', '3/17/2017', '10', 'single', '39.99', 'Yes', '1/15/2018', 'Become as gods.'],
                  2: ['TBT', 'Advanced Wars: Days of Ruin', 'IntelligentSystems', 'Nintendo','Nintendo DS', '1/21/2008', '9.5', 'Either', '20.00', 'No', ' ', 'Last entry to the Advanced Wars series']}
def fix_it():
    datafile = open("game_lib.pickle", "wb")
    pickle.dump(backup_content, datafile)
    datafile.close()
    