# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:34:48 2021

@author: Geeth
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)

class DataUnderstanding:
    def __init__(self):
        print("Data Understanding")
         
   
    def PrintDetails(self, data):
        df = pd.DataFrame(data)
        print("\n# # # # # # # # # Size of the dataset # # # # # # # # #")
        print(df.shape)

        print("\n# # # # # # # # # Column names of the dataset # # # # # # # # #")
        print(df.columns)
        
        print("\n# # # # # # # # # Information of the dataset # # # # # # # # #")
        print(df.info())

        print("\n# # # # # # # # # First 10 records of the dataset # # # # # # # # #")
        print(df[0:10])

        print("\n# # # # # # # # # Statistics of the dataset # # # # # # # # #")
        print(df.describe())
        
        print("\n# # # # # # # # # Data Types # # # # # # # # #")
        print(df.dtypes)

        print("\n# # # # # # # # # First 5 rocords # # # # # # # # #")
        print(df.head)
        
        print("\n# # # # # # # # # Last 5 rocords # # # # # # # # #")
        print(df.tail)

    def DrawCountPlot(self, fn1, fn2):
        # set the background colour of the plot to white
        sns.set(style="whitegrid", color_codes=True)

        # setting the plot size for all plots
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        
        # create a countplot
        sns.countplot(fn1, data=sales_data,hue = fn2)

        # Remove the top and down margin
        sns.despine(offset=10, trim=True)
        
        # display the 
        plotplt.show()

        
    def DistPlot(self, data):
        df = pd.DataFrame(data)
        sns.barplot(df["Class"], df["Amount"])
       # sns.jointplot(df["Class"], df["Amount"])


    def DrawHist(self, data, fieldName, title, bins):
         df = pd.DataFrame(data)
         
         plt.hist(df[fieldName],bins = bins)
         plt.xlabel(fieldName)
         plt.title(title)
         plt.ylabel('Frequency')
         plt.show()
          
    def PlotData(self, data, x_axis, y_axis, title):
         df = pd.DataFrame(data)
         x = df[x_axis]
         y = df[y_axis]
                 
         plt.plot(x,y)
         plt.xlabel(x_axis)
         plt.ylabel(y_axis)
         plt.title(title)
         plt.show()

         
    def ExploreData(self, data):
        df = pd.DataFrame(data)
        df.head() # show first 5 rows
        df.tail() # last 5 rows
        df.columns # list all column names
        df.shape # get number of rows and columns
        df.info() # additional info about dataframe
        df.describe() # statistical description, only for numeric values
       
    # count unique values in a column
    def CountUniqueValues(self, data, fieldName):
        df = pd.DataFrame(data)
        df[fieldName].value_counts(dropna=False)
        
    def BarPlots(self, data, fieldName):
        df = pd.DataFrame(data)
        df[fieldName].plot('hist')
        
    def BoxPlot(slef, data, col_name1, col_name2):
        df = pd.DataFrame(data)
        df.boxplot(column=col_name1, by=col_name2)   
        
    def DataStat(data, fieldName):
        df = pd.DataFrame(data)
       
        all = len(df.index)
        
        
        ls = pd.DataFrame(df[fieldName])
        
        nulls = ls.isnull().sum()
    
        ls = df[fieldName].dropna()
    
        lables = 0
        
        new_df = ls.groupby(ls).count()
    
        
        ones = countX(ls,1)
        zeros = countX(ls,0)
        #nulls = countX(ls,'')
     
      
        onesp = ones/(all)*100
        zerosp = zeros/(all)*100
        nullp = nulls/(all)*100
        
        #oStr = "1 Count=" + str(ones) + ", " + "{:.2f}".format(onesp) + "%"
        #zStr = "0 Count=" + str(zeros) + ", " + "{:.2f}".format(zerosp) + "%"
        #nStr = "Null Count=" + str(nulls) + ", " + "{:.2f}".format(nullp) + "%"
