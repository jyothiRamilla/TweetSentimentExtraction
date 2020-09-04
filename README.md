# TweetSentimentExtraction
This project is about defining the quality of a statement(tweet)



To run the code: 
I have used streamlit in order to provide good user interface.

(Install all the dependencies before from requirements.txt file by using the folowing command)

pip -r requirements.txt

Run this command in your cmd:

streamlit run app.py


Problem Statement:

Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Can you write a program which can indicate the degree of profanity for each sentence in the file?

Solution:

This is a Natural language processing task. I am going to use python for this.
In order to classify the statements and to find the profanity of each statement we need a dataset to train.

So I have taken the following dataset from kaggle:

[a link](https://www.kaggle.com/kazanova/sentiment140)

I trained my model using this dataset.


According to this dataset there are 1.6 million tweets which includes positive,negative and neutral statements

Here we have 3 labels:

0 -> negative 

2 -> neutral

4 -> positive

[target: the polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)

ids: The ids of the tweet

date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)

flag: The query (lyx). If there is no query, then this value is NO_QUERY.

user: the user that tweeted (name of the user)

text: the text of the tweet (This is the tweet)]

This is about the dataset.

When it comes to the training part, I have used tokenizer in order to generate tokens for each statement.(I used nltk,keras and tensorflow)

I have used nltk in order to remove all the stopwords(like is,the,her,his,... which does not have that impact in giving the solution)

train data: 80 % data
test data: 20 % data

When it comes to the model, I am using 

1. Embedding layer(word to vector)
2.LSTM
3. An activation function: Sigmoid


The model gave me an accuracy of: 78%  for 8 epochs.

