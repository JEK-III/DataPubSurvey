# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:27:56 2014

Script to read the anonymized survey data in and perform some filtereing

@author: jkratz
"""

execfile("DefineConstants.py")

responses = pd.read_csv('DataPubSurvey_anon.csv')

responses = responses[responses['role'] != 'Librarian' ]
responses = responses[responses['discipline'] != "Information science"]
responses = responses[responses['highest_degree'] != 'Highschool']
responses = responses[responses['generated_data'] != 'No']

for column in CHECKBOX_COLUMNS:
    responses[column] = responses[column].str.split("; ")
