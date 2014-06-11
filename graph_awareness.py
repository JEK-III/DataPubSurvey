# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 14:59:22 2014

@author: jkratz
"""


# Graph formatting -------------------------------------------------------------
COLORS = ['#08519c',
          '#3182bd',
          '#6baed6',
          '#eff3ff']
          
GRAPH_TITLE = "Familiarity"        

IVAR = 'discipline'
QUESTIONS = ['aware_nsf_dmp', 
             'aware_nih_data_sharing_policy', 
             'aware_ostp_policy']


execfile("ReadInSurvey.py")

responses.discipline = responses.discipline.map(PAPER_DISCIPLINE_MAP)

responses_ft = responses[responses.discipline == 'Biology']

responses_ct = responses_ft.aware_nih_data_sharing_policy.value_counts()

responses_ct = responses_ct.div(responses_ct.sum().astype(float))

responses_ct.plot(kind='barh',
                  stacked=True)



