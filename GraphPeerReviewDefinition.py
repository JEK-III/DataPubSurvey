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

IVAR_LABEL = 'total_responses'

#responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

# extract checkbox column and split responses into array
split_checkbox = responses[dvar].str.split(", ").dropna()

# DF of bools; responders x checkbox answers 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in PR_FEATURES})

# graft ivar column on
checkbox_responses[ivar] = responses[ivar]
checkbox_responses = checkbox_responses.dropna()

# count ivar responses
ivar_counts = checkbox_responses[ivar].value_counts()
ivar_counts = pd.DataFrame(ivar_counts, columns=[IVAR_LABEL])

# count dvar responses
response_counts = checkbox_responses.groupby(ivar).sum()

response_counts = pd.merge(response_counts, pd.DataFrame(ivar_counts), 
                           left_index=True, right_index=True)



#response_counts = response_counts + ivar_counts.T

f = lambda x : x.div(x[IVAR_LABEL])

response_counts = response_counts.apply(f, axis=1)


# sort for graphing
response_counts = response_counts.reindex(columns=PR_FEATURES, index = CONFIDENCE_LEVELS)

response_counts.plot(kind='bar')


#split = responses[dvar].str.split(", ")

#responses[dvar] = responses[dvar].str.split(", ")
#split[split in PR_FEATURES] = True





#for column in PR_FEATURES:
#    responses['role'] = responses['role'] == 'Postdoc'

#plan is ultimately to make a pivot table