from flask import Flask, render_template, jsonify
import pandas as pd
import random

app = Flask(__name__)

# Загружаем Excel
df = pd.read_excel("street-names.xlsx")
df = df.dropna(subset=["שם ראשי", "שכונה"])

streets = list(zip(df["שם ראשי"], df["שכונה"]))
all_neighborhoods = list(df["שכונה"].unique())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/question")
def question():
    street, correct_neighborhood = random.choice(streets)

    wrong_answers = random.sample(
        [n for n in all_neighborhoods if n != correct_neighborhood], 3
    )

    options = wrong_answers + [correct_neighborhood]
    random.shuffle(options)

    return jsonify({
        "street": street,
        "options": options,
        "answer": correct_neighborhood
    })

if __name__ == "__main__":
    app.run(debug=True)
