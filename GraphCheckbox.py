# -*- coding: utf-8 -*-
"""
Created on Thu May  1 10:26:47 2014

Graph checkbox responses to a single question.

@author: jkratz
"""

ANSWERS = COLUMN_TO_ANSWERS[dvar]

responses_ft = responses[responses.reused_others_data == 'Yes']


# extract checkbox column and split responses into array
#split_checkbox = responses_ft[dvar].str.split("; ").dropna()

# DF of bools; responders x checkbox (checked = True) 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in ANSWERS})

# count checked boxes 
response_counts = checkbox_responses.sum()



print response_counts

response_counts = response_counts.apply(lambda x: 
                                        float(x) / len(checkbox_responses))
print response_counts

# sort descending for graph
response_counts.sort(ascending=True)

title_string = dvar + " (n=" + str(len(checkbox_responses)) + ')'

# plot bar graph
response_counts.plot(kind='barh', 
                     alpha=1, 
                     color='b',
                     grid=False,
                     title=title_string,
                     xlim=(0,1))
