import os
import random
from flask import Flask, render_template, session, request
from Movies import movies


app = Flask(__name__)
app.secret_key = "dashwood123"

autofill = "AEIOU~`!@#$%^&*()-_=+{[}]\\|:;'\"<>?,./1234567890 "
woods = ["Bollywood", "Hollywood", "Marvelwood"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game/<wood>")
def game(wood):
    chosen_movie = random.choice(movies[wood])
    board = []
    for letter in chosen_movie.upper():
        if letter in autofill:
            board.append(letter)
        else:
            board.append("_")
    session["board"] = board
    session["movie"] = chosen_movie
    session["lives"] = list(wood.upper())
    session["wood"] = wood
    return render_template("game.html", board=board, lives=list(wood.upper()), wood=wood)

@app.route("/guess", methods=["POST"])
def guess():
    guess = request.form["guess"].upper()
    board = session["board"]
    movie = session["movie"]
    lives = session["lives"]
    wood = session["wood"]

    if guess in movie.upper():
        for index, letter in enumerate(movie.upper()):
            if letter == guess:
                board[index] = guess
        session["board"] = board
        message = "Correct!"
    else:
        if len(lives) == 0:
            return render_template("game.html", board=board, lives=lives, wood=wood, message="You Lost! The movie was: " + movie)
        elif guess == lives[0]:
            message = "Lucky! Life saved!"
        else:
            lives.pop(0)
            session["lives"] = lives
            message = "Wrong Guess :("

    if "_" not in board:
        return render_template("game.html", board=board, lives=lives, wood=wood, message="You guessed it! The movie was: " + movie)

    return render_template("game.html", board=board, lives=lives, wood=wood, message=message)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)