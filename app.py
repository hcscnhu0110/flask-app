from flask import Flask
import random

app = Flask(__name__)

# 3個分類
data = {
    "中式": ["滷肉飯", "牛肉麵", "水餃店"],
    "日式": ["拉麵", "壽司", "丼飯"],
    "速食": ["麥當勞", "肯德基", "漢堡王"]
}

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>吃什麼抽選器</title>
    </head>

    <body style="text-align:center; font-family:Arial;">
        <h1>今天吃什麼？</h1>

        <h3>先選類型</h3>

        <button onclick="setType('中式')">中式</button>
        <button onclick="setType('日式')">日式</button>
        <button onclick="setType('速食')">速食</button>

        <br><br>

        <button onclick="pickFood()">開始抽</button>

        <h2 id="type"></h2>
        <h2 id="result"></h2>

        <script>
            let currentType = ""

            function setType(t){
                currentType = t
                document.getElementById("type").innerHTML = "已選：" + t
                document.getElementById("result").innerHTML = ""
            }

            function pickFood(){
                if(!currentType){
                    alert("先選類型！")
                    return
                }

                fetch('/pick?type=' + currentType)
                .then(res => res.text())
                .then(data => {
                    document.getElementById("result").innerHTML = data
                })
            }
        </script>
    </body>
    </html>
    """

@app.route("/pick")
def pick():
    from flask import request

    t = request.args.get("type")

    if t not in data:
        return "請先選類型"

    return random.choice(data[t])