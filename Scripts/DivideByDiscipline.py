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
              'Earth science',
              'Life science',
              'Chemistry',
              'Physics',
              'Computer science',
              'Mathematics',
              'Information science']
              
# map subdisciplines to disciplines
sub_to_discipline = {'-Anthropology' : 'Social science',
                   '-Archaeology' : 'Social science',
                   '-Area studies' : 'Social science',
                   '-Economics' : 'Social science',
                   '-Political science' : 'Social science',
                   '-Sociology' : 'Social science',
                   '-Astronomy' : 'Space science',
                   '-Astrophysics' : 'Space science',
                   '-Environmental science' : 'Earth science',
                   '-Geology' : 'Earth science',
                   '-Oceanography' : 'Earth science',
                   '-Planetary science' : 'Earth science',
                   '-Biochemistry' : 'Life science',
                   '-Bioinformatics' : 'Life science',
                   '-Biology' : 'Life science',
                   '-Evolutionary Biology' : 'Life science',
                   '-Neurobiology' : 'Life science',
                   'Social science' : 'Social science',
                   'Space science' : 'Space science',
                   'Earth science' : 'Earth science',
                   'Life science' : 'Life science',
                   'Chemistry' : 'Chemistry',
                   'Physics' : 'Physics',
                   'Computer science' : 'Computer science',
                   'Mathematics' : 'Mathematics',
                   'Information science' : 'Information science'}




# filter out everyone else
responses[CATEGORY_TYPE] = responses[CATEGORY_TYPE].map(sub_to_discipline)
mask = responses[CATEGORY_TYPE].isin(CATEGORIES)
responses_ft = responses.ix[mask]