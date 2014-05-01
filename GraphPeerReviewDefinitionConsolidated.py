# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 17:32:26 2014

Graph peer review checkbox definitions 

Group confidence into high
@author: jkratz
"""
from collections import Counter

PR_FEATURES = ['methods_evaluated',
               'good_metadata',
               'standard_metadata',
               'technical_review',
               'scientific_review',
               'impact']


COLORS = ['#e41a1c',
          '#377eb8',
          '#4daf4a',
          '#984ea3',
          '#ff7f00',
          '#ffff33']

IVAR_LABEL = 'total_responses'

RESPONSE_MERGE = {"Complete confidence" : "Peer review",
               "High confidence" : "Peer review",
               "Some confidence" : "Peer review",
               "Little confidence" : "Peer review",
               "No confidence" : "Peer review"}

GRAPH_INDEX = ["Peer review"]
            

#responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

# extract checkbox column and split responses into array
split_checkbox = responses[dvar].str.split(", ").dropna()

# DF of bools; responders x checkbox answers 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in PR_FEATURES})

# graft ivar column on
checkbox_responses[ivar] = responses[ivar]
checkbox_responses = checkbox_responses.dropna()

# merge ivar responses
checkbox_responses[ivar] = checkbox_responses[ivar].map(RESPONSE_MERGE)

# count ivar responses
ivar_counts = checkbox_responses[ivar].value_counts()
ivar_counts = pd.DataFrame(ivar_counts, columns=[IVAR_LABEL])

# count dvar responses
response_counts = checkbox_responses.groupby(ivar).sum()

response_counts = pd.merge(response_counts, pd.DataFrame(ivar_counts), 
                           left_index=True, right_index=True)




response_counts = response_counts.apply(lambda x : x.div(x[IVAR_LABEL]),
                                        axis=1)


# sort for graphing
response_counts = response_counts.reindex(columns=PR_FEATURES, 
                                          index = GRAPH_INDEX)

response_counts.plot(kind='bar', color=COLORS)
