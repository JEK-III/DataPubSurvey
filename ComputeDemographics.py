# -*- coding: utf-8 -*-
"""
Created on Tue May 27 16:41:14 2014

@author: jkratz
"""

DEMO_COLUMNS = ['discipline',
                'role',
                'institution']

execfile("ReadInSurvey.py")

for column in DEMO_COLUMNS:
    counts = responses[column].value_counts()
    percentages = 100 * counts.apply(lambda x: float(x) / counts.sum())
    stats = pd.DataFrame([counts, percentages], index=['counts', 'percent'])
    print "\nColumn: ", column
    print stats.T
    print "total: ", responses[column].value_counts().sum()
