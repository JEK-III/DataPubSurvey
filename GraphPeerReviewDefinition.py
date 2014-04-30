# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 14:22:59 2014

@author: jkratz
"""
from collections import Counter

PR_FEATURES = ['methods_evaluated',
               'good_metadata',
               'standard_metadata',
               'technical_review',
               'scientific_review',
               'impact']



#responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

split_checkbox = responses[dvar].str.split(", ").dropna()

checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in PR_FEATURES})

checkbox_responses[ivar] = responses[ivar]

checkbox_responses = checkbox_responses.dropna()

ivar_counts = checkbox_responses[ivar].value_counts()

response_counts = checkbox_responses.groupby(ivar).sum()

response_pct = response_counts.div(ivar_counts)

response_pct.plot(kind='bar')


#split = responses[dvar].str.split(", ")

#responses[dvar] = responses[dvar].str.split(", ")
#split[split in PR_FEATURES] = True





#for column in PR_FEATURES:
#    responses['role'] = responses['role'] == 'Postdoc'

#plan is ultimately to make a pivot table