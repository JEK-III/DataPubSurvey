# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 22:14:09 2014

@author: kratzscience
"""

# must first supply the question to graph

COLORS = ["#000000", "#555555", "#AAAAAA", "#FFFFFF"]


# set the response order
button_labels = ["Know all the details", 
                 "Read about it", 
                 "Heard of it", 
                 "Never heard of it"]

#build filename
ouput_filename = column + '_faimiliarity_by_' + CATEGORY_TYPE + '.svg'

#crosstab to summarize responses from each category
category_ct = pd.crosstab(responses_ft[CATEGORY_TYPE], responses_ft[column])

#normalize by row to % of total responses
category_ct = category_ct.div(category_ct.sum(1).astype(float), axis = 0)



#put rows in order for graph
category_ct = category_ct.reindex([CATEGORIES])

#put columns in order for graph
category_ct = category_ct.reindex(columns=button_labels)

#plot result
category_ct.plot(kind='bar', stacked=True, alpha=1.0, color=COLORS)
savefig(ouput_filename, format="svg")
