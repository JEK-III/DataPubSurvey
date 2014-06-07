# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 16:04:14 2014

@author: jkratz
"""
# must first set column = index of the column to graph

IVAR = 'discipline'
DVAR = 'aware_nsf_dmp'


GRAPH_TITLE = DVAR + " by " + IVAR

# define color scheme

"""
COLORS = ['#08519c',
          '#3182bd',
          '#6baed6',
          '#bdd7e7',
          '#eff3ff']
"""
COLORS = ['#08519c',
          '#3182bd',
          '#6baed6',
          '#eff3ff']
          
responses.discipline = responses.discipline.map(PAPER_DISCIPLINE_MAP)


#crosstab to summarize responses from each role
category_ct = pd.crosstab(responses[IVAR], responses[DVAR])

#normalize by row to % of total responses
category_ct = category_ct.div(category_ct.sum(1).astype(float), axis = 0)

#put rows in order for graph
category_ct = category_ct.reindex(columns=COLUMN_TO_ANSWERS[DVAR])
category_ct = category_ct.sort_index()

#drop empty rows
category_ct = category_ct.dropna()

#plot result
category_ct.plot(kind='barh',
                 stacked=True,
                 alpha=1.0,
                 color=COLORS,
                 edgecolor='w',
                 grid=False,
                 title=GRAPH_TITLE)
#savefig(output_filename, format="svg")
