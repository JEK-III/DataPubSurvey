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

DISCIPLINE_AGGREGATION = {"-Planetary Science" : "Earth science",
                          "-Geology" : "Earth science",
                          "Computer & Information Sciences" : "Computer science",
                          "Social, Behavioral & Economic Sciences" : "Social science",
                          "-Astronomy" : "Other",
                          "-Oceanography" : "Earth science"}



responses = pd.read_csv("DataPubSurveyResponses - Form Responses.csv")



#responses['discipline'] = responses['discipline'].map(DISCIPLINE_AGGREGATION)



# replace any anwser not in the provided list with 'Other'
def strip_other(cell, column):
    if cell != cell:
        return cell
    else:
        cell = pd.Series(cell)        
        cell[~cell.isin(COLUMN_TO_ANSWERS[column])] = 'Other'
        return cell



# drop unecessary demographic or revealing columns

responses_ft = responses.drop(COLUMNS_TO_DROP, axis=1)


for column in CHECKBOX_COLUMNS:      

    # split into individual answers on ','
    filtered_column = responses_ft[column].str.split(", ").dropna()
    
    # replace free-text with 'Other'    
    filtered_column = filtered_column.map(lambda x : strip_other(x, column))
    
    filtered_column = filtered_column.map(lambda x : '; '.join(x))
    
    responses_ft[column] = filtered_column

 
responses_ft.to_csv('test_output.csv')
# consolidate sparsely populated disciplines