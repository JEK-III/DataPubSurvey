# -*- coding: utf-8 -*-
"""
Created on Thu May  1 10:26:47 2014

Graph checkbox responses.



@author: jkratz
"""
"""
COLORS = ['a6cee3',
          '#1f78b4',
          '#b2df8a',
          '#33a02c',
          '#fb9a99',
          '#e31a1c',
          '#fdbf6f',
          '#ff7f00',
          '#cab2d6',
          '#6a3d9a']
"""
COLORS = 'w'



# extract checkbox column and split responses into array
split_checkbox = responses[dvar].str.split(", ").dropna()

# DF of bools; responders x checkbox (checked = True) 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in REVIEW_ACTIONS})

# count checked boxes 
response_counts = checkbox_responses.sum()

# sort descending for graph
response_counts.sort(ascending=False)

# plot bar graph
response_counts.plot(kind='bar', alpha=1, color=COLORS)
