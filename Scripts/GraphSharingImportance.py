# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 16:04:14 2014

@author: jkratz
"""
# must first supply the question to graph

import scipy.stats as sps

COLORS = ['#08519c',
          '#3182bd',
          '#6baed6',
          '#bdd7e7',
          '#eff3ff']
          
dvar = 'data_sharing_importance'
ivar = 'discipline'


#IMPORTANCE_AGGREGATOR = { 1 : 1, 2 : 1, 3 : 1, 4 : 5, 5 : 5}

#output_filename = column + '_by_' + CATEGORY_COLUMN + '.svg'


#crosstab to summarize responses from each role
responses_ct = pd.crosstab(responses[ivar].map(PAPER_DISCIPLINE_MAP), 
                           responses[dvar])

#normalize by row to % of total responses

print responses_ct.sum(axis=1)


print sps.chi2_contingency(responses_ct.as_matrix())

responses_ct = responses_ct.div(responses_ct.sum(1).astype(float), axis = 0)

#put rows in order for graph
#responses_ct = responses_ct.reindex([CATEGORIES])
#plot result
responses_ct.plot(kind='barh', 
                  stacked=True, 
                  alpha=1.0,
                  legend=False,
                  grid=False,
                  xlim = (0,1),
                  color=COLORS,
                  edgecolor='w')
#savefig(output_filename, format='svg')

