import sentiment_analysis

class Comparison:
	# topics_fake - result of the fake article topics, topics_others = other articles from the web for comparison
	def compare(topics_fake, topics_others, headline_main, headlines_others):

		# Points system. T - total score
		# 0.25T - actual length of the articles found
		# 0.50T - relevence according to the topic words
		# 0.15T - headlines
		# 0.10T - negativity ranking
		# Max 10 relevant articles in google news. 
		
		# Start score = 0 (unreliable, probably fake), max score = 10 (reliable, probably not fake)
		total_score = 0

		# 1. Actual length of articles
		topics_fake_length = len(topics_fake)
		topics_others_length = len(topics_others)
		length_score = topics_others_length * 5 # 0 < topics_others_length < 5, 0 < total_score < 25
		total_score = total_score + length_score

		temp_score_unit = 50 / topics_fake_length

		#Relevance according to the topics
		for item in topics_others:
			for i in range(0, topics_fake_length):
				if topics_fake[i] in item:
					total_score = total_score + temp_score_unit

		# Headlines score
		if len(headlines_others) != 0:
			onepts = 15/len(headlines_others)
			for headline in headlines_others:
				score_tmp = len([w for w in headline if w in headline_main])
				if score_tmp >= len(headline)/2:
					total_score += onepts 

		#15 pts 
		doc_complete = open("testeroo.txt", "r").readlines()
		# Negativity score
		negativity_rating = int(10 - (sentiment_analysis.Model.startModel(doc_complete)*10)) #sentiment_analysis gives back result from 0*10 to 1*10 from negative side, so 10 - result gives back normal score result
		total_score = int(total_score + negativity_rating) #/ 10

		print(total_score)
		return total_score

if __name__ == "__main__":
	# Random data inputs for testing purposes
	doc_complete = open("text.txt", "r").readlines()
	topics_fake = ['spanish', 'catalan', 'independence', 'mr', 'it', 'say']
	topics_others = [['independence', 'mr', 'catalan', 'catalonia', 'government', 'spanish'], ['mr', 'spanish', 'catalan', 'independence', 'puigdemont', 'rajoy', 'government']]
	Comparison.compare(doc_complete, topics_fake, topics_others)
