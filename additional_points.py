import nltk

class MoreCheck:

	def checkMore(doc_complete):

		adjectives = []
		adverbs = []
		modal = []

		# Check adjective similarity
		for sentence in doc_complete:
			doc_tokens = nltk.word_tokenize(sentence)
			doc_pos_tags = nltk.pos_tag(doc_tokens)
			for i in range (0, len(doc_pos_tags)):
				if doc_pos_tags[i][1] in ["JJ"]:
					adjectives.append(doc_pos_tags[i][0])
				elif doc_pos_tags[i][1] in ["RB"]:
					adverbs.append(doc_pos_tags[i][0])
				# Modal auxiliary
				elif doc_pos_tags[i][1] in ["MD"]:
					adverbs.append(doc_pos_tags[i][0])
		print(adjectives)
		return adjectives

if __name__ == "__main__":
	doc_complete = open("text.txt", "r").readlines()

	MoreCheck.checkMore(doc_complete)
