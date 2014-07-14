# -*- coding: utf-8 -*-
"""
Created on Tue May 27 13:13:28 2014

@author: jkratz
"""
def is_answer_yes (answer):
    return answer == 'Yes'

share_mask = responses['have_shared'].apply(is_answer_yes)                
reuse_mask = responses['others_reused_data'].apply(is_answer_yes)
publish_mask = responses['others_published'].apply(is_answer_yes)