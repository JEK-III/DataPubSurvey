# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 09:37:28 2014

@author: jkratz
"""

import pandas as pd

#set category
CATEGORY_TYPE = 'institution'

# set of roles to graph
CATEGORIES = ['Academic: research-focused', 
                     'Academic: teaching-focused',
                     'Academic: medical school',
                     'Government',
                     'Nonprofit',
                     'Commercial']


# filter out everyone else
mask = responses['institution'].isin(INSTITUTION_TYPES)
responses_ft = responses.ix[mask]