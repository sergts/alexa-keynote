import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from subprocess import call

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def start_presentation():
    welcome_msg = render_template('welcome')
    call(["osascript", "start_presentation.scpt"])
    return statement(welcome_msg)


@ask.intent("Next_slide")
def next_slide():
    next_msg = render_template('next')
    call(["osascript", "move.scpt"])
    return statement(next_msg)



if __name__ == '__main__':
    app.run(debug=True)