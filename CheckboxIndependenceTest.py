# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 09:52:32 2014

@author: jkratz
"""
import scipy.stats as sps
execfile("ReadInSurvey.py")
execfile("DefineConstants.py")
ANSWERS = COLUMN_TO_ANSWERS[dvar]


# extract checkbox column and split responses into array
split_checkbox = responses[dvar].str.split("; ").dropna()

# DF of bools; responders x checkbox (checked = True) 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in ANSWERS})

# count checked boxes 
response_counts = checkbox_responses.sum()

file_title = 'chi2_independence_' + dvar + '.csv'
pvalues = pd.DataFrame(index=ANSWERS, columns=ANSWERS)


i=0
for a in ANSWERS:
    i +=1    

    a_t = checkbox_responses[checkbox_responses[a] == True]
    a_f = checkbox_responses[checkbox_responses[a] == False]

    for b in ANSWERS[i:]:
        square = pd.DataFrame(index=[True, False], columns=[True, False])
        square[True] = a_t[b].value_counts()
        square[False] = a_f[b].value_counts()

        chi2, p, df, expected = sps.chi2_contingency(square.as_matrix())
        
        pvalues.ix[a,b] = p
       
        if chi2 == chi2:
            print a + " x " + b + ": chi2= " + str(chi2) + " p= " + str(p)
            print expected
            relationship = square.as_matrix() - expected
            print relationship[0][0]

pvalues.to_csv(file_title)