# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 15:37:17 2014


Graph data publication checkbox definitions as a function 
of discipline
@author: jkratz
"""
import scipy.stats as sps

execfile("ReadInSurvey.py")



COLORS = ['#8dd3c7',
          '#bebada',
          '#ccebc5',
          '#fb8072',
          '#80b1d3',
          '#fdb462',
          '#b3de69',
          '#fccde5',
          '#d9d9d9',
          '#bc80bd']

IVAR_LABEL = 'total_responses'
ivar = 'discipline'
dvar = 'data_sharing_credit'
#FEATURES = COLUMN_TO_ANSWERS[dvar]
FEATURES = ["Authorship on paper",
            "Acknowledgement in the paper",
            "Data cited in the reference list",
            "Data cited informally in the text of the paper"]


GRAPH_INDEX = set(PAPER_DISCIPLINE_MAP.values())






#responses_ft = responses.reindex(columns=[ivar, dvar]).dropna()

responses.discipline = responses.discipline.map(PAPER_DISCIPLINE_MAP)
#mask = responses[CATEGORY_TYPE].isin(CATEGORIES)
#responses_ft = responses.ix[mask]



# extract checkbox column and split responses into array
split_checkbox = responses[dvar].str.split("; ").dropna()


# DF of bools; responders x checkbox answers 
checkbox_responses = pd.DataFrame({name : 
    split_checkbox.apply(lambda x: name in x) for name in FEATURES})

# graft ivar column on
checkbox_responses[ivar] = responses[ivar]
checkbox_responses = checkbox_responses.dropna()

# count ivar responses
ivar_counts = checkbox_responses[ivar].value_counts()
ivar_counts = pd.DataFrame(ivar_counts, columns=[IVAR_LABEL])

# count dvar responses
response_counts = checkbox_responses.groupby(ivar).sum()

response_counts = pd.merge(response_counts, pd.DataFrame(ivar_counts), 
                           left_index=True, right_index=True)



response_counts = response_counts.drop(['Mathematics', 'Other'], axis=0)

print response_counts['total_responses']

rc_array = np.array(response_counts.as_matrix())
chi2, p, df, expected = sps.chi2_contingency(rc_array)

response_counts_raw = response_counts

response_counts = response_counts.apply(lambda x : x.div(x[IVAR_LABEL]),
                                        axis=1)
                                        
            
response_counts = response_counts.sort(columns='total_responses')


# sort for graphing
response_counts = response_counts.reindex(columns=FEATURES)


title_string = "Appropriate data sharing credit by discipline\nchi2= " \
                + str(chi2) + " p=" + str(p)


fig = response_counts.plot(kind='bar', 
                           color=COLORS,
                           grid=False,
                           #legend=False,
                           ylim=(0,1),
                           rot=0,
                           title=title_string,
                           edgecolor='w')

fig.spines['right'].set_visible(False)
fig.spines['top'].set_visible(False)
fig.spines['bottom'].set_color('#c8c8c8')
fig.spines['left'].set_color('#c8c8c8')
                    
fig.tick_params(axis='both', 
                which='both',
                bottom='off',
                top='off',
                right='off')