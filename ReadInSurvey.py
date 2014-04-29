# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:27:56 2014

@author: jkratz
"""

responses = pd.read_csv("DataPubSurveyResponses - Form Responses.csv")


responses = responses[responses['role'] != 'Librarian' ]
responses = responses[responses['highest_degree'] != 'Highschool']
responses = responses[responses['generated_data'] != 'No']
