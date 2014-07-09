# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 15:07:14 2014

@author: jkratz
"""
import scipy.stats as sps

execfile("ReadInSurvey.py")

dvar = 'peer_review_definition'
ANSWERS = COLUMN_TO_ANSWERS[dvar]

RESPONSE_MERGE = {"Complete confidence" : "High confidence",
               "High confidence" : "High confidence",
               "Some confidence" : "Low confidence",
               "Little confidence" : "Low confidence",
               "No confidence" : "Low confidence"}

TWO_LEVELS = set(RESPONSE_MERGE.values())
# CSV of all the pairwise p-values
FILE_TITLE = 'chi2_independence_PR_trust_consolidated_and_definition.csv'

# extract checkbox column and split responses into array
#split_checkbox = responses[dvar].str.split("; ").dropna()
split_checkbox = responses[dvar].dropna()

# DF of bools; responders x checkbox (checked = True) 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in ANSWERS})

checkbox_responses =pd.merge(checkbox_responses, 
                             pd.DataFrame(responses.peer_review_confidence.map(RESPONSE_MERGE)),
                             left_index=True,
                             right_index=True,
                             how='outer')

# empty DF of pairwise p-values
#pvalues = pd.DataFrame(index=CONFIDENCE_LEVELS, columns=ANSWERS)

# empty DF of all the counts to test for overall significance
#total_square = pd.DataFrame(index=[True, False], columns=ANSWERS)




for b in ANSWERS:
    
    # initialize pairwise count table
    square = pd.DataFrame(index=[True, False], 
                          columns=TWO_LEVELS)        
    
    # fill in counts
    for c_level in TWO_LEVELS:
        square[c_level] = (checkbox_responses[checkbox_responses.peer_review_confidence
                        == c_level][b].value_counts())

    square.fillna(value=0, inplace=True)
    #chi2, p, df, expected = sps.chi2_contingency(square.as_matrix())
    oddrat, p = sps.fisher_exact(square.as_matrix())
    
    #pvalues.ix[c_level,b] = p
    if oddrat == oddrat:
        print "Peer Review Confidence x " + b + ": odds ration= " + str(oddrat) + ", p= " + str(p)
        #print expected
        #relationship = square.as_matrix() - expected
        #print ("positive correlation" if relationship[0][0] > 0 else 
        #       "negative correlation")

#t_chi2, t_p, t_df, t_expected = sps.chi2_contingency(total_square.as_matrix())

#print "total chi2= " + str(t_chi2) + ", p= " + str(t_p)

#pvalues.to_csv(FILE_TITLE)