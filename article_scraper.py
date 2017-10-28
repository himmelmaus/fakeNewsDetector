from newspaper import Article
def article_scrape(url):
	article = Article(url)
	article.download()
	article.parse()
	return article.text
