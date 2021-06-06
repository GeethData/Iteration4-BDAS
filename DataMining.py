# -*- coding: utf-8 -*-
"""
Created on Wed May  5 09:11:29 2021

@author: Geeth
"""
import pandas as pd



class DataMining:
   # df = pd.DataFrame
    def __init__(self, data):
        self.df = pd.DataFrame(data)
        
        
    def Training(self):
        #ke.data 
        print("\n############################ Training ############################")
        print(self.df.columns)