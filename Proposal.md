# Machine Learning Engineer Nanodegree
## Capstone Proposal
George Vargas
Date TBD

## Proposal

### Domain Background

Accurately predicting the financial markets has long been the holy grail for all types of investors. Many individual investors seek this grail but never find it. This tends to be because many underestimate the extreme complexity of the financial markets. Though many fail some individual investors do attain moderate success implementing trading systems that work for the highly-focused conditions in which they find themselevs trading.  Likewise some hedgefunds, such as Renaissance Technologies, achieve great success building complexing trading systems based on standard and alternative data whilst utilizing much more scientific methods for decision making.[[1]]((https://www.linkedin.com/pulse/20141117150538-17004994-pure-alpha-story-of-renaissance-technologies/))

Approaching the problem as a hedgefund might it can be found that the success rate of any particular trade can be significantly increased by considering the system as components all feeding a decision engine, much like neurons in a neural network feed the output layer. While these systems are made of many complex components there has been increasing focus on alternative data and it's use in sentiment analysis components. Data mining news, blog and twitter posts has been proven to increase the probability of a successful trade.[[2]](https://arxiv.org/pdf/1010.3003.pdf)[[3]](http://cs229.stanford.edu/proj2015/029_report.pdf).

My personal motivation for looking at possible solutions to this task is purely for my own financial independence. As a hobbyist day trader I've been somewhat profitable but my time is limited because of my full-time employment. Having the ability to create a trading system with the ability to trade as I do but not have the time limitations that I have would be an extremely valuable step toward achieveing financial independence.

### Problem Statement

The problem with financial markets is that they are largely driven by emotions. Even in a time when a majority of the trades are being placed by sophicated bots emotion still rules the market. This can be seen by the effect Donald Trump's tweets have on the stock of the particular companies he targets. Utilizing text sources to reliably predict these types of market movements will be the problem this capstone attempts to solve.

### Datasets and Inputs

The datasets used are from Kaggle, specifically [these datasets](https://www.kaggle.com/aaron7sun/stocknews#Combined_News_DJIA.csv) provided by a user in the community. The datasets span approximately eight years from August 2008 to July 2016. Contained is a dataset of the Dow Jones Industrial Average price history with columns including Date, Open, High, Low, Close, Volume and Adj Close; A dataset of Reddit news and a combined dataset with a Dow Jones Industrial Average label and a column each for one of the top twenty-five user upvoted headlines for that day. The label has a value of either "1" for DJIA closing up and "0" for DJIA closing down. The provider of the dataset recommends using data from 2008-08-08 to 2014-12-31 for training and data from 2015-01-02 to 2016-07-01 for testing since this splits the overall dataset in an eighty-twenty fashion. 

For our purposes we will exclude the data up to April 2009. The reason for excluding this data in training, validation and testing is because leading up to April 2009 the market was in a strong downward trend that was a direct result of the housing market crash. Aside from training and tetsing for correlation between news headlines and the DJIA closing up or down we will be reserving the data up to April 2009 as an additional test to see if the model can generalize from being trained in only a bull market to succeeding in a predominantly bear market.

### Solution Statement

In this capstone we will attempt to predict whether the Dow Jones Indistrial Average will close up or close down based on text classification performed on the news headlines of that day. We will be using word embeddings to prepare our text data to be fed to a supervised model. Our prediction value will be the label from the combined dataset denoting the upward or downward movement of the DJIA for a given day.

### Benchmark Model

Although anecdotal most individual investors will cite roughly a fifty to fifty-five percent accuracy when trading. This is mainly gathered from watching students in trading programs or from discussions with other individual investors. Anecdotal information isn't necessarily considered reliable, however, this researcher is inclined to believe such claims as most trading programs require students to methodically write down every trade(entry, exit, stoploss, etc.) before placing a trade. This is done to develop discipline and help remove emotion from the trades which is one of the most important factors for becoming a successful individual investor.

Now, fifty to fifty-five may seem like slim margins but keep in mind that with just a fifty-one percent win percentage and proper risk management card counters can effectively clean house at casinos. Also considering that the data spans a period of time where the market was particularly bullish we will be using the [sklearn.dummy.DummyClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html) in an effort to benchmark against the multiple simple strategies provide by the dummy classifier. This will help figure out if the bullish bias in the data can be exploited via simpler means.

### Evaluation Metrics

To get a better idea of what is going on with the model we will be utilizing a few different metrics to evaluate the performance against the benchmark model. Firstly, we will look at accuracy just to give us a general idea of the model's performance. This will be followed up by a dive into the root mean squared error and mean average percentage error. These will help us gauge, more objectively, how close the model predictions are to the actuals.

### Project Design

In this final section, summarize a theoretical workflow for approaching a solution given the problem. Provide thorough discussion for what strategies you may consider employing, what analysis of the data might be required before being used, or which algorithms will be considered for your implementation. The workflow and discussion that you provide should align with the qualities of the previous sections. Additionally, you are encouraged to include small visualizations, pseudocode, or diagrams to aid in describing the project design, but it is not required. The discussion should clearly outline your intended workflow of the capstone project.

To start we will first split the dataset to create the previously mentioned bearish holdout set. After which we will split the remaining bullish data into two portions; one for training and the other for testing.

In order to be able to feed our text from the dataset to a classification model we will need to perform some preprocessing. Based on preliminary research the most effective method currently used for text classification is the conversion of words to vectors[TBD referecne]. While there are several libraries that are popular and provide good performance we will be utilizing the [fastText pyhton library](https://github.com/facebookresearch/fastText) created by the facebook AI research team. The reason for utilizing this library over word2vec or gLoVe is that fastText creates word representations from word n-grams in a convolution-like manner instead of entire words or sentences. This creates a much more specific representation for each word and also allows us to construct vectors on words that are outside of the training corpus which will be useful when generalizing against the portion of the dataset that was held out for testing generalization against a bear market.

To aid in preprocessing we will build a pipeline to feed in any dataset with the same structure and return a fully preprocessed dataset. The pipeline will first encode all text columns to UTF-8 since fastText requires this encoding to perform it's functions. The pipeline will then remove any non-sensical words. Finally, the pipeline will produce two separate datasets; one which includes stop words and one which has been stripped of stop words. This creation of the two separate datasets is to observe any difference in performance when stop words are removed [TBD Why stop words may affect performance]. Since we are using the fastText library the pipelie doesn't need to strip punctuation or clean up whitespaces.

After preprocessing the text, the two datasets will be passed into the skipgram model in fastText for training. This skipgram model will output vector representations for each word in each dataset and a trained model for each dataset that can be used for analyzing the corpus by means such as nearest neighbor and analogy quieries. A function will be used to loop through each word in each headline in each column of the dataset and generate a new dataset that ???

Convert vectors of words into one approximation for a sentence use bag-of-words approach
Preprocess tokens like "New York" into a single token "New_York" to aid in teh bag of word approach

After converting the words to their vector representations we will perform some cursory analysis of the data. This will help us to visualize aspects such as trends over time, distribution, frequency, popularity of headlines and other commonalities.

Once the headlines have been converted into vectors we will feed them to a Support Vector Machine

Kfold for cross validation if thinsg get strange

-----------

**Before submitting your proposal, ask yourself. . .**

- Does the proposal you have written follow a well-organized structure similar to that of the project template?
- Is each section (particularly **Solution Statement** and **Project Design**) written in a clear, concise and specific fashion? Are there any ambiguous terms or phrases that need clarification?
- Would the intended audience of your project be able to understand your proposal?
- Have you properly proofread your proposal to assure there are minimal grammatical and spelling mistakes?
- Are all the resources used for this project correctly cited and referenced?
