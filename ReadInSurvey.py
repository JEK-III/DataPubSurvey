# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 11:27:56 2014

@author: jkratz
"""

CONFIDENCE_LEVELS = ["No confidence",
                     "Little confidence",
                     "Some confidence",
                     "High confidence",
                     "Complete confidence"]

DP_FEATURES = ["Openly available without contacting the author(s)",
               "Deposited in a database or repository",
               "Assigned a unique identifier such as a DOI",
               "A traditional research paper is based on the data",
               "A data paper (without conclusions) describes the data",
               "Packaged with a thorough description of the data",
               "Packaged with formal metadata describing the data (e.g. as XML)",
               "Dataset is \"peer reviewed\"",
               "I don't see any difference"]

PR_FEATURES = ['methods_evaluated',
               'good_metadata',
               'standard_metadata',
               'technical_review',
               'scientific_review',
               'impact']

REVIEW_ACTIONS = ["reviewed a journal article",
                  "reviewed a grant proposal",
                  "reviewed an application to graduate school",
                  "reviewed a CV to hire someone for your lab",
                  "served on a hiring committee",
                  "served on a tenure & promotions committee"]


responses = pd.read_csv("DataPubSurveyResponses - Form Responses.csv")


responses = responses[responses['role'] != 'Librarian' ]
responses = responses[responses['highest_degree'] != 'Highschool']
responses = responses[responses['generated_data'] != 'No']

