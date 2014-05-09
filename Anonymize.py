# -*- coding: utf-8 -*-
"""
Created on Wed May  7 11:23:12 2014

@author: jkratz
"""

COLUMNS_TO_DROP = ["can_name_data_journal",
                   "country",
                   "uc_affiliated",
                   "uc_campu",
                   "data_to_publish"]

STANDARD_RESPONSES = DP_FEATURES


responses = pd.read_csv("DataPubSurveyResponses - Form Responses.csv")



def strip_other(cell):
    if cell != cell:
        return cell
    else:
        cell = pd.Series(cell)        
        cell[~cell.isin(STANDARD_RESPONSES)] = 'Other'
        return cell



# drop unecessary demographic or revealing columns

responses_ft = responses.drop(COLUMNS_TO_DROP, axis=1)

for column in CHECKBOX_COLUMNS:
    responses_ft[column] = responses_ft[column].str.split(", ")
    responses_ft[column] = responses_ft[column].map(strip_other)
