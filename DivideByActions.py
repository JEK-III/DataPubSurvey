# -*- coding: utf-8 -*-
"""
Created on Thu May  1 11:50:33 2014

Graph peer review checkbox definitions as a function 
of confidence in a peer-reviewed dataset
@author: jkratz
"""

COLORS = ['#e41a1c',
          '#377eb8',
          '#4daf4a',
          '#984ea3',
          '#ff7f00',
          '#ffff33']




#responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

# extract checkbox column and split responses into array
split_checkbox = responses[ivar].str.split(", ").dropna()



# DF of bools; responders x checkbox answers 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in REVIEW_ACTIONS})

# graft ivar column on
checkbox_responses[dvar] = responses[dvar]
checkbox_responses = checkbox_responses.dropna()

# count ivar responses
ivar_counts = checkbox_responses[dvar].value_counts()
ivar_counts = pd.DataFrame(dvar_counts, columns=[IVAR_LABEL])

# count dvar responses
response_counts = checkbox_responses.groupby(dvar).sum()

response_counts = pd.merge(response_counts, pd.DataFrame(ivar_counts), 
                           left_index=True, right_index=True)



#response_counts = response_counts + ivar_counts.T


response_counts = response_counts.apply(lambda x : x.div(x[IVAR_LABEL]),
                                        axis=1)


# sort for graphing
response_counts = response_counts.reindex(columns=PR_FEATURES, 
                                          index = CONFIDENCE_LEVELS)

response_counts.plot(kind='bar', color=COLORS)
