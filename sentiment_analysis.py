import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy

# Base code: https://www.twilio.com/blog/2017/09/sentiment-analysis-python-messy-data-nltk.html

def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})

pos = []
with open("./TrainingData/pos_tweets.txt") as f:
    for i in f: 
        pos.append([format_sentence(i), 'pos'])
 
neg = []
with open("./TrainingData/neg_tweets.txt") as f:
    for i in f: 
        neg.append([format_sentence(i), 'neg'])
 
# next, split labeled data into the training and test data
training = pos[:int((.8)*len(pos))] + neg[:int((.8)*len(neg))]
test = pos[int((.8)*len(pos)):] + neg[int((.8)*len(neg)):]

classifier = NaiveBayesClassifier.train(training)
 
doc_complete = open("text.txt", "r").readlines()
avg = 0
length = len(doc_complete)
for items in doc_complete:
	avg = avg + float(classifier.prob_classify(format_sentence(items)).prob('neg'))
avg = avg / length
print(avg)
