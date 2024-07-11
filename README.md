## WSA Exam Project
We decided to focus on the debate between Pro-Trump supporters and Anti-Trump citizens during the
first three years of Donald Trump’s presidency about two sociopolitical topics, i.e., gun control and minorities discrimination. Indeed, the political rise of Donald Trump has further exacerbated the divide between Republicans and Democrats, making the debate even more polarized.
The main objective of this study is to explore how these topics, generally associated with liberal and left-wing ideologies, are influenced by anti-Trump narratives in social media debates.
We built our approach upon Reddit, which make quite easy to identify online debates about a wide range of different issues thanks to its structure divided into subreddits, searching for topic-related communities. This platform is particularly active in controversial discussions.

In order to infer users' ideology on the topics, we first trained a text classifier using a ground truth of polarized posts with respect to Pro-Trump and Anti-Trump beliefs, collected from various subreddits.
Then, we applied the model to the topics data, and built a users' debate network for each topic basing on the predictions. Thus, we develop our analysis, carrying out detailed statistical analyses and applying community detection techniques, to the point of identifying so-called 'echo chambers', subsets of the network nodes (users) who share the same ideology and tend to have dense connections primarily within the same group, amplifying ideas.

We applied Named Entity Recognition (NER) techniques and sentiment analysis to delve into the nature of the discourses and emotions expressed in the comments, providing an additional layer of understanding of the context and dynamics of the debates.

