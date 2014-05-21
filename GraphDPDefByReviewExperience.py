# -*- coding: utf-8 -*-
"""
Created on Wed May 21 10:35:06 2014

@author: kratzscience
"""

ivar = 'researcher_review_experience'
dvar = 'publish_definition'

COLORS = ['#8dd3c7',
          '#ffffb3']

execfile("ReadInSurvey.py")

# extract checkbox column and split responses into array
split_ivar_checkbox = responses[ivar].str.split("; ").dropna()
split_dvar_checkbox = responses[dvar].str.split("; ").dropna()

# DF of bools; responders x checkbox answers 
ivar_checkbox_responses = pd.DataFrame({name : 
    split_ivar_checkbox.apply(lambda x: name in x) for name in REVIEW_ACTIONS}) 

dvar_checkbox_responses = pd.DataFrame({name : 
    split_dvar_checkbox.apply(lambda x: name in x) for name in 
        DP_FEATURES + ['Other']})
        
merged_responses = pd.merge(ivar_checkbox_responses, dvar_checkbox_responses,
                      left_index=True, right_index=True)
                      
#test_group = test_merge.groupby(REVIEW_ACTIONS).sum()

#new_df=pd.DataFrame()

experience_dfs = []

for action in REVIEW_ACTIONS:
    responses_by_action = pd.DataFrame(merged_responses.groupby(action).sum())
    total_counts = pd.value_counts(merged_responses[action])
    test_df = new_df    
    responses_by_action = responses_by_action.reindex(columns=DP_FEATURES)
    
    responses_by_action.ix[True] = responses_by_action.ix[True].apply(lambda x : x/total_counts[True])
    responses_by_action.ix[False] = responses_by_action.ix[False].apply(lambda x : x/total_counts[False])
   
    experience_dfs.append(responses_by_action)


combined_frame = pd.concat(experience_dfs, REVIEW_ACTIONS).T
combined_frame = combined_frame.reindex(columns=[True, False])

fig, subfigs = plt.subplots(2, 3, sharex=True, sharey=True)


combined_frame.plot(kind='bar', color=COLORS, figure=fig, axes=subfigs[1][1])

#test_group[True]