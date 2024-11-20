from flask import Flask, render_template

import test

app = Flask(__name__)
@app.route("/")
def index():
    fruits = [
        {"name": "apples", "quantity": 3},
            {"name": "oranges", "quantity": 2},
            {"name": "strawberries", "quantity": 6}
    ]

    filter_fruit =[]
    for fruit in fruits:
        if fruit ['name'].startswith('o') or fruit ['quantity']>3:
            filter_fruit.append(fruit)

    print(test.MY_SECRET_API_KEY_1)
    print(test.MY_SECRET_API_KEY_2)

    return render_template("index.html", fruits=filter_fruit,)
