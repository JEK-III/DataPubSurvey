#Roadmap
##Introduction
* Data sharing is good, buy we need/ want to move from 'sharing' to 'publishing'
* To do this, it's very, very important to talk to researchers, not just library folks
* a lot of surveys about data sharing have been done, which is great, but...
* no one has asked about publication before now.

* data sharing is good, and we've done a lot of surveys / interviews / needs assessments
* *Tenopir
* *Kim

* the idea in data publication is to borrow terminology ('publication', 'peer review') from the existing publication system and in that way tie in to the existing academic reward system
* Lots of data publication initiatives are steaming ahead
* in particular, lots of new venues for data papers
* however, it's still not clear what 'data publicaiton' means, and 'data peer review' even less so
* if we want to use those words, we'd better figure out what they mean to the real audience: researchers

* therefore we decided to survey researchers directly about:
1. what they think 'data publication' and 'data peer review' mean
2. what potential components of a data publication would they find useful for evaluating the data and its creators


##Methods

###Ethics

* UC Human Subjects IRB approved this survey
* UC respondents had the option of identifying themselves, but that information is omitted here
* Officially open January 22nd - February 28, 2014.  Got 2 responses in March, last one on the 25th
* Distributed by email, social media (twitter, Facebook)
* Open to anyone

###Distribution

* Cover letter with link to survey sent
* *UC campus libraries
* *Librarian Listservs
* Social media
* *twitter
* *Facebook
* Blog post on DataPub

###Survey
* Few required questions
* Some questions presented based on answers to others, therefore n varies considerably from question to question
* Demographics (minimal)
* Data sharing experiences / attitudes / knowledge
* Data publication perceptions
* *expectations from the terms 'data publication' and 'data peer review'
* *value of various possible DP features in various contexts

###Anonymization

* Location converted to US and 'Other'
* UC & campus affiliation redacted
* * knowledge of UC OA mandate redacted
* free text answers standardized
* * data journals converted to standardized list by hand
* * all text boxes associated with 'Other' buttons recoded as 'other', except for a limited number of cases in 'role', where judgement was used to assign the respondent to one of the standard responses
* Sub-disciplines with < 3 respondents were merged into the corresponding discipline

###Filtering for analysis

* Removed anyone who self-identified as a librarian
* Removed information scientists
* Removed anyone who said they hadn't generated any data in the last 5 years
* *90 respondents didn't answer.  too many to discard, so we kept them.
* Removed anyone whose highest degree was from high school
* We filtered out:
* *16 librarians
* *13 information scientists (6 of whom are also librarians)
* *3 without college degrees
* *11 who hadn't generated any data (2 librarians, 1 info scientist)
* *sometimes the same person was filtered by multiple criteria

##Analysis

* Chi-squared was used for all significance testing
* Consider questions where no answer was marked as skipped, rather than an intentional 'none of these' answer


##Results

###Demographics
* In demographics table
* 281 unique responses   
* 249 (89%) passed filters 
* Largest response from biologists: (37%), followed by Archaeologists (13%), Social scientists (13%), and Environmental scientists (11%)
* Responses from across the career spectrum: 41% principle investigator/lab heads, 24% postdocs, and 16% grad students.
* Overwhelmingly, biggest response (85%) from academic institutions, 90% of those are research-focused.

###Background knowledge
* attempted to gauge familiarity with issues around data publication/sharing/access
* 


####Policies
* In policy awareness figure
* we asked respondents to rate their familiarity with 3 US federal policies related to data sharing/availability
* b/c policies are specific to US, we only report the results from the 197 (79%) of respondents who are in the US
* United States Office of Science and Technology Policy (OSTP) Open Data Initiative \cite{obama_making_2013}
* *not yet relevant to scientists, but will eventually impact everyone
* *less than half 75 (38%) have heard of it at all
* NSF DMP requirements \cite{national_science_foundation_gpg_2011}
* *the most well-known of the bunch
* *32 (16%) knew all the details
* NIH data sharing policy \cite{national_institutes_of_health_final_2003}
* *only looked at biologists (n=71)
* *only 4 (5%) claimed to "know all the details", much fewer than the 18 (24%) who had never heard of it
* *this even though the policy was enacted 11 years ago


####Data journals
* No figure
* most frequently named: ecological archive (16), Nature's Scientific Data (14)
* then, ESSD (7), Biodiversity Data Journal (6), Geoscience Data Journal (5)
* 29% (39) of respondents who answered the question in some way named at least one data journal
* 16% (39) of all respondents named a data journal
* a number of respondents listed or asked about repositories: figshare (6), dryad (3), zenodo (1)


###Sharing background
* In Sharing Experience figure
* asked about prior experience with sharing own data and using others
* some background attitudes about sharing

###Channels
* we asked three questions about mechanisms for sharing
* *Have you shared data in any of the following ways?
* *[If] your data [has] been re-used by anyone outside your research group / collaborators, how did they get your data?
* *[If] you ever re-used data from another research group (not as part of an existing collaboration), how did you get the data?
* respondents were instructed to check all answers that applied
* provided answers were equivalent to the 4 methods for external data sharing found by Kim (2012) \cite{kim_institutional_2012} in interviews with faculty:
* *Email / direct contact
* *database or repository
* *journal website (as supplemental material)
* *personal or lab website


###Credit
* we wanted to asses what researchers thought was appropriate credit for the creators of a dataset
* the most common response was formal citation in the reference list at 83% (126)
* acknowledgement also ranked highly at 62% (93)
* the most common actual practice <CITATION>, informal reference in the body of the paper, ranked lowest at 16% (24)
	
* we provided an 'Other' option with a free-text field.  
* Overwhelmingly, some variant on "it depends"
* many specified one of two factors:
* *the role of the data in the paper
* **"depends on the amount of data shared and the importance to the study-if just some support in discussion, acknowledgement; vs. half or more of main study, authorship."
* **"authorship if data is primary source of analysis, otherwise acknowledgement"
* **"depends how central the data is to the resulting paper"
* *the publication status of the dataset
* **"Depends on whether the data is already published"
* **"Data should be archived at publication of its first use. After that it can be acknowledged or cited if used in the future."

* because there are substantial differences in culture between disciplines \cite{harley_assessing_2010, swan_share_2008} we examined them separately
* biology and the physical sciences had a relatively high expectation of authorship at 53% (48) and 50% (9) respectively
* surprisingly, discounting Mathematics (b/c of low n) and Other (b/c meaningless), a chi2 test did not find significant differences between disciplines
* *chi2=15.6, p=0.9

* we also asked the subset who had published on someone else's data what they actually did
* results agreed rougly with the responses to the hypothetical
* formal citation rated highest with 63% (81)
* no one admitted to informal citation in the text



###Data vultures
* In credit figure
* 'data vultures' / being taken advantage of is a concern in data publication 
* we wanted to know how much of a problem it currently is
* we asked respondents whose data had been reused in a publication by someone else "how did you feel about the amount of credit you were given?"

* 86 answered the question
* a majority 63% (54) thought they got the right amount of credit
* 78% (67)thought they got sufficient or too much credit
* 22% (19) were unhappy, 2% (2) got 'very insufficient' credit

* belief that formal citation is appropriate credit was associated with more satisfaction 
* *32% (6) insufficient/very insufficient and 5% (1) excessive/very excessive vs.
* *19% (13) insufficient/very insufficient and %18 (12) excessive
* *not significant, chi2 = 2.56, p = 0.28

* belief that authorship is appropriate credit was associated with more dissatisfaction
* *16% (9) insufficient/very insufficient and 15% (8) excessive/very excessive vs.
* *32% (10) insufficient/very insufficient and 16% (5) excessive/very excessive
* *not significant, chi2 = 3.26, p = 0.20



###Definitions

####Data Publication
* in definitions figure
* two most common expectations relate to access & preservation
* *availability at 166 / 68%
* *repository at 133 / 54%
* traditional paper (105 / 43%) more expected than data paper (55 / 22%)
* thorough metadata (97 / 39%) outranks formal metadata (62 / 25%)
* most researchers *don't* expect publication to imply peer review (only 70 / 29%)


####Peer review
* in definitions figure
* Evaluation of metadata ranks highly (196 / 80%)
* *researchers recognize it's importance
* *more respondents expected metadata evaluation from peer review than good metadata from publication (what's that mean?)
* a majority (150 / 62%) expect an evaluation of plausibility that requires domain expertise
* collection and processing methods (220 / 90%) presumably also demand some domain expertise
* low expectation that impact will be considered (53 / 22%)


###Values

####Data trust
* in values figure
* part of the rationale for data publication is to make reuse of data easier
* we wanted to know what features of a data publication would be useful to researchers in deciding whether to trust a dataset

* easily the biggest factor was peer review
* *175 / 72% said complete or high confidence
* *only 4 / 2% said little or no confidence

* traditional paper was second with 137 / 56% complete or high confidence
* reuse in 3rd, with 106 / 43% 
* finally, data paper was the least convincing with 89 / 37%

* all of the features inspired at least some confidence in a large majority of researchers
* *the largest fraction of little/no confidence was reuse, at 25 / 10%

* no strong relationship between peer review definition and peer review confidence


####Data value/impact
* in values figure
* we wanted to know what dataset metrics researchers would value

* citations, not surprisingly, was the winner
* *119 / 49% extremely or highly useful

* downloads did surprisingly well relative to citations
* *77 / 32% extremely or highly useful
* if somewhat useful is added in, downloads gets even closer to citations 179 (73%) vs. 201 (82%)

* There was a substantial drop for search rank and altmetrics
* *102 (42%) find search rank at least somewhat useful
* *91 (37%) find altmetrics at least somewhat useful 
* * furthermore, a majority of researchers find each to be slightly or not at all useful

####Researcher evaluation
* in values figure
* part of the rationale for data publication is to incentivize data sharing by fitting data into the academic reward system
* to that end, we wanted to know what features of a data publication would increase its value as an item on a CV
* we considered the imprimatur of peer review and the inclusion of a data paper 

* to establish a baseline, we asked about traditional papers
* *not surprisingly, they are highly valued
* *145 (60%) give it a great deal of weight and another 87 (36%) give it significant weight
* we have a lot of biologists, who value peer reviewed publications above all else \cite{harley_assessing_2010}

* data publications were much less highly valued at 23 (10%) a great deal for highest scorer, a peer-reviewed data paper, although 109 (46%) still gave that significant weight.

* peer review appeared to be the more important feature
* *from that 10%, a peer-reviewed dataset only dropped to 5% (12), while an un-peer-reviewed data paper dropped to 0.01% (2)
* *if significant weight is added in, a peer reviewed data paper comes in at 134 (56%), a peer reviewed dataset at 85 (36%), and an un-reviewed data paper at 31 (12%)
* not surprisingly, a significant number of respondents 65 (27%) gave un-peer reviewed data no weight at all.

* we were particularly interested in the 26% (59) respondents who had served on a tenure and promotions committee.
* their responses were similar to those who had not served on such a committee
* we compared the set of values assigned to each item between those who had and had not served on a t&p committee by chi-square
* values ranged from 
* *chi2= 7.427 (p= 0.115) for peer-reviewed datasets (valued slightly less by experienced respondents) to 
* *chi2= 2.097 (p= 0.351) for traditional papers (valued slightly more by experienced respondents)
* for 5 items, alpha=0.01, none can be considered statistically significant


##Discussion


###Our demographics vs. previous surveys
* Tenopir (2011) \cite{tenopir_data_2011}
* *81% academic vs. our 85% is quite similar
* *most heavily environmental sciences & ecology (36%), followed by social science (16%) and biology (14%)
* *we're heavy in biology (37%), but with a significant representation from Earth and environmental science (16%) and social science (13%).

* Others have found significant differences in data sharing / scholarly communication culture between disciplines
* Tenopir (2011) \cite{tenopir_data_2011} asked what conditions/credit would be fair in exchange for use of data (you using others and others using yours)
* found statistically significant differences between disciplines for every condition
* we didn't, which might be a function of the lower n or different test (we lumped everything together, they considered each column separately)

* comparison between Tenopir results and ours; authorship is the only truly parallel condition
>Is each of the following conditions a fair exchange for the use of data? 
>Co-authorship on publications resulting from use of the data
> >61% (105) biolgists
> >53% (104) social scientists
> >52% (59) computer science/engineering
> >55% (84) physical sciences
>we asked: How should a researcher who shares data be credited?
>authorship on the paper
> >53% (48) biolgists
> >31% (10) social science
> >27% (3) computer science
> >50% (9) physical science
* pretty good agreement among biologists, physical science.  our #s are lower for social & computer science
* *could be change over time or question, but probably it's just the smaller n

 


###Sharing channels
* likely to be distorted by, e.g. the fact that a researcher always knows when someone gets their data though email, might not know about it if it's downloaded from a repository

###Credit/citation
* there is consensus in the scholarly communication community that the right thing to do is to cite formally in the reference list \cite{force11_data_citation_synthesis_group_joint_2014}
* however, past studies have found that this is rarely actually done
* *\cite{sieber_not_1995}: [old, somewhat complicated table of locations to parse]
* here, most respondents agreed that formal citation is the way to go
* furthermore, none of them would admit to informally citing data in the body of the paper
* there was good agreement between the hypothetical and the reported actual behavior
* *obviously, self-reported behavior comes with caveats
* *e.g. very likely that a bio researcher using a GenBank sequence won't view that as data reuse
* suggests that what we need to do is enable data citation, not make the case in the first place


###Data vultures 
* although the majority of respondents were satisfied, the fraction who were not (22%) is too large to ignore
* In kim (2012) study, 32% (8/25) researchers "Worried about data theft; cannot trust others" /cite{kim_institutional_2012}
* no judgement implied about whether researcher expectations are reasonable or not
* could potentially address by some combination of encouraging people to credit more and expect less
* maybe disciplines will work it out for themselves


###Validation

####Peer review
* both the biggest factor in evaluating the trustworthiness of a dataset and the value on a CV
* peer review is valued, but not expected (71% don't think publish implies peer review)
* a majority of researchers expect peer review to involve assessments that require domain expertise
* low expectation that impact would be considered fits with the practices of current DP efforts
* *"I wouldn't expect metadata to be standardized, but I would like it if it were!"
* data publication initiatives should probably incorporate some form of peer review if they can

* "I have never heard this term applied to a dataset and I don't know what it means"


####Use as review
* Successful reuse was rated relatively low, to our surprise
* basis of a traditional paper did a little better.  not reuse, but use.


###Data papers
* the majority of respondents (84%) did not name any data journals
* data papers confer less trust than any other feature we looked at, but everything except peer review is pretty comparable.
* data papers are valued vastly less than traditional papers
* data papers do clearly add value to a dataset on a CV, but peer-reviewed datasets without papers do quite well
* our results don't really resolve the question of whether data papers are a good use of one's time
* the idea of data papers is to fit into the existing scholarly reward system; they don't seem to fit all that much better than datasets
* the hope/presumption/trend is that data is getting more recognition->  the gap might shrink.  on the other hand, no one thinks data papers *should* be considered as valuable as research papers, so perhaps this is all fine


###Metrics
* citations are, not surprisingly, the most valued
* however, downloads do well and are much easier for a data publisher to implement
* *if you're publishing data, you should provide download statistics
* altmetrics still have a ways to go
* *"why would I care about any of that?"
* *while few give them much weight, a majority do give them at least a little



#Tables & Figures

##Demographics
* Discipline, role, highest degree, and institution-type
* analyzed responses from 249 researchers
* Most common: Biologist, PI, PhD, research-focused academic

##Policy Awareness
* Respondents were asked to rate their familiarity with three US government policies related to data sharing
* *scale from "never heard of it" to "know all the details"
* Analysis restricted to US respondents
* (A) OSTP Open Data Initiative (n=197)
* (B) NSF DMP requirements (n=197)
* (C) NIH data sharing policy: only relevant to biologists (n=71)

##Sharing Experience
* restricted to respondents who answered "yes" "to "have you shared data?"
* (A) - (C) are concerned with channels for sharing data
* *Email / direct contact
* *database or repository
* *journal website (as supplemental material)
* *personal or lab website
* (A) Through what channels have you shared data? (n=122)
* (B) If your data has been reused by someone else, how did they get it?
* (C) If you have reused someone else's data, how did you get it? (n=150)
* (D) looks at accompanying documentation (n=121)
* *A traditional research paper based on the data (with analysis and conclusions)
* *A data paper describing the data (without analysis or conclusions)
* *Informal text describing the data
* *Formal metadata describing the data (e.g. as XML)
* *Computer code used to process or generate the data
* *Shared with no additional documentation

##Credit
* (A, B) mechanisms for credit
* *Authorship on paper
* *Acknowledgement in the paper
* *Data cited in the reference list
* *Data cited informally in the text of the paper
* (A) theoretical: how data sharer should be credited (n=151)
* (B) concrete: how the respondent credited others (n=129)
* (C) how satisfied they were with the credit they got (n=86)
* *scale of 1-5 from very insufficient to very excessive
* *mean = 2.9, SE = 0.8

##Definitions
* data publication (vs. sharing) and peer review

##Values
* data trust, data value, data publication value


#Scrap
* at 22% peer review is low on the list (6/8) of expected publication features, but it's highly valued

* people who haven't reviewed a journal article value journal articles less and everything else more than people who have
* *nothing significant at p = 0.01

* Scaramozzino (2012) \cite{scaramozzino_study_2012} survey of 131 tenure-track faculty at a teaching-oriented university (Cal Poly)
>Over 65 percent of respondents believe it is important that they openly share their data and that their colleagues do the same. Of those who be- lieve it is important, fewer than half (48%) report always or frequently sharing data with those outside their research group.

*Kim (2012) \cite{kim_insitutional_2012} interviewed 25 researchers about data sharing.
* *15 of them mentioned credit/reputation as a benefit.
* *methods mentioned: on request/email, personal website, external repository, supplemental material

* Differences in actual and reported behavior: Ceci (1988) surveyed 57 "nonacademic scientists working in both the private and the public sectors at places like the Centers for Disease Control, the National Insitutes of Health, and various research hospitals" and found that 87% reported routinely honoring requests for data, but "59% claimed that their colleagues were not prone to sharing their data, even when they were obtained with the benefit of federal funds." \cite{ceci_scientists_1988}