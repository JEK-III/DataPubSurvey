# -*- coding: utf-8 -*-
"""
Created on Wed May 28 11:45:44 2014

@author: jkratz
"""

import datetime

DTE_BINS = [0,2,5,10,20,30,40,50]

degree_dates = \
    responses[responses['highest_degree'] == 'Doctorate'].degree_year.dropna()

degree_time_elapsed =\
     degree_dates.sub(datetime.date.today().year).apply(lambda x : abs(x))

degree_time_elapsed.hist(bins=DTE_BINS)

dte_counts = degree_time_elapsed.value_counts()
dte_counts = dte_counts.sort_index()
#dte_counts.plot(kind='bar')
 
thing, other_thing = np.histogram(degree_time_elapsed, bins=DTE_BINS)
