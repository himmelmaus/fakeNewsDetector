import machine
import article_topics
import comparison_topic
from article_scraper import article_scrape
import re

url = "http://www.bbc.co.uk/news/world-europe-41785292/"

def main(url):


    score = 0

    if machine.SatireCheck(url):
        return 100 # If satire, it's fake news

    # get the srs words
    titlekeywords = machine.FindTitle(url)
    print(titlekeywords)


    # TRUMP CHECK START
    trump = machine.TrumpCheck(titlekeywords)

    if trump >= 2:
        return "Trump" # if it's Trump, it's almost guaranteed fake news
    else:
        score += 50.0
    # TRUMP CHECK OVER

    # initiate the class
    topics = article_topics.OnStart()

    # get article you are evaluating text
    mainArticleContent = article_scrape(url)

    with open("testeroo.txt", 'w') as file:
        file.write(mainArticleContent)
    
    with open("testeroo.txt", 'r') as file:
        mainArticleContent = file.readlines()

    # get topics of the main article you are evaluating
    mainArticleTopics = topics.FindTopics(mainArticleContent)
    for elem in mainArticleTopics:
        elem = re.sub(r'\W+', '', elem)

    # gets a list of lists.
    # each list includes:
    # 0. matched words
    # 1. the title/description
    # 2. article url
    # 3. topics
    articlecompare = machine.NewsCheck(titlekeywords)
    topicothers = []
    titles = [] 
    articletxt = ""
    for key in articlecompare:
        articletxt = article_scrape(articlecompare[key])
        with open("test2.txt", 'w') as file:
            file.write(articletxt)
        with open("test2.txt", 'r') as file:
            articletxt = file.readlines()
        topicothers.append(topics.FindTopics(articletxt))
        titles.append(articlecompare[key])

    scoring = comparison_topic.Comparison
    #print(titles)
    scoring.compare(mainArticleTopics, topicothers, titlekeywords, titles)





if __name__ == "__main__":
    main(url)