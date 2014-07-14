# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 15:48:11 2014


@author: jkratz
"""
import scipy.stats as sps

execfile("ReadInSurvey.py")

IVAR_ANSWERS = COLUMN_TO_ANSWERS[ivar]
DVAR_ANSWERS = COLUMN_TO_ANSWERS[dvar]

# CSV of all the pairwise p-values
FILE_TITLE = 'fisher_exact_independence_' + dvar + '_by_' + ivar + '.csv'

# extract checkbox column and split responses into array
#split_checkbox = responses[dvar].str.split("; ").dropna()
split_checkbox_ivar = responses[ivar].dropna()
split_checkbox_dvar = responses[dvar].dropna()


# DF of bools; responders x checkbox (checked = True) 
checkbox_responses_ivar = pd.DataFrame({name : 
    split_checkbox_ivar.apply(lambda x: name in x) for name in IVAR_ANSWERS})
checkbox_responses_dvar = pd.DataFrame({name : 
    split_checkbox_dvar.apply(lambda x: name in x) for name in DVAR_ANSWERS})

checkbox_responses = pd.concat([checkbox_responses_ivar, checkbox_responses_dvar], axis=1)


# DF of pairwise p-values
pvalues = pd.DataFrame(index=IVAR_ANSWERS, columns=DVAR_ANSWERS)

# DF of all the counts to test for overall significance
#total_square = pd.DataFrame(index=[True, False], columns=ANSWERS)

for a in IVAR_ANSWERS:
    # fill in T and F counts for this answer 
 #   total_square[a] = checkbox_responses[a].value_counts()
    
    # separate series 

    for b in DVAR_ANSWERS:
        
        # initialize pairwise count table
        square = pd.DataFrame({ 0 : 0, 0 : 0},
                              index=[True, False], 
                              columns=[True, False])        
        
        # fill in counts
        square[True] = (checkbox_responses[checkbox_responses[a]
                        == True][b].value_counts())
        square[False] = (checkbox_responses[checkbox_responses[a] 
                        == False][b].value_counts())

        # check odds ratio and flip columns if it's going to be < 1
        # needed for comparison b/c odds ratio isn't symmetric      
        prelim_oddsratio = ((float(square[True][True]) * square[False][False]) /
                        (square[False][True] * square[True][False]))
        if prelim_oddsratio < 1:
            square = square.reindex(columns=[False,True])
       
        count_table = square.as_matrix()

        if ~numpy.isnan(count_table).any():
            oddsratio, p = sps.fisher_exact(count_table)
            
            pvalues.ix[a,b] = p
           
            print (a + " x " + b + ":\n  odds ratio= " + str(oddsratio) + 
                   ", p= " + str(p))
            print "  positive\n" if prelim_oddsratio == oddsratio \
             else "  negative\n"
            

#t_chi2, t_p, t_df, t_expected = sps.chi2_contingency(total_square.as_matrix())

#print "total chi2= " + str(t_chi2) + ", p= " + str(t_p)

pvalues.to_csv(FILE_TITLE)