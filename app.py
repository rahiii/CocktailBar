from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='src')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bloody-orange-martini')
def bloody_orange_martini():
    return render_template('bloody_orange_martini/bloody_orange_martini.html')

@app.route('/bloody-orange-martini-2')
def bloody_orange_martini_2():
    return render_template('bloody_orange_martini/bloody_orange_martini_2.html')

@app.route('/tequila-sunrise')
def tequila_sunrise():
    return render_template('tequila_sunrise.html')

@app.route('/grapefruit-paloma')
def grapefruit_paloma():
    return render_template('grapefruit_paloma.html')

if __name__ == '__main__':
    app.run(debug=True)
