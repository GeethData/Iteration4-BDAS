# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:54:33 2021

@author: Geeth
"""


import pandas as pd
from Utils import Utils

class DataTransform:
    dataset1 = "credit_card_Dataset1.csv"
    
    ut = Utils()
    
    df = ut.readData(dataset1)
    

    
    #df.Class.value_counts().plot(kind='bar', title='Count (target)');
    
    count_class_0, count_class_1 = df.Class.value_counts()
    
    # Divide by class
    df_class_0 = df[df['Class'] == 0] #majority class
    df_class_1 = df[df['Class'] == 1] #minority class
    
    # Sample Majority class (Class=0, to have same number of records as minority calls (Class=1)
    df_class_0_under = df_class_0.sample(count_class_1)
    
    # join the dataframes containing Class=1 and Class=0
    df_test_under = pd.concat([df_class_0_under, df_class_1])
    
    
    
    
    print('Random under-sampling:')
    print(df_test_under.Class.value_counts())
    print("Num records = ", df_test_under.shape[0])
    
    df_test_under.Class.value_counts().plot(kind='bar', title='Count (target)');
    
    print(df_test_under.shape)
    print(df_test_under['Class'].value_counts())
    
    ut.exportToCSV(df_test_under, "tt1.csv")