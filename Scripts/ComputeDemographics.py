# -*- coding: utf-8 -*-
"""
Created on Tue May 27 16:41:14 2014

@author: jkratz
"""

DEMOGRAPHICS = ['discipline',
                'highest_degree',
                'role',
                'institution']


from DefineConstants import SUBDISCIPLINE_TO_DISCIPLINE

counts = responses.discipline.map(SUBDISCIPLINE_TO_DISCIPLINE).value_counts()
percentages = 100 * counts.apply(lambda x: float(x) / counts.sum())
stats = pd.DataFrame([counts, percentages], index=['counts', 'percent'])
print "\nColumn: aggegated discipline"
print stats.T
print "total: ", counts.sum()

for column in DEMOGRAPHICS:
    counts = responses[column].value_counts()
    percentages = 100 * counts.apply(lambda x: float(x) / counts.sum())
    stats = pd.DataFrame([counts, percentages], index=['counts', 'percent'])
    print "\nColumn: ", column
    print stats.T
    print "total: ", counts.sum()
