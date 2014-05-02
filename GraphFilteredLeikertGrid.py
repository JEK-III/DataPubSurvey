# -*- coding: utf-8 -*-
"""
Created on Thu May  1 15:35:12 2014

@author: jkratz
"""

COLORS = ["#000000", "#404040", "#808080", "#C0C0C0", "#FFFFFF"]

      
FEATURES = RESEARCHER_VALUE
VALUES = RESEARCHER_VALUE_SEQUENCE

FILTER = "served on a tenure & promotions committee"

#build output filename
output_filename = 'data_value.svg'

responses_ft = responses.reindex(columns=([ivar] + FEATURES))

responses_ft[ivar] = responses_ft[ivar].str.split(", ").dropna()

checks = pd.DataFrame(responses_ft[ivar])

checkbox_responses = pd.DataFrame({name : 
    checks.apply(lambda x: name in x) for name in REVIEW_ACTIONS})


"""
responses_ft = responses_ft.mask(responses_ft[FILTER in responses_ft[ivar]])

mask = responses_ft['role'].isin(CATEGORIES)
responses_ft = responses.ix[mask]
"""


counts = {}
for column in FEATURES:
  counts[column] = responses_ft[column].value_counts()
  
response_ct = pd.DataFrame(counts)

response_ct = response_ct.transpose()


#print response_ct


#crosstab to summarize responses from each role
#category_ct = pd.crosstab(responses_ft['reuse_confidence'])

#print category_ct

#normalize by row to % of total responses
response_ct = response_ct.div(response_ct.sum(1).astype(float), axis = 0)
#put rows in order for graph
response_ct = response_ct.reindex(columns=VALUES)
#response_ct = response_ct.reindex(DATA_TRUST)
print response_ct

response_ct = response_ct.sort(columns=VALUES, ascending=True)

#print response_ct
#drop empty rows
#category_ct = category_ct.dropna()

#plot result
response_ct.plot(kind='barh', stacked=True, alpha=1.0, color=COLORS)
#savefig(output_filename, format="svg")