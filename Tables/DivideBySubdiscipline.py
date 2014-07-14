# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 09:37:28 2014

@author: jkratz
"""

import pandas as pd

#set category
CATEGORY_TYPE = 'discipline'

# set of roles to graph
CATEGORIES = ['Social science',
              '-Anthropology',
              '-Archaeology',
              '-Area studies',
              '-Economics',
              '-Political science',
              '-Psychology',
              '-Sociology',
              'Space science',
              '-Astronomy',
              '-Astrophysics',
              'Earth science',
              '-Environmental Science',
              'Geology',
              'Oceanography',
              '-Planetary Science',
              'Life science',
              '-Biochemistry',
              '-Bioinformatics',
              '-Biology',
              '-Evolutionary Biology',
              '-Neurobiology',
              'Chemistry',
              'Physics',
              'Computer science',
              'Mathematics',
              'Information science']
              


# filter out everyone else
mask = responses[CATEGORY_TYPE].isin(CATEGORIES)
responses_ft = responses.ix[mask]