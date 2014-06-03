# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 16:04:14 2014

@author: jkratz
"""
# must first set column = index of the column to graph

# define color scheme
COLORS = ["#000000", "#404040", "#808080", "#C0C0C0", "#FFFFFF"]


#build output filename
#output_filename = column + '_by_' + CATEGORY_TYPE + '.svg'

#crosstab to summarize responses from each role
category_ct = pd.crosstab(responses_ft[CATEGORY_TYPE], responses_ft[column])

#normalize by row to % of total responses
category_ct = category_ct.div(category_ct.sum(1).astype(float), axis = 0)

#put rows in order for graph
category_ct = category_ct.reindex([CATEGORIES])

#drop empty rows
category_ct = category_ct.dropna()

#plot result
category_ct.plot(kind='bar', stacked=True, alpha=1.0, color=COLORS)
savefig(output_filename, format="svg")
