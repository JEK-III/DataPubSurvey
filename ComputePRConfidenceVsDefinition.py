# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 12:35:42 2014

@author: jkratz
"""
import scipy.stats as sps

execfile("ReadInSurvey.py")

dvar = 'peer_review_definition'
ANSWERS = COLUMN_TO_ANSWERS[dvar]

# CSV of all the pairwise p-values
FILE_TITLE = 'chi2_independence_PR_trust_and_definition.csv'

# extract checkbox column and split responses into array
split_checkbox = responses[dvar].str.split("; ").dropna()

# DF of bools; responders x checkbox (checked = True) 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in ANSWERS})

checkbox_responses =pd.merge(checkbox_responses, 
                             pd.DataFrame(responses.peer_review_confidence),
                             left_index=True,
                             right_index=True,
                             how='outer')

# empty DF of pairwise p-values
pvalues = pd.DataFrame(index=CONFIDENCE_LEVELS, columns=ANSWERS)

# empty DF of all the counts to test for overall significance
#total_square = pd.DataFrame(index=[True, False], columns=ANSWERS)




for b in ANSWERS:
    
    # initialize pairwise count table
    square = pd.DataFrame(index=[True, False], 
                          columns=CONFIDENCE_LEVELS)        
    
    # fill in counts
    for c_level in CONFIDENCE_LEVELS:
        square[c_level] = (checkbox_responses[checkbox_responses.peer_review_confidence
                        == c_level][b].value_counts())

    square.fillna(value=0, inplace=True)
    chi2, p, df, expected = sps.chi2_contingency(square.as_matrix())
    
    
    pvalues.ix[c_level,b] = p
    if chi2 == chi2:
        print "Peer Review Confidence x " + b + ": chi2= " + str(chi2) + ", p= " + str(p)
        print expected
        #relationship = square.as_matrix() - expected
        #print ("positive correlation" if relationship[0][0] > 0 else 
        #       "negative correlation")

#t_chi2, t_p, t_df, t_expected = sps.chi2_contingency(total_square.as_matrix())

#print "total chi2= " + str(t_chi2) + ", p= " + str(t_p)

pvalues.to_csv(FILE_TITLE)