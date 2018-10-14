# Machine Learning Engineer Nanodegree
## Capstone Proposal
George Vargas
Date TBD

## Proposal

### Domain Background

Accurately predicting the financial markets has long been the holy grail for all types of investors. Many individual investors seek this grail but never find it. This tends to be because many underestimate the extreme complexity of the financial markets. Though many fail some individual investors do attain moderate success implementing trading systems that work for the highly-focused conditions in which they find themselevs trading.  Likewise some hedgefunds, such as Renaissance Technologies, achieve great success building complexing trading systems based on standard and alternative data whilst utilizing much more scientific methods for decision making.[[1]]((https://www.linkedin.com/pulse/20141117150538-17004994-pure-alpha-story-of-renaissance-technologies/))

Approaching the problem as a hedgefund might it can be found that the success rate of any particular trade can be significantly increased by considering the system as components all feeding a decision engine, much like neurons in a neural network feed the output layer. While these systems are made of many complex components there has been increasing focus on alternative data and it's use in sentiment analysis components. News, blog and twitter posts data mining has been proven to increase the probability of a successful trade.[[2]](https://arxiv.org/pdf/1010.3003.pdf)[[3]](http://cs229.stanford.edu/proj2015/029_report.pdf).

My personal motivation for looking at possible solutions to this task is purely for my own financial independence. As a hobbyist day trader I've been somewhat profitable but my time is limited because of my full-time employment. Having the ability to create a trading system with the ability to trade as I do but not have the time limitations that I have would be an extremely valuable step toward achieveing financial independence.

### Problem Statement
_(approx. 1 paragraph)_

In this section, clearly describe the problem that is to be solved. The problem described should be well defined and should have at least one relevant potential solution. Additionally, describe the problem thoroughly such that it is clear that the problem is quantifiable (the problem can be expressed in mathematical or logical terms) , measurable (the problem can be measured by some metric and clearly observed), and replicable (the problem can be reproduced and occurs more than once).

The problem with financial markets is that they are largely driven by sentiment. Even in a time when a majority of the trades are being placed by sophicated bots sentiment still rules the market. This can be seen by the effect Trump's tweets have on the stock of the particular companies he targets. Deriving these sentiments from text sources and using them to reliably predict market movements will be the problem this capstone attempts to solve.

### Datasets and Inputs

The datasets used are from Kaggle, specifically [these datasets](https://www.kaggle.com/aaron7sun/stocknews#Combined_News_DJIA.csv) provided by a user in the community. The datasets span approximately eight years from August 2008 to July 2016. Contained is a dataset of the Dow Jones Industrial Average price history with columns including Date, Open, High, Low, Close, Volume and Adj Close; A dataset of Reddit news and a combined dataset with a Dow Jones Industrial Average label and a column each for one of the top twenty-five user upvoted headlines for that day. The label has a value of either "1" for DJIA closing up and "0" for DJIA closing down. The provider of the dataset recommends using data from 2008-08-08 to 2014-12-31 for training and data from 2015-01-02 to 2016-07-01 for testing since this splits the overall dataset in an eighty-twenty fashion. 

For our purposes we will exclude the data up to April 2009. The reason for excluding this data in training, validation and testing is because leading up to April 2009 the market was in a strong downward trend that was a direct result of the housing market crash. Aside from training, validating and tetsing for correlation between news sentiment and the DJIA closing up or down we will be reserving the data up to April 2009 as an additional test to see if the model can generalize from being trained in only a bull market to succeeding in a predominantly bear market.

### Solution Statement
_(approx. 1 paragraph)_

In this section, clearly describe a solution to the problem. The solution should be applicable to the project domain and appropriate for the dataset(s) or input(s) given. Additionally, describe the solution thoroughly such that it is clear that the solution is quantifiable (the solution can be expressed in mathematical or logical terms) , measurable (the solution can be measured by some metric and clearly observed), and replicable (the solution can be reproduced and occurs more than once).

In this capstone we will attempt to predict whether the Dow Jones Indistrial Average will close up or close down based on sentiment analysis performed on the news headlines of that day. We will be using word embeddings to prepare our text data to be fed to a supervised model. Our prediction value will be the label from the combined dataset denoting the upward or downward movement of the DJIA for that particular day.

### Benchmark Model
_(approximately 1-2 paragraphs)_

In this section, provide the details for a benchmark model or result that relates to the domain, problem statement, and intended solution. Ideally, the benchmark model or result contextualizes existing methods or known information in the domain and problem given, which could then be objectively compared to the solution. Describe how the benchmark model or result is measurable (can be measured by some metric and clearly observed) with thorough detail.

Although anecdotal most individual investors will cite roughly a fifty to fifty-five percent accuracy when trading. This is mainly gathered from watching students in trading programs or from discussions with other individual investors. Anecdotal information isn't necessarily considered reliable, however, this researcher is inclined to believe such claims as most trading programs require students to methodically write down every trade(entry, exit, stoploss, etc.) before placing a trade. This is done to develop discipline and help remove emotion from the trades which is one of the most important factors for becoming a successful individual investor.

Now, fifty to fifty-five may seem like slim margins but keep in mind that with just a fifty-one percent win percentage and proper risk management card counters can effectively clean house at casino. Also considering that the data spans a period of time where the market was particularly bullish we will be using the [sklearn.dummy.DummyClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html) in an effort to benchmark against the multiple simple strategies provide by the dummy classifier. This will help figure out if the bullish bias in the data can be exploited via simpler means.

### Evaluation Metrics
_(approx. 1-2 paragraphs)_

In this section, propose at least one evaluation metric that can be used to quantify the performance of both the benchmark model and the solution model. The evaluation metric(s) you propose should be appropriate given the context of the data, the problem statement, and the intended solution. Describe how the evaluation metric(s) are derived and provide an example of their mathematical representations (if applicable). Complex evaluation metrics should be clearly defined and quantifiable (can be expressed in mathematical or logical terms).

### Project Design
_(approx. 1 page)_

In this final section, summarize a theoretical workflow for approaching a solution given the problem. Provide thorough discussion for what strategies you may consider employing, what analysis of the data might be required before being used, or which algorithms will be considered for your implementation. The workflow and discussion that you provide should align with the qualities of the previous sections. Additionally, you are encouraged to include small visualizations, pseudocode, or diagrams to aid in describing the project design, but it is not required. The discussion should clearly outline your intended workflow of the capstone project.

In an attempt to predict the direction of the DJIA we will first take the top twenty-five user upvoted headlines and convert the words to vectors utilizing the [fastText pyhton library](https://github.com/facebookresearch/fastText) created by the facebook research team. The reason for utilizing this library over word2vec or gLoVe is that fastText creates word embeddings from character n-grams instead of words. This creates a much more specific representation for each word and also allows us to construct vectors that are outside of the corpus which may come in useful when generalizing against the portions of the dataset that are held out for validation, testing and generalization.

Once the headlines have been converted into vectors we will implemen

-----------

**Before submitting your proposal, ask yourself. . .**

- Does the proposal you have written follow a well-organized structure similar to that of the project template?
- Is each section (particularly **Solution Statement** and **Project Design**) written in a clear, concise and specific fashion? Are there any ambiguous terms or phrases that need clarification?
- Would the intended audience of your project be able to understand your proposal?
- Have you properly proofread your proposal to assure there are minimal grammatical and spelling mistakes?
- Are all the resources used for this project correctly cited and referenced?
