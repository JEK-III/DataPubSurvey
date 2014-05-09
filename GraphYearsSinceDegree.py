# -*- coding: utf-8 -*-
"""
Created on Wed May  7 11:10:22 2014

requires previously defined responses_ft with the frame to graph

@author: jkratz
"""

import datetime

degree_dates = responses_ft.degree_year.dropna()
degree_time_elapsed = degree_dates.sub(datetime.date.today().year)
degree_time_elapsed = degree_time_elapsed.apply(lambda x : abs(x))
dte_counts = degree_time_elapsed.value_counts()
dte_counts = dte_counts.sort_index()
dte_counts.plot(kind='bar')