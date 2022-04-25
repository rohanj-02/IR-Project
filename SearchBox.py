from flask import Flask, render_template, request
from flask.helpers import flash
import pickle

app = Flask(__name__)
with open("AllDomains.pkl","rb") as file:
    domains = pickle.load(file)


@app.route('/',methods = ['GET','POST'])
def home():
    selected = domains[0]
    print("hello")
    if request.method=='POST':
        domain = request.form['search-input']
        selected = domain
        print(selected)
    return render_template('index.html',domains=domains,selected=selected)


if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8000)