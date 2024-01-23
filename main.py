from flask import Flask
from random import randint

app = Flask(__name__)


def get_random_number(min_value, max_value):
    return randint(min_value, max_value)


@app.route("/")
def index():
    return "This is a payment page! Please pay %s USD"%(get_random_number(0, 100))


if __name__== "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
