# -*- coding: utf-8 -*-
"""
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

IVAR_LABEL = 'total_responses'


#responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

# extract checkbox column and split responses into array
split_checkbox = responses[dvar].str.split("; ").dropna()


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


response_counts = response_counts.apply(lambda x : x.div(x[IVAR_LABEL]),
                                        axis=1)


# sort for graphing
response_counts = response_counts.reindex(columns=PR_FEATURES, 
                                          index = GRAPH_INDEX)

response_counts.plot(kind='bar', color=COLORS)
