# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:05:13 2021

@author: Geeth
"""
import pandas as pd


class Utils:
    relative_path = ''
    
    def __init__(self):
        self.relative_path = ".\\data\\"
        self.missing_value_formats = ["n.a.","?","NA","n/a", "na", "--"]
    
    def readData(self, file_name):
        filepath = self.relative_path + file_name
        data = pd.read_csv(filepath, na_values = self.missing_value_formats)
        
        return pd.DataFrame(data)
    
    def exportToCSV(self, data, file_name):
        export_file_path = self.relative_path + file_name + ".csv"
        df=pd.DataFrame(data)
        df.to_csv (export_file_path, index = False, header=True)
    
    @staticmethod
    def getSampleDataSet():
        cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
        'Price': [22000,25000,27000,35000]}

        return pd.DataFrame(cars, columns= ['Brand', 'Price'])