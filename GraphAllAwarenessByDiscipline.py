# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 15:48:56 2014


@author: jkratz
"""
import scipy.stats as sps


# Graph formatting -------------------------------------------------------------
COLORS = ['#08519c',
          '#3182bd',
          '#6baed6',
          '#eff3ff']
          
GRAPH_TITLE = "Familiarity by discipline"        

IVAR = 'discipline'
QUESTIONS = ['aware_nsf_dmp', 
             'aware_nih_data_sharing_policy', 
             'aware_ostp_policy']

SORT_ORDER = ["Other",
              "Mathematics",
              "Computer science",
              "Earth science",
              "Physical science",
              "Environmental science",
              "Social science",
              "Archaeology",
              "Biology",
              "Physcial science"]

# Set up the figure and subfigures
fig, subfigs = plt.subplots(len(QUESTIONS), sharex=True)
i = 0

fig.suptitle(GRAPH_TITLE, fontsize=14)  

execfile("ReadInSurvey.py")
responses.discipline = responses.discipline.map(PAPER_DISCIPLINE_MAP)


for dvar in QUESTIONS:
    
    dvar_responses = COLUMN_TO_ANSWERS[dvar]


    #crosstab to summarize responses from each role
    category_ct = pd.crosstab(responses.discipline, responses[dvar])

    #compute chi squared
    chi = "N/A"
    p = "N/A"    
    
    print dvar
    chi2_counts = category_ct.dropna(axis=1)
    counts_matrix = category_ct.as_matrix()    
    
    print counts_matrix
    chi, p, dof, expected_counts = sps.chi2_contingency(counts_matrix)
    #normalize by row to % of total responses
    category_ct = category_ct.div(category_ct.sum(1).astype(float), axis = 0)

    #put rows in order for graph
    category_ct = category_ct.reindex(columns=COLUMN_TO_ANSWERS[dvar])
    category_ct = category_ct.reindex(SORT_ORDER)    
    
    #drop empty rows
    category_ct = category_ct.dropna()
    
   
    
    
    category_ct.plot(kind='barh',
                          stacked=True, 
                          color=COLORS, 
                          figure=fig,
                          ax=subfigs[i], 
                          grid=False, 
                          legend=False,
                          xlim = (0,1),
                          edgecolor='w') 
          
    # format the subplot
    subfigs[i].tick_params(axis='both', 
                           which='both',
                           left='off',
                           top='off',
                           right='off')
    
    title = dvar + " (chi2= " + str(chi) + ", p= " + str(p) + ')'                         
    subfigs[i].set_title(title)
    subfigs[i].spines['right'].set_visible(False)
    subfigs[i].spines['top'].set_visible(False)
    subfigs[i].spines['bottom'].set_color('#5b6f74')
    subfigs[i].spines['left'].set_color('#5b6f74')
    
    # test significance
                     
    # move to the next subplot
    i += 1                                    

