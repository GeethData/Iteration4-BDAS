# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:42:48 2021

@author: Geeth
"""
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


class DataPreparation:
    def __init__(self):
         print("Initiate")
    
    def BalanceDataSetUnder(self, data, fieldName):
        df = pd.DataFrame(data)
        #df.Class.value_counts().plot(kind='bar', title='Count (target)');
    
        count_class_0, count_class_1 = df[fieldName].value_counts()
    
        # Divide by class
        df_class_0 = df[df[fieldName] == 0] #majority class
        df_class_1 = df[df[fieldName] == 1] #minority class
    
        # Sample Majority class (Class=0, to have same number of records as minority calls (Class=1)
        df_class_0_under = df_class_0.sample(count_class_1)
    
        # join the dataframes containing Class=1 and Class=0
        df_test_under = pd.concat([df_class_0_under, df_class_1])
    
        #print('Random under-sampling:')
        #print(df_test_under[fieldName].value_counts())
        #print("Num records = ", df_test_under.shape[0])
    
        df_test_under[fieldName].value_counts().plot(kind='bar', title='Count (target)');
    
        #print(df_test_under.shape)
        #print(df_test_under[fieldName].value_counts())
    
        return df_test_under
    
    
    # Merge 2 datasets on given index
    def MeargeDataSets(self, data1, data2, index):
        df1 = pd.DataFrame(data1)
        df2 = pd.DataFrame(data2)
        return  pd.merge(df1, df2, on=index)
    
    def DropDuplicates(self, data):
        df = pd.DataFrame(data)
        return  df.drop_duplicates()
    
    # Remove any rows with missing values   
    def RemoveRowsWithMissingValues(data):
        df = pd.DataFrame(data)
        return df.dropna(axis=0)
        
    def Clustering(self, data):
        df = pd.DataFrame(data)
    
    
    def FillNanWithMean(self, data):
        df = pd.DataFrame(data)
        return df.fillna(df.mean())

        ############# Clustering #############
        # Initialize the model with 2 parameters -- number of clusters and random state.
        kmeans_model = KMeans(n_clusters=5, random_state=1)
        
        # Get only the numeric columns from the data set.
        good_columns = df._get_numeric_data()
        
        # Fit the model using the good columns.
        kmeans_model.fit(good_columns)

        # Get the cluster assignments.
        labels = kmeans_model.labels_    

        
############# Plotting Clusters #############
        # Create a PCA model.
        pca_2 = PCA(2)
        
        # Fit the PCA model on the numeric columns from earlier.
        plot_columns = pca_2.fit_transform(good_columns)
        
        # Make a scatter plot of each game, shaded according to cluster assignment.
        plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
        
        # Show the plot.
        plt.show()
        
        