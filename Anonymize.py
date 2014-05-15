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


# drop unecessary demographic or revealing columns
responses_ft = responses.drop(COLUMNS_TO_DROP, axis=1)

# checkboxes -------------------------------------------------------------------

# filter checkbox columns to replace free text with 'Other' and split multiple
# answers with '; '
 
# replace any anwser not in the provided list with 'Other'
def strip_other(cell, column):
    cell = pd.Series(cell)        
    cell[~cell.isin(COLUMN_TO_ANSWERS[column])] = 'Other'
    return cell


for column in CHECKBOX_COLUMNS:      
    # split answers on ',' into seires
    filtered_column = responses_ft[column].str.split(", ").dropna()
    
    # replace free-text with 'Other'    
    filtered_column = filtered_column.map(lambda x : strip_other(x, column))
    
    # rejoin as string with new delimeter
    filtered_column = filtered_column.map(lambda x : "; ".join(x))
    
    # replace original column
    responses_ft[column] = filtered_column

# discipline -------------------------------------------------------------------

# merge disciplines with < 3 responders into larger classes
 
def merge_disciplines(cell):
    if cell in DISCIPLINE_AGGREGATION.keys():
        cell = DISCIPLINE_AGGREGATION[cell]
    return cell

responses_ft['discipline'] = responses_ft['discipline'].map(merge_disciplines)

responses_ft.to_csv('test_output.csv')
# consolidate sparsely populated disciplines