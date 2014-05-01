# -*- coding: utf-8 -*-
"""
Created on Thu May  1 14:09:50 2014

@author: jkratz
"""
RESPONSE_MERGE = {"Complete confidence" : "High confidence",
               "High confidence" : "High confidence",
               "Some confidence" : "Low confidence",
               "Little confidence" : "Low confidence",
               "No confidence" : "Low confidence"}

GRAPH_INDEX = ["Low confidence", "High confidence"]

COLORS = 'w'

responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

# extract checkbox column and split responses into array
responses_ft[dvar] = responses_ft[dvar].str.split(", ").dropna()

responses_ft['box_counts'] = responses_ft[dvar].apply(lambda x: len(x))



responses_ft[ivar] = responses_ft[ivar].map(RESPONSE_MERGE)


# count dvar responses
response_counts = responses_ft.groupby(ivar).mode()


response_counts = response_counts.reindex(index=GRAPH_INDEX)

response_counts.plot(kind='bar', color=COLORS, ylim=[0,6], legend=None)