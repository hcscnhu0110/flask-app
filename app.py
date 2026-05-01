from flask import Flask
import random

app = Flask(__name__)

restaurants = ["A餐廳", "B餐廳", "C餐廳"]

@app.route("/")
def home():
    return f"今天吃：{random.choice(restaurants)}"

if __name__ == "__main__":
    app.run()