# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 16:04:14 2014

@author: jkratz
"""
# must first supply the question to graph

COLORS = ["#000000", "#404040", "#808080", "#C0C0C0", "#FFFFFF"]

column = 'data_sharing_importance'

output_filename = column + '_by_' + CATEGORY_COLUMN + '.svg'

#crosstab to summarize responses from each role
responses_ct = pd.crosstab(responses_ft[CATEGORY_COLUMN], 
                           responses_ft[column])

#normalize by row to % of total responses
responses_ct = responses_ct.div(responses_ct.sum(1).astype(float), axis = 0)

#put rows in order for graph
responses_ct = responses_ct.reindex([CATEGORIES])
#plot result
responses_ct.plot(kind='bar', stacked=True, alpha=1.0, color=COLORS)
savefig(output_filename, format='svg')
