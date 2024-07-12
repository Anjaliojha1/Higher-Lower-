import random
from flask import Flask

random_number = random.randint(0,9)
app = Flask(__name__)

# The Homepage
@app.route('/')
def home():

    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="Guess a number GIF">')
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return("<h1 style='color: purple'>Too high, try again!</h1>"\
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    elif guess < random_number:
        return ("h1 style='color: red'>Too Low, Guess Again!<h1>"
                "img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>")
    else:
        return ("<h1 style='color: green'>You Found Me!<h1>"
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")

if __name__ == '__main__':
    app.run(debug=True)


