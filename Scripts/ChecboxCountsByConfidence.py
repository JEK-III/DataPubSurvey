# -*- coding: utf-8 -*-
"""
Graph peer review checkbox definitions as a function 
of confidence in a peer-reviewed dataset
@author: jkratz
"""
"""
COLORS = ['#e41a1c',
          '#377eb8',
          '#4daf4a',
          '#984ea3',
          '#ff7f00',
          '#ffff33']
"""
COLORS = 'w'

responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

# extract checkbox column and split responses into array
responses_ft[dvar] = responses_ft[dvar].str.split(", ").dropna()

responses_ft['box_counts'] = responses_ft[dvar].apply(lambda x: len(x))

response_counts = responses_ft.groupby(ivar).mean()

response_counts = response_counts.reindex(index=CONFIDENCE_LEVELS)

response_counts.plot(kind='bar', color=COLORS, ylim=[0,6], legend=None)