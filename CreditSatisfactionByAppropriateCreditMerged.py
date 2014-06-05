# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 09:47:40 2014

@author: jkratz

@author: kratzscience
"""
import scipy.stats as sps

# constant definitions ---------------------------------------------------------
execfile("DefineConstants.py")

GRAPH_TITLE = "Credit satisfaction as a function of appropriate credit"

IVAR = 'data_sharing_credit'
DVARS = ['how_much_credit']

SCORE_AGGREGATE = {1 : 'Insufficient',
                   2 : 'Insufficient',
                   3 : 'Appropriate',
                   4 : 'Excessive',
                   5 : 'Excessive'}


IVAR_RESPONSES = COLUMN_TO_ANSWERS[IVAR]
DVAR_RESPONSES = set(SCORE_AGGREGATE.values())

# build pandas MultiIndex for collected_counts 
# First, whether the researcher checked the IVAR box
# Second, each row from the Leikert grid
INDEX_LIST = []
for i in DVARS:
    INDEX_LIST.extend([i, i])

GRAPH_INDEX = pd.MultiIndex.from_arrays(
                                [len(DVARS) * [True, False],
                                 INDEX_LIST], 
                                 names = ['ivar', 'dvars'])


# Graph formatting -------------------------------------------------------------
"""
COLORS = ['#ffb754',
          '#b5b5b5',
          '#6baed6']
"""
COLORS = ['#b5b5b5']

TITLE_FONT={'name' : 'Helevetica',
            'size' : 12}

# Set up the figure and subfigures
fig, subfigs = plt.subplots(2, 3, sharex=True, sharey=True)
i = j = 0

fig.suptitle(GRAPH_TITLE, fontsize=14)        

# Start ------------------------------------------------------------------------           
execfile("ReadInSurvey.py")




# extract checkbox column and split responses into array
split_ivar_checkbox = responses[IVAR].str.split("; ").dropna()

# combine with the relevant columns from the response DataFrame
merged_responses = pd.merge(pd.DataFrame(split_ivar_checkbox), responses[DVARS],
                            right_index=True, left_index=True)

merged_responses['how_much_credit'] = merged_responses['how_much_credit'].map(SCORE_AGGREGATE)

# ------------------------------------------------------------------------------                    
# Each time through draws one of the subplots

for action in IVAR_RESPONSES:
        
    # create mask of bools depending on whether this action was checked
    mask = merged_responses[IVAR].apply(lambda x: action in x)
    
    # set up empty dataframe to hold the counts            
    collected_counts = pd.DataFrame(index=DVAR_RESPONSES, columns=GRAPH_INDEX)        
    
    # count responses in each Leikert column by action done or not
    for column in DVARS:            
        collected_counts[True, column] = \
            merged_responses[mask][column].value_counts().fillna(0)
        collected_counts[False, column] = \
            merged_responses[~mask][column].value_counts().fillna(0)
        
    collected_counts = collected_counts.transpose() 
    
    #compute chi squared
    print action
    chi2_counts = collected_counts.dropna(axis=1)
    counts_array = np.array([chi2_counts.ix[True, column], 
                             chi2_counts.ix[False, column]])
    print counts_array
    if len(counts_array[0]) > 0 and len(counts_array[1]) > 0:
        print sps.chi2_contingency(counts_array)
    
    # normalize     
    print collected_counts    
    
    collected_counts = \
        collected_counts.div(collected_counts.sum(1).astype(float), axis = 0)
    print collected_counts

    # reverse the order of rows for graphing purposes
    collected_counts = \
        collected_counts.reindex(index=collected_counts.index[ ::-1 ])

    # draw the subplot
    collected_counts.plot(kind='bar',
                          #stacked=True, 
                          color=COLORS, 
                          figure=fig,
                          ax=subfigs[i][j], 
                          grid=False, 
                          legend=False,
                          ylim=(0,1),
                          #title=action,
                          edgecolor='w') 
    
    # format the subplot
    subfigs[i][j].tick_params(axis='both', 
                              which='both',
                              bottom='off',
                              top='off',
                              right='off')
                              
    subfigs[i][j].set_title(action, fontdict=TITLE_FONT)
    subfigs[i][j].spines['right'].set_visible(False)
    subfigs[i][j].spines['top'].set_visible(False)
    subfigs[i][j].spines['bottom'].set_color('#5b6f74')
    subfigs[i][j].spines['left'].set_color('#5b6f74')
                    
    
    # move to the next subplot
    if (i == 0 and j == 2):
        i += 1  
        j = 0
    else:
        j += 1

fig.show()
