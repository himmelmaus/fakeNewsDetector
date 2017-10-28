import machine
import article_topics
import comparison_topic
from article_scraper import article_scrape
import re

url = "https://www.infowars.com/gorka-deep-state-withholding-of-jfk-files-stinks-to-high-heaven/"

def main(url):


    score = 0

    if machine.SatireCheck(url):
        return 100 # If satire, it's fake news

    # get the srs words
    titlekeywords = machine.FindTitle(url)
    print("titlekeywords:")
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
    print ("main article:")
    print (mainArticleContent)

    with open("testeroo.txt", 'w') as file:
        file.write(mainArticleContent)
    
    with open("testeroo.txt", 'r') as file:
        mainArticleContent = file.readlines()

    # get topics of the main article you are evaluating
    mainArticleTopics = topics.FindTopics(mainArticleContent)
    for elem in mainArticleTopics:
        elem = re.sub(r'\W+', '', elem)
        
    print ("main topics:")
    print (mainArticleTopics)

    # gets a list of lists.
    # each list includes:
    # 0. matched words
    # 1. the title/description
    # 2. article url
    # 3. topics
    print (titlekeywords)
    articlecompare = machine.NewsCheck(titlekeywords)
    print (articlecompare)
    topicothers = []
    titles = [] 
    for key in articlecompare:
        print ("LOOP")
        articletxt = article_scrape(articlecompare[key])
        topicothers.append(topics.FindTopics(articletxt))
        print (topicothers)
        titles.append(articlecompare[1])
        print (key)
    
    print ("this happens after loop")

    faketopic = ['spanish', 'catalan', 'independence', 'mr', 'it', 'say']

    scoring = comparison_topic.Comparison
    #print(titles)
    scoring.compare(mainArticleTopics, topicothers, titlekeywords, titles)





if __name__ == "__main__":
    main(url)