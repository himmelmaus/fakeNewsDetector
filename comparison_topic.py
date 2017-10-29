import sentiment_analysis

class Comparison:
	# topics_fake - result of the fake article topics, topics_others = other articles from the web for comparison
	def compare(topics_fake, topics_others, headline_main, headlines_others, additional_fake, additional_others):

		# Points system. T - total score
		# 0.20T - actual length of the articles found
		# 0.40T - relevence according to the topic words
		# 0.15T - adjectives and adverbs
		# 0.15T - headlines
		# 0.10T - negativity ranking
		# Max 10 relevant articles in google news. 
		
		# Start score = 0 (unreliable, probably fake), max score = 10 (reliable, probably not fake)
		total_score = 0

		# 1. Actual length of articles
		topics_fake_length = len(topics_fake)
		topics_others_length = len(topics_others)
		length_score = topics_others_length * 4 # 0 < topics_others_length < 5, 0 < total_score < 25 ???
		total_score = total_score + length_score

		print("Score 1 " + str(total_score))

		if ((topics_fake_length * topics_others_length) != 0):
			temp_score_unit = 40 / (topics_fake_length * topics_others_length)

			#Relevance according to the topics
			for item in topics_others:
				for i in range(0, topics_fake_length):
					if topics_fake[i] in item:
						total_score = total_score + temp_score_unit
					#print(str(total_score) + " = " + topics_fake[i] + ", " + str(item[item.index(topics_fake[i])]))

			print("Score 2 " + str(total_score))

		# Headlines score
		if len(headlines_others) != 0:
			onepts = 15/len(headlines_others)
			for headline in headlines_others:
				score_tmp = len([w for w in headline.split(' ') if w in headline_main])
				print (score_tmp)
				if score_tmp >= 3:
					total_score += onepts 
					print (total_score)

		print("Score 3 " + str(total_score))


		additional_fake_length = len(additional_fake)
		additional_others_length = len(additional_others)
		print(additional_fake_length)
		print(additional_others_length)
		total_ratio = 0

		if additional_others_length > 0:
			for item in additional_others:
				for i in range(0, additional_fake_length):
					if additional_fake[i] in item:
						total_ratio = total_ratio + 1
			total_ratio = total_ratio / (additional_fake_length * additional_others_length)

			if (total_ratio < 0.1):
				total_score = total_score + 2
			elif (total_ratio < 0.2):
				total_score = total_score + 7
			elif (total_ratio < 0.5):
				total_score = total_score + 13
			else:
				total_score = total_score + 15
		print(total_ratio)

		print("Score 4 " + str(total_score))

		#15 pts 
		doc_complete = open("testeroo.txt", "r").readlines()
		# Negativity score
		negativity_rating = int(10 - (sentiment_analysis.Model.startModel(doc_complete)*10)) #sentiment_analysis gives back result from 0*10 to 1*10 from negative side, so 10 - result gives back normal score result
		total_score = float(total_score + negativity_rating) / 10
		print("Score 5 " + str(total_score))

		print(total_score)
		return total_score

if __name__ == "__main__":
	# Random data inputs for testing purposes
	doc_complete = open("text.txt", "r").readlines()
	topics_fake = ['spanish', 'catalan', 'independence', 'mr', 'it', 'say']
	topics_others = [['independence', 'mr', 'catalan', 'catalonia', 'government', 'spanish'], ['mr', 'spanish', 'catalan', 'independence', 'puigdemont', 'rajoy', 'government']]
	Comparison.compare(topics_fake, topics_others)
