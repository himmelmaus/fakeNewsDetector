from flask import Flask
from flask import request
from flask import render_template
from time import sleep

app = Flask(__name__)

def real(n):
    if int(n) > 5:
        return "fake"
    else:
        return "real"

@app.route('/', methods=['GET','POST'])
def print_form():
    if request.method == 'POST':
        result = request.form['input']                                                                                                                         
        return render_template('index.html', result=real(result))
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run()