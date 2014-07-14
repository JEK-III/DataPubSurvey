# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 13:52:06 2014

@author: jkratz
"""

execfile("ReadInSurvey.py")

column = responses['number_data_journals_named']

mean_with_blanks = column.sum()/len(column)
print mean_with_blanks


mean_without_blanks = column.dropna().mean()
print mean_without_blanks

print column.dropna().value_counts()
print column.dropna().value_counts().apply(lambda x: float(x) / 
        len(column.dropna()))
