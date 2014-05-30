# -*- coding: utf-8 -*-
"""
Created on Wed May 28 09:50:20 2014

@author: kratzscience
"""
import scipy.stats as sps

IVAR = 'have_shared'

QUESTIONS = ['publish_definition', 'peer_review_definition']

            
execfile("ReadInSurvey.py")

ivar_column = responses[IVAR].apply(lambda x: x == 'Yes')                


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

    responses_by_action = responses_by_action.T
    
    rba_t = responses_by_action[True]
    rba_f = responses_by_action[False]
    rba_array = np.array([rba_t, rba_f])
    print sps.chi2_contingency(rba_array)
  