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
    try:
        n = fakenews.fakeNews(url)
    except:
        print('a')
        #raise
        return {'status':"oops"}
    try:
        if n.lower() == "trump":
            return {'status':"trump", 'value': 101}
    except:
        pass
    try:
        if n > 50:
            return {'status':"fake", 'value': int((n-50)*20)}
        elif n < 50:
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