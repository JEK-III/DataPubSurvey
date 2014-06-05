# -*- coding: utf-8 -*-
"""
Created on Tue May 27 11:54:48 2014

@author: kratzscience
"""

IVAR = 'have_shared'

QUESTIONS = ['publish_definition',
             'peer_review_definition']


COLORS = ['#08519c',
          '#6baed6']

TITLE_FONT={'name' : 'Serif',
            'size' : 12}

            
execfile("ReadInSurvey.py")

ivar_column = responses[IVAR].apply(lambda x: x == 'Yes')                
#ivar_column = responses[IVAR]


fig, subfigs = plt.subplots(len(QUESTIONS), sharex=False, sharey=True)
fig.suptitle('Definitions as a function of whether shared', 
             fontsize=14)        

i = 0

for question in QUESTIONS:
    
    dvar = question
    DVAR_RESPONSES = COLUMN_TO_ANSWERS[dvar]
    
    split_dvar_checkbox = responses[dvar].str.split("; ").dropna()
    
    dvar_checkbox_responses = pd.DataFrame({name : 
    split_dvar_checkbox.apply(lambda x: name in x) for name in 
        DVAR_RESPONSES + ['Other']})

    merged_responses = pd.merge(pd.DataFrame(ivar_column), dvar_checkbox_responses,
                      left_index=True, right_index=True)
                      
  
    responses_by_action = pd.DataFrame(merged_responses.groupby(IVAR).sum())

    total_counts = pd.value_counts(merged_responses[IVAR])

    responses_by_action = responses_by_action.reindex(columns=DVAR_RESPONSES)
    
    for answer in responses_by_action.index:
        if answer in total_counts.index:
            responses_by_action.ix[answer] = (
                responses_by_action.ix[answer].apply(lambda x : 
                    x/total_counts[answer]))
        else: 
            total_counts = total_counts.append(pd.Series({answer : 0}))
              

    responses_by_action = responses_by_action.T

    
    #plt.tick
    responses_by_action.plot(kind='bar', 
                             color=COLORS, 
                             figure=fig,
                             ax=subfigs[i], 
                             ylim=(0,1),
                             yticks=[0,0.5,1],
                             grid=False, 
                             legend=False,
                             #title=action,
                             edgecolor='w') 

    subfigs[i].tick_params(axis='both', 
                           which='both',
                           bottom='off',
                           top='off',
                           right='off')
                              
    subfigs[i].set_title(question, fontdict=TITLE_FONT)
    subfigs[i].spines['right'].set_visible(False)
    subfigs[i].spines['top'].set_visible(False)
    subfigs[i].spines['bottom'].set_color('#969696')
    subfigs[i].spines['left'].set_color('#969696')
                    
                        
    n_string = ("n =\n" + str(total_counts[True]) + " have shared\n" + 
        str(total_counts[False]) + " have not shared")
    
    subfigs[i].text(1,0.9,
                    n_string,
                    fontsize=10,
                    horizontalalignment='left',
                    transform=subfigs[i].transAxes)
    
    i += 1



fig.show()
 #   experience_dfs.append(responses_by_action)


#combined_frame = pd.concat(experience_dfs, REVIEW_ACTIONS).T
#combined_frame = combined_frame.reindex(columns=[True, False])




#test_group[True]