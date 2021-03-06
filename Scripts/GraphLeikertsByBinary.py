# -*- coding: utf-8 -*-
"""
Created on Fri May 23 17:17:25 2014


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
          
GRAPH_TITLE = "Leikert grids as a function of having shared data or not."        
IVAR = 'have_shared'  

QUESTIONS = ['data_trust', 'data_value', 'researcher_value']




# Set up the figure and subfigures
fig, subfigs = plt.subplots(len(QUESTIONS), sharex=True)
i = 0

fig.suptitle(GRAPH_TITLE, fontsize=14)  

execfile("ReadInSurvey.py")

mask = responses[IVAR].apply(lambda x: x == 'Yes')



for question in QUESTIONS:
    
    dvars = GRID_QUESTIONS_TO_COLUMNS[question]    
    dvar_responses = GRID_QUESTIONS_TO_ANSWERS[question]
        
    
    INDEX_LIST = []
    for dvar in dvars:
        INDEX_LIST.extend([dvar, dvar])
    
    GRAPH_INDEX = pd.MultiIndex.from_arrays(
                                    [len(dvars) * [True, False],
                                     INDEX_LIST], 
                                     names = ['ivar', 'dvars'])
    
  
    
    collected_counts = pd.DataFrame(index=dvar_responses, columns=GRAPH_INDEX)        
    
    for column in dvars:            
        collected_counts[True, column] = \
            responses[mask][column].value_counts().fillna(0)
        collected_counts[False, column] = \
            responses[~mask][column].value_counts().fillna(0)
         
      
    collected_counts = collected_counts.T
        
    
    collected_counts = collected_counts.div(collected_counts.sum(1).astype(float), 
                                            axis = 0)      
    collected_counts = collected_counts.reindex(
        index=collected_counts.index[ ::-1 ])

    
    collected_counts.plot(kind='barh',
                          stacked=True, 
                          color=COLORS, 
                          figure=fig,
                          ax=subfigs[i], 
                          grid=False, 
                          legend=False,
                          xlim = (0,1),
                          edgecolor='none') 
          
    # format the subplot
    subfigs[i].tick_params(axis='both', 
                           which='both',
                           left='off',
                           top='off',
                           right='off')
                              
    subfigs[i].set_title(question)
    subfigs[i].spines['right'].set_visible(False)
    subfigs[i].spines['top'].set_visible(False)
    subfigs[i].spines['bottom'].set_color('#5b6f74')
    subfigs[i].spines['left'].set_color('#5b6f74')
                     
    # move to the next subplot
    i += 1                                    

