from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def print_form():
    if request.method == 'POST':
        return render_template('index.html', result=request.form['input'])
    if request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run()