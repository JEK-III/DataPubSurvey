# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:27:56 2014

Script to read the anonymized survey data in and perform some filtereing:
* filter out self-identified librarians and information scientists
* filter out anyone with out a B.A.
* filter out anyone who reports not generating data


@author: jkratz
"""
import pandas as pd

EXCLUDE = {'role' : 'Librarian',
           'discipline' : 'Information science',
           'highest_degree' : 'Highschool',
           'generated_data' : 'No'}


responses = pd.read_csv('../Tables/DataPubSurvey_anon.csv')

for column, value in EXCLUDE.iteritems():
    responses = responses[responses[column] != value]
