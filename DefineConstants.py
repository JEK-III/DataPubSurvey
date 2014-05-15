# -*- coding: utf-8 -*-
"""
Created on Wed May  7 16:19:13 2014

@author: jkratz
"""

# lists of columns --------------------------------

COLUMNS_TO_DROP = ["can_name_data_journal",
                   "country",
                   "uc_affiliated",
                   "uc_campu",
                   "data_to_publish"]


CHECKBOX_COLUMNS = ['data_sharing_credit',
                    'how_shared',
                    'how_documented',
                    'how_others_got',
                    'how_you_got',
                    'how_you_credited',
                    'publish_definition',
                    'peer_review_definition',
                    'researcher_review_experience']
                    
RADIO_BUTTON_COLUMNS = ['institution',
                        'role']

# Leikert responses -------------------------------
                    
CONFIDENCE_LEVELS = ["No confidence",
                     "Little confidence",
                     "Some confidence",
                     "High confidence",
                     "Complete confidence"]

DATA_VALUE_SEQUENCE = ["Extremely useful",
                       "Highly useful",
                       "Somewhat useful",
                       "Slightly useful",
                       "Not at all useful"]


RESEARCHER_VALUE_SEQUENCE = ["A great deal",
                             "Significant",
                             "Some",
                             "A small amount",
                             "None"]
                             
DATA_TRUST_SEQUENCE = ["Complete confidence",
                       "High confidence",
                       "Some confidence",
                       "Little confidence",
                       "No confidence"]
# Checkbox answers --------------------------------                       
DP_FEATURES = ["Openly available without contacting the author(s)",
               "Deposited in a database or repository",
               "Assigned a unique identifier such as a DOI",
               "A traditional research paper is based on the data",
               "A data paper (without conclusions) describes the data",
               "Packaged with a thorough description of the data",
               "Packaged with formal metadata describing the data (e.g. as XML)",
               "Dataset is \"peer reviewed\"",
               "I don't see any difference"]

PR_FEATURES = ["Collection and processing methods were evaluated",
               "Descriptive text is thorough enough to use or replicate the dataset",
               "Necessary metadata is standardized (e.g. in XML)",
               "Technical details have been checked (e.g. no missing files no missing values)",
               "Plausibility considered based on area expertise",
               "Novelty/impact considered"]

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
              

DATA_VALUE = ["impact_citation",
              "impact_downloads",
              "impact_altmetrics",
              "impact_google_rank"]                                        


RESEARCHER_VALUE = ["traditional_paper_value",
                    "data_paper_pr_value",
                    "data_paper_npr_value",
                    "dataset_pr_value",
                    "dataset_npr_value"]       


DATA_SHARING_CREDIT_ANSWERS = ["Authorship on paper",
                               "Acknowledgement in the paper",
                               "Data cited in the reference list",
                               "Data cited informally in the text of the paper",
                               "Not credited",
                               "Not applicable"]
                               
HOW_SHARED_ANSWERS = ["Email / direct contact",
                      "Personal or lab website",
                      "Journal website (as supplemental material)",
                      "Database or repository",
                      "Don’t know",
                      "Not applicable"]
                      
HOW_DOCUMENTED_ANSWERS = ["A traditional research paper based on the data (with analysis and conclusions)",
                          "A data paper describing the data (without analysis or conclusions)",
                          "Informal text describing the data",
                          "Formal metadata describing the data (e.g. as XML)",
                          "Computer code used to process or generate the data",
                          "Shared with no additional documentation"]
                  
HOW_YOU_GOT_ANSWERS = ["Email / direct contact",
                       "Personal or lab website",
                       "Journal website (as supplemental material)",
                        "Database or repository",
                        "Don't know"]

HOW_OTHERS_GOT_ANSWERS = ["Email / direct contact",
                          "Personal or lab website",
                          "Journal website (as supplemental material)",
                          "Database or repository",
                          "Don't know"]
                          
HOW_CREDITED_ANSWERS = ["Authorship on paper",
                        "Acknowledgement in the paper",
                        "Data cited in the reference list",
                        "Data cited informally in the  text of the paper",
                        "Not credited",
                        "Not applicable"]

INSTITUTION_ANSWERS = ["Academic: research-focused",
                       "Academic: teaching-focused",
                       "Academic: medical school",
                       "Government",
                       "Nonprofit",
                       "Commercial"]


ROLES_ANSWERS = ['PI',
                 'Postdoc',
                 'Graduate_student',
                 'Tech',
                 'Librarian']

COLUMN_TO_ANSWERS = {'data_sharing_credit' : DATA_SHARING_CREDIT_ANSWERS,
                     'how_shared' : HOW_SHARED_ANSWERS,
                     'how_documented' : HOW_DOCUMENTED_ANSWERS,
                     'how_others_got' : HOW_OTHERS_GOT_ANSWERS,
                     'how_you_got' : HOW_YOU_GOT_ANSWERS,
                     'how_you_credited' : HOW_CREDITED_ANSWERS,
                     'publish_definition' : DP_FEATURES,
                     'peer_review_definition' : PR_FEATURES,
                     'researcher_review_experience' : REVIEW_ACTIONS,
                     'institution' : INSTITUTION_ANSWERS,
                     'role' : ROLES_ANSWERS}
                     