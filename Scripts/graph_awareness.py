# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 14:59:22 2014

@author: jkratz
"""
import math

# Graph formatting -------------------------------------------------------------
COLORS = ['#08519c',
          '#3182bd',
          '#6baed6',
          '#eff3ff']
          
GRAPH_TITLE = "Familiarity"        

#IVAR = 'discipline'
QUESTIONS = ['aware_nsf_dmp', 
             'aware_nih_data_sharing_policy', 
             'aware_ostp_policy']

VALUE_TO_NUMBER = {"Know all the details" : 3,
                   "Read about it" : 2,
                   "Heard of it" : 1,
                   "Never heard of it" : 0}

execfile("ReadInSurvey.py")
responses.discipline = responses.discipline.map(PAPER_DISCIPLINE_MAP)
output = {}

for question in QUESTIONS:
    responses_ft = pd.DataFrame()    
    
    if question != 'aware_nih_data_sharing_policy':
        responses_ft = responses
    else:
        responses_ft = responses[responses.discipline == 'Biology']
    
    responses_ft = responses_ft[responses_ft.united_states]
    
    responses_ct = responses_ft[question].value_counts()
    output[question] = responses_ct
    
    print '\n' + question + "\n\nCOUNT"
    print responses_ct
    print "n= " + str(responses_ct.sum())
    print "mean= " + str(responses_ft[question].map(VALUE_TO_NUMBER).mean())
    print "SEM= " + str(responses_ft[question].map(VALUE_TO_NUMBER).std() /
                        math.sqrt(len(responses_ft[question].dropna())))
    
    
    responses_ct = responses_ct.div(responses_ct.sum().astype(float))
    print "\nPERCENT"    
    print responses_ct


output_df = pd.DataFrame(output).T

output_df.to_csv("Policy_awareness.csv")

"""
responses_ct.plot(kind='barh',
                  stacked=True,
                  xlim=(0,1))
"""


