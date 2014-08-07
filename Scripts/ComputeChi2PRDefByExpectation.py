# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 10:25:29 2014

This script compares definitions of peer review (by chi2) between respondents
who expect data publication to include it and those who don't.

@author: kratzscience
"""
import scipy.stats as sps

IVAR_COL = 'publish_definition'
IVAR = 'Dataset is "peer reviewed"'

DVAR = 'peer_review_definition'

            
execfile("ReadInSurvey.py")

ivar_column = responses[IVAR_COL].dropna().apply(lambda x: IVAR in x)                

DVAR_RESPONSES = COLUMN_TO_ANSWERS[DVAR]

split_dvar_checkbox = responses[DVAR].dropna()

dvar_checkbox_responses = pd.DataFrame({name : 
    split_dvar_checkbox.apply(lambda x: name in x) for name in 
       DVAR_RESPONSES})

merged_responses = pd.merge(pd.DataFrame(ivar_column), dvar_checkbox_responses,
                  left_index=True, right_index=True)
                  
responses_by_action = pd.DataFrame(merged_responses.groupby(IVAR_COL).sum())

total_counts = pd.value_counts(merged_responses[IVAR_COL])

responses_by_action = responses_by_action.reindex(columns=DVAR_RESPONSES)         

responses_by_action = responses_by_action.T
    
rba_t = responses_by_action[True]
rba_f = responses_by_action[False]
rba_array = np.array([rba_t, rba_f])
print sps.chi2_contingency(rba_array)
  