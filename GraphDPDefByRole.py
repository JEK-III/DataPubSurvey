# -*- coding: utf-8 -*-
"""
Created on Fri May 16 08:48:58 2014

Graph data publication checkbox definitions as a function 
of role
@author: jkratz
"""

COLORS = ['#8dd3c7',
          '#bebada',
          '#ccebc5',
          '#fb8072',
          '#80b1d3',
          '#fdb462',
          '#b3de69',
          '#fccde5',
          '#d9d9d9',
          '#bc80bd']

IVAR_LABEL = 'total_responses'
ivar = 'role'
dvar = 'publish_definition'


GRAPH_INDEX = ['PI',
               'Postdoc',
               'Grad_student',
               'Tech',
               'Other']
GRAPH_TITLE = "Data publication definition as a function of role."

execfile("ReadInSurvey.py")

#responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

# extract checkbox column and split responses into array
split_checkbox = responses[dvar].str.split("; ").dropna()


# DF of bools; responders x checkbox answers 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in DP_FEATURES + ['Other']})

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

print response_counts['total_responses']


response_counts = response_counts.apply(lambda x : x.div(x[IVAR_LABEL]),
                                        axis=1)


# sort for graphing
response_counts = response_counts.reindex(columns=DP_FEATURES + ['Other'],                                      
                                          index=GRAPH_INDEX)

fig = response_counts.plot(kind='bar', 
                           color=COLORS,
                           grid=False,
                           #legend=False,
                           ylim=(0,1),
                           rot=0,
                           title=GRAPH_TITLE,
                           edgecolor='w')

fig.spines['right'].set_visible(False)
fig.spines['top'].set_visible(False)
fig.spines['bottom'].set_color('#c8c8c8')
fig.spines['left'].set_color('#c8c8c8')
                    
fig.tick_params(axis='both', 
                which='both',
                bottom='off',
                top='off',
                right='off')
