# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 09:52:32 2014

@author: jkratz
"""
import scipy.stats as sps

execfile("ReadInSurvey.py")

ANSWERS = COLUMN_TO_ANSWERS[dvar]

# CSV of all the pairwise p-values
FILE_TITLE = 'chi2_independence_' + dvar + '.csv'

# extract checkbox column and split responses into array
#split_checkbox = responses[dvar].str.split("; ").dropna()
split_checkbox = responses[dvar].dropna()

# DF of bools; responders x checkbox (checked = True) 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in ANSWERS})

# DF of pairwise p-values
pvalues = pd.DataFrame(index=ANSWERS, columns=ANSWERS)

# DF of all the counts to test for overall significance
total_square = pd.DataFrame(index=[True, False], columns=ANSWERS)

i=0
for a in ANSWERS:
    i +=1    
    
    # fill in T and F counts for this answer 
    total_square[a] = checkbox_responses[a].value_counts()
    
    # separate series 

    for b in ANSWERS[i:]:
        
        # initialize pairwise count table
        square = pd.DataFrame({ 0 : 0, 0 : 0},
                              index=[True, False], 
                              columns=[True, False])        
        
        # fill in counts
        square[True] = (checkbox_responses[checkbox_responses[a]
                        == True][b].value_counts())
        square[False] = (checkbox_responses[checkbox_responses[a] 
                        == False][b].value_counts())

        chi2, p, df, expected = sps.chi2_contingency(square.as_matrix())
        
        pvalues.ix[a,b] = p
       
        if chi2 == chi2:
            print a + " x " + b + ": chi2= " + str(chi2) + ", p= " + str(p)
            print expected
            relationship = square.as_matrix() - expected
            print ("positive correlation" if relationship[0][0] > 0 else 
                   "negative correlation")

t_chi2, t_p, t_df, t_expected = sps.chi2_contingency(total_square.as_matrix())

print "total chi2= " + str(t_chi2) + ", p= " + str(t_p)

pvalues.to_csv(FILE_TITLE)