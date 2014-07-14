# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 16:26:53 2014


@author: jkratz
"""
import scipy.stats as sps

execfile("ReadInSurvey.py")

#DVARS = ['data_sharing_credit', 'how_you_credited']

ANSWERS = COLUMN_TO_ANSWERS['data_sharing_credit']
ANSWERS = ANSWERS[0:4]


checkbox_responses_theory = pd.DataFrame({name : 
    responses.data_sharing_credit.apply(lambda x: name in x) for name in ANSWERS})
theory_counts = np.array(checkbox_responses_theory.sum())


checkbox_responses_practice = pd.DataFrame({name : 
    responses[responses.reused_others_data == 'Yes'].how_you_credited.dropna().apply(lambda 
    x: name in x) for name in ANSWERS})
practice_counts = np.array(checkbox_responses_practice.sum())


total_counts = np.matrix([theory_counts,
                          practice_counts])

print total_counts
print sps.chi2_contingency(total_counts)



