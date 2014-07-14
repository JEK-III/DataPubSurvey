# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 10:51:03 2014

@author: jkratz
"""

# source of many necessary constants
execfile('DefineConstants.py')

# ------------------------------------------------------------------------------
# read in survey data
responses_ft = pd.read_csv("DataPubSurveyResponses - Form Responses.csv")

free_text_responses = pd.DataFrame()
pd.set_printoptions(max_colwidth=1000)

# checkboxes -------------------------------------------------------------------

# replace any anwser not in the provided list with 'Other'
def print_other_checkbox(cell, column):
    cell = pd.Series(cell)
    free_text = cell[~cell.isin(COLUMN_TO_ANSWERS[column])]
    if len(free_text) > 0:
        print "-------------------------\n"        
        print free_text.to_string()

for column in CHECKBOX_COLUMNS:      
    print column + " ++++++++++++++++++++++++++++++++++"
    # split answers on ',' into seires
    filtered_column = responses_ft[column].str.split(", ").dropna()
    
    # replace free-text with 'Other'    
    filtered_column.map(lambda x : print_other_checkbox(x, column))
    


# radio buttons ----------------------------------------------------------------
# replace free text answers with 'Other'

def print_other_radio(cell, column):       
    if ~(cell in COLUMN_TO_ANSWERS[column]):
        print cell
    return cell if cell in COLUMN_TO_ANSWERS[column] else 'Other'
    
for column in RADIO_BUTTON_COLUMNS:
    print column
    responses_ft[column].map(lambda x: print_other_radio(x, column))
