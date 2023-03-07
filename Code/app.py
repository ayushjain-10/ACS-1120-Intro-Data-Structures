"""Main script, uses other modules to generate sentences."""
from crypt import methods
import twitter
from flask import Flask, redirect, render_template, request
from twitter import tweet
from tokens import tokenize
from dictogram import Dictogram
# import get sentence from markov
from markov import MarkovChain


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.



@app.route('/')
def index():
#   store the new sentence generated from markov.py in generated_text
    markov = MarkovChain('output.txt')
    return render_template('index.html', title='Cuban Tweet', generated_text= markov.compose_sentence(10))

@app.route('/tweet', methods=['POST'])
def create_tweet():
  status = request.form['sentence']
  print(status)
  twitter.tweet(status)
  return redirect('/')




if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
