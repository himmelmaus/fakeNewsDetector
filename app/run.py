from flask import Flask, request, render_template
from flask import request
from flask import render_template
import nltk
import sys, os.path
fakenews_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
+ '/')
sys.path.append(fakenews_dir)
import fakenews

app = Flask(__name__)

def real(url): #placeholder function before parsing url input
    if fakenews.blackList(url):
        return {'status':'network'}
    if fakenews.whiteList(url):
        return {'status':'trusted'}
    if fakenews.invalid(url):
        return {'status':"oops"}
    try:
        n = fakenews.fakeNews(url)
    except:
        raise
        return {'status':"oops"}
    try:
        if n.lower() == "trump":
            return {'status':"trump", 'value': 101}
        if n.lower() == "oops":
            return {'status':'oops'}
    except:
        pass
    try:
        print ('\n\n')
        print (n)
        if n < 4:
            print ('\n\n')
            print (n)
            return {'status':"fake", 'value': int((5 - n)*20) }
        elif n >= 5:
            return {'status':"real", 'value':int((n)*10)}
    except:
        print ('b')
        #raise
        return {'status':"oops"}


@app.route('/', methods=['GET','POST'])
def print_form():
    if request.method == 'POST': #code to be executed when submit button is pushed
        result = request.form['input']                                                                                                                         
        return render_template('index.html', result=real(request.form['input']))
    if request.method == 'GET': #base text
        return render_template('index.html')

if __name__ == '__main__':
    app.run()