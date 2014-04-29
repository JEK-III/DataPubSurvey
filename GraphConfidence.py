# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 21:44:03 2014

@author: kratzscience
"""
import pandas as pd

#set category flag
#CATEGORY_TYPE = 'role'

# set of roles to graph
#COLUMNS = ['Tech', 'Grad_student', 'Postdoc', 'PI']
COLORS = ["#000000", "#404040", "#808080", "#C0C0C0", "#FFFFFF"]

# filter out everyone else
mask = responses['role'].isin(CATEGORIES)
responses_ft = responses.ix[mask]




#crosstab to summarize responses from each role
role_ct = pd.crosstab(responses_ft.role, responses_ft['data_sharing_importance'])

#normalize by row to % of total responses
role_ct = role_ct.div(role_ct.sum(1).astype(float), axis = 0)

#put rows in order for graph
role_ct = role_ct.reindex([RESEARCH_ROLES])
#plot result
role_ct.plot(kind='bar', stacked=True, alpha=1.0, color=COLORS)
savefig("roleImportance.svg", format="svg")