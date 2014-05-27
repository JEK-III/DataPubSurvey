# -*- coding: utf-8 -*-
"""
Created on Wed May 21 15:34:25 2014

@author: kratzscience
"""

ivar = 'how_shared'
dvar = 'publish_definition'

IVAR_RESPONSES = COLUMN_TO_ANSWERS[ivar]
DVAR_RESPONSES = COLUMN_TO_ANSWERS[dvar]


COLORS = ['#678bbc',
          '#f8c690']

TITLE_FONT={'name' : 'Helevetica',
            'size' : 12}

            
execfile("ReadInSurvey.py")

# extract checkbox column and split responses into array
split_ivar_checkbox = responses[ivar].str.split("; ").dropna()
split_dvar_checkbox = responses[dvar].str.split("; ").dropna()

# DF of bools; responders x checkbox answers 
ivar_checkbox_responses = pd.DataFrame({name : 
    split_ivar_checkbox.apply(lambda x: name in x) for name in IVAR_RESPONSES}) 

dvar_checkbox_responses = pd.DataFrame({name : 
    split_dvar_checkbox.apply(lambda x: name in x) for name in 
        DVAR_RESPONSES + ['Other']})
        
merged_responses = pd.merge(ivar_checkbox_responses, dvar_checkbox_responses,
                      left_index=True, right_index=True)
                      


fig, subfigs = plt.subplots(2, 3, sharex=True, sharey=True)

i = j = 0

for action in IVAR_RESPONSES:
    responses_by_action = pd.DataFrame(merged_responses.groupby(action).sum())
    total_counts = pd.value_counts(merged_responses[action])
    responses_by_action = responses_by_action.reindex(columns=DVAR_RESPONSES)
#    responses_by_action = responses_by_action.reindex([True, False])    

    for answer in [True, False]:
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
                             ax=subfigs[i][j], 
                             ylim=(0,1),
                             yticks=[0,0.5,1],
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
                    
                        
    n_string = ("n =\n" + str(total_counts[True]) + " have done\n" + 
        str(total_counts[False]) + " have not done")
    
    subfigs[i][j].text(1,0.9,
                       n_string,
                       fontsize=10,
                       horizontalalignment='left',
                       transform=subfigs[i][j].transAxes)
    
    if (i == 0 and j == 2):
        i += 1  
        j = 0
    else:
        j += 1

fig.suptitle('Data publication definition as a function of sharing experience', 
             fontsize=14)        

fig.show()
 #   experience_dfs.append(responses_by_action)


#combined_frame = pd.concat(experience_dfs, REVIEW_ACTIONS).T
#combined_frame = combined_frame.reindex(columns=[True, False])




#test_group[True]