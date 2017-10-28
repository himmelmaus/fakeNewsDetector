import machine
import article_topics
from article_scraper import article_scraper

def main(url):

    score = 50.0


    if machine.SatireCheck(url):
        return 0 # If satire, it's neutral 

    # get the srs words
    titlekeywords = machine.FindTitle(url)


    # TRUMP CHECK START
    trump = machine.TrumpCheck(titlekeywords)

    if trump >= 2:
        return -100.0 # if it's Trump, it's almost guaranteed fake news
    else:
        score -= 50.0
    # TRUMP CHECK OVER

    # initiate the class
    topics = article_topics.OnStart()

    # get article you are evaluating text
    mainArticleContent = article_scraper(url)

    # get topics of the main article you are evaluating
    mainArticleTopics = topics.FindTopics(mainArticleContent)

    # gets a list of lists.
    # each list includes:
    # 0. matched words
    # 1. the title/description
    # 2. article url
    # 3. topics
    articlecompare = machine.NewsCheck(titlekeywords)

    for article in articlecompare:
        articletxt = article_scraper(article[2])
        article.append(topics.FindTopics(articletxt))


    

    
    
 


    















if __name__ == "__main__":
    main()