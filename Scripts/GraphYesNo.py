# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 21:47:18 2014

@author: kratzscience
"""

# must first set column = index of the column to graph

# define color scheme
COLOR = ['w', 'k']


#build output filename
output_filename = column + '_by_' + CATEGORY_TYPE + '.svg'

# replace blank cell with 0s
responses_ft[column] = responses_ft[column].replace(np.nan, 'No')
responses_ft[column] = responses_ft[column].replace("Not sure / Not applicable", 'No')

#crosstab to summarize responses from each role
category_ct = pd.crosstab(responses_ft[CATEGORY_TYPE], responses_ft[column])

#normalize by row to % of total responses
category_ct = category_ct.div(category_ct.sum(1).astype(float), axis = 0)

#put rows in order for graph
category_ct = category_ct.reindex([CATEGORIES])

#drop empty rows
category_ct = category_ct.dropna()

#plot result
category_ct.plot(kind='bar', alpha=1.0, color=COLOR)
savefig(output_filename, format="svg")
