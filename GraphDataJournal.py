# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 13:58:28 2014

@author: jkratz
"""
execfile("ReadInSurvey.py")

column = responses['data_journals_named'].str.split(",")

# dict to collect journal names & counts
journal_counts = {}

# populate journal_counts with 'journal name' : # of times mentioned
for cell in column:
    for journal in cell:
      if journal in journal_counts:
        journal_counts[journal] += 1
      else:
        journal_counts[journal] = 1
        
# convert to pandas series for plotting
count_series = pd.Series(journal_counts)

# sort in descending order of mentions
count_series.sort(ascending=False)

# plot
count_series.plot(kind='bar', 
                  color='w',
                  grid=False)

savefig("number_of_data_journal_mentions.svg", format="svg")

