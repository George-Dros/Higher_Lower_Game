from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0,9)
print(number)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9 </h1> " \
           "<img src= https://media3.giphy.com/media/xUn3CftPBajoflzROU/200w.webp?cid=ecf05e47n51f8yu7" \
           "dmlbu3ppsu86phgrs8bec31k0ki4fp0k&ep=v1_gifs_search&rid=200w.webp&ct=g>"


@app.route("/<int:guess>")
def guess_url(guess):
    if guess > number:
        return "<h1>Too High, try again!</h1> " \
               "<img src= https://media.giphy.com" \
               "/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"

    if guess < number:
        return "<h1>Too Low, try again!</h1> " \
               "<img src= https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"

    if guess == number:
        return "<h1>You have found me!!!!</h1> " \
               "<img src= https://media2.giphy.com/media/ICOgUNjpvO0PC/" \
           "giphy.gif?cid=ecf05e47rsiyzfnaa8vujw8nkqy9ie3h9lihysp2t5m7y660&ep" \
           "=v1_gifs_search&rid=giphy.gif&ct=g>"


if __name__ == "__main__":
    app.run(debug=True)
