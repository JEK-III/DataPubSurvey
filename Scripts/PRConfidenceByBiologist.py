# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 12:15:22 2014

This script compares value attached to peer review (by chi2) between biologists
and everyone else.

@author: kratzscience
"""
import scipy.stats as sps

IVAR_COL = 'discipline'
IVAR = 'Biology'

DVAR = 'peer_review_confidence'

            
execfile("ReadInSurvey.py")

frame = responses[[IVAR_COL, DVAR]]

frame[IVAR_COL] = frame[IVAR_COL].dropna().apply(lambda x: x == IVAR)                


frame_xtab = pd.crosstab(frame[IVAR_COL], frame[DVAR])


print sps.chi2_contingency(frame_xtab.as_matrix())
  