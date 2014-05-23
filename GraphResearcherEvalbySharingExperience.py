# -*- coding: utf-8 -*-
"""
Created on Wed May 21 15:34:25 2014

@author: kratzscience
"""
execfile("DefineConstants.py")
GRAPH_TITLE = "Researcher evaluation as a function of sharing experience."

IVAR = 'how_shared'
DVARS = RESEARCHER_VALUE

IVAR_RESPONSES = COLUMN_TO_ANSWERS[IVAR]
DVAR_RESPONSES =RESEARCHER_VALUE_SEQUENCE



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






TITLE_FONT={'name' : 'Helevetica',
            'size' : 12}

INDEX_LIST = []
for i in DVARS:
    INDEX_LIST.extend([i, i])


GRAPH_INDEX = pd.MultiIndex.from_arrays(
                                [len(DVARS) * [True, False],
                                 INDEX_LIST], 
                                 names = ['ivar', 'dvars'])
            
execfile("ReadInSurvey.py")

# extract checkbox column and split responses into array
split_ivar_checkbox = responses[IVAR].str.split("; ").dropna()


# DF of bools; responders x checkbox answers 
ivar_checkbox_responses = pd.DataFrame({name : 
    split_ivar_checkbox.apply(lambda x: name in x) for name in IVAR_RESPONSES}) 

merged_responses = pd.merge(pd.DataFrame(split_ivar_checkbox), responses[DVARS],
                            right_index=True, left_index=True)

# ------------------------------------------------------------------------------                    

fig, subfigs = plt.subplots(2, 3, sharex=True, sharey=True)
i = j = 0

for action in IVAR_RESPONSES:
        
    mask = merged_responses[IVAR].apply(lambda x: action in x)
                
    collected_counts = pd.DataFrame(index=DVAR_RESPONSES, columns=GRAPH_INDEX)        
    
    
    #responses_by_action = pd.DataFrame(merged_responses.groupby(action).sum())
    #total_counts = pd.value_counts(ivar_checkbox_responses[action])
#    responses_by_action = responses_by_action.reindex(columns=DVAR_RESPONSES)
#    responses_by_action = responses_by_action.reindex([True, False])    
    
    #mask = merged_responses.groupby(action in merged_responses[IVAR])
    
    #counts = {}
    for column in DVARS:            
        collected_counts[True, column] = \
            merged_responses[mask][column].value_counts().fillna(0)
        collected_counts[False, column] = \
            merged_responses[~mask][column].value_counts().fillna(0)
    
    collected_counts = collected_counts.transpose() 
     
    #collected_counts[True] = collected_counts[True].div(collected_counts[True].sum(1).astype(float), axis = 0)
    #collected_counts[False] = collected_counts[False].div(collected_counts[False].sum(1).astype(float), axis = 0)
    collected_counts = collected_counts.div(collected_counts.sum(1).astype(float), axis = 0)

            
            
    """
    for answer in [True, False]:
        if answer in total_counts.index:
            responses_by_action.ix[answer] = (
                responses_by_action.ix[answer].apply(lambda x : 
                    x/total_counts[answer]))
        else: 
            total_counts = total_counts.append(pd.Series({answer : 0}))
    """     

    #responses_by_action = responses_by_action.T
    
    #plt.tick
    collected_counts.plot(kind='barh',
                                stacked=True, 
                             color=COLORS, 
                             figure=fig,
                             ax=subfigs[i][j], 
                             grid=False, 
                             legend=False,
                             #title=action,
                             edgecolor='none') 
    subfigs[i][j].tick_params(axis='both', 
                              which='both',
                              bottom='off',
                              top='off',
                              right='off')
                              
    subfigs[i][j].set_title(action, fontdict=TITLE_FONT)
    subfigs[i][j].spines['right'].set_visible(False)
    subfigs[i][j].spines['top'].set_visible(False)
    subfigs[i][j].spines['bottom'].set_color('#5b6f74')
    subfigs[i][j].spines['left'].set_color('#5b6f74')
                    
    """                    
    n_string = ("n =\n" + str(total_counts[True]) + " have done\n" + 
        str(total_counts[False]) + " have not done")
    
    subfigs[i][j].text(1,0.9,
                       n_string,
                       fontsize=10,
                       horizontalalignment='left',
                       transform=subfigs[i][j].transAxes)
    """
    if (i == 0 and j == 2):
        i += 1  
        j = 0
    else:
        j += 1

fig.suptitle(GRAPH_TITLE, fontsize=14)        

fig.show()
 #   experience_dfs.append(responses_by_action)


#combined_frame = pd.concat(experience_dfs, REVIEW_ACTIONS).T
#combined_frame = combined_frame.reindex(columns=[True, False])




#test_group[True]