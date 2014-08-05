# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 14:55:23 2014


@author: jkratz
"""

import math

# Graph formatting -------------------------------------------------------------
COLORS = ['#08519c',
          '#3182bd',
          '#6baed6',
          '#bdd7e7',
          '#eff3ff']
          
GRAPH_TITLE = "Leikert grids."        

QUESTIONS = ['data_trust', 'data_value', 'researcher_value']

VALUE_TO_NUMBER = {"Extremely useful" : 4,
                   "Highly useful" : 3,
                   "Somewhat useful" : 2,
                   "Slightly useful" : 1,
                   "Not at all useful" : 0,
                   "A great deal" : 4,
                   "Significant" : 3,
                   "Some" : 2,
                   "A small amount" : 1,
                   "None" : 0,
                   "Complete confidence" : 4,
                   "High confidence" : 3,
                   "Some confidence" : 2,
                   "Little confidence" : 1,
                   "No confidence" : 0}


# Set up the figure and subfigures
fig, subfigs = plt.subplots(len(QUESTIONS), sharex=True)
i = 0

fig.suptitle(GRAPH_TITLE, fontsize=14)  

execfile("ReadInSurvey.py")


for question in QUESTIONS:
    
    dvars = GRID_QUESTIONS_TO_COLUMNS[question]    
    dvar_responses = GRID_QUESTIONS_TO_ANSWERS[question]

    print '\n' + question    
    
    collected_counts = pd.DataFrame(index=dvar_responses) 
    mean_values = pd.Series(index=dvars)
    sem_values = pd.Series(index=dvars)
    
    for column in dvars:            
        collected_counts[column] =  responses[column].value_counts().fillna(0)
        mean_values[column] = responses[column].map(VALUE_TO_NUMBER).mean()
        sem_values[column] = (responses[column].map(VALUE_TO_NUMBER).std() /
                              math.sqrt(len(responses[column].dropna())))
        print column + " n= " + str(len(responses[column].dropna()))                      

    mean_values = mean_values + 1 #* 25 * 4.2
    sem_values = sem_values #* 25 * 4.2
    print mean_values
    print sem_values
    
    #test = collected_counts     
      
    collected_counts = collected_counts.T
    
    #print collected_counts    
    
    collected_counts = collected_counts.div(collected_counts.sum(1).astype(float), 
                                            axis = 0)      
                                            
    print collected_counts
                                        
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
                          edgecolor='w') 
          
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

