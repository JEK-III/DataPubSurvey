# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 16:06:56 2014

@author: jkratz
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 16:04:14 2014

@author: jkratz
"""
# must first supply the question to graph

# define color scheme
COLORS = ["#000000", "#404040", "#808080", "#C0C0C0", "#FFFFFF"]

#build filename
output_filename = column + '_by_' + CATEGORY_TYPE + '.svg'

# replace blank cell with 0s
responses_ft[column] = responses_ft[column].replace(np.nan, 0)

print responses_ft[column]
category_ct.reindex(index=category_ct.index[ ::-1 ])

#crosstab to summarize responses from each role
category_ct = pd.crosstab(responses_ft[CATEGORY_TYPE], responses_ft[column])

print category_ct

#normalize by row to % of total responses
#category_ct = category_ct.div(category_ct.sum(1).astype(float), axis = 0)

#put rows in order for graph
category_ct = category_ct.reindex([CATEGORIES])

#drop empty rows
category_ct = category_ct.dropna()

#plot result
category_ct.plot(kind='bar', alpha=1.0, color=COLORS)
savefig(output_filename, format="svg")
