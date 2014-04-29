# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 17:58:46 2014

@author: jkratz
"""

import pandas as pd

#set category flag
CATEGORY_TYPE = 'role'

# set of roles to graph
CATEGORIES = ['Tech', 'Grad_student', 'Postdoc', 'PI']
COLORS = ["#000000", "#404040", "#808080", "#C0C0C0", "#FFFFFF"]

# filter out everyone else
mask = responses['role'].isin(CATEGORIES)
responses_ft = responses.ix[mask]

