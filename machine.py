import re
#import scrapy
import urllib
import multiprocessing
import json
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

# temp
import sys

#local imports
from article_scraper import article_scraper


def FindTitle(url):
	##
    title_list, words_filtered = [],[]
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'lxml')
    print("Loading page")
    __title = soup.find('h1').get_text()
    print("Found %s" % __title)
    title_list = __title.split(" ")

    for element in title_list:
        print (element)
        if element.lower() not in set(stopwords.words('english')):
            words_filtered.append(element)

    return words_filtered

	##
#if __name__ == "__main__":
	#inputvar = "https://www.theonion.com/popular-new-amazon-service-just-comes-to-your-house-and-1819917496"
	#print(FindTitle(inputvar))
# satire or parody check

def NewsCheck(wordlist):

    # get a list of words, put it back into one big string. that's it. 
    # ' '.join(words_filtered)
    # headingstr = ' '.join(heading)
    matches = 0
    matchratio = 0.0

    wordstr = ' '.join(wordlist)
    headings = []
    articleurl = []

    #similarity points, desc, url
    packeddata = []

    #wordlist = ["Trump", "threatens", "Korea"]

    searchurl = 'https://news.google.com/news/search/section/q/{}'.format('\%20'.join(wordlist))

    f = urllib.request.urlopen(searchurl).read()
    soup = BeautifulSoup(f, 'html.parser')


    for headinghtml in soup.find_all(role="heading"):
        headings.append(headinghtml.get_text())
        print (headinghtml.get_text())
        articleurl.append(headinghtml.get('href'))
        print (headinghtml.get('href'))


    for n in len(headings):
        words = (len([w for w in wordstr if w in headings[n]]))
        if words >= len(headings[n])/2:
            matches += words
        else:
            matches += words/2 
        
        if matches > 0:
            temp = []
            temp.append(matches)
            temp.append(headings[n])
            temp.append(articleurl[n])
            packeddata.append(temp)

    return packeddata
            


    #matchratio = matches/len(headings)


    

    

def SatireCheck(url):
    #instring:
    satiresites = ["theonion", "waterfordwhispersnews", "clickhole", "private-eye.co.uk", "eljueves.es"
    "thedailymash.co.uk", "borowitz", "fakingnews", "satirewire", "thebeaverton"]

    if any(x in url for x in satiresites):
        print ("it's satire you silly sausage")
        return True
    else:
        return False

def TrumpCheck(words_filtered):

    wordtemp = []
    for word in words_filtered:
        wordtemp.append(word.lower())

    words_filtered = wordtemp

    trumpfactor = len([w for w in ['donald', 'trump'] if w in words_filtered]) 

    if set(['make', 'america', 'great', 'again']).issubset(set(words_filtered)) or ('maga' in words_filtered):
        trumpfactor += 2

    return trumpfactor 

# TODO: ARTICLE CHECK 
    

def main():
    fakepoints = 0.0

    url = sys.argv[1]

    # checks if satire
    if SatireCheck(url):
        return "satire"

    words_filtered = FindTitle(url)

    fakepoints += NewsCheck(words_filtered)/100

    # checks if related to Trump
    trump = TrumpCheck(words_filtered)
    if trump >= 2:
        return "trumped"
    elif trump == 1:
        fakepoints += 30
    else:
        print ("trump free")

    #if fakepoints > 90:
    #    add = "Trump would build a WALL around this."
    #elif fakepoints > 80:
    #    add = "It's fake."
    #elif fakepoints > 50:
    #    add = "That's fishy."
    #elif fakepoints <= 50 and fakepoints > 45:
    #    add = "It could go either way."
    #elif fakepoints < 45 and fakepoints > 30:
    #    add = "It's more true than fake."
    #elif fakepoints < 30:
    #    add = "It's LEGIT!"
    

    return "this site is {}%% FAKE NEWS. {}".format(fakepoints, add)


if __name__ == "__main__":
    print (main()) 
    


    
    
        






# false connection (headlines and visual captions don't support content)




# false contextual information


# check authors 
