from nltk.corpus import stopwords # pip3 instlal nltk
from nltk.stem.wordnet import WordNetLemmatizer
import nltk
from nltk.collocations import *
import string
import gensim # pip3 install Gensim
from gensim import corpora

# Base code from: https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/
# Outputs around 6 words that describes the topic of the article

def FindTopics():
	# Present the article in a sentence per new line
	doc_complete = open("text.txt", "r").readlines()

	stop = set(stopwords.words('english'))
	exclude = set(string.punctuation)
	lemma = WordNetLemmatizer()
	unnecessary = []

	# Pos tag words and remove tags "IN", "MD", "CD"
	for i in range (0, len(doc_complete)):
		doc_tokens = nltk.word_tokenize(doc_complete[i])
		doc_pos_tags = nltk.pos_tag(doc_tokens)
		for i in range (0, len(doc_pos_tags)):
			if doc_pos_tags[i][1] in ["IN", "MD", "CD", "PDT", "PRP"]:
				unnecessary.append(doc_pos_tags[i][0])

	# Cleans the composed string from stop words (stop_free), puncuation (punc_free) and l
	def clean(doc):
	    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
	    unnecessary_free = " ".join([i for i in stop_free.lower().split() if i not in unnecessary])
	    punc_free = ''.join(ch for ch in unnecessary_free if ch not in exclude)
	    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
	    return normalized

	# Use clean function on doc_complete
	doc_clean = [clean(doc).split() for doc in doc_complete]

	# Matrix representation of a corpus using corpora
	dictionary = corpora.Dictionary(doc_clean)

	# Document - term matrix
	doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean] 

	# Training LDA model
	Lda = gensim.models.ldamodel.LdaModel
	ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

	pairs = ldamodel.print_topics(num_topics=3, num_words=3)
	pairs_dictionary = {}

	for i in range(0, len(pairs)):
		for y in range(1, len(pairs[i])):
			pairs_split = pairs[i][y].split(" + ")
			for x in range(0, len(pairs_split)):
				pairs_split2 = pairs_split[x].split("*")
				pairs_split2[0] = float(pairs_split2[0])
				pairs_split2[1] = pairs_split2[1][1:(len(pairs_split2[1])-1)]
				pairs_dictionary[pairs_split2[1]] = pairs_split2[0]

	# Decending
	most_popular_topics = sorted(pairs_dictionary, key=pairs_dictionary.get, reverse=True)
	print(most_popular_topics)

if __name__ == "__main__":
	FindTopics()