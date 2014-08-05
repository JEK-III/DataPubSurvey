# -*- coding: utf-8 -*-
"""
Created on Wed May 28 15:55:18 2014

@author: jkratz

"""


QUESTIONS = ['publish_definition', 
             'peer_review_definition', 
             'researcher_review_experience']


BAR_COLOR = ['#005695']

TITLE_FONT={'name' : 'Serif',
            'size' : 12}

            
execfile("ReadInSurvey.py")


fig, subfigs = plt.subplots(len(QUESTIONS), sharex=True)
fig.suptitle('Definitions', 
             fontsize=14)        

i = 0

for question in QUESTIONS:
    
    #split_checkbox = responses[question].str.split("; ").dropna()
    split_checkbox = responses[question].dropna()

    # DF of bools; responders x checkbox (checked = True) 
    checkbox_responses = pd.DataFrame({name : 
        split_checkbox.apply(lambda x: name in x) \
            for name in COLUMN_TO_ANSWERS[question]})
    
    # count checked boxes 
    response_counts = checkbox_responses.sum()
    
    # sort descending for graph
    response_counts.sort(ascending=True)
    print response_counts
    
    # normalize
    n = len(checkbox_responses)    
    response_counts = response_counts.apply(lambda x: float(x) / n)    
    
    print "n= " + str(n)
    print response_counts    
    
    #plt.tick
    ax = response_counts.plot(kind='barh', 
                              color=BAR_COLOR, 
                              figure=fig,
                              ax=subfigs[i], 
                              xlim=(0,1),
                              xticks=[0,0.5,1],
                              grid=False, 
                              legend=False,
                              edgecolor='w')
                         
    for container in ax.containers:
        plt.setp(container, height=1)

    subfigs[i].tick_params(axis='both', 
                           which='both',
                           bottom='off',
                           top='off',
                           right='off',
                           left='off')
                              
    subfigs[i].set_title(question, fontdict=TITLE_FONT)
    subfigs[i].spines['right'].set_visible(False)
    subfigs[i].spines['top'].set_visible(False)
    subfigs[i].spines['bottom'].set_color('#969696')
    subfigs[i].spines['left'].set_color('#969696')
                 
                        
    """
    subfigs[i].text(1,0.9,
                    n_string,
                    fontsize=10,
                    horizontalalignment='left',
                    transform=subfigs[i].transAxes)
    """
    i += 1



fig.show()
 #   experience_dfs.append(responses_by_action)


#combined_frame = pd.concat(experience_dfs, REVIEW_ACTIONS).T
#combined_frame = combined_frame.reindex(columns=[True, False])




#test_group[True]