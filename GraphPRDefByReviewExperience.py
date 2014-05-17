# -*- coding: utf-8 -*-
"""
Created on Fri May 16 11:52:29 2014

@author: kratzscience
"""

ivar = 'researcher_review_experience'
dvar = 'peer_review_definition'


execfile("ReadInSurvey.py")

# extract checkbox column and split responses into array
split_ivar_checkbox = responses[ivar].str.split("; ").dropna()
split_dvar_checkbox = responses[dvar].str.split("; ").dropna()

# DF of bools; responders x checkbox answers 
ivar_checkbox_responses = pd.DataFrame({name : 
    split_ivar_checkbox.apply(lambda x: name in x) for name in REVIEW_ACTIONS}) 

dvar_checkbox_responses = pd.DataFrame({name : 
    split_dvar_checkbox.apply(lambda x: name in x) for name in 
        PR_FEATURES + ['Other']})
        
test_merge = pd.merge(ivar_checkbox_responses, dvar_checkbox_responses,
                      left_index=True, right_index=True)
                      
test_group = test_merge.groupby(REVIEW_ACTIONS).sum()

new_df=pd.DataFrame()

for action in REVIEW_ACTIONS:
    new_df = test_merge.groupby(action).sum()
    print new_df.ix[True]


#test_group[True]