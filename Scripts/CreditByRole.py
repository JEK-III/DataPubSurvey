# -*- coding: utf-8 -*-
"""
Created on Tue May 27 16:23:47 2014

@author: jkratz

Graph data publication checkbox definitions as a function 
of discipline
@author: jkratz
"""
GRAPH_TITLE = "Sharing credit as a function of role."

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
IVAR = 'role'
DVAR = 'data_sharing_credit'
DVAR_ANSWERS = COLUMN_TO_ANSWERS[DVAR]


GRAPH_INDEX = COLUMN_TO_ANSWERS[IVAR]


execfile("ReadInSurvey.py")

#responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

#responses.discipline = responses.discipline.map(SUBDISCIPLINE_TO_DISCIPLINE)
#mask = responses[CATEGORY_TYPE].isin(CATEGORIES)
#responses_ft = responses.ix[mask]


# extract checkbox column and split responses into array
split_checkbox = responses[DVAR].str.split("; ").dropna()


# DF of bools; responders x checkbox answers 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in DVAR_ANSWERS + ['Other']})

# graft ivar column on
checkbox_responses[IVAR] = responses[IVAR]
checkbox_responses = checkbox_responses.dropna()

# count ivar responses
ivar_counts = checkbox_responses[IVAR].value_counts()
ivar_counts = pd.DataFrame(ivar_counts, columns=[IVAR_LABEL])

# count dvar responses
response_counts = checkbox_responses.groupby(IVAR).sum()

response_counts = pd.merge(response_counts, pd.DataFrame(ivar_counts), 
                           left_index=True, right_index=True)


print response_counts['total_responses']

response_counts = response_counts.apply(lambda x : x.div(x[IVAR_LABEL]),
                                        axis=1)
                                        
            
response_counts = response_counts.sort(columns='total_responses')


# sort for graphing
response_counts = response_counts.reindex(columns=DVAR_ANSWERS + ['Other'])



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