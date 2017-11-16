#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:46:32 2017

@author: garrettboseck
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

fileLocation = '/Users/garrettboseck/Desktop/ratings.csv'

pd.set_option('display.max_rows', None) #show every row

df = pd.read_csv(fileLocation)
df1 = df.iloc[:,1:172] #append original dataframe to remove timestamp

lst = []
for i in range (0,96): #number of users
    df2 = df1.iloc[i] #show only the current users' ratings
    df3 = df2.iloc[1:] 
    lst.append(df3.count()) #append number of ratings for current user to a list

lst_sum = sum(lst) #sum of the list after looping
lst_len = len(lst) #number of elements in list (should be 96)
average = lst_sum/lst_len #calculate the average number of ratings per user
print(average) #print

df4 = df1.T #transpose the Series and perform the same list of operations as above but for average ratings per joke

lst1 = []
for i in range(0,171):
    df5 = df4.iloc[i]
    lst1.append(df5.count())

lst1_sum = sum(lst1)
lst1_len = len(lst1)
average1 = lst1_sum/lst1_len
print(average1)

