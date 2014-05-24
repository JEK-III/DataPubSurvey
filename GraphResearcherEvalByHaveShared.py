# -*- coding: utf-8 -*-
"""
Created on Fri May 23 16:24:39 2014

@author: jkratz
"""
# Graph formatting -------------------------------------------------------------
COLORS = ['#08519c',
          '#3182bd',
          '#6baed6',
          '#bdd7e7',
          '#eff3ff',
          '#006d2c',
          '#31a354',
          '#74c476',
          '#bae4b3',
          '#edf8e9']
          
GRAPH_TITLE = "Data evaluation as a function of having shared data or not."        
IVAR = 'have_shared'  
DVARS = RESEARCHER_VALUE
DVAR_VALUES = RESEARCHER_VALUE_SEQUENCE


execfile("ReadInSurvey.py")

responses_ft = responses.reindex(columns=[IVAR] + DVARS)


INDEX_LIST = []
for i in DVARS:
    INDEX_LIST.extend([i, i])

GRAPH_INDEX = pd.MultiIndex.from_arrays(
                                [len(DVARS) * [True, False],
                                 INDEX_LIST], 
                                 names = ['ivar', 'dvars'])


mask = responses_ft[IVAR].apply(lambda x: x == 'Yes')

collected_counts = pd.DataFrame(index=DVAR_RESPONSES, columns=GRAPH_INDEX)        

for column in DVARS:            
    collected_counts[True, column] = \
        responses_ft[mask][column].value_counts().fillna(0)
    collected_counts[False, column] = \
        responses_ft[~mask][column].value_counts().fillna(0)
     
  
collected_counts = collected_counts.T

collected_counts = collected_counts.div(collected_counts.sum(1).astype(float), 
                                        axis = 0)      
collected_counts = collected_counts.reindex(
    index=collected_counts.index[ ::-1 ])

collected_counts.plot(kind='barh',
                      stacked=True, 
                      color=COLORS,
                      grid=False, 
                      legend=False,
                      title=GRAPH_TITLE,
                      edgecolor='none') 

"""                      
set_title(action, fontdict=TITLE_FONT)
spines['right'].set_visible(False)
spines['top'].set_visible(False)
spines['bottom'].set_color('#5b6f74')
spines['left'].set_color('#5b6f74')
"""                                        

