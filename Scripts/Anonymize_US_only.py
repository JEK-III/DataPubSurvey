# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 08:38:18 2014

Script to perform light anonymization of DataPub survey data.

Reads in "DataPubSurveyResponses - Form Responses.csv" and
1. drops unused columns that contain free text or demographic information
2. scans checkbox answers for free text (filled in by checking 'Other') and
    replaces with 'Other'.  Replace ',' delimeters with ';'
3. scans radio button answers for or free text (filled in by checking 'Other') 
    and replaces with 'Other'
4. folds discipline answers with >0 and <3 respondents into broader categories
Writes out as 'DataPubSurvey_anon.csv'

@author: jkratz
"""


# source of many necessary constants
execfile('DefineConstants.py')

COLUMNS_TO_DROP = ["can_name_data_journal",
                   "uc_affiliated",
                   "uc_campu",
                   "data_to_publish"]


DISCIPLINE_AGGREGATION = {"Planetary Science" : "Earth science",
                          "Geology" : "Earth science",
                          "Computer & Information Sciences" : 
                              "Computer science",
                          "Social, Behavioral & Economic Sciences" : 
                              "Social science",
                          "Astronomy" : "Other",
                          "Oceanography" : "Earth science"}

# ------------------------------------------------------------------------------
# read in survey data
responses = pd.read_csv("DataPubSurveyResponses - Form Responses.csv")

# drop unecessary demographic or revealing columns
responses_ft = responses.drop(COLUMNS_TO_DROP, axis=1)

# restrict to US
respones_ft = responses_ft[responses_ft.country == "United States"]

# checkboxes -------------------------------------------------------------------
# filter checkbox columns to replace free text with 'Other' and split multiple
# answers with '; '
 
# replace any anwser not in the provided list with 'Other'
def strip_other_checkbox(cell, column):
    cell = pd.Series(cell)        
    cell[~cell.isin(COLUMN_TO_ANSWERS[column])] = 'Other'
    return cell

for column in CHECKBOX_COLUMNS:      
    # split answers on ',' into seires
    filtered_column = responses_ft[column].str.split(", ").dropna()
    
    # replace free-text with 'Other'    
    filtered_column = filtered_column.map(lambda x : 
        strip_other_checkbox(x, column))
    
    # rejoin as string with new delimeter
    filtered_column = filtered_column.map(lambda x : "; ".join(x))
    
    # replace original column
    responses_ft[column] = filtered_column

# radio buttons ----------------------------------------------------------------
# replace free text answers with 'Other'

def strip_other_radio(cell, column):       
    return cell if cell in COLUMN_TO_ANSWERS[column] else 'Other'
    
for column in RADIO_BUTTON_COLUMNS:
    responses_ft[column] = \
        responses_ft[column].map(lambda x: strip_other_radio(x, column))

# discipline -------------------------------------------------------------------

# get rid of annoying dashes
responses_ft['discipline'] = responses_ft['discipline'].str.replace('-', '')

# merge disciplines with < 3 responders into larger classes
 
def merge_disciplines(cell):
    if cell in DISCIPLINE_AGGREGATION.keys():
        cell = DISCIPLINE_AGGREGATION[cell]
    return cell

responses_ft['discipline'] = responses_ft['discipline'].map(merge_disciplines)

responses_ft.to_csv('DataPubSurvey_US_anon.csv')

