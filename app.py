from flask import Flask
import random

app = Flask(__name__)

restaurants = ["A餐廳", "B餐廳", "C餐廳", "D餐廳"]

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>吃什麼抽選器</title>
    </head>
    <body style="text-align:center; font-family:Arial;">
        <h1>今天吃什麼？</h1>
        <button onclick="getFood()">幫我抽</button>
        <h2 id="result"></h2>

        <script>
            function getFood(){
                fetch('/pick')
                .then(res => res.text())
                .then(data => {
                    document.getElementById('result').innerHTML = data;
                })
            }
        </script>
    </body>
    </html>
    """

@app.route("/pick")
def pick():
    return random.choice(restaurants)