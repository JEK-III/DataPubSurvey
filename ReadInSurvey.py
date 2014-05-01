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


DATA_TRUST = ['traditional_paper_confidence',
              'data_paper_confidence',
              'peer_review_confidence',
              'reuse_confidence']
              
DATA_TRUST_SEQUENCE = ["Complete confidence",
                       "High confidence",
                       "Some confidence",
                       "Little confidence",
                       "No confidence"]

DATA_VALUE = ["impact_citation",
              "impact_downloads",
              "impact_altmetrics",
              "impact_google_rank"]                                        

DATA_VALUE_SEQUENCE = ["Extremely useful",
                       "Highly useful",
                       "Somewhat useful",
                       "Slightly useful",
                       "Not at all useful"]

RESEARCHER_VALUE = ["traditional_paper_value",
                    "data_paper_pr_value",
                    "data_paper_npr_value",
                    "dataset_pr_value",
                    "dataset_npr_value"]       

RESEARCHER_VALUE_SEQUENCE = ["A great deal",
                             "Significant",
                             "Some",
                             "A small amount",
                             "None"]

responses = pd.read_csv("DataPubSurveyResponses - Form Responses.csv")


responses = responses[responses['role'] != 'Librarian' ]
responses = responses[responses['highest_degree'] != 'Highschool']
responses = responses[responses['generated_data'] != 'No']

